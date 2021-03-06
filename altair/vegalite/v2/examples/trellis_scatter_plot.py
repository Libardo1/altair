"""
Trellis Scatter Plot
-----------------------
This example shows how to make a trellis scatter plot.
"""

import altair as alt
from vega_datasets import data

source = data.movies.url

chart = alt.Chart(source).mark_point().encode(
    x = 'Worldwide_Gross:Q', 
    y = 'US_DVD_Sales:Q', 
    column = 'MPAA_Rating:N'
)