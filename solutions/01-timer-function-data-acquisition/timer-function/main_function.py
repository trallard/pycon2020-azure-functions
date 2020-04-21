import datetime
import logging
from typing import Optional

import azure.functions as func
from dotenv import find_dotenv, load_dotenv

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
        logging.info("Loading directly from system")


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
