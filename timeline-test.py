import streamlit as st
from streamlit_timeline import st_timeline

st.set_page_config(page_title="Timeline", layout="wide")

st.title("Streamlit Timeline")
st.markdown(
    """
    Streamlit component for rendering [vis.js timeline](https://github.com/visjs/vis-timeline). 
    Check out the GitHub repositories [streamlit-timeline](https://github.com/giswqs/streamlit-timeline) and 
    [streamlit-timeline-demo](https://github.com/giswqs/streamlit-timeline-demo). For JavaScript examples, 
    check out the vis.js timeline [examples](https://visjs.github.io/vis-timeline/examples/timeline/) and 
    [documentation](https://visjs.github.io/vis-timeline/docs/timeline/).
"""
)

st.header("Basic Example")

items = [
    {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
    {"id": 2, "content": "2022-10-09", "start": "2022-10-09"}
]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)

st.header("With groups")

items = [
    {
        "id": 1,
        "content": "editable",
        "editable": True,
        "start": "2022-08-23",
        "group": 1,
    },
    {
        "id": 2,
        "content": "editable",
        "editable": True,
        "start": "2022-08-23T23:00:00",
        "group": 2,
    }
]


groups = [
    {"id": 1, "content": "group 1"},
    {"id": 2, "content": "group 2"},
]

timeline = st_timeline(items, groups=groups, options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
