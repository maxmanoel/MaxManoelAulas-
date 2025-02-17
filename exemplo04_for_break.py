pessoas_presentes = ["john Show" , "Jesse pinkman", "Aria Stark" , "Tyrion Lannister"]
#QUERO SABER SE UMA PESSOA ESPICIFICA ESTA PRESENTE
chamada = "Aria Stark"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} esta presente.".format(chamada))
        break
else:
    print("So um print para mostrar que for passou por essa pessoa:" +str (pessoa))





    pessoas_presentes = ["john Show" , "Jesse pinkman", "Aria Stark" , "Tyrion Lannister"]
#QUERO SABER SE UMA PESSOA ESPICIFICA ESTA PRESENTE
chamada = "Aria Stark"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} esta presente.".format(chamada))
    
        break
else:
    continue
    print("So um print para mostrar que for passou por essa pessoa:" +str (pessoa))