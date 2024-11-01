import streamlit as st
import pandas as pd
import openai
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from pinecone import Pinecone

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Competency Tagger App"
)

# endregion <--------- Streamlit App Configuration --------->
st.title("Competency Tagger App")

# Sidebar Navigation
page = st.sidebar.success("Select a Page:")


