# -*- coding: utf-8 -*-

UC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

d = ['0','1','2','3','4','5','6','7','8','9']
e = ['1','2','3','4','5','6','7','8','9']

ALL = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
       '0','1','2','3','4','5','6','7','8','9',
       '+','-','*','/','%','&','|','!','<','>','=','(',')','[',']','{','}',';',',',':','.','?','\n','\t','\0','\b','EOF','EOL']
    
    
#Al analizador le vas pasando letras, él se encarga de ir concatenando y/o creando tokens
def anaizador_lexico(char):
    return


with open("/home/filstrup/hub/pdl/Ejem.js") as f: #abrimos el archivo
        c = f.read().splitlines(1)
        texto = ""
        for i in c:
            texto+=i
        print texto
        
        with open("output.txt", "w") as text_file:
            for i in c:
                text_file.write(i)
                
        for i in c:
            for letra in i:
                analizador_lexico(letra)