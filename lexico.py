# -*- coding: utf-8 -*-

UC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

d = ['0','1','2','3','4','5','6','7','8','9']
e = ['1','2','3','4','5','6','7','8','9']
o = ['0','1','2','3','4','5','6','7']
x = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

ALL = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
       '0','1','2','3','4','5','6','7','8','9',
       '+','-','*','/','%','&','|','!','<','>','=','(',')','[',']','{','}',';',',',':','.',"_",'?','\n','\t','\0','\b','\r']

entrada = 0

string = ""
estado = 0
cont = 0
lista_tokens  = []

def concat(char):
    global string
    if (char == "reset"):
        string = ""
    else:
        string += char  
    return 
    
def concatN(digit):
    global cont
    if (digit == "reset"):
        cont = 0
    else:
        cont = cont*10 + cont  
    return 
    
def pertenece(char, lista):
    return (char in lista)
    
def error(estado, char):
    print "############################"
    print("Error:" + "\n" + "caracter leido = " + str(ord(char)) + "\n" + "estado = " + str(estado))
    print "############################"

def create_token(arg):
    global string
    global lista_tokens

    if(arg == ";"):
        lista_tokens.append(["simbolo", ";"])
    elif(arg =="?"):
        lista_tokens.append(["simbolo", "?"])
    elif(arg =="."):
        lista_tokens.append(["simbolo", "."])
    elif(arg ==","):
        lista_tokens.append(["simbolo", ","])
    elif(arg ==":"):
        lista_tokens.append(["simbolo", ":"])
    elif(arg =="("):
        lista_tokens.append(["simbolo", "("])
    elif(arg ==")"):
        lista_tokens.append(["simbolo", ")"])
    elif(arg =="["):
        lista_tokens.append(["simbolo", "["])
    elif(arg =="]"):
        lista_tokens.append(["simbolo", "]"])
    elif(arg =="{"):
        lista_tokens.append(["simbolo", "{"])
    elif(arg =="}"):
        lista_tokens.append(["simbolo", "}"])
    elif(arg =="++"):
        lista_tokens.append(["simbolo", "++"])
    elif(arg =="+="):
        lista_tokens.append(["simboloAsignOp", "+="])
    elif(arg =="+"):
        lista_tokens.append(["simboloIntInt", "+"])
    elif(arg =="--"):
        lista_tokens.append(["simbolo", "--"])
    elif(arg =="-="):
        lista_tokens.append(["simboloAsignOp", "-="])
    elif(arg =="-"):
        lista_tokens.append(["simboloIntInt", "-"])
    elif(arg =="&&"):
        lista_tokens.append(["simboloBoolBool", "&&"])
    elif(arg =="||"):
        lista_tokens.append(["simboloBoolBool", "||"])
    elif(arg =="="):
        lista_tokens.append(["simbolo", "="])
    elif(arg =="=="):
        lista_tokens.append(["simboloIntBool", "=="])
    elif(arg =="<="):
        lista_tokens.append(["simboloIntBool", "<="])
    elif(arg =="<"):
        lista_tokens.append(["simboloIntBool", "<"])
    elif(arg ==">="):
        lista_tokens.append(["simboloIntBool", ">="])
    elif(arg ==">"):
        lista_tokens.append(["simboloIntBool", ">"])
    elif(arg =="!="):
        lista_tokens.append(["simboloIntBool", "!="])
    elif(arg =="!"):
        lista_tokens.append(["simboloBoolBool", "!"])
    elif(arg =="%="):
        lista_tokens.append(["simboloAsignOp", "%="])
    elif(arg =="%"):
        lista_tokens.append(["simboloIntInt", "%"])
    elif(arg =="*="):
        lista_tokens.append(["simboloAsignOp", "*="])
    elif(arg =="*"):
        lista_tokens.append(["simboloIntInt", "*"])
    elif(arg == "string"):
        lista_tokens.append(["string", string])
    elif(arg == "/="):
        lista_tokens.append(["simboloAsignOp", "/="])
    print arg
    return
    
def create_token_ident():
    global string
    global lista_tokens
    lista_tokens.append(["ident", string])
    print string
    return
    
