import os
import chainlit as cl
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

HUGGINGFACEHUB_API_TOKEN = "Your API_Key"

model_id = "gpt2-medium"
conv_model = HuggingFaceEndpoint(huggingfacehub_api_token= HUGGINGFACEHUB_API_TOKEN,
                            repo_id=model_id,
                           temperature=0.8,
                           max_new_tokens=150)

template = """You are a story writer AI assistant that completes a story based on the query received as input.

{query}
"""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, input_variables=['query'])
    conv_chain = LLMChain(
        llm=conv_model,
        prompt=prompt,
        verbose=True
    )
    cl.user_session.set("llm_chain", conv_chain)

@cl.on_message
async def handle_message(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    query = message.content

    res = await llm_chain.acall(query, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()

