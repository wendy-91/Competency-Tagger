# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
import openai
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from pinecone import Pinecone

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Competency Framework App"
)
# Sidebar Navigation
page = st.sidebar.success("Select a Page:")

# --- Configuration ---
openai.api_key = st.secrets["openai_api_key"]  # Replace with your actual key
pinecone = Pinecone(api_key=st.secrets["pinecone_api_key"], environment="Default")  # Initialize Pinecone
index_name = st.secrets["pinecone_index"]  # Replace with your Pinecone index name

# --- Query ---
index = pinecone.Index(index_name)

# Title of page
st.title("Competency Tagger")

# Get user input
query_text = st.text_area(
    "Enter your programme details here:",
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


# --- Model Training Section ---
st.subheader("Train Model for Improved Accuracy")
train_model = st.button("Train Model")

if train_model:
    # Simulated data for training (in practice, replace this with your actual dataset)
    texts = ["Example sentence 1", "Example sentence 2"]
    labels = [0, 1]  # Example binary labels

    # Load tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    # Create a custom dataset (this is simplified for illustration)
    class TextDataset(torch.utils.data.Dataset):
        def __init__(self, texts, labels, tokenizer):
            self.texts = texts
            self.labels = labels
            self.tokenizer = tokenizer

        def __len__(self):
            return len(self.texts)

        def __getitem__(self, idx):
            encoding = self.tokenizer(self.texts[idx], padding='max_length', truncation=True, return_tensors='pt')
            item = {key: val.squeeze() for key, val in encoding.items()}
            item['labels'] = torch.tensor(self.labels[idx])
            return item

    dataset = TextDataset(texts, labels, tokenizer)
    
    # Train the model
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=2,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    trainer.train()
    st.success("Model training completed!")
