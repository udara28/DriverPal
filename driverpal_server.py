from flask import Flask

application = Flask(__name__)

@application.route("/alert")
def hello():
    return "Driver Sleeping"
