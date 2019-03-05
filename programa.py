with open("overwatch-api-complete-player-profile-example.json") as fichero
datos=json.load(fichero)

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