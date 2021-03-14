# Instalação

Versão do Python 3.9.2

Para criar o ambiente virtual Python, entre na pasta `server` e digite:

> python -m venv venv

Para **ativar** o ambiente virtual, digite:

Obsercacao: O ponto '.' no inicio do comando so deve ser usado em terminais 'bash'.

#### No Windows:
>. venv/Scripts/activate

#### No Linux ou MacOS:
>source venv/bin/activate 

Você vai observar que o ambientenvirtual está ativo pq vai aparecer o nome da maquina virtual assim: (venv) 

Em seguida, instale os requirements:
> pip install --require-hashes -r requirements.txt

Rode as migrations:
> python manage.py migrate

.

# Ambiente de desenvolvimento

Para rodar o projeto:
> python manage.py runserver  

Agora vc pode acessar as rotas localmente

E para acessar o admin, não pare o servidor, em outro terminal, ative a maquina virtual e rode o comando:
>
> (venv) $ python manage.py createsuperuser

```
    Username: <seu usuario>
    Email address: seuemail@email.com
    Password:
    Password (again):
```
Se tudo estiver okay, vai aparecer
```
    Superuser created successfully.
```
# Importante!
Caso instale um novo pacote e necessite criar um novo requirements.txt siga os passos abaixo:


Primeiro crie o arquivo requirements.txt
> pip freeze > requirements.txt   


Em seguida o comando abaixo irá gerar os hashes.
> pip-compile requirements.txt --generate-hashes  --output-file requirements.txt

