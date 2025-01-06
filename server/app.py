# TODO: This will be the app server.
from flask import Flask, render_template, request, Response


app = Flask(__name__)


def twiml_response(body: str):
    return Response(body, content_type="application/xml")


@app.route("/welcome")
def welcome_message():
    return twiml_response(
        render_template("welcome.xml.j2", hostname=request.host_url.rstrip("/"))
    )

@app.route("/play_stream")
def play_stream():
    return twiml_response(
        render_template("play_stream.xml.j2")
    )


if __name__ == "__main__":
    app.run(debug=True)
