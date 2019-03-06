import json
with open("overwatch-api-complete-player-profile-example.json") as fichero:
    datos=json.load(fichero)

lista_win=[]
lista_vic_derr=[]
lista_daño=[]

def ejer1(datos):
    lista_heroes=[]
    lista_heroes=(datos.get("quickplay").get("heroComparison").get("timePlayed"))
    for heroe in lista_heroes.keys():
        print("-",heroe)
    print("")


def ejer2(datos):
    lista_datos=[]
    lista_oro=[]
    medallas=int(input("Dime cuantas medallas especificas: "))
    lista_datos=(datos["quickplay"]["careerStats"])
    cont=0

    for campo,valor in lista_datos.items():
        for c,v in valor.items():
        
            if c=="matchAwards":

                lista_oro.append(v.get("medalsGold",0))
                
    print(len(lista_oro))
                    
    for num in lista_oro:
            
        if num>=medallas:
           cont=cont+1

    print("Has conseguido %d medallas o mas con %d héroes"%(medallas,cont-1))


while True:
    print("================================================================================")
    print("1.Lista los heroes")
    print("2.Contar con cuantos Héroes has conseguido mas o las mismas medallas de oro que especifiques por teclado.")
    print("3.Pide por teclado un numero de partidas ganadas y te lista los héroes con los que has conseguido esas o mas victorias.")
    print("4.Mostrar las victorias y derrotas de un héroe introducido por teclado")
    print("5.Pides por teclado un numero de daño y te muestra los héroes con los que has realizado menos daño.")
    print("6.Salir")
    print("================================================================================")
    elec=int(input("Elige una opción: "))
    print("")

    if elec==6:
        break
    
    elif elec==1:
        ejer1(datos)
        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==2:
        ejer2(datos)
        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")