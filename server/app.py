# TODO: This will be the app server.
from flask import Flask, render_template, Response


app = Flask(__name__)


def twiml_response(body: str):
    return Response(body, content_type="application/xml")


@app.route("/welcome")
def welcome_message():
    return twiml_response(
        render_template("welcome.xml.j2", hostname="https://example.org")
    )


if __name__ == "__main__":
    app.run(debug=True)
