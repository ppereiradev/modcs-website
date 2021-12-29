# MoDCS - Projeto do Novo Website
Aqui estaremos construíndo a nova versão do Website do MoDCS.

# Pré-requisitos
Para poder rodar esse projeto, primeiro você deve ter o docker e o docker-compose instalado na sua máquina. Caso você ainda não tenha instalado o docker e o docker-compose, veja esse [tutorial](https://dev.to/semirteskeredzic/docker-docker-compose-on-ubuntu-20-04-server-4h3k), siga esses passos e configure de forma que não precise usar o `sudo` para executar o docker.

# Executando
Uma vez que o docker e o docker-compose esteja instalado na sua máquina, clone esse repositório, acesse o diretório `modcs-website`, e altere o arquivo `env-sample` e salve como `.env` para que o docker-compose encontre as variáveis de ambiente que serão usadas no container.

Após isso, execute o seguinte comando:
```bash
foo:~/modcs-website$ docker-compose up -d
```
Verifique se dois containers estão rodando com o comando:
```bash
foo:~/modcs-website$ docker ps
```
A saída deverá ser similiar a isso:
```bash
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                           NAMES
5764a7ca4fc6   modcs_website:0.1.0   "sh -c 'python manag…"   47 minutes ago   Up 47 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp       modcs_website
fdb323487a4d   mongo:latest          "docker-entrypoint.s…"   47 minutes ago   Up 47 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   modcs_website_mongo
```
Se estiver assim, tudo está funcionando como esperado, aguarde uns 2 minutos para poder dar tempo de o servidor Django fazer a migração de seus componentes para o banco de dados, e então acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) que o projeto do novo site do MoDCS provavelmente estará rodando.

# Estrutura dos diretórios
```console
.
├── ...
├── app
│   ├── accounts                    # não iremos mexer por agora mas conterá as páginas para acesso à área restrita
│   ├── dashboard                   # não iremos mexer por agora mas conterá os dashboards
│   ├── static                      # ingore por enquanto
│   ├── templates                   # ingore por enquanto
│   ├── website                     # onde vamos trabalhar, aqui é onde iremos passar a maior parte do tempo inicialmente
|   │    ├── urls.py                # cada nova página que criarmos temos que adicionar aqui o mapeamento da url dela para o método da view.py
|   │    ├── views.py               # toda nova página que criamos temos que adicionar um método na view.py para mapear para o arquivo
|   │    ├── models.py              # pode ingorar
|   │    ├── static                 # static files (css, js, img)
|   │    │   ├── css                # css files
│   |    |   |    ├── style.css     # style css file
│   |    |   |    └── ...
│   |    |   ├── js                 # js files
│   |    |   |    ├── script.js     # main js file
│   |    |   |    └── ...
│   |    |   ├── assets             # images folder
│   |    |   |    ├── favicon.ico   # image file
│   |    |   |    └── ...
│   |    |   └── ...
│   |    ├── templates              # aqui colocaremos nossas páginas html
│   |    |   ├── index.html         # html file
│   |    |   ├── about.html         # html file
│   |    |   └── ...
│   |    └── ...                    # etc.
│   ├── modcs_prod                  # arquivos docker que utilizaremos quando formos fazer o deploy do novo site do MoDCS, pode ignorar por enquanto
│   ├── nginx                       # arquivos do nginx que utilizaremos quando formos fazer o deploy do novo site do MoDCS, pode ignorar por enquanto
│   ├── .gitignore                  # lista de arquivos que o git irá ignorar quando formos fazer os commits
│   ├── docker-compose.yml          # arquivo de configuração para a criação dos nossos containers no ambiente de desenvolvimento, aqui só estamos criando o container da aplicação Django e do mongodb
│   ├── Dockerfile                  # arquivo do docker para a criação da imagem do nosso container de desenvolvimento
│   ├── env-sample                  # arquivo de exemplo para a criação do arquivo .env, esse arquivo .env é necessário para que você possa executar o projeto e representa as variáveis de ambiente que serão utilizadas nos containers
│   ├── Jenkinsfile                 # arquivo do jenkins, para integração contínua, pode desconsiderar por enquanto
│   ├── README.md                   # nosso famoso README.md
│   ├── requirements.txt            # lista dos pacotes necessários do python para poder rodar nosso projeto
|   └── ...
└── ...
```

# Guidelines
Não sobrescreva a branch principal do repositório (`main`), sempre que for fazer alguma alteração crie uma nova branch, trabalhe em cima dela e quando achar que ela está boa faça um pull request (PR) para o repositório. Então podemos revisar e sugerir alterações se necessário!

Na dúvida, sempre pergunte antes de fazer o push!

# Bem-vindo ao Django!
Espero que vocês gostem do Django e que a gente consiga fazer um site massa para o professor Paulo Maciel.
