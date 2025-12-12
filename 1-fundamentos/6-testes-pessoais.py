from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(
  model="gemini-2.5-flash",
  model_provider="google_genai",
  temperature=0.5
)

user_prompt_template = PromptTemplate(
  input_variables=["name"],
  template="Oi, me chamo {name}. Fale o significado do meu nome, e a origem dele."
)

input_name = input("Digite seu nome: ")
system_prompt = ("system", "Você é um especialista em nomes de toda a história, e seus significados.")
user_prompt = ("user", user_prompt_template.format(name=input_name))

chat_prompt = ChatPromptTemplate([system_prompt, user_prompt])
messages = chat_prompt.format_messages()

for msg in messages:
  print(f"{msg.type}: {msg.content}")


response = model.invoke(messages)
print(response.content)
print("\n\n")
print(response)

