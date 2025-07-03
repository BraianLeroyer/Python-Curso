import mercaderia
import gestion
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1) Gestión de mercadería")
    print("2) Gestion de ventas")
    print("0) Salir")    
    opcion = input("Seleccione una opción: ")
    if opcion not in[1,2,0]:
        match opcion:
            case '1':
                mercaderia.menu_mercaderia()
            case '2':
                gestion.menu_gestion()
            case '0':
                break
    else:
        print("Valor incorrecto vuelva a ingresar un valor")
        continue        