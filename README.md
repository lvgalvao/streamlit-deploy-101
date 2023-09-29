# Projeto Streamlit: Transformando Jupyter Notebook em Aplicação Web

Este projeto busca ilustrar a transformação de um Jupyter Notebook em uma aplicação web completa usando o framework Streamlit. A ideia é fornecer um guia para aqueles que desejam levar seus projetos de análise de dados para um ambiente de produção de forma eficiente e interativa.

## Tópicos Abordados

* Introdução ao conceito de deploy.
* Análise de frameworks Python para desenvolvimento web.
* Utilização do Streamlit para criar aplicações interativas.
* Uso de caching para otimizar o desempenho.
* Introdução à gestão de variáveis de ambiente para maior segurança.

## Pré-requisitos

* Python 3.7+
* Streamlit
* Pandas

## Como Executar

1. Clone o repositório para a sua máquina local.

```bash
git clone git@github.com:lvgalvao/streamlit-deploy-101.git
```

2. Navegue até a pasta do projeto.

```bash
cd streamlit-deploy-101
```

3. Instale as dependências.

```bash
pip install -r requirements.txt
```

4. Execute o app Streamlit.

```bash
streamlit run app.py
```

## Estrutura do Projeto

* `app.py`: Arquivo principal da aplicação Streamlit.
* `.env`: (Não incluído por motivos de segurança) Contém variáveis de ambiente e configurações sensíveis.
* `requirements.txt`: Lista de pacotes Python necessários para executar o projeto.

## Conclusão

Streamlit oferece uma maneira incrivelmente rápida e eficaz de transformar análises de dados em aplicações web interativas. Este projeto serve como um guia inicial para aqueles que desejam explorar esta ferramenta poderosa.