# ONGNautas
### Descrição: 
Aplicação Web para ONGs ambientais que visa facilitar suas operações e aumentar sua eficiência na realização de ações e projetos. A plataforma oferecerá diversas funcionalidades essenciais para o bom funcionamento da organização, bem como a transparência em relação aos recursos utilizados.

### Tecnologias Utilizadas:
- Python
- Django
- Docker
- Docker Compose
- Git

### Como usar?
Essa aplicação é dividida em perfis de projeto, sendo apenas dois perfis disponíveis para uso. Primeiro, instale as dependências. Depois, clone o repositório. Em seguida, execute o perfil de teste ou de desenvolvimento. Descrição dos passos a seguir:

##### Downloads Necessários
Para usar a aplicação, é necessário que tenha instalado em sua máquina o Git CLI, Docker Engine e o plugin Docker Compose.

* __Download Git CLI:__ [Git CLI Download](https://git-scm.com/downloads)
* __Docker Engine Download:__ [Docker Engine Download](https://docs.docker.com/engine/install/)
* __Docker Compose Plugin:__ [Docker Compose Plugin Download](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

##### Clonando o Repositório
Com as dependências instaladas, hora de clonar o repositório.
Navegando para o diretório onde deseja clonar o projeto, digite o seguinte comando:

__Usando HTTPS:__ ```git clone https://github.com/weblerson/ONGNautas.git```

__Usando SSH:__ ```git clone git@github.com:weblerson/ONGNautas.git```

<p style="color: red;">Eu recomendo usar o link SSH</p>

### Perfis de Projeto
Para utilizar os perfis de teste e desenvolvimento, certifique-se de ter o Docker e o plugin Docker Compose instalados no seu computador.

##### Perfil de Testes

Para executar o perfil de testes, siga os seguintes passos:

1. __Subindo os Serviços__
Dentro do diretório raiz do projeto, digite o comando ```docker compose -f docker-compose.test.yaml --env-file test.env up --build``` <br>
Dessa forma, automaticamente o docker vai criar o banco de testes, executar as migrações e rodar todos os testes do projeto automaticamente.
<br>

2. __Derrubando os Serviços__
Aperte o comando ```CTRL + C``` para parar os containers. Após isso, digite o comando ```docker compose -f docker-compose.test.yaml``` down para derrubar os containers completamente. Depois de fazer isso, todos os containers vão ser encerrados.
<br>
##### Perfil de Desenvolvimento

Para executar o perfil de desenvolvimento, siga os seguintes passos:

1. __Subindo os Serviços__
Dentro do diretório raiz do projeto, digite o comando ```docker compose -f docker-compose.dev.yaml --env-file dev.env up --build``` <br>
Dessa forma, todos os serviços necessários para o funcionamento do projeto vão subir e poderá acessar a aplicação navegando na url _http://localhost:8000/_
<br>
2. __Derrubando os Serviços__
Aperte o comando ```CTRL + C``` para parar os containers. Após isso, digite o comando ```docker compose -f docker-compose.dev.yaml``` down para derrubar os containers completamente. Depois de fazer isso, a aplicação não vai mais estar disponível para acesso no navegador, a menos que suba os serviços novamente.
