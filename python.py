# api="AIzaSyAicy4xhrZbSporHM6t-PyJLausFf4UbZw"

import PIL.Image
from dotenv import load_dotenv

import os
import google.generativeai as genai
import pathlib
import textwrap

import google.generativeai as genai
from rich import print
from IPython.display import display
from IPython.display import Markdown
# Used to securely store your API key
# from google.colab import userdata
load_dotenv()
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro')



for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return textwrap.indent(text, '> ', predicate=lambda _: True)


# model = genai.GenerativeModel('gemini-pro')

# %%time
# response = model.generate_content("What is the meaning of life?")

# Input a text string and get a response

# input_text = input("Enter your worries ... ")

# %% time
# response = model.generate_content(input_text, stream=True)
# # to_markdown(response.text)
# for chunk in response:
#   print(chunk.text)
#   print("_"*80)

# print(to_markdown(response.text))

# Taking in an image now and display the output 


# img = PIL.Image.open('image.jpg')
# model = genai.GenerativeModel('gemini-pro-vision')

# response = model.generate_content(["Write a short engaging block with this picture", img])

# print(to_markdown(response.text))


# chart section with germini pro

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# response = chat.send_message(
#     "In one sentence, explain how a computer works to a young child.")
# print(to_markdown(response.text))
