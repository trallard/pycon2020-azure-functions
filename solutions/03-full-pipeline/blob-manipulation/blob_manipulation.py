import logging
from pathlib import Path
from typing import Iterator, Optional

import azure.functions as func
import pandas as pd

from .utils import processing

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


# --------------------------
# Main method
# --------------------------


def main(
    myblob: func.InputStream,
    sendemail: func.Out[str],
    context: func.Context,
    outputBlob: func.Out[bytes],
):
    logging.info(
        f"⚡️ Python blob trigger function processed blob \n"
        f"Name: {myblob.name}\n"
        f"Blob Size: {myblob.length} bytes"
    )

    get_vars()

    # pass the object
    created_file = myblob

    try:
        # read the csv file from the blob
        se_items = pd.read_csv(created_file)
    except OSError as e:
        logging.error(f"EXCEPTION: Unable to read input: {e}")
        sys.exit(254)
    except Exception as e:
        logging.error(f"EXCEPTION: {e}")
        sys.exit(255)

    # use the data processing methods
    processor = processing.funcprocess()

    wrangling_out = processor.data_wrangle(se_items, email=True)

    if len(wrangling_out) == 2:

        sendemail.set(wrangling_out[1])
        logging.info("📨 Email has been sent")

    # stores in the Blob container
    with open(wrangling_out[0], "rb") as f:

        outputBlob.set(f.read())
        f.close()


if __name__ == "__main__":

    # set logging format - personal preference
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # call main function
    main()
