# Pokédex Desafio

Este é um projeto de uma Pokédex simples em Python, construída com Flask e usando um banco de dados MySQL. Neste aplicativo, os treinador possui cadastro único onde pode cadastrar seus Pokémons, e visualizar as características desses Pokémons. Cada Pokémon possui um número sequencial na Pokédex, até dois tipos entre os 18 tipos existentes, e pode ser marcado como capturado pelo treinador. Além disso, cada Pokémon possui um grito característico, uma foto de frente e uma foto de trás.

## Tecnologias Usadas

- Python
- Flask
- MySQL (banco de dados)
- HTML e Jinja2 (para templates)
- Bootstrap (Framework)

## Instalação

Siga as etapas abaixo para configurar o ambiente de desenvolvimento e executar o aplicativo:

1. Abra o git bash e clone o repositorio:

   ```bash
   git clone https://github.com/carlorique/desafio_projex.git
   cd desafio_projex/
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   # No Windows, use venv/Scripts/activate #No Linux, use source venv/bin/activate
3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
4. Inicialize o banco de dados:
   ```bash
   python form_db.py
5. Inicie o servidor Flask:
   ```bash
   python app.py # Ou flask run :)
   
## Uso
- No aplicativo, os treinadores podem cadastrar, editar e deletar seus Pokémons.
- Eles podem visualizar as características de cada Pokémon, editar as caracteristicas, inserir uma foto(em processo) de cada Pokémon.

## Experiencia 

Aprender Flask em 7 dias pode ser desafiador, mas com dedicação e determinação, consegui me apaixonar por essa tecnologia. Admito que foi um projeto desafiador e que não foi fácil. Com base nos meus conhecimentos básicos, fiz o meu melhor, embora algumas funcionalidades tenham ficado pendentes. No entanto, consegui compreender o funcionamento das rotas, a criação de templates e como isso faz toda a diferença na estruturação do código. Estou orgulhoso do progresso que fiz e animado para continuar aprendendo e aprimorando minhas habilidades no Flask.
