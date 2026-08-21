import streamlit as st
from utils import extract_pdf, create_vector_text

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


st.set_page_config(page_title="help4code placement RAG")
st.title("help4code Resume Analyzer AI")
resume_file = st.file_uploader("Upload Resume(PDF)", type=['pdf'])
jd_text = st.text_area("Paste job description")

if st.button("Resume Analysis"):
    if resume_file and jd_text:
        #Extract Resume
        resume_text = extract_pdf(resume_file)

        #combine resume and jd
        combine_text = resume_text +"\n\n" + jd_text

        #create vector store
        vectorstore = create_vector_text(combine_text)
        retriever = vectorstore.as_retriever()

        #Load and integrate ollama llm models
        llm = Ollama(model="llama3.2:latest")

        #Prompt template design
        prompt = ChatPromptTemplate.from_template("""
        You are an AI placement coach for help4code.

        Context:
        {context}

        Question:
        {question}

        provide:
        1. Overall Match Score (0-100)
         - Briefly explain the score.

        2. Skills Match
        - Skills the candidate has
        - Skills partially matching
        - Important missing skills

        3. Technology Gap
        - Technologies/tools the candidate should learn
        - Mark each as High, Medium, or Low priority.

        4. ATS Score (0-100)
        - Explain the main reasons for the score.

        5. Resume Improvements
        - Give 5 specific suggestions to improve the resume for this job.

        6. Interview Preparation
        - Give 10 technical interview questions based on the job description
          and the candidate's resume.

        7. Final Recommendation
        - Strong Match / Moderate Match / Weak Match
        - Give the top 3 actions the candidate should take next.
        """)

        chain =(
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        response = chain.invoke("Analyze resume against job description")

        st.subheader("Analysis Result")
        st.write(response)
    else:
        st.warning("Please upload resume and job description")