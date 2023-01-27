Embeding bokeh static plots and bokeh server plots in a website using flask app:
* Run the flask app: `python app.py`
* Run bokeh server: `bokeh serve streaming_data.py  --allow-websocket-origin=127.0.0.1:5000`
* Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

For bokeh itself:
* To run bokeh server independent of flask app `bokeh serve streaming_data.py --show`
* for dev purposes to see code changes reflect in browser `bokeh serve streaming_data.py --show --dev`