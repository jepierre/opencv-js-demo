# Importing required functions
import random

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
import os

# Flask constructor
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static"


# Root endpoint
@app.route("/")
@app.route("/index")
def homepage():

    img_file_name = os.path.join(app.config["UPLOAD_FOLDER"], "lena.png")

    # Return all the charts to the HTML template
    return render_template(
        template_name_or_list="charts.html",
        user_image=img_file_name,
    )


# Main Driver Function
if __name__ == "__main__":
    # Run the application on the local development server
    app.run(debug=True)
    # to export to file use: python .\flask_blog.py > temp.html
    # with app.app_context():
        # print(homepage())
