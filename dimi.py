from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import numpy as np
import pandas as pd
import xmltodict
from pandas import json_normalize
import urllib.request
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
from PIL import Image
import gender_guesser.detector as gender
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_book = load_lottieurl('https://assets4.lottiefiles.com/temp/lf20_aKAfIn.json')
st_lottie(lottie_book, speed=1, height=200, key="initial")


matplotlib.use("agg")

_lock = RendererAgg.lock


sns.set_style('darkgrid')
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (.1, 2, .2, 1, .1))

row0_1.title('Analyzing Your Goodreads Reading Habits')


with row0_2:
    st.write('')

row0_2.subheader(
    'DIMI Test creation')

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))

with row1_1:
    st.markdown("Hey there! Welcome to Tyler's Goodreads Analysis App. This app scrapes (and never keeps or stores!) the books you've read and analyzes data about your book list, including estimating the gender breakdown of the authors, and looking at the distribution of the age and length of book you read. After some nice graphs, it tries to recommend a curated book list to you from a famous public reader, like Barack Obama or Bill Gates. One last tip, if you're on a mobile device, switch over to landscape for viewing ease. Give it a go!")
    st.markdown(
        "**To begin, please enter the link to your [Goodreads profile](https://www.goodreads.com/) (or just use mine!).** 👇")

row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .1))
with row2_1:
    default_username = st.selectbox("Select one of our sample Goodreads profiles", (
        "89659767-tyler-richards", "7128368-amanda", "17864196-adrien-treuille", "133664988-jordan-pierre"))
    st.markdown("**or**")
    user_input = st.text_input(
        "Input your own Goodreads Link (e.g. https://www.goodreads.com/user/show/89659767-tyler-richards)")
    need_help = st.expander('Need help? 👉')
    with need_help:
        st.markdown(
            "Having trouble finding your Goodreads profile? Head to the [Goodreads website](https://www.goodreads.com/) and click profile in the top right corner.")

    if not user_input:
        user_input = f"https://www.goodreads.com/user/show/{default_username}"
