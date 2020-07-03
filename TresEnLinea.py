ficha = None
continuar = True

matriz = []
for i in range(3):    # n = 3
    lista = ['-'.upper() for j in range(3)]     # n = 3  ( n * n = 9 )
    matriz.append(lista)       #Crea matriz "vacia" de 3 x 3

def tablero_de_juego():  #Dibuja y actualiza el tablero con la ficha escogida'''

    print(matriz[0][0] + " | ", matriz[0][1] + " | ", matriz[0][2])
    print(matriz[1][0] + " | ", matriz[1][1] + " | ", matriz[1][2])
    print(matriz[2][0] + " | ", matriz[2][1] + " | ", matriz[2][2])
print('TRES EN RAYA')
tablero_de_juego()

def escoger_ficha():   #Elección y validación de ficha escogida
    ficha = input('Jugador que inicia juego escoge ficha (X/O): ').upper()
    while True:                                    # n  veces
        while ficha != "X" and ficha != "O":       # n veces
            ficha = input('Inválido, escoja ficha (X/O): ').upper()
            if ficha == "X" or ficha == "O":       # n veces
                break
        break
    return ficha  # Retorna ficha X ó O

def mov_horizontal(ficha):  #Valida los tres movimientos horizontales ganadores      # n veces (maximo 4 o 3 veces)
    global continuar
    if (matriz[0][0]=="X" and matriz[0][1]== "X" and matriz[0][2]=="X") or \
            (matriz[0][0]=="O" and matriz[0][1]== "O" and matriz[0][2]=="O") :
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False
    elif (matriz[1][0]== "X" and matriz[1][1]=="X" and matriz[1][2]=="X") or (matriz[1][0]== "O" and matriz[1][1]=="O" and matriz[1][2]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False
    elif (matriz[2][0]=="X"and matriz[2][1]== "X" and matriz[2][2]=="X")  or (matriz[2][0]=="O"and matriz[2][1]== "O" and matriz[2][2]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False

def mov_vertical(ficha):   #Valida los tres movimientos verticales ganadores       # n veces (maximo 4 o 3 veces)
    global continuar
    if (matriz[0][0]=="X" and matriz[1][0]=="X" and matriz[2][0]=="X") or \
            (matriz[0][0]=="O" and matriz[1][0]=="O" and matriz[2][0]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False
    elif (matriz[0][1]=="X" and matriz[1][1]=="X" and matriz[2][1]=="X") or (matriz[0][1]=="O" and matriz[1][1]=="O" and matriz[2][1]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False
    elif (matriz[0][2]=="X" and matriz[1][2]=="X" and matriz[2][2]=="X") or (matriz[0][2]=="O" and matriz[1][2]=="O" and matriz[2][2]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False

def mov_diagonales(ficha):    #Valida los dos movimientos diagonales ganadores       # n veces (maximo 4 o 3 veces)
    global continuar
    if (matriz[0][2] =="X" and matriz[1][1]=="X" and matriz[2][0]=="X") or (matriz[0][2] =="O" and matriz[1][1]=="O" and matriz[2][0]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False
    elif (matriz[0][0]=="X" and matriz[1][1]=="X" and matriz[2][2]=="X") or (matriz[0][0]=="O" and matriz[1][1]=="O" and matriz[2][2]=="O"):
        print('¡GANÓ LA FICHA', ficha + "!")
        continuar = False

def principal():
    ficha = escoger_ficha()
    print('            ¡EMPIECE A JUGAR!')
    print('Estos son los número que corresponden a las casillas: ')
    print("7" + " | ", "8" + " | ", "9")
    print("4" + " | ", "5" + " | ", "6")
    print("1" + " | ", "2" + " | ", "3")
    fichas_en_tablero = 0   # contador de fichas en tablero ( para validar empate )
    while continuar:                                                                       # n veces
        numero_teclado = input('Ingrese posición con los números del teclado: ')
        while numero_teclado not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:          # n veces
            numero_teclado = input("Tecla inválida, Ingrese posición con los números del teclado:  ")

        if numero_teclado == "1":             # n veces
            if matriz[2][0] == '-':           # n veces
                matriz[2][0] = ficha
                fichas_en_tablero +=1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "2":              # n veces
            if matriz[2][1] == '-':              # n veces
                matriz[2][1] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "3":             # n veces
            if matriz[2][2] == '-':             # n veces
                matriz[2][2] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "4":              # n veces
            if matriz[1][0] == '-':              # n veces
                matriz[1][0] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "5":               # n veces
            if matriz[1][1] == '-':               # n veces
                matriz[1][1] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "6":               # n veces
            if matriz[1][2] == '-':               # n veces
                matriz[1][2] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "7":               # n veces
            if matriz[0][0] == '-':               # n veces
                matriz[0][0] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "8":                # n veces
            if matriz[0][1] == '-':                # n veces
                matriz[0][1] = ficha
                fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue
        elif numero_teclado == "9":                # n veces
            if matriz[0][2] == '-':                # n veces
               matriz[0][2] = ficha
               fichas_en_tablero += 1
            else:
                print('Casillero ocupado, ingrese otra posición')
                continue

        tablero_de_juego()   # Actualiza el tablero de juego con la ficha escogida       # n veces

        mov_horizontal(ficha)
        mov_vertical(ficha)
        mov_diagonales(ficha)

        if fichas_en_tablero == 9:                    # n veces ( después de 9 veces se ejecuta)
            print('FICHA X - FICHA O --> ¡EMPATE!')
            break

        if continuar == True:                         # n veces
            if ficha == 'X':
                ficha = 'O'
            elif ficha == 'O':
                ficha = 'X'
            print('TURNO DE LA FICHA', ficha)

principal()

''' CONCLUSIÓN :

El algoritmo tiene una complejidad de n. Esto es
una complejidad con curva lineal que pertenece a 
la familia o tiene un aproximado de: n ~ O(n) ,
donde n: 1,2,3,4,5,...,n

'''