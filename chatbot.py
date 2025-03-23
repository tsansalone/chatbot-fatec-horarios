import openai
import os
from dotenv import load_dotenv, find_dotenv
import panel as pn

_ = load_dotenv(find_dotenv())
API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=API_KEY)

nPerguntas = 0
pn.extension()
panels = []

with open('context/grade.txt', 'r',encoding='windows-1252') as f:
    grade_data = f.read()

with open('context/apresentacao.txt', 'r',encoding='windows-1252') as f:
    apresentacao = f.read()

context = [{'role': 'system', 'content':grade_data}]

inp = pn.widgets.TextInput(value="Olá", placeholder='Digite sua dúvida aqui')
button_conversation = pn.widgets.Button(name="Enviar")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

def collect_messages(_):
    global nPerguntas
    prompt = inp.value_input
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    if prompt == '':
        context.append({'role': 'user', 'content': f"{apresentacao}"})
    response = get_completion_from_messages(context)

    context.append({'role': 'assistant', 'content': f"{response}"})
    if(prompt != ''):
        panels.clear()
        panels.append(
            pn.Row('**Usuário**:', pn.pane.Markdown(prompt, width=600)))
        nPerguntas += 1
    panels.append(
        pn.Row('**Assistante**:', pn.pane.Markdown(response, width=600)))

    if nPerguntas == 3:
        summary_prompt = "Por favor, resuma as 3 respostas anteriores."
        context.append({'role': 'user', 'content': summary_prompt})
        summary_response = get_completion_from_messages(context)
        panels.append(pn.Row('**Assistente (Resumo):**', pn.pane.Markdown(summary_response, width=600)))
        nPerguntas = 0
    return pn.Column(*panels)

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    pn.panel(interactive_conversation, loading_indicator=True, scroll=True),
    pn.Row(inp, button_conversation),
)
dashboard.show("Assistente de Horários - FATEC PG - 2025/1", port=80)