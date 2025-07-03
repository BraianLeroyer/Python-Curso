Un comercio requiere un programa para controlar su operatoria interna se requieren los siguientes modulos funcionales:
1) Gestion de mercaderias
2) Gestion de ventas 

Al iniciar el programa, se debera mostrar un menu de opciones conrrespondientes, mas la opcion salir.
Estos menus, y cada una de sus acciones, deberán implementarse como unda FUNCION distinta.

**Accion del modulo 1**

a) Alta de Mercaderia

b) Modificación de datos 

c) Auditoría 

d) Volver al menú principal

La mercaderia deberá gestionarse en un arreglo de hasta 100 Estructuras (Instancia de Objetos), que se inicitalizará con una estructura 'vacia' (codigo de producto 0). Los productos se guardan
en el arreglo, en el orden que fueron cargados, y se localizan mediante búsqueda lineal por el códgo de producto.
 Cada mercaderia debera contener codigo de producto (entre 1 y 100), denominacion, precio unitario (Validar que sea mayor a 0) y fecha de vencimiento (DATATIME). El codigo de producto es unico, 
No se puede repetirse.

a) EL ALTA DE MERCADERIA, solicitará y validará los datos para una mercaderia nueva, y registrará el ingreso en la proxima "Vacia" del arreglo (codigo de producto 0).

b) LA MODIFICACION DE DATOS, solicitará un codigo de producto (que debe existir registrado), con él se localizará el producto correspondiente, y se actualizará los datos para ESA mercaderia (igual que en el alta, pero solo para ESE producto particular).

c) LA AUDITORIA, recorrerá el arreglo completo, y mostrará los datos de aquellos productos que se encuentran vencidos al dia de hoy, junto con la cantidad de dias transcurridos desde el vencimiento. 

**Accion del Modulo 2**

a) Carga de clientes

b) Listado de clientes

c) Promo de sorteo

d) Volver al menú principal 

Para los clientes se guardará únicamente su nombre, en una matriz de caracteres de hasta 20 filas. La posicion del arreglo +1 su n° de cliente. Se puede inicializar
dicha matriz con caracteres en 0 

a) LA CARGA DE CLIENTES ingresará los nombres de todos los clientes secuencialmente.

b) EL LISTADO DE CLIENTES mostrará los nombres de los clientes, ordenado alfabéticamente y convertido a Mayusculas.

c) LA PROMO SORTEO cambia su nombre dependiendo de la estacion del año, la cual a su vez depende del mes actual (Obtenido del reloj del sistema): Se debe deterninar y mostrar dicho nombre en pantalla (ej. PROMO SORTEO INVIERNO). Luego, el programa seleccionará un número de cliente al azar (VEA MODULO RANDOM), mostrará su nombre en pantalla, junto con la leyenda:
"HAS RESULTADO GANADOR!" y la fecha actual.  
