# Esse documento tem o objetivo de explicar o processo de criação dessa aplicação

1. Instalar python:
   - Baixar via arquivo download e instalar
   - Baixar pelo terminal com 'which python'

2. Instalar biblioteca requests:  
   - Usando o camando 'pip install requests' 
>pip é o gerenciador de pacotes do python, assim como o 'npm' do node

3. Instalando virtual env
   - 'python -m venv .venv' 
   >vai permitir instalar as dependências localmente no projeto
   - '.\venv\Scripts\Activate.ps1'
   > para ativar essa virtualização

4. Instalando django  
   - 'pip install upgrade pip'
   > atualizar gerenciador pip
   - 'pip install django'

5. Checando dependências
   - Com o comando 'pip freeze' irá mostrar todas as dependências desse projeto

6. Iniciando administração do django
   - 'django-admin startproject config' 
   >chamamos esse arquivo de config

7. Iniciando servidor python
   - 'python manage.py runserver'

8. Alterando língua e hora do servidor
   - Em 'config' no arquivo 'settings.py' alterar 'LANGUAGE_CODE' para 'pt-br'
   - É possivel mudar o local no mesmo arquivo alterando 'TIME_ZONE' para 'America/Sao_Paulo'

9. Criando o aplicativo django
   - 'python manage.py' startapp pensamentos   

## 10 -RESTANTE EM CONSTRUÇÃO...
### CONTINUA...

video api framework django ( tempo 14:26 )
https://www.youtube.com/watch?v=BKChTO8GADk

video requets ( tempo 11:45 )
https://www.youtube.com/watch?v=XRUdG2msE0Q


