import os
import pygame
import keyboard
import copy


def mostrar_equipo():
    print("Este es nuestro equipo")
    for miembro in equipo:
        print(miembro)


def mostrar_proyecto():
    print("Nuestro proyecto se trata sobre el juego de mesa Batalla Naval:\n El mismo será realizado usando un formato via terminal en ASCII, y contará \n con un modo multijugador en linea, en el cual cada jugador podrá \n colocar a libertad sus barcos, bombardear el lado enemigo del tablero, y recibir \n feedback en tiempo real de los resultados de sus acciones en una partida por turnos.") #TODO revisar esta funcion

#menu
def menu():
    repetir = True
    while repetir:
        os.system("cls")
        print ("1-Equipo")
        print ("2-Proyecto")
        print ("4-Salir")
        try:
            op=int(input("Eliga una opcion: "))
            
            if op == 1:
                mostrar_equipo()
            elif op == 2:
                mostrar_proyecto()
            elif op == 4:
                repetir=False
            elif op == 5:
                juego()
            else:
                print("Opcion invalida")
            input()
        except:
            print("Error, debe usar un numero")
            input()
            
def dibujar(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()
        
def generar_tablero():
    pass
#Hardcodeame el tablero
def movimiento_barco(direccion,barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for i in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][i]
            tablero[old_x][old_y] = (f"\033[36m~\033[0m")
            x,y = direccion
            new_x = old_x + x
            new_y = old_y + y
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][i] = (new_x,new_y)
        
    
        
def visualizar_barco(barcos,tablero_barcos):
    for barco in barcos:
        for coordenada in barco:
            tablero_barcos[coordenada[0]][coordenada[1]] = (f"\033[33m≡\033[0m")
            
def rotacion_a_vertical(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = f"\033[36m~\033[0m"
            new_x = old_x + coordenada
            new_y = old_y - coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)
        
def rotacion_a_horizontal(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = (f"\033[36m~\033[0m")
            new_x = old_x - coordenada
            new_y = old_y + coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)

def confirmar_barco(barcos,barco):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            for barco2 in range(len(barcos)):
                if barco2 != barco:
                    for coordenada2 in range(len(barcos[barco2])):
                        if barcos[barco][coordenada] == barcos[barco2][coordenada2]:
                            posible = False
    if posible:
        barco+=1
    return barco

def confirmar_tiro(pos_bomba,tirosj1):
#TODO el primer parámetro tiene que ser el nombre que le demos a la posición actual del disparo
    confirmable=True
    if len(tirosj1)==0:
        return confirmable
    else:
        if confirmable:
            for tiro in range(len(tirosj1)):
                if tirosj1[tiro]==pos_bomba:
                    confirmable==False
        if confirmable:
            tirosj1.append(pos_bomba)
    
    return confirmable
       
def juego():
    pygame.init()
    clock = pygame.time.Clock()
    o=(f"\033[36m~\033[0m")
    b=(f"\033[33m≡\033[0m")
    portaaviones =b
    mulportaaviones = 5
    destructor = b
    muldestructor = 4
    crucero1 = (f"\033[31mDestruido\033[0m")
    mulcrucero1= 1
    crucero2 =b
    mulcrucero2 = 3
    lancha=b
    mullancha = 2
    # ░≡¤

   
    j1_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗","portaaviones: ",portaaviones*mulportaaviones],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║","destructor: ",destructor*muldestructor],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║","crucero: ",crucero1*mulcrucero1],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║","crucero: ",crucero2*mulcrucero2],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║","lancha: ", lancha*mullancha],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j1_tablerobarcos   = [
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    j2_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j2_tablerobarcos   = [
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    num_barco = 0
    todos_barcos = [[(1,1),(1,2),(1,3),(1,4),(1,5)],[(1,1),(1,2),(1,3),(1,4)],[(1,1),(1,2),(1,3)],[(1,1),(1,2),(1,3)],[(1,1),(1,2)]]
    barcosj1 = [[], [], [], [], []]
    tirosj1=[]
    game = True
    while game == True:
        if barcosj1[num_barco] == []:
            barcosj1[num_barco] = todos_barcos[num_barco]
        #Esta sección toma los inputs del teclado, en caso de querer agregar una nueva tecla, se añade otro
        #elif con la tecla deseada, y se usa el mismo formato con la bandera "presionado"
        estado = "posicionar barcos"
        if keyboard.is_pressed('w'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((-1,0),barcosj1,num_barco,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('s'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((1,0),barcosj1,num_barco,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('d'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((0,1),barcosj1,num_barco,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('a'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((0,-1),barcosj1,num_barco,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('r'):
            if presionado == False:
                if estado == "posicionar barcos":
                    if barcosj1[num_barco][0][0]==barcosj1[num_barco][1][0]:
                        rotacion_a_vertical(barcosj1,num_barco,j1_tablerobarcos)
                    else:
                        rotacion_a_horizontal(barcosj1,num_barco,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('enter'):
            if presionado == False:
                if estado == "posicionar barcos":
                    num_barco = confirmar_barco(barcosj1,num_barco)
                elif estado =="posicionar disparos":
                    confirmar_tiro(pos_bomba,tirosj1)
                    pass#TODO hacer lo mismo en todo, llamar funciones
            presionado = True
        else:
            presionado = False
        if num_barco == 4:
            estado = "posicionar disparos"
        visualizar_barco(barcosj1,j1_tablerobarcos)
        dibujar(j1_tablerodisparos)
        dibujar(j1_tablerobarcos)
        clock.tick(24)
        os.system("cls")
equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella Jazmín", "Trimarco, Tomas","McLovin"]
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir