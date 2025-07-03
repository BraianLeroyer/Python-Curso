from datetime import datetime

class Producto:
     def __init__(self, denominacion, producto, precio, codigo, fecha_vencimiento):
        self.denominacion = denominacion
        self.producto = producto
        self.codigo = codigo
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
     
     def __str__(self):
        return f"[Denominacion: {self.denominacion}] | [Nombre: {self.producto}] | [Precio: ${self.precio:.2f}] | [Codigo: {self.codigo} | vencimiento: {self.fecha_vencimiento}]"


class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def es_valida(self) -> bool:
        try:
            datetime(self.anio, self.mes, self.dia)
            return True
        except ValueError:
            return False
        
    def como_datetime(self) -> datetime:
        return datetime(self.anio, self.mes, self.dia)

    def __str__(self):
        return f"[{self.dia}/{self.mes}/{self.anio}]"

Listaproducto = []

def menu_mercaderia():
    while True:
        print("\n--- Gestión de Mercadería ---")
        print("a) Alta mercadería")
        print("b) Ver listado de productos ")
        print("c) Modificación")
        print("d) Auditoría")
        print("e) Volver al menú principal")
        opcion = input("Seleccione una opción: ").lower()
      
        if(opcion not in('a','b','c','d','e')):
            print("Opcion incorrecta, Vuelva a ingresar una opcion")
        else:
            match opcion:
                case 'a':
                    while True:
                        print("*** Agregar Productos ***")
                        denominacion = input("Ingrese la denominacion (comercio): ")
                        nombre_producto = input("Ingrese el nombre del producto: ") 
                        try:
                            precio = float(input("Ingrese el precio del Producto: "))
                        except ValueError:
                            print("Valor ingresado incorrecto") 
                            continue
                        codigo = int(input("Ingrese codigo del producto tiene que ser entre 1 y 100: "))
                        
                        if(codigo < 1 or codigo > 100):
                            print("Error ingrese nuevamente el codigo")
                            continue
                                
                        codigo_ya_existe = any(p.codigo == codigo for p in Listaproducto)
                        
                        if codigo_ya_existe:
                            print("Error: ese código ya está en uso.")
                            continue
                        
                        print("Ingrese la fecha de vencimiento en formato DD/MM/AA")
                        dia= int(input("Ingrese el dia: "))           
                        mes = int(input("Ingrese el mes: "))
                        anio = int(input("Ingrese el anio: "))
                        fecha = Fecha(dia, mes, anio)
                        
                        if not fecha.es_valida():
                            print("Error: la fecha de vencimiento no es valida ")
                            print(f"Fecha ingresada: {dia:02d}/{mes:02d}/{anio}")
                            continue

                        nuevo_producto = Producto(denominacion, nombre_producto, precio,codigo, fecha)
                        Listaproducto.append(nuevo_producto)
                        print("Producto agregado exitosamente!")
                       
                        seguir = input("Desea Seguir agregando producto? S/N: ").lower()
                        if seguir == 's':
                            continue
                        elif seguir == 'n':
                            break
                     
                case 'b': 
                     if(Listaproducto is None):
                         print("La lista de producto esta vacia")
                     else:
                        print("\n--- Lista de productos cargados ---")
                        for producto in Listaproducto:
                           print(f"{producto }")

                case 'c':
                    if(Listaproducto is None):
                        print("La lista de productos esta vacia")
                    else:
                        print("\n ---Modificacion de Mercaderia")
                        codigo_buscar = int(input("ingrese un codigo valido para modificar el producto: "))
                        producto_encontrado = None
                        for producto in Listaproducto:
                            if producto.codigo == codigo_buscar :
                                print(f"Se encontro el codigo {codigo_buscar}")
                                print(f"El producto a cambiar {producto}")
                                producto_encontrado = producto        
                                break
                        if producto_encontrado:
                            print(f"Producto a modificar con el codigo: {codigo_buscar}")
                            nueva_denominacion = input("Ingrese la denominacion a Modificar: ")
                            try:
                                 nueva_precio = float(input("Ingrese el precio del Producto a Modificar: "))
                            except ValueError:
                                print("El precio ingresado es incorrecto!")
                            producto_encontrado.denominacion = nueva_denominacion
                            producto_encontrado.precio = nueva_precio
                            print("Producto modificado exitosamente!")
                        else:
                            print("No se encuentra el producto")
                            break
                case 'd':
                    print("---/n Los Productos ya vencidos en el dia de hoy")
                    hoy = datetime.now()
                    for product in Listaproducto:
                        vencimiento = product.fecha_vencimiento.como_datetime()
                        diferencias_dias = (hoy - vencimiento).days
                        if diferencias_dias == 0:
                            print(f"Producto: [{product.producto}]  esta en fecha (Vence hoy)")
                        elif diferencias_dias > 0:
                            print(f"Producto: [{product.producto}] Vencido hace {diferencias_dias} dias. " )
                case 'e':
                    print("Vuelve al menu Principal!!!")
                    break