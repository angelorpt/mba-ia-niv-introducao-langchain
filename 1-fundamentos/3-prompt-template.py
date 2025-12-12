from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Oi, Me chamo {name}! Fala uma coisa interessante sobre meu nome."
)

text = template.format(name="Angelo")
print(text)
