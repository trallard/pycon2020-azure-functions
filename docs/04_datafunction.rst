|pipe| Data processing with functions
=========================================

We already have a working and deployed function, but so far it is not doing anything exciting.

Let's start working on the data processing part of the function.

The details
-------------
To demonstrate the capabilities of Azure functions for data processing scenarios, we will build the following pipeline:

#. Collect data from the `StackExchange API <https://api.stackexchange.com/>`_ using the timer trigger. We will focus on extracting questions from StackOverflow within a time range and with specific tags.
#. Store the raw data in our Azure storage account.
#. Trigger the processing function that cleans the data and leaves it in a usable format.

Let's get started!

Connecting to the StackExchange API
-------------------------------------

1. Create necessary files and dirs
*********************************** 

In the :ref:`functions101` section we created a basic timer function and explored the generated files.

To keep things neat we are going to create a ``utils`` folder as well and ``__init__.py`` and ``stack.py`` file in it. From the command line (bash):

.. code-block:: bash

    mkdir -p <your-function-dir>/utils
    touch <your-function-dir>/utils/__init__.py 
    touch <your-function-dir>/utils/stack.py 


2. Add methods 
*****************************

Now that we have the necessary files we have to update  ``utils/stack.py`` to handle the requests to the StackExchange API:

.. code-block:: python
    :name: utils/stack.py
    :caption: utils/stack.py

    import datetime
    import json
    import logging
    import os
    from dataclasses import dataclass
    from json import JSONDecodeError
    from typing import Optional

    import requests


    @dataclass
    class se_object:
        """Class to deal with StackExchage data collection and manipulation.
        """

        search_terms: list
        main_uri: str = "https://api.stackexchange.com/2.2/questions"

        def __repr__(self) -> str:
            return f"<Object for site {self.main_uri}>"

        def get_questions(self, n=100) -> Optional[list]:
            """Collect questions from SE and returns a list
            
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
                    new_questions = [q for q in resp.json().get("items", [])]

                    logging.info(
                        f"🐍 Collected {len(new_questions)} new questions for the search term"
                    )
                    return new_questions

                except (JSONDecodeError, KeyError) as e:
                    logging.error(f"{e.__class__.__name__}: {e}")
            else:
                error = resp.json()["error_message"]
                logging.error(
                    f"(Unable to connect to Stack Exchage: status code {resp.status_code} - {error}"
                )

Note how we use the trigger time to set the ``todate`` and ``fromdate`` in the StackExchange query. 

So we need to modify the main script for our function too:

.. code-block:: python
    :caption: __init__.py 

    import datetime
    import logging

    import azure.functions as func
    from dotenv import find_dotenv, load_dotenv
    from typing import Optional

    from .utils import stack

    # --------------------------
    # Helper methods
    # --------------------------


    def get_vars() -> Optional[bool]:
        """Collect the needed keys to call the APIs and access storage accounts.

        
        Returns:
            bool: Optional - if dotenv file is present then this is loaded, else the
            vars are used directly from the system env
        """
        try:
            dotenv_path = find_dotenv(".env")
            logging.info("Dotenv located, loading vars from local instance")
            return load_dotenv(dotenv_path)

        except:
            logging.info("Loading directly from the system")


    # -----------------------------------------
    # Main method - executed by the function
    # -----------------------------------------


    def main(mytimer: func.TimerRequest) -> None:
        """Main function to collect questions from stackexchange.
        Note that right now the site is harcoded to "StackOverflow" but this
        can be changed in stack.py
        
        Args:
            mytimer (func.TimerRequest): Timer trigger for the function, for more 
            details check function.json
        """

        # collect timestamp for the function that is being called
        utc_timestamp = (
            datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
        )

        logging.info(f"Function executing at {utc_timestamp}")

        get_vars()

        # as many search terms as wanted - must be a list
        stackexchange = stack.se_object(["python", "azure-functions"])

        se_questions = stackexchange.get_questions(n=20)


    if __name__ == "__main__":

        # set logging format - personal preference
        log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=log_fmt)

        main()

3. Tidying and finishing off
*****************************

To make it easier to identify files we will rename the function script to ``main_function.py``:

    .. image:: _static/images/snaps/main_function.png
            :align: center
            :alt: Function name

.. warning:: You also need to change the name of the ``scriptFile`` in the ``function.json`` file. Otherwise, your function is  not able to locate the file.



Finally, we need to create a ``.env`` file to store API keys and other environment variables for local development and debugging. 

.. code-block:: 
    :caption: .env

    # Stackexchange

    SE_client_id = <your secret>
    SE_client_secret = <your secret>
    SE_key = <your secret>


.. warning:: **Do not** commit this file to version control. Make sure to add ``.env`` to your ``.gitignore`` file.



|floppy| Additional resources and docs
---------------------------------------

- `Stack Exchange API docs <https://api.stackexchange.com/docs/>`_ 