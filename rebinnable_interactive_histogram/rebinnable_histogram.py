# %% [markdown]
# # How to interactively rebin your histograms on the fly

# %%
import pandas as pd
import plotly.graph_objs as go
import ipywidgets as widgets

# %%
df = pd.read_csv("../data/flights.csv")


# %% [markdown]
# ## The bare minimum

# %%
def rebinnable_interactive_histogram(series, initial_bin_width=10):
    figure_widget = go.FigureWidget(
        data=[go.Histogram(x=series, xbins={"size": initial_bin_width})]
    )

    bin_slider = widgets.FloatSlider(
        value=initial_bin_width,
        min=1,
        max=30,
        step=1,
        description="Bin width:",
        readout_format=".0f",  # display as integer
    )

    histogram_object = figure_widget.data[0]

    def set_bin_size(change):
        histogram_object.xbins = {"size": change["new"]}

    bin_slider.observe(set_bin_size, names="value")

    output_widget = widgets.VBox([figure_widget, bin_slider])
    return output_widget


# %%
rebinnable_interactive_histogram(df["air_time"])


# %% [markdown]
# ## With a bit of styling to get you started

# %%
def rebinnable_interactive_histogram(series, initial_bin_width=10):
    trace = go.Histogram(x=series, xbins={"size": initial_bin_width})
    figure_widget = go.FigureWidget(
        data=[trace],
        layout=go.Layout(yaxis={"title": "Count"}, xaxis={"title": "x"}, bargap=0.05,),
    )

    bin_slider = widgets.FloatSlider(
        value=initial_bin_width,
        min=1,
        max=30,
        step=1,
        description="Bin width:",
        readout_format=".0f",  # display as integer
    )

    histogram_object = figure_widget.data[0]

    def set_bin_size(change):
        histogram_object.xbins = {"size": change["new"]}

    bin_slider.observe(set_bin_size, names="value")

    output_widget = widgets.VBox([figure_widget, bin_slider])
    return output_widget


# %%
rebinnable_interactive_histogram(df["air_time"])

# %%
