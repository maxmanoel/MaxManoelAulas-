#TRANFROMAR TODAS AS LETRAS EM MAIUSCULAS 
nome = "max"
print (nome.capitalize (), "\n")


#TRANFORMA TODAS AS LETRAS EM MINUSCULAS
nome = "MAX"
print (nome.casefold (), "\n")


#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.
nome = "maxmanoel@gmail.com"
print (nome.count ('m') , "\n")



#RETORNA TRUE ( VERDADEIRO) OU FALSE (FALSO) PARA UM TESTE SE A STRING TERMINA COM UMA STRING ESPECIFICA.
nome = "maxmanoel@gmail.com"
print(nome.endswith ('gmail.com') , "\n")



#ENCONTRA A POSIÇÃO DE TERMO PROCURANDO LEMBRE-SE COMECA DO ZERO.
nome = "maxmanoel@gmail.com"
print(nome.find ('@') , "\n")

#VERIFICAR SE O TEXTO E TODOS FEITO COM LETRAS.
nome = "max1"
print(nome.isalpha() , "\n")


#VERIFICA SE  O TEXTO E FEITO COM NUMEROS.
nome = "123"
print(nome.isnumeric() , "\n")


#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO.
nome = "max"
print(nome.replace ('o') , ('u') , "\n")

#SEPARA O TEXTO STRING BASEADO EM ALGUM CARACTERE INDICADO.
nome = "Max @ manoel ferreira"
print(nome.split("@") , "\n")


#COLOCAR TODAS AS LETRAS INICIAS EM MAIUSCULA.
nome = "max manoel ferreira dos santos"
print(nome.title() , "\n")



#RETIRA AS CARACTERES INDESEJADOS, COMO POR EXEMPLO ESPAÇOS QUE NAO AGRARAM VALOR.
nome = "max manoel ferreira dos santos"
print(nome.strip() , "\n")



#retorna true ou false para um testede  uma string se inicia com um texto especifico.
nome = "max 2008"
print(nome.startswith ("ser") , "\n")
print(nome.startswith ("ser")  , "\n")

