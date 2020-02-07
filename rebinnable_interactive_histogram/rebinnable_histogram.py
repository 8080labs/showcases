# %% [markdown]
# # How to interactively rebin your histograms on the fly
#
# In this notebook we use the [NYCFlights13](https://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf) dataset, which contains information on all flights that departed NYC in 2013 (over 300,000 flights in total). To explore how to rebin a plotly histogram on the fly, we will visualize the distribution of **arrival delays in minutes**.

# %%
import pandas as pd
import plotly.graph_objs as go
import ipywidgets as widgets

# %%
df = pd.read_csv("../data/flights.csv")


# %% [markdown]
# ## The starting point - an interacive histogram
#
# Here, we need to set the binwidth in the code.

# %%
def interactive_histogram(df, column_name):
    series = df[column_name]

    # Change size to anything you want in order to adjust the binwidth, e.g. xbins={"size": 5}
    trace = go.Histogram(x=series, xbins={"size": None})
    figure_widget = go.FigureWidget(
        data=[trace],
        layout=go.Layout(
            yaxis={"title": "Count"},
            xaxis={"title": column_name},
            bargap=0.05,
        )
    )

    return figure_widget

interactive_histogram(df, "arr_delay")


# %% [markdown]
# ## Choose bin width interactively on the fly
#
# Adding an interactive slider to the histogram allows us to interactively change the bin width.

# %%
def rebinnable_interactive_histogram(df, column_name):
    DEFAULT_BINWIDTH = 10

    series = df[column_name]

    trace = go.Histogram(x=series, xbins={"size": DEFAULT_BINWIDTH})
    figure_widget = go.FigureWidget(
        data=[trace],
        layout=go.Layout(
            yaxis={"title": "Count"},
            xaxis={"title": column_name},
            bargap=0.05,
        )
    )

    bin_slider = widgets.FloatSlider(
        value=DEFAULT_BINWIDTH,
        min=1,
        max=30,
        step=1,
        description="Bin width:",
        readout_format=".0f"  # display as integer
    )

    histogram_object = figure_widget.data[0]

    def set_bin_size(change):
        histogram_object.xbins = {"size": change["new"]}
    bin_slider.observe(set_bin_size, names="value")

    return widgets.VBox([figure_widget, bin_slider])


rebinnable_interactive_histogram(df, "arr_delay")

# %%
