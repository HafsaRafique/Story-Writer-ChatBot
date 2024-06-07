# Story-Writer-ChatBot
A small chatbot model based on HuggingFace API and langchain.
## HuggingFace
Go to [Hugging Face](https://huggingface.co/) and in side bar go to 'Access Tokens'. Generate an API key, name it whatever you want and copy to clipboard.
## VS Code
Check Hugging Face documentation on langchain, HuggingFaceHub and PromptTemplate as in some versions they are deprecated.
You will need to run the following commands in a terminal:
 1.   pip install transformers
 2.   pip install chainlit
 3.   pip install langchain
 4.   pip install --upgrade langchain_community
 ## Model Selection
 The model selected for this project is GPT2-Medium, a text generation model. You may choose to experiment with another model.
 ## Visualizing the ChatBot
 1. Save your file with the name 'story_writer_bot'.
 2. Now, enter the terminal and write the following (You may use any port):
    chainlit run .\story_writer_bot.py -w --port 8080
 3. If your authentication key is declared invalid, go to Hugging Face website, to 'Access Tokens'. Click on 'Manage', and refresh token.
 4. You will be taken to a chatbot interface. Enter a prompt, it should be sentence that the bot can complete.

<img src="https://github.com/HafsaRafique/Story-Writer-ChatBot/raw/main/chatbot.png" alt="Chatbot" width="50"/>

 
 
