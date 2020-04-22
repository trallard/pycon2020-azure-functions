import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from datetime import datetime, timezone

from jinja2 import Environment, FileSystemLoader, select_autoescape
from dataclasses import dataclass

import mplcyberpunk
import matplotlib.pyplot as plt
import pandas as pd
import json
from pathlib import Path
import logging


@dataclass
class funcprocess:
    """
    Class to perform the data processing functions.
    """

    def data_json(self, dataframe):
        """Create a  json from the dataframe for use by the jinja2 template
        
        Args:
            dataframe (df): clean dataset
        
        Returns:
            json: json version of the dataframe with the SE items
        """

        return json.loads(dataframe.to_json(orient="records"))

    def email_body(self, answered, unanswered):

        unanswered_json = self.data_json(unanswered)
        answered_json = self.data_json(answered)
        date_now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

        dir_path = project_dir = Path(__file__).resolve().parent
        template_path = dir_path.joinpath("templates")

        logging.info(f"Templates located in {template_path}")

        env = Environment(
            loader=FileSystemLoader(template_path),
            autoescape=select_autoescape(["html", "xml"]),
        )

        template = env.get_template("body.html")
        rendered_template = template.render(
            date_now=date_now,
            answered=unanswered_json,
            unanswered=answered_json,
            image_path="",
        ).replace("\n", "")

        with open(template_path.joinpath("tests.html"), "w") as f:
            f.write(rendered_template)

        return rendered_template

    def create_email(self, answered, unanswered):
        to_email = os.environ.get("receiver")
        from_email = os.environ.get("sender")
        subject = "Your daily digest - StackExchange"

        body = self.email_body(answered, unanswered)

        # Sendgrid
        message = {
            "personalizations": [
                {"to": [{"email": to_email}]},
                {"from": [{"email": from_email}]},
            ],
            "subject": subject,
            "content": [{"type": "html", "value": body}],
        }

        return json.dumps(message)

    def clean_data(self, dataframe):

        processed = dataframe.copy()
        processed.sort_values(by=["owner_reputation"], inplace=True, ascending=False)

        processed["tags"] = processed["tags"].map(
            lambda x: x.lstrip("[")
            .rstrip("]")
            .replace(r"'", "")
            .replace(r",", "")
            .replace(r"python", "")
            .replace(r"machine-learning", "")
            .split()
        )

        return processed

    def is_answered(self, dataframe):
        unanswered = (
            dataframe.loc[dataframe["is_answered"] == False]
            .copy()
            .drop(columns=["is_answered"])
        )

        answered = (
            dataframe.loc[dataframe["is_answered"] == True]
            .copy()
            .drop(columns=["is_answered"])
        )

        return answered, unanswered

    def create_plot(self, dataframe):
        import mplcyberpunk
        import matplotlib.pyplot as plt
        import vapeplot

        # general settings
        plt.style.use("cyberpunk")
        vapeplot.set_palette("cool")
        plt.rcParams["axes.linewidth"] = 0.8
        plt.rcParams.update({"font.size": 16})
        foreground = "#efefef"

        # creating the plot
        fig = plt.figure(figsize=(16, 12))
        ax = (
            pd.Series([item for sublist in dataframe.tags for item in sublist])
            .value_counts()
            .plot(kind="barh")
        )

        # customise
        ax.set_ylabel("Tags", fontsize=18, fontweight="black", color=foreground)
        ax.set_xlabel("Count", fontsize=18, fontweight="black", color=foreground)
        ax.spines["left"].set_smart_bounds(True)
        ax.spines["bottom"].set_smart_bounds(True)
        ax.spines["top"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["bottom"].set_color(foreground)
        ax.spines["left"].set_color(foreground)

        date_now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
        fig_path = f"{date_now}-tags-count.png"

        fig.savefig(fig_path, dpi=fig.dpi, bbox_inches="tight")

        return fig_path

    def data_wrangle(self, dataframe, email=True):
        """Call the helper methods to process the data in the Blob
        
        Args:
            dataframe (df): Dataframe with the SE items
        """

        processed = self.clean_data(dataframe)

        # split if answered or not
        answered, unanswered = self.is_answered(processed)

        # create plots
        fig_path = self.create_plot(processed)

        if email == True:

            email_item = self.create_email(answered, unanswered)

            return email_item

        else:
            logging.info("Not sending emails")
