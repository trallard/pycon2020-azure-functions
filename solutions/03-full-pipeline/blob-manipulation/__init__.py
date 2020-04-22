import logging
from pathlib import Path
import pandas as pd

import azure.functions as func

from .utils import processing

# --------------------------
# Helper methods
# --------------------------

main_path = project_dir = Path(__file__).resolve()

# --------------------------
# Main method
# --------------------------


def main(myblob: func.InputStream, sendemail: func.Out[str]):
    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Name: {myblob.name}\n"
        f"Blob Size: {myblob.length} bytes"
    )

    # pass the object
    created_file = myblob

    # read the csv file from the blob
    se_items = pd.read_csv("out.csv")

    # use the data processing methods
    processor = processing.funcprocess()

    wrangling_out = processor.data_wrangle(se_items, email=True)

    if wrangling_out != None:

        sendemail.set(wrangling_out)


if __name__ == "__main__":

    # set logging format - personal preference
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # call main function
    main()
