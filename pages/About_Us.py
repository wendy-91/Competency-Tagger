import streamlit as st
import pandas as pd
import openai
from pinecone import Pinecone
from utility import check_password

st.title("About Us")

st.subheader("Project Scope:")
st.write("The Competency Tagger project aims to develop an AI-powered platform to automate the process of tagging learning programs with relevant competencies from various Competency Frameworks. This will streamline program management for Institute Development Officers (IDOs), freeing up their time for higher-value tasks like program development and evaluation.")
