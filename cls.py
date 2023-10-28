import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
from constants import openai_key


os.environ["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"] = openai_key

template = """Question: {question}

Answer: Let's Think."""

@cl.langchain_factory(use_async=true)
def factory():
    prompt = PromptTemplate(template=template,input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain