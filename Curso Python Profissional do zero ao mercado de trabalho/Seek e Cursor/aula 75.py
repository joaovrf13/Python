arquivo = open("texto2.txt")
texto = arquivo.read()
for linha in texto.splitlines():
    print(i, linha)
    i += 1
arquivo.close()