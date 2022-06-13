import socket
import sys

domain = input("digite o dominio que quer pesquisar.\nOBS: inclua o .COM.BR se houver: ")
names =['ns1','ns2', 'www', 'ftp','intranet','mail','pop3','smtp'] #Aqui defino os possíveis servidores de DNS

for name in names: 
    dns = name+"."+domain #aqui faço um laço de repetição para cada nome ser adicionado . e o domínio
    try:
        print(dns,":",socket.gethostbyname(dns)) #Aqui pego a função de acima e adiciono a tradução de endereço DNS para IP após os :
    except socket.gaierror: #Tratamento de erro
        print("Este dominio não é valido") #Aqui exibo a mensagem caso não exista o domínio.
        pass # Aqui mando o comando continuar até que se acabe. 