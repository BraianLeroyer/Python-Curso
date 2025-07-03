from datetime import datetime
import random as rd
filas = 6
columnas = 6

matriz = [[("",0) for _ in range(columnas)] for _ in range(filas)]
array = []
def menu_gestion():
    while True:
        print("\n --- Gestion de ventas ")
        print("a) Carga de Clientes")
        print("b) Listado de Clientes")
        print("c) Promo Sorteo")
        print("d) Volver al menu Principal")
        opcion = input("Ingrese una opcion: ")
        if opcion not in('a','b','c','d'):
            print("Opcion incorrecta vuelva a ingresar una opcion ")
            continue
        else:
            match opcion:
                case 'a':
                  salir = False
                  numero = 0
                  for i in range(filas):
                    for j in range(columnas):
                      clientes = input(f"digite el nombre del cliente en posicon: [{i+1}][{j+1}]: ").strip().lower()
                      numero += 1
                      matriz[i][j] = (clientes, numero)
                      seleccionar = input("Desea se(guir agregando clientes? (S/N): ").strip().lower()
                      if seleccionar == 's':
                         continue
                      elif seleccionar == 'n':
                         salir = True
                         break
                      else:
                         print("Opcion incorrecta")
                         break
                    if salir:
                       break

                case 'b':
                  print("Matriz desordenada alfabeticamente: ")
                  for i in range(columnas):
                   print(f"Nombre y numero del cliente = {matriz[0][i]}")
     
                  array = [matriz[i][j][0] for i in range(filas) for j in range(columnas)]
                  for i in range(len(array)):
                     for j in range(len( array)-i-1):
                        if array[j] > array[j+1]:
                           array[j], array[j+1] = array[j+1], array[j]
                  print("Ordenados alfabeticamente!")
                  print(array)
                case 'c':
                  mes_actual = datetime.now().month
                  if mes_actual in [12, 1, 2]:
                     estacion = "VERANO"
                  elif mes_actual in [3,4,5]:
                     estacion = "OTOÑO"
                  elif mes_actual in [6,7,8]:
                     estacion = "INVIERNO"
                  elif mes_actual in [9,10,11]:
                     estacion = "PRIMAVERA"
                  else:
                     estacion = "DESCONOCIDO" 
                  print(f"PROMO SORTEO DE: {estacion}") 
                  numero_aleatorio = rd.randint(0,6)
                  ganador = False
                  for i in range(filas):
                     for j in range(columnas):
                        clientes, numero = matriz[i][j]
                        if (numero == numero_aleatorio):
                           ganador = True
                           break
                     if ganador:
                       today = datetime.today
                       print(f" El cliente ganador es: {clientes} con el numero de cliente: {numero_aleatorio} en la fecha fecha: {today}")
                       break
                     else:
                        print("Todabia no hay ganador" \
                        " ")