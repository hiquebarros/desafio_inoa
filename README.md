# Desafio INOA

Esse repositório é referente ao desafio proposto pela empresa INOA. O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender ativos. Para tal, ele deve registrar periodicamente a cotação atual de ativos da B3 e também avisar, via e-mail, caso haja oportunidade de negociação. Os seguintes requisitos funcionais são necessários:

•	Obter periodicamente as cotações de alguma fonte pública qualquer e armazená-las, em uma periodicidade configurável (em minutos)  para cada túnel, para consulta posterior
•	Expor uma interface web para permitir consultar os preços armazenados, configurar os ativos a serem monitorados e parametrizar os túneis de preço de cada ativo e periodicidade da checagem (em minutos) de cada ativo
•	Enviar e-mail para o investidor sugerindo Compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior, e sugerindo Venda sempre que o preço de um ativo monitorado cruzar o seu limite superior


## Table of Contents

- [Demonstração](#demonstração)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)

## Demonstração
![](https://github.com/desafio_inoa/inoa_gif.gif)

## Pré-requisitos

É necessário que você tenha as seguintes ferramentas instaladas em seu computador: Git, PIP, Python, PIP.

## Instalação

```bash
- Clone o repo:
$ git clone https://github.com/hiquebarros/desafio_inoa.git

- Crie um ambiente virtual (aqui apelidamos de venv):
$ python -m venv venv

- Ative o venv
$ venv/scripts/activate

- Instale as dependências do projeto
$ pip install -r requirements.txt

- Rode migrações
$ python manage.py migrate

- Execute o projeto (aqui estamos usando o a flag --noreload para o ambiente de desenvolvimento não iniciar a job de atualização de preços 2 vezes)
$ python manage.py runserver --noreload

```
