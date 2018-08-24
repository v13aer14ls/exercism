#/!bin/python3.x
#MANTAINER=Guilherme Amaral

#Importando modulos
import subprocess, getpass

#Solicitando entrada do usuario
host=input("Informe o servidor a ser acessado: ")

#Adicionando porta padrão de acesso (no meu caso é a XXXXX, desprezar a linha caso não seja necessario)
host = host + ":XXXXX"

#Adicionando a senha por entrada de usuario, repare que a senha nao ira aparecer no terminal por causa do modulo getpass.
senha=getpass.getpass(prompt='Insira sua Senha: ')

#Adiconando a senha de modo estatico, nao é o metodo mais seguro.
#senha = "XXXXXX"

#Adicionando o usuario de modo estatico, o usuario tambem pode ser solicitado por entrada do usuario, mas eu fiquei com preguiça.
user ="DOMINIO\\USUARIO"

#Concatenação dos dados coletados pelas variaveis e direcionando eles para um pipe.
v1 = subprocess.Popen(['rdesktop' , '-g90%', host,'-u', user,'-p', senha,], stdout=subprocess.PIPE)

#Execução do comando.
output = v1.communicate()[0]
