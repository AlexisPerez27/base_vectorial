import numpy as np
import time
import matplotlib.pyplot as plt
""" 
============================ para verificar version y carpeta virtual =====================================
import sys
import numpy
import matplotlib

print("Python    :", sys.version.split()[0])
print("numpy     :", numpy.__version__)
print("matplotlib:", matplotlib.__version__)
print("Ejecutable:", sys.executable)"""


"""
============================ listas o vectores =====================================
a = [2, 3]   # un vector de 2 dimensiones
b = [5, 1]   # otro vector de 2 dimensiones

print("a =", a)
print("b =", b)
print("Dimensiones de a:", len(a))    # len() cuenta cuántos números tiene
print("Primer número de a:", a[0])    # los índices empiezan en 0
print("Segundo número de a:", a[1])"""



""" 
============================ vectores con numpy =====================================
# --- Listas de Python: "+" concatena ---
lista_a = [2, 3]
lista_b = [5, 1]
print("Listas   a + b =", lista_a + lista_b)

# --- Arrays de numpy: "+" suma elemento por elemento ---
a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])
print("Arrays   a + b =", a + b)"""

""" 
# ============================ informacion del arreglo =====================================

a = np.array([2.0, 3.0])

print("Contenido :", a)
print("shape     :", a.shape)   # (2,)  -> 2 elementos en un solo eje
print("ndim      :", a.ndim)    # 1     -> es un vector (un solo eje)
print("dtype     :", a.dtype)   # float64 -> decimales de 64 bits
print("Primer elemento:", a[0]) # se indexa igual que una lista """



""" # =========================== operaciones de un arreglo ============================
a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])

print("a + b  =", a + b)      # [2+5, 3+1]
print("a - b  =", a - b)      # [2-5, 3-1]
print("a * b  =", a * b)      # [2*5, 3*1]  (¡ojo! esto NO es el producto punto, lo vemos en la sección 5)
print("a * 2  =", a * 2)      # [2*2, 3*2]  un número contra un array se aplica a todos
print("a ** 2 =", a ** 2)     # [2^2, 3^2]  cada elemento al cuadrado
print("sqrt(a)=", np.sqrt(a)) # raíz cuadrada de cada elemento
print("suma de a =", np.sum(a))  # suma todos los elementos: 2+3 """





# =========================== operacion de velocidad ============================
""" n = 1_000_000   # el guion bajo es solo para leer mejor: 1_000_000 = 1000000
lista_grande = list(range(n))
array_grande = np.arange(n)   # equivalente a range(n), pero como array

inicio = time.perf_counter()
resultado_lista = [x * 2 for x in lista_grande]
t_lista = time.perf_counter() - inicio

inicio = time.perf_counter()
resultado_array = array_grande * 2
t_array = time.perf_counter() - inicio

print(f"Lista de Python: {t_lista:.4f} s")
print(f"Array de numpy : {t_array:.4f} s")
print(f"numpy fue aproximadamente {t_lista / t_array:.0f} veces más rápido en esta ejecución") """



#===================================================================================================
#
#
#
#                                          MATPLOTLIB
#
#
#
#===================================================================================================

# figura de ejemplo 
""" fig,ax = plt.subplots(figsize=(6,6)) # crea el lienzo y un area de dibujo(ancho,alto)
ax.arrow() #digubas sobre el area(puntos,lineas,textos,titulos)
plt.show() #muestra la figura
 """
 
 
# =============================== primera grafica ==================================
#variables de arregllo
""" a = np.array([2.0,3.0])
b = np.array([5.0,1.0])

# crea el lienzo y un area de dibujo(ancho,alto)
fig, ax = plt.subplots(figsize=(5, 5))

# scatter(lista_de_x, lista_de_y)
#scatter dibuja todos los pntos de un solo lado
#ya sea que esten en el eje x o en el eje y sin unir los puntos
#[a[0], b[0]], [a[1], b[1]] = obtiene los valores del arreglo dependiendo su posicion, la s=80 es el tamaño del punto
ax.scatter([a[0], b[0]], [a[1], b[1]], s=80)   # s = tamaño del punto

ax.set_xlim(0, 7)        # rango del plano que se muestra en el eje x
ax.set_ylim(0, 5)        # rango del plano que se muestra en el eje y
ax.set_title("Dos vectores vistos como puntos") #titulo del grafico
ax.set_xlabel("dimensión 1 (x)") #etiqueta debajo del eje x
ax.set_ylabel("dimensión 2 (y)") #etiquetal debajo del eje y
ax.grid(True)            # cuadrículado el plano

plt.show() #para mostrar el plano
 """


# =============================== dibujar grafica con flechas ==================================
#variable de vectores
# a = np.array([2.0,3.0])
# b = np.array([5.0,1.0])
#funcion para preparar plano para la grafica
def preparar_plano(titulo, limite_x=(-1, 8), limite_y=(-1, 8)):
    '''Crea una figura con un plano cartesiano listo para dibujar vectores.'''
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(*limite_x)          # *tupla desempaqueta: set_xlim(-1, 8) Es solo una forma de no escribir limite_x[0], limite_x[1].
    ax.set_ylim(*limite_y)          # *tupla desempaqueta: set_ylim(-1, 8) Es solo una forma de no escribir limite_y[0], limite_y[1].
    ax.set_aspect("equal")          # misma escala en X e Y 1:1
    ax.grid(True, linestyle="--", alpha=0.4)   # grid: sirve para cuadriculuar, pero el estilo de la cuadricula cambia a --, y alpha = transparencia (0=invi, 1=visi)
    ax.axhline(0, color="black", linewidth=0.8)  # línea horizontal en y = 0, son lineas de ejes cartesianos
    ax.axvline(0, color="black", linewidth=0.8)  # línea vertical en x = 0, son lineas de ejes cartesianos
    ax.set_title(titulo) # el titulo cambia dependiendo de lo escrito al llamar la funcion
    ax.set_xlabel("dimensión 1 (x)") #titulo del eje en x
    ax.set_ylabel("dimensión 2 (y)") #titutlo del eje en y
    return fig, ax #Devuelve fig y ax para que quien llamó a la función pueda seguir dibujando sobre ellos.


#funcion para que reciba el plano donde dibujar (ax), el vector, su nombre, el color y desde dónde sale (por defecto del origen, el (0, 0)).
def dibujar_flecha(ax, vector, etiqueta, color, origen=(0, 0)):
    '''Dibuja un vector como flecha desde 'origen' hasta origen + vector.'''
    #Calcula dónde termina la flecha: origen + vector, componente por componente. Con a = [2, 3] y origen (0, 0): (0+2, 0+3) = (2, 3).
    destino = (origen[0] + vector[0], origen[1] + vector[1])
    #annotate normalmente sirve para poner texto con una flecha apuntando a algo. Aquí se usa solo por la flecha:
    ax.annotate(
        "",                  # sin texto: solo queremos la flecha
        xy=destino,          # la punta de la flecha, hacia dónde apunta la flecha
        xytext=origen,       # la cola, de donde sale, desde dónde sale
        arrowprops=dict(arrowstyle="->", color=color, linewidth=2), #diccionario con el aspecto de la flecha ("->" es el estilo, más color y grosor).
    )
    #Escribe la letra del vector ("a", "b") en la gráfica, en la posición de la punta más un pequeño desplazamiento de 0.15, para que el texto no quede encima de la flecha.
    ax.text(destino[0] + 0.15, destino[1] + 0.15, etiqueta, color=color, fontsize=12)


""" # Probamos nuestras funciones con a y b
#Llama a la primera función: prepara el plano vacío y guarda fig y ax.
fig, ax = preparar_plano("a = [2, 3] y b = [5, 1] como flechas")
#Dibuja una flecha del (0,0) a (2,3) en azul "tab:blue"  son nombres de colores predefinidos de matplotlib.
dibujar_flecha(ax, a, "a", "tab:blue")
# otra del (0,0) a (5,1) en rojo.  "tab:red" son nombres de colores predefinidos de matplotlib.
dibujar_flecha(ax, b, "b", "tab:red")
# Muestra el resultado.
plt.show() """



# =============================== operaciones vectores ==================================
""" suma   = a + b
resta  = a - b
doble  = 2 * a

print("a + b  =", suma)    # esperado a mano: [7, 4]
print("a - b  =", resta)   # esperado a mano: [-3, 2]
print("2 * a  =", doble)   # esperado a mano: [4, 6]
 """


