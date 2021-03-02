## Instalação

Versão do Python:

> 3.9.2

Para criar o ambiente virtual Python, entre na pasta `server` e digite:

> python -m venv venv

Para **ativar** o ambiente virtual, digite:


> venv/Scripts/activate

Em seguida, instale os requirements:

> pip install --require-hashes -r requirements.txt



## Ambiente de desenvolvimento

Caso instale um novo pacote e necessite criar um novo requirements.txt siga os passos abaixo:


Primeiro crie o arquivo requirements.txt
> pip freeze > requirements.txt   


Em seguida o comando abaixo irá gerar os hashes.
> pip-compile requirements.txt --generate-hashes  --output-file requirements.txt

