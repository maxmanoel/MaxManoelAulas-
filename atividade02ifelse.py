#FAÇA UM PROGRAMA QUE RECEBA UMA NOTA DO ALUNOE SE FOR SUPERIOR OU IGUAL A 7 (SETE) APAREÇA MENSAGEM QUE ELE ESTA APROVADO, SE FOR INFERIOR A 5 (CINCO) ELE ESTA "NAO APROVADO/ REPROVADO DIRETO" 
#E SE ESTIVER ENTRE 5 (CINCO) E 7 (SETE) APAREÇA A MNSAGEM "NAO APROVADO/ RECUPERAÇÃO"

nota= int (input("digite sua primeira nota: "))
if (nota >= 7):
    print("aprovado")
if (nota <= 5):
   print ("reprovado")
else:
    print("nao aprovado \ recuperação")
