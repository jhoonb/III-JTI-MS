#---------------------------------------------
# teste de manipulação de arquivos em Python3
#--------------------------------------------

#------------- criação e gravação ------------------ 
# criar um arquivo
arquivo = open("novo.txt", "w")

# adicionar dados no arquivo
arquivo.write("mensagem dentro do arquivo :)")

# fecha o arquivo
arquivo.close()


#------------- leitura do arquivo ------------------
# abre o arquivo
arquivo = open('novo.txt', 'w')

# retorna todos os dados do arquivo numa str
dados = arquivo.read()

# retorna a primeira linha do arquivo (str)
linha = arquivo.readline()

# retorna a segunda linha do arquivo.... e assim até o final
linha2 = arquivo.readline()

# retorna uma lista com cada elemento sendo uma linha do arquivo
dados = arquivo.readlines()

# percorre linha a linha do arquivo com um for
for linha in arquivo:
    print(linha)

#  captura todo o valor do arquivo com um for em formato str
s = ""
for linha in arquivo:
    s += linha

# captura todo valor do arquivo em uma lista 
dados = [linha for linha in arquivo]

# fecha o arquivo
arquivo.close()


