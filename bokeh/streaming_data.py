from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import layout
from math import pi, cos, sin, radians
import numpy as np


# prepare data
data = {}
for i, r in enumerate(range(1, 4)):
    data[f"x{i}"] = [r * cos(t) for t in np.linspace(0, 2 * pi, num=50)]
    data[f"y{i}"] = [r * sin(t) for t in np.linspace(0, 2 * pi, num=50)]
source0 = ColumnDataSource(data)
source1 = ColumnDataSource(data={"x": [], "y": [], "theta": []})
source2 = ColumnDataSource(data={"x": [], "y": [], "theta": []})

# plot circles & customise
f = figure(x_range=(-4, 4), y_range=(-4, 4))
f.line("x0", "y0", line_color="yellow", source=source0)
f.circle(
    x=0, y=0, radius=1, fill_color="yellow", line_color=None
)  # not exact radius
f.line("x1", "y1", line_color="black", source=source0)
f.line("x2", "y2", line_color="black", source=source0)
# NB. Bokeh circle won't be exact when you want to overlay two objects.

# plot small circle
f.scatter(
    x="x",
    y="y",
    marker="circle",
    size=10,
    line_color=None,
    fill_color="red",
    source=source1,
)
f.scatter(
    x="x",
    y="y",
    marker="circle",
    size=20,
    line_color=None,
    fill_color="green",
    source=source2,
)


def point_on_circle(theta, r):
    x = [r * cos(theta)]
    y = [r * sin(theta)]
    return {"x": x, "y": y, "theta": [theta]}


theta = 0


def update():
    global theta
    theta += 0.1
    source1.stream(point_on_circle(theta, 2), rollover=1)  # add some lag
    source2.stream(point_on_circle(theta, 3), rollover=1)


# Add user input phase lag
select = Select(
    title="Phase lag:", value="0", options=["0", "90", "180", "270"]
)


def select_update(attr, old, new):
    global theta
    # get current angle and add the phase lag
    phase_lag = radians(float(select.value))
    theta = float(source1.data["theta"][0]) + phase_lag


select.on_change("value", select_update)

curdoc().add_root(layout([[f], [select]]))
curdoc().add_periodic_callback(update, 1000)
