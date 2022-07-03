# Explicação das técnologias utilizadas

## Requests
É uma biblioteca HTTP para python. Tem a função de capturar dados de uma página web, técnica conhecida como web scraping.

### Funcionamento
- Na linha de comando: **response = requests.get('https://quotes.toscrape.com/')** requests está acessando o link via get e agregando isso na variável response  

- Na linha de comando: **content = response.content** requests está acessando o conteúdo da variável response e agregando isso a outra variável chamada content.

- Na linha de comando: **site = BeautifulSoup(content, 'html.parser')** a biblioteca BeautifulSoup está deixando visualmente legível o conteúdo da variável content em formato html e agregando o resultado a variável site.

- Na linha de comando: **reflexoes = site.findAll('div', attrs={'class': 'quote'})')** requests está procurando dentro da variável site em tags div com atributo classe igual a quote, e agregará o primeiro resultado a variável reflexoes.

- Na linha de comando: **autor = reflexao.find('small', attrs={'class': 'author'}).text** requests está fazendo uma nova busca dessa vez em tags com atributo classe igual a author e por último pegando apenas o conteúdo através do filtro .text, e agregará o primeiro resultado a variável autor.

- Na linha de comando: **for reflexao in reflexoes:** É criado um laço de repetição onde a variável reflexao irá receber o conteúdo do array reflexoes a cada volta até que chegue o último ítem.

- Na linha de comando: **print(autor)** será simplesmento mostrado o conteúdo contido na variável autor. Quando colodado em conjunto do laço for, irá imprimir uma nova posição do array a cada volta.

## Sqlite
SQLite é uma biblioteca C que fornece um banco de dados leve baseado em disco que não requer um processo de servidor separado e é o banco que vem já incluso com framework django.

### Funcionamento

- Na linha de comando: **def ConexaoBanco():** define ConexaoBanco como uma função python

- Na linha de comando: **caminho="C:\\xampp\\htdocs\\DESAFIO-FIREMAN\\db.sqlite3"** define o caminho absoluto do arquivo do banco.

- Na linha de comando: **con=None** variável de conexão.

- Na linha de comando: **con=sqlite3.connect(caminho)** con receber a conexão do sqlite3 com o caminho absoluto do banco.

- Na linha de comando:  
**except Error as ex:  
print(ex)** É mostrado algum possível erro na conexão com o banco.

- Na linha de comando: **vcon=ConexaoBanco()** É colocado a chamada da função ConexaoBranco() dentro da variável vcon.

- Na linha de comando: **vsql='INSERT INTO pensamentos_pensador (autor,fala) VALUES (nome, fala)'** É agregado a variável vsql o comando para inserir na tabela pensamentos_pensador nas colunas autor e fala os valores das variáveis nome e fala.

- Na linha de comando: **def inserir(conexao, autor, fala):** É criada uma função inserir para realizar as inserções no banco, passando como parametros conexao, autor e fala

- Na linha de comando: **c=conexao.cursor()** É agregado a variável c o comando que possibilita chamar a execução.

- Na linha de comando: **c.execute("INSERT INTO pensamentos_pensador (autor,fala) VALUES (?,?)", (autor, fala))** Executa o comando de inserção acessado atraves da variável c

- Na linha de comando: **conexao.commit()** apenas através do comit é de que de fato possibilitado que as informações sejam escritas no banco.

- Na linha de comando: **inserir(vcon, autor, fala)** É chamada a função inserir passando como parâmetrs a conexão e os dados a serem gravados (autor e fala). Posto dentro do laço de repetição irá inserir um novo dado contido nas variáveis a rada volta.

## Django Rest Framework
A estrutura Django REST é um kit de ferramentas para a construção de APIs da Web. Permite inserir novos dados inclusive atraves de interface. 

### Funcionamento
OBS: O Django Rest Framework utiliza o serializer para convertar os dados da aplicação em JSON e ainda pegar JSON e transformar em dados novamente interpretados pelo python

- Ainda na construção do projeto é utilizado a linha de comando: **pip install djangorestframework** para instalar o django rest framework.

## Django
É uma estrutura da Web Python de alto nível, uma espécie de framework de python com uma estrutura parecida com MVC, chamada de MVT por django em como um todo já se considera um controler.

- [ ] ~~MVC~~
- [x] MVT

### Funcionamento
O usuário faz uma requisição através da **URL** e o django passa essa requisição para a **View** e a **View** por sua vez acessa e retorna dados do **Model** e por ultimo mostra esses dados através do tamplate  

[Demonstração](img/django.PNG)

- Ainda na construção do projeto é utilizado a linha de comando: **python - venv** para criar um ambiente virtual, que possibilita utilizar as dependências apenas localmente no projeto.

- Também na construção do projeto é utilizado a linha de comando: **.\venv\Scripts\Activate.ps1** para ativar o ambiente virtual.

- Por fim ainda na construção inicial do projeto é utilizado a linha de comando: **django-admin startproject config .** para criar a pasta que fará o projeto funcionar e um . "ponto" para evitar criação de outras pastas.



