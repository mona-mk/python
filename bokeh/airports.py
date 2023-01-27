import xyzservices.providers as xyz
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.sampledata.airport_routes import airports
from pyproj import Transformer
from bokeh.embed import components

# prepare data
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857")
airports[["x", "y"]] = airports.apply(
    lambda row: transformer.transform(row.Latitude, row.Longitude),
    axis=1,
    result_type="expand",
)
airports_data = ColumnDataSource(airports)

# instantiate figure object and add objects
f = figure(x_axis_type="mercator", y_axis_type="mercator")
f.circle(
    x="x",
    y="y",
    size=10,
    fill_color="#F46B42",
    line_color="white",
    line_width=0.5,
    source=airports_data,
)
f.add_tile(xyz.OpenStreetMap.Mapnik)

# add tooltip
hover = HoverTool(
    tooltips=[("Name", "@Name"), ("City", "@City"), ("Country", "@Country")]
)
f.add_tools(hover)

# return individual components of a standalone document to embed
airports_script, airports_div = components(f)