# =============================== dibujar grafica con operaciones vectores ==================================
#dibuja plano, con la funcion preparar plano, envia el titulo y los limites cartesianos desde donde
#van a iniciar los panos de x tanto como y
""" fig, ax = preparar_plano("Suma de vectores: a + b", limite_x=(-1, 9), limite_y=(-1, 6))

#aqui se define la funcion de dibujar flecha
#ax=0,0, a=2,3,"a"=encabezado de la fecha, "tab:blue" = color de flecha
dibujar_flecha(ax, a, "a", "tab:blue")
#ax=0,0, a=5,1,"b"=encabezado de la fecha, "tab:red" = color de flecha
dibujar_flecha(ax, b, "b", "tab:red")
#ax=0,0, a=7,4,"a + b"=encabezado de la fecha, "tab:green" = color de flecha
dibujar_flecha(ax, suma, "a + b", "tab:green")

# b copiada con origen en la punta de a: llega exactamente a la punta de a + b
dibujar_flecha(ax, b, "", "salmon", origen=(a[0], a[1]))

plt.show() """



# =============================== PRODUCTO PUNTO ==================================
#EL PRODUCTO PUNTO TOMA DOS VECTORES Y DEVULVE UN SOLO NUMERO
# EJEMPLO: A*B = (2*5)+(3*1)= 10 + 3 = 13

""" a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])
 """
""" # Forma 1: paso a paso, igual que a mano
multiplicados = a * b                 # [2*5, 3*1] = [10, 3]
punto_manual = np.sum(multiplicados)  # 10 + 3
print("a * b (elemento por elemento):", multiplicados)
print("Suma de eso (producto punto)  :", punto_manual)

# Forma 2: la función de numpy
print("np.dot(a, b)                  :", np.dot(a, b))

# Forma 3: el operador @ (hace lo mismo con vectores)
print("a @ b                         :", a @ b) """


""" mismo_lado = np.array([1.0, 0.0])
perpendicular = np.array([0.0, 1.0])
lado_opuesto = np.array([-1.0, 0.0])

ref = np.array([1.0, 0.0])   # vector de referencia: apunta a la derecha

print("[1,0] · [1,0]  =", ref @ mismo_lado,    "-> mismo lado     (positivo)")
print("[1,0] · [0,1]  =", ref @ perpendicular, "-> perpendiculares (cero)")
print("[1,0] · [-1,0] =", ref @ lado_opuesto,  "-> lados opuestos  (negativo)") """


# =============================== NORMA ("LONGITUD DE UN VECTOR") ==================================
#la norma es la longitud de su fecha de un vector.
""" v = np.array([3.0, 4.0])
a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])

# Forma 1: paso a paso (cuadrados -> suma -> raíz), igual que a mano
# v** 2 = es para elevar algo al cuadrado
#np.sum() = suma los valores que estan dentro del parentesis
#np.sqrt() = es para sacar la raiz cuadrada del valor dentro del parentesis
#norma_v_manual = √3**2 + 4**2 = √ 9 + 16 = √25 = 5
norma_v_manual = np.sqrt(np.sum(v ** 2))
print("Norma de [3,4] paso a paso:", norma_v_manual)   # esperado: 5

# Forma 2: la función de numpy
#la funcion np.linalg.norm() hace el mismo proceso que lo anterior pero con menos lineas
#linalg.norm = hace referencia a alguebra lineal y norm es la norma.
print("np.linalg.norm([3,4])     :", np.linalg.norm(v))

print()
print("Norma de a (esperado ≈ 3.6056):", np.linalg.norm(a))
print("Norma de b (esperado ≈ 5.0990):", np.linalg.norm(b))

# Un dato útil: el producto punto de un vector consigo mismo es su norma al cuadrado
print()
print("a · a        =", a @ a, " (esperado a mano: 2*2 + 3*3 = 13)")
print("norma(a) ** 2 =", np.linalg.norm(a) ** 2, " (debe ser casi igual a 13)")
 """



# =============================== DISTANCIA EUCLIDIANA ==================================
#es la distancia entre dos puntos en este ejemplo a y  b
#para obtener la distania es necesario hacer esa formula
#d(a,b) = a - b = √(a-b)**2 + (a-b)**2 + (a-b)**2
#ejemplo : a=[2,3] y b = [5,1]
# d(a,b) = [2,-5, 3-1] = [-3,2] = √(-3)**2 + (2)**2 = √9 + 4 = √13 = 3.6056


