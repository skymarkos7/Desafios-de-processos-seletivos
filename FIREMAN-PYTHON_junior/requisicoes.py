import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error


response = requests.get('https://quotes.toscrape.com/') 

content = response.content

site = BeautifulSoup(content, 'html.parser')


#criar conexão com banco
def ConexaoBanco():
    caminho="C:\\xampp\\htdocs\\DESAFIO-FIREMAN\\db.sqlite3"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon=ConexaoBanco()    

vsql='INSERT INTO pensamentos_pensador (autor,fala) VALUES (nome, fala)'

# inserir dados
def inserir(conexao, autor, fala):
    try:
        c=conexao.cursor()
        c.execute("INSERT INTO pensamentos_pensador (autor,fala) VALUES (?,?)", (autor, fala))
        conexao.commit()
        print("Registro inserido")
    except Error as ex: 
        print(ex)   

# obtendo o conjunto de reflexao
reflexoes = site.findAll('div', attrs={'class': 'quote'})

for reflexao in reflexoes:

# obtendo o autor e mostrando
    autor = reflexao.find('small', attrs={'class': 'author'}).text           
    print(autor)
   
# obtendo e mostrando a citação
    fala = reflexao.find('span', attrs={'class': 'text'}).text   
    print(fala)

#inserindo no banco em cada repetição do laço
    inserir(vcon, autor, fala)

#organizando com um espaço
    print()
    