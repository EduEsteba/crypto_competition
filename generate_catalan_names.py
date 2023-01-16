file=open("Passwords/catalan_names.txt","r")
lineas=file.readlines()
for linea in lineas:
    ## Majuscula amb numero davant 0Edu
    ##for i in range(0000, 10000):
    ##    with open('calatan_names_num.txt', 'a') as f:
    ##        f.writelines(str(i)+linea.capitalize())
    ## Nums davant 0edu
    for i in range(0000, 10000):
        with open('calatan_names_num.txt', 'a') as f:
            f.writelines(str(i)+linea)
    ## Majuscula amb numero radera Edu0
    ##for i in range(0000, 10000):
    ##    with open('calatan_names_num.txt', 'a') as f:
    ##        f.writelines(linea.capitalize()+str(i))
    ## Numero radera edu0
    for i in range(0000, 10000):
        with open('calatan_names_num.txt', 'a') as f:
            f.writelines(linea+str(i))
file.close()
