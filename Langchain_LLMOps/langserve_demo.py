import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from langserve import add_routes
import uvicorn

_ = load_dotenv(find_dotenv())
llm = ChatGroq(
    model="llama3-70b-8192"
)

parser = StrOutputParser()

system_template = "You are an expert in Theory of Computation (TOC). Answer the following question."

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{question}')
])

chain = prompt_template | llm | parser

app = FastAPI(
  title="TOCQuestionAnswering",
  version="1.0",
  description="A simple API server for answering Theory of Computation questions using LangChain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