def create_token_decimal():
    global cont
    global lista_tokens
    lista_tokens.append(["int", cont])
    print cont
    return
    
def create_token_octal():
    global cont
    global string
    cont = int("0" + string,8)
    create_token_decimal()
    string = ""
    return
    
def create_token_hexadecimal():
    global cont
    global string
    cont = int("0x" + string,16)
    create_token_decimal()
    string = ""
    return

def analizador_lexico(char):
    
    global estado
    
    if (estado == 0):
        
        if (char == "/"):
            estado = 1
            return
            
        elif (pertenece(char, LC) or pertenece(char, UC)):
            estado = 5
            concat(char)
            return
            
        elif (pertenece(char, e)):
            estado = 6
            concatN(char)
            return
            
        elif (char == "0"):
            estado = 7
            return
            
        elif (char == "+"):
            estado = 10
            return
            
        elif (char == "-"):
            estado = 11
            return
            
        elif (char == "&"):
            estado = 12
            return
            
        elif (char == "|"):
            estado = 13
            return
            
        elif (char == "'"):
            estado = 14
            return
            
        elif (char == '"'):
            estado = 15
            return
            
        elif (char == "="):
            estado = 16
            return
            
        elif (char == "<"):
            estado = 17
            return
            
        elif (char == ">"):
            estado = 18
            return
            
        elif (char == "!"):
            estado = 19
            return
            
        elif (char == "%"):
            estado = 20
            return
            
        elif (char == "*"):
            estado = 21
            return
            
        ##################################
        elif (char == "\\"):
            estado = 22
            return
            
        elif (char == "\n"):
            return
            
        elif (char == "\t"):
            return
            
        elif (char == "\0"):
            return
            
        elif (char == "\r"):
            return
        ##################################
            
        elif (char == ";"):
            create_token(";")
            return
            
        elif (char == "?"):
            create_token("?")
            return
            
        elif (char == "."):
            create_token(".")
            return
            
        elif (char == ","):
            create_token(",")
            return
            
        elif (char == ":"):
            create_token(":")
            return
            
        elif (char == "("):
            create_token("(")
            return
            
        elif (char == ")"):
            create_token(")")
            return
            
        elif (char == "["):
            create_token("[")
            return
            
        elif (char == "]"):
            create_token("]")
            return
            
        elif (char == "{"):
            create_token("{")
            return
            
        elif (char == "}"):
            create_token("}")
            return
            
        elif (char == " "):
            return
        else:
            error(estado, char)
            return
            
    elif (estado == 1):
        # /
        if (char == "*"):
            estado = 2
            return
        elif (char == "/"):
            estado = 4
            return
        elif (char == "="):
            create_token("/=")
        error(estado, char)
        return
            
            
    elif (estado == 2):
        # /* ...
        if (char == "*"):
            estado = 3
            return
        return
        # ¿¿¿ Hay algo que no se pueda meter en /* ... */ ??? --> error(estado, char)
        
    elif (estado == 3):
        # /* ... *
        if (char == "*"):
            return
        elif (char == "/"):
            estado = 0
            return
            #Fin del comentario, no sirve de nada, asi que no se crea token
        estado = 2
        return
        
    elif (estado == 4):
        
        if (char == "\n"):
            estado = 0
            return
        elif (char == "\r"):
            estado = 26
            return
        return
        
    elif (estado == 26):
        
        if (char == "\n"):
            estado = 0
            return
        error(estado, char)
        return
            
    elif (estado == 5):
        # Letra
        if (pertenece(char, LC) or pertenece(char, UC) or pertenece(char, d) or (char == "_")):
            concat(char)
            return
        create_token_ident()
        estado = 0
        concat("reset")
        analizador_lexico(char)
        return
        
    elif (estado == 6):
        
        if (pertenece(char, d)):
            concatN(char)
            return
        create_token_decimal()
        estado = 0
        concatN("reset")
        analizador_lexico(char)
        return
        
    elif (estado == 7):
        
        if (pertenece(char, o)):
            estado = 8
            concat(char)
            return
        elif (char == "x"):
            estado = 9
            concat(char)
            return
            
    elif (estado == 8):
        
        if (pertenece(char, o)):
            concat(char)
            return
        create_token_octal()
        estado = 0
        analizador_lexico(char)
        return
        
    elif (estado == 9):
        
        if (pertenece(char, x)):
            concat(char)
            return
        create_token_hexadecimal()
        estado = 0
        analizador_lexico(char)
        return
        
    elif (estado == 10):
        
        if (char == "+"):
            estado = 0
            concat("reset")
            create_token("++")
            return
        elif (char == "="):
            estado = 0
            concat("reset")
            create_token("+=")
            return
        estado = 0
        concat("reset")
        create_token("+")
        analizador_lexico(char)
        return
        
    elif (estado == 11):
        
        if (char == "-"):
            estado = 0
            concat("reset")
            create_token("--")
            return
        elif (char == "="):
            estado = 0
            concat("reset")
            create_token("-=")
            return
        estado = 0
        concat("reset")
        create_token("-")
        analizador_lexico(char)
        return
        
    elif (estado == 12):
        
        if (char == "&"):
            estado = 0
            concat("reset")
            create_token("&&")
            return
        error(estado, char)
        return
            
    elif (estado == 13):
        
        if (char == "|"):
            estado = 0
            concat("reset")
            create_token("||")
            return
        error(estado, char)
        return
            
    elif (estado == 14):
        
        if (char == "'"):
            estado = 0
            create_token("string")
            concat("reset")
            return
        else:
            concat(char)
            return
        error(estado, char)
        return
        
            
    elif (estado == 15):
        
        if (char == '"'):
            estado = 0
            create_token("string")
            concat("reset")
            return
        else:
            concat(char)
            return
        
        error(estado, char)
        return
            
    elif (estado == 16):
        
        if (char == "="):
            estado = 0
            create_token("==")
            return
        estado = 0
        create_token("=")
        analizador_lexico(char)
        return
        
    elif (estado == 17):
        
        if (char == "="):
            estado = 0
            create_token("<=")
            return
        estado = 0
        create_token("<")
        analizador_lexico(char)
        return
        
    elif (estado == 18):
        
        if (char == "="):
            estado = 0
            create_token(">=")
            return
        estado = 0
        create_token(">")
        analizador_lexico(char)
        return
        
    elif (estado == 19):
        
        if (char == "="):
            estado = 0
            create_token("!=")
            return
        estado = 0
        create_token("!")
        analizador_lexico(char)
        return
        
    elif (estado == 20):
        
        if (char == "="):
            estado = 0
            create_token("%=")
            return
        estado = 0
        create_token("%")
        analizador_lexico(char)
        return
        
    elif (estado == 21):
        
        if (char == "="):
            estado = 0
            create_token("*=")
            return
        estado = 0
        create_token("*")
        analizador_lexico(char)
        return
    
    elif (estado == 22):
        
        if (char == "n"):
            estado = 0
            return
        error(estado, char)


with open("/home/filstrup/hub/pdl/Ejem.js") as f: #abrimos el archivo
        c = f.readlines()
        print c
        texto = ""
        for i in c:
            texto+=i
        ##print texto
                
        for i in c:
            for letra in i:
                analizador_lexico(letra)
        analizador_lexico(" ")
        
        #la idea es mandar un delimitador como ultimo caracter, ya que al alcanar el EOF
        #salimos del bucle, y es posible que se quede el ultimo token sin crear
        #(seria raro,ya que normakmente lo ultimo que se leera sera "}" o "\t" o algo por el estilo)
        #asi forzamos la creacion del ultimo token
        
        print(lista_tokens)
        with open("output.txt", "w") as text_file:
            for i in lista_tokens:
                tp = 0
                p = 0
                text_file.write("<")
                for j in i:
                    if(tp ==1):
                        text_file.write(str(j))
                    else:
                        text_file.write(j)
                    if(j == "int"):
                        tp = 1
                    else:
                        tp = 0
                    if(p == 0):
                        text_file.write(", ")
                        p = 1
                    else:
                        text_file.write(">")
                        p = 0
                text_file.write("\n")
