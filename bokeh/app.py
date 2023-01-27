from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session
from airports import airports_div, airports_script

app = Flask(__name__)


@app.route("/")
def hello():
    # unique id to keep users from stomping on each other
    with pull_session(url="http://localhost:5006/streaming_data") as session:
        bokeh_script = server_session(
            None,
            url="http://localhost:5006/streaming_data",
            session_id=session.id,
        )
        return render_template(
            "index.html",
            bokeh_script=bokeh_script,
            airports_div=airports_div,
            airports_script=airports_script,
        )


if __name__ == "__main__":
    app.run(debug=True)
