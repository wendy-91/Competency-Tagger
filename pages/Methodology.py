import streamlit as st

# Title of the app
st.title("Competency Tagger Flowchart")

# Display an image
st.image("Competency Tagger Flowchart.jpg", use_column_width=True)

st.subheader("Data Flow and Processing:")
st.write("**Input:** IDOs provide the learning program description through the platform's interface in the form of text.")
st.write("**Preprocessing of user inputs:** The input data is cleaned and prepared for analysis. This may involve removing irrelevant information, extracting key phrases, and standardizing formatting.")
st.write("**LLM Analysis:** The preprocessed text is fed into the LLM. The LLM analyzes the content, identifies key concepts and skills, and maps them to potential competencies within the relevant framework.")
st.write("**Competency Tag Suggestions:** The LLM generates a list of suggested competency tags with associated confidence scores.")
st.write("**IDO Review and Refinement:**  IDOs review the suggested tags, add or remove tags as needed.")

st.subheader("Implementation Details:")
st.write("**Open-AI embedding model:** Embedding texts into vectors")
st.write("**Vector Database:** A vector database is used to store vectorised competencies which are then used to compare with the IDOs vectorised input. The top 5 semantically similar results are then returned to the user.)
st.write("**User Interface Development:**  A user-friendly interface will be designed to facilitate easy interaction and feedback from IDOs.")
st.write("**System Architecture:** The platform will be built using a scalable and secure cloud-based architecture.")
st.write("**Integration and Deployment:** The system will be integrated with relevant CSC systems and deployed in a phased approach.")