""" a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])

diferencia = a - b
print("a - b          =", diferencia)                  # esperado: [-3, 2]
print("cuadrados      =", diferencia ** 2)             # esperado: [9, 4]
print("suma           =", np.sum(diferencia ** 2))     # esperado: 13
print("raíz           =", np.sqrt(np.sum(diferencia ** 2)))   # esperado: ≈ 3.6056

print()
print("np.linalg.norm(a - b) =", np.linalg.norm(a - b))
print("np.linalg.norm(b - a) =", np.linalg.norm(b - a), " (mismo resultado: el orden no importa)")


#vamos hacer la misma oiperacion pero vamos a visualizar esto en una grafica
distancia = np.linalg.norm(a - b)

# colocamos la plantilla para dibujar el plano carteciano
fig, ax = preparar_plano("Distancia euclidiana entre a y b", limite_x=(-1, 8), limite_y=(-1, 6))
# dibujamos las flechas de a y b 
dibujar_flecha(ax, a, "a", "tab:blue")
dibujar_flecha(ax, b, "b", "tab:red")

# Segmento entre las puntas: su longitud ES la distancia
ax.plot([a[0], b[0]], [a[1], b[1]], linestyle="--", color="tab:green", linewidth=2)

# Etiqueta en el punto medio del segmento
punto_medio = (a + b) / 2
ax.text(punto_medio[0] + 0.1, punto_medio[1] + 0.2, f"d = {distancia:.4f}", color="tab:green", fontsize=12)

plt.show()

 """



# =============================== SIMILITUD COSENO ==================================
#mide el angulo de la flechas, que tanto apuntan en la misma direccion. 
#para obtener la similitud de coseno es igual al producto divido entre el producto de las normas
#el coseno siempre estara entre -1 y 1 
#1 = 0° misma direccion, maxima similitud
#0 = 90° perpendiculares, sin relacion
#-1 = 180° direcciones opuestas
#ejemplo: cos() = a*b / ||a|| * ||b||
#cos = producto punto de a * b / normas(a) * normas(b)
# cos = 13 / || √13 || * || √26 ||
#cos = 13 / √338 = 13/18.3847 = 0.7071



""" a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])

producto_punto = a @ b #obtener producto puno
norma_a = np.linalg.norm(a) #norma de a 
norma_b = np.linalg.norm(b) #norma de b

#obtenemos el coseno
coseno = producto_punto / (norma_a * norma_b)

print("a · b          =", producto_punto)               # esperado: 13
print("||a||          =", norma_a)                     # esperado: ≈ 3.6056
print("||b||          =", norma_b)                     # esperado: ≈ 5.0990
print("||a|| * ||b||  =", norma_a * norma_b)           # esperado: ≈ 18.385 (√338)
print("coseno         =", coseno)                      # esperado: ≈ 0.7071
print("1 / raíz(2)    =", 1 / np.sqrt(2), " (debe coincidir con el coseno)")

# Del coseno al ángulo: arccos es la función inversa del coseno : te permite encontrar el ángulo (medido en radianes) cuyo valor de coseno es igual al número que le pasas como argumento.
angulo_radianes = np.arccos(coseno)
#convierte un ángulo expresado en radianes a su equivalente en grados
angulo_grados = np.degrees(angulo_radianes)
print("ángulo         =", angulo_grados, "grados")     # esperado: 45

print("distancia coseno (1 - coseno) =", 1 - coseno)



fig, ax = preparar_plano(f"Ángulo entre a y b: {angulo_grados:.1f}°  |  coseno = {coseno:.4f}",
                         limite_x=(-1, 8), limite_y=(-1, 6))
dibujar_flecha(ax, a, "a", "tab:blue")
dibujar_flecha(ax, b, "b", "tab:red")
plt.show()
 """

# =============================== FUNCIONES REUTILIZABLES ==================================
def distancia_euclidiana(a, b):
    '''Distancia en línea recta entre dos vectores. Menor = más cercanos.'''
    return np.linalg.norm(a - b)


def similitud_coseno(a, b):
    '''Coseno del ángulo entre dos vectores, entre -1 y 1. Mayor = más parecidos.'''
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))


""" a = np.array([2.0, 3.0])
b = np.array([5.0, 1.0])

print("distancia_euclidiana(a, b) =", distancia_euclidiana(a, b))
print("similitud_coseno(a, b)     =", similitud_coseno(a, b))

# Comprobación contra los cálculos a mano (np.isclose compara decimales con tolerancia)
print("¿Distancia ≈ raíz(13)?  ", np.isclose(distancia_euclidiana(a, b), np.sqrt(13)))
print("¿Coseno ≈ 1/raíz(2)?    ", np.isclose(similitud_coseno(a, b), 1 / np.sqrt(2)))
 """


# =============================== CUANDO USAR UNA METRICA ==================================

