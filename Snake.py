# Simulacion de un laberinto
import readchar as readchar
import os
import random
    # CONSTANTES
POS_Y = 1
POS_X = 0   
MAP_WIDTH = 20  # numero de filas (ancho) del mapa , coordenadas x
MAP_HEIGHT = 15 # numero de columnas (alto) del mapa, coordenadas y
NUM_OF_MAP_OBJECTS = 11
    # VARIABLES
my_position = [3, 1]
tail_lenght = 0
tail = []
map_objects = [] # obstaculos para el jugador
end_game = False

    # generate random object on the map
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

    # PROGRAMA main loop
# creamos el mapa que representara el laberinto
while not end_game:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None 
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"    
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@" # este seria el jugador 
                    tail_in_cell = tail_piece
            
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@" # este seria el jugador 
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1
                if tail_in_cell:
                    print("Has muerto")
                    end_game = True
            
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # preguntamos al usuario donde se quiere mover
    #direction = input("¿Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar()

    # pasamos a mover el jugador
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    os.system("clear")

