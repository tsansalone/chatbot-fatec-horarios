# Assistente de Horários - FATEC PG - 2025/1

## Descrição do Projeto
Este é um chatbot desenvolvido em Python que utiliza a API da OpenAI para responder a perguntas sobre um contexto específico relacionado aos horários da FATEC Praia Grande. O chatbot permite que o usuário faça até três perguntas sobre o tema e, ao final, gera um resumo das respostas fornecidas.

## Tecnologias Utilizadas
- Python
- OpenAI API
- Panel (para interface gráfica)
- dotenv (para carregar variáveis de ambiente)

## Como Executar o Projeto
### Requisitos
- Python 3.8+
- Conta e chave de API da OpenAI
- Bibliotecas necessárias (pode ser instalado via `pip install -r requirements.txt`)

### Passos para Execução
1. Clone este repositório:
   ```sh
   git clone https://github.com/tsansalone/chatbot-fatec-horarios.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd chatbot-fatec-horarios
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):

    [Como criar e utilizar ambientes virtuais](https://docs.python.org/pt-br/3.13/tutorial/venv.html/)

4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

5. Copie o arquivo `.env.example` para `.env`:
   ```sh
   cp .env.example .env
   ```
6. Edite o arquivo `.env` e adicione sua chave de API da OpenAI:
   ```sh
   OPENAI_API_KEY=SUA_API_KEY_AQUI
   ```
7. Execute o chatbot:
   ```sh
   python chatbot.py
   ```
8. O chatbot estará disponível em `http://localhost:80` no navegador.


## Demonstração

[![](https://markdown-videos-api.jorgenkh.no/vimeo/1068608825)](https://vimeo.com/1068608825/bc4924518b?share=copy)