a = np.array([1.0, 2.0])
b = np.array([3.0, 6.0])   # b = 3 * a  (misma dirección, 3 veces más largo)
c = np.array([2.0, 1.0])   # dirección distinta
"""
print("--- Distancia euclidiana (menor = más cercano) ---")
print("d(a, b) =", distancia_euclidiana(a, b), " (esperado ≈ 4.4721)")
print("d(a, c) =", distancia_euclidiana(a, c), " (esperado ≈ 1.4142)")

print()
print("--- Similitud coseno (mayor = más parecido) ---")
print("cos(a, b) =", similitud_coseno(a, b), " (esperado 1)")
print("cos(a, c) =", similitud_coseno(a, c), " (esperado 0.8)")



fig, ax = preparar_plano("b tiene la misma dirección que a; c no", limite_x=(-1, 7), limite_y=(-1, 7))
dibujar_flecha(ax, a, "a", "tab:blue")
dibujar_flecha(ax, b, "b = 3a", "tab:red")
dibujar_flecha(ax, c, "c", "tab:orange")
plt.show() """


def normalizar(v):
    '''Devuelve el vector con la misma dirección pero longitud 1.'''
    return v / np.linalg.norm(v)


# --- Comprobación de la relación con u = [1,0] y v = [0.6, 0.8] ---
""" u = np.array([1.0, 0.0])
v = np.array([0.6, 0.8])

print("norma de u:", np.linalg.norm(u), "| norma de v:", np.linalg.norm(v))   # ambas 1
print("coseno(u, v)           =", similitud_coseno(u, v))                      # esperado 0.6
print("distancia(u, v) ** 2   =", distancia_euclidiana(u, v) ** 2)             # esperado 0.8
print("2 - 2 * coseno         =", 2 - 2 * similitud_coseno(u, v))              # esperado 0.8

# --- El ejemplo de documentos, ahora con vectores normalizados ---
a_n = normalizar(a)
b_n = normalizar(b)
c_n = normalizar(c)

print()
print("Normalizados:")
print("a_n =", a_n, "| b_n =", b_n, "| c_n =", c_n)
print("d(a_n, b_n) =", distancia_euclidiana(a_n, b_n), " (b ahora sí es el más cercano)")
print("d(a_n, c_n) =", distancia_euclidiana(a_n, c_n), " (esperado a mano: raíz(2 - 2*0.8) = raíz(0.4) ≈ 0.6325)")
print("cos(a_n, c_n) =", similitud_coseno(a_n, c_n), " (el coseno no cambió: normalizar no altera ángulos)") """



# =============================== VECTORES DE MUCHAS DIMENSIONES ==================================
#Este objeto utiliza un algoritmo moderno, seguro y muy rápido llamado PCG64 para producir aleatoriedad.
#el numero 42 solo es un numero de referencia para que inicie la ramdomizacion, puede ser cualquier otro
""" rng = np.random.default_rng(42)

#generar un conjunto de números aleatorios que siguen una distribución normal
#Distribución Normal Estándar: Como no le pasaste parámetros de media o desviación estándar,
# por defecto genera números con una media de 0.0 y una desviación estándar de 1.0.
# el size = 384 le indica a Python que quieres un vector (arreglo) de 384 números aleatorios.
v1 = rng.normal(size=384)
v2 = rng.normal(size=384)

#  sirve para saber el tamaño y la estructura (las dimensiones)
print("shape de v1:", v1.shape)
print("Primeros 5 números de v1:", v1[:5])   # [:5] = los primeros 5 elementos
print()
print("norma de v1             :", np.linalg.norm(v1))
print("distancia_euclidiana    :", distancia_euclidiana(v1, v2))
print("similitud_coseno        :", similitud_coseno(v1, v2))
 """


rng = np.random.default_rng(42)

cosenos = []
for _ in range(1000):                     # "_" = variable que no vamos a usar
    x = rng.normal(size=384)
    y = rng.normal(size=384)
    cosenos.append(similitud_coseno(x, y))

cosenos = np.array(cosenos)               # lista -> array, para usar min(), max(), mean()
print("Mínimo :", cosenos.min())
print("Máximo :", cosenos.max())
print("Promedio:", cosenos.mean())

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(cosenos, bins=30)                 # bins = número de cajas
ax.set_title("Coseno entre 1000 pares de vectores aleatorios (384 dimensiones)")
ax.set_xlabel("similitud coseno")
ax.set_ylabel("cantidad de pares")
ax.set_xlim(-1, 1)                        # mismo rango posible del coseno, para ver qué tan concentrados están
plt.show()