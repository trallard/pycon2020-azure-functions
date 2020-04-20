import datetime
import json
import logging
import os
from dataclasses import dataclass
from json import JSONDecodeError
from typing import Optional, Iterator

import requests


@dataclass
class se_object:
    """Class to deal with StackExchage data collection and manipulation.
    """

    search_terms: list
    main_uri: str = "https://api.stackexchange.com/2.2/questions"

    def __repr__(self) -> str:
        return f"<Object for site {self.main_uri}>"

    def get_questions(self, n=100) -> Optional[Iterator[dict]]:
        """Collect questions from SE and returns an iterator containint the items founf
        
        Args:
            n (int, optional): Number of questions to collect from the last 24 hours. Defaults to 100.            
        """

        # note that this needs to be in epoch
        time_now = datetime.datetime.now(datetime.timezone.utc)
        start_time = time_now - datetime.timedelta(hours=24)

        payload = {
            "fromdate": int(start_time.timestamp()),
            "todate": int(time_now.timestamp()),
            "site": "stackoverflow",
            "sort": "votes",
            "order": "desc",
            "tagged": self.search_terms,
            "client_id": os.environ.get("SE_client_id"),
            "client_secret": os.environ.get("SE_client_secret"),
            "key": os.environ.get("SE_key", None),
        }

        if os.environ.get("SE_key", None) is None:
            logging.info("No StackExchange API key provided, limited use may apply")

        resp = requests.get(self.main_uri, payload)

        if resp.status_code == 200:
            try:
                new_questions = self.extract_items(resp)

                logging.info(f"🐍 Collected new questions for the search term")

                return new_questions

            except (JSONDecodeError, KeyError) as e:
                logging.error(f"{e.__class__.__name__}: {e}")
        else:
            error = resp.json()["error_message"]
            logging.error(
                f"(Unable to connect to Stack Exchage: status code {resp.status_code} - {error}"
            )

    def extract_items(self, response) -> Iterator[dict]:
        """Method used to extract the response items. This returns a generator for simplicity.
        
        Args:
            response (HTTPResponse): Response from the API call
        
        Returns:
            Iterator[dict]: Generator- dictionary with the response items
        
        Yields:
            Iterator[dict]: Generator- dictionary with the response items
        """
        for question in response.json().get("items", []):
            yield {
                "question_id": question["question_id"],
                "title": question["title"],
                "is_answered": question["is_answered"],
                "link": question["link"],
                "owner_reputation": question["owner"].get("reputation", 0),
                "score": question["score"],
                "tags": question["tags"],
            }
