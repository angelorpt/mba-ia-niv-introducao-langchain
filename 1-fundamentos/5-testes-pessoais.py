from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

template = PromptTemplate(
    input_variables=["name"],
    template="Oi, me chamo {name}. Fala uma curiosidade sobre meu nome"
)

input_name=input("Digite seu nome: ")
prompt = template.format(name=input_name)
model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
# model = init_chat_model(model="gpt-5-nano", model_provider="openai")
message = model.invoke(prompt)

print(message)
