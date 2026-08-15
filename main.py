#from openai import OpenAI 
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

#client = OpenAI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question = input("Entrer votre question: ")

# reponse = client.chat.completions.create(
#     model = "gpt-4o-mini",
#     messages = [{"role": "user", "content":question},{"role":"system", "content":"Tu es un assistant de programmation"}],
# )
# print(reponse.choices[0].message.content)

reponse = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question,
)
print(reponse.text)