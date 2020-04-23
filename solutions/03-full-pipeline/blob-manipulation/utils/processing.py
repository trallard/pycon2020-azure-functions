import base64
import json
import logging
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import mplcyberpunk
import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


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

    def email_body(self, answered, unanswered, fig_path):

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

        img_b64 = self.encode_img(fig_path)

        template = env.get_template("body.html")
        rendered_template = template.render(
            date_now=date_now,
            answered=unanswered_json,
            unanswered=answered_json,
            img_b64=img_b64,
        ).replace("\n", "")

        with open(template_path.joinpath("tests.html"), "w") as f:
            f.write(rendered_template)

        return rendered_template

    def encode_img(self, fig_path):

        with open(fig_path, "rb") as f:
            img = f.read()
            img_base64 = base64.encodestring(img).decode("utf-8")

            f.close()

        return img_base64

    def create_email(self, answered, unanswered, fig_path):
        to_email = os.environ.get("receiver")
        from_email = os.environ.get("sender")
        subject = "Your daily digest - StackExchange"

        body = self.email_body(answered, unanswered, fig_path)

        # Sendgrid
        message = {
            "personalizations": [{"to": [{"email": to_email}]}],
            "subject": subject,
            "from": {"email": from_email},
            "content": [{"type": "text/html", "value": body}],
            # "attachments": [
            #     {
            #         "content": img,
            #         "content_id": "tag_plots",
            #         "disposition": "inline",
            #         "filename": fig_path,
            #         "name": "Popular tags",
            #         "type": "image/png",
            #     }
            # ],
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
        plt.rcParams.update({"font.size": 12})
        foreground = "#efefef"

        # creating the plot
        fig = plt.figure(figsize=(16, 12))
        ax = (
            pd.Series([item for sublist in dataframe.tags for item in sublist])
            .value_counts()
            .head(n=15)
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

            email_item = self.create_email(answered, unanswered, fig_path)

            outputs = [fig_path, email_item]

            return outputs

        else:

            outputs = [fig_path]

            return outputs
