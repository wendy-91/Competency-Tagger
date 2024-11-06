import streamlit as st
import pandas as pd
import openai
from pinecone import Pinecone
from utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Competency Tagger App"
)

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit App Configuration --------->
st.title("Competency Tagger App")
st.text_area("<b>IMPORTANT NOTICE:</b> This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalized advice.")

# --- Configuration ---
openai.api_key = st.secrets["openai_api_key"]  # Replace with your actual key
pinecone = Pinecone(api_key=st.secrets["pinecone_api_key"], environment="Default")  # Initialize Pinecone
index_name = st.secrets["pinecone_index"]  # Replace with your Pinecone index name

# --- Query ---
index = pinecone.Index(index_name)

# Get user input
query_text = st.text_area(
    "nter your programme details here:",
    placeholder="Programme Title:\nProgramme Outline:\nProgramme Activities:",
    height=200  # You can adjust the height as needed
)

if st.button("Submit"):
    # Generate embedding for the query
    query_embedding = openai.embeddings.create(input=query_text, model="text-embedding-ada-002").data[0].embedding
    
    # Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True  # Include metadata if you stored any
    )
    
    # --- Process results ---
    for match in results.matches:
        #st.write(f"Match ID: {match.id}")
        #st.write(f"Score: {match.score}")
        # Assuming you stored the original text in the metadata
        if "original_text" in match.metadata:
            st.write(f"{match.metadata['original_text']}".replace("%%%","  \n").replace("Framework:","**Framework:**").replace("Competency Name:","**Competency Name:**").replace("Proficiency Level:","**Proficiency Level:**").replace("Behavioural Indicator:","**Behavioural Indicator:**"))
        st.write("---")
