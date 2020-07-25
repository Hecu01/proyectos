import time
from datetime import date
from datetime import datetime                                #falta hacer el "def" tacticas, fundamentos y reglas, de los deportes de gimnasio
now = datetime.now()
format = now.strftime("""Hoy es: [%d/%m/%Y]
Hora de inicio: [%H:%M] hs""")


a = ("""1) Carreras a pie:

Correr es un proceso complejo y coordinado que involucra
a todo el cuerpo. Cada ser humano corre de una manera diferente,
pero ciertos aspectos son generales de los movimientos de carrera comunes.

Las carreras a pie son competiciones de atletismo para determinar cuál
de los competidores corre determinada distancia en el menor tiempo. Existen
campeonatos mundiales de carreras a pie, entre ellos los Juegos Olímpicos
y el Campeonato Mundial de Atletismo
""")

a1 = ("""   1.1) Carrera de velocidad:

Las carreras de velocidad en el atletismo consisten en recorrer
un corto espacio de terreno no superior a los 400 metros en el
menor tiempo posible.

Las distancias de las carreras de velocidad en campeonatos oficiales
varía dependiendo si son en pista cubierta o al aire libre, en pista
cubierta se disputan competiciones de 60, 200 y 400 metros lisos, al
aire libre se disputan 100, 200 y 400 metros lisos. También se realizan
competiciones sobre otras distancias fuera de las campeonatos oficiales,
como los 50 metros lisos, las 100 yardas o los 300 metros lisos entre
otras.

Los atletas que realizan estas pruebas suelen utilizar un calzado
especial con clavos en la parte inferior de la suela, conocidas
como zapatillas de clavos.

Los 100  m es la carrera más corta en el calendario de actividades
al aire libre. Es también una de las más antiguas ya que se han
encontrado indicios de esta carrera en el siglo XV  a. C, si nos
basamos en Homero y los poetas griegos.
""")
    
b = ("""2) Carreras de medio fondo:

Las carreras de media distancia son aquellas que se realizan sobre
una distancia superior a los 400 metros, deben su nombre a que se
disputan en distancias intermedias entre las de velocidad y las de
fondo (de más de 400 a 3000  m). De todas las pruebas reconocidas
por la IAAF, solo las de 800  m y las de 1500  m figuran en el
programa de los Juegos Olímpicos o Campeonatos del Mundo.

Los 800  m se realizaban originalmente con una distancia 880 yardas
o media milla (804,67  m).35​Es una prueba con las características
de la velocidad prolongada de las pruebas de velocidad largas y la
resistencia de las pruebas de fondo. Los atletas realizan el primer
cuarto de vuelta en su propia calle como en los 400  m, antes de
reintegrarse a la cuerda después de 100  m de carrera. Los
competidores deben demostrar, además de su capacidad física,
una táctica de anticipación y habilidad.

Los 1500  m, de tradición europea se supone que empezó a realizarse
hacia 1890 en Francia de evolución probable desde pruebas de una
milla británicas. Requiere en los competidores de una cierta
resistencia, un sentido táctico de la carrera y tanto velocidad
como resistencia en la última vuelta.

La milla británica (1609,32  m) está cercana a los (1500  m) y
es hasta la fecha la única disciplina reconocida por la IAAF,
definida por una longitud no métrica. Otras carreras de media
distancia son los 1000  m, los 2000  m y los 3000  m.


""")

c = ("""3) Larga distancia (fondo):

Las carreras que son mayores a 3000 m se consideran pruebas
de larga distancia. Entre las carreras más difíciles de larga
distancia están los maratones junto con los de campo a través
o cross. Estas últimas se realizan sobre un terreno tosco y
natural. La carrera de maratón invariablemente se realiza en
un circuito de 21 km 42 km.
""")
        
c1 = ("""   3.1) Carreras de fondo:

Las carreras de fondo son pruebas cuya distancia es superior
a 3000 metros de distancia. Hay referencias de pruebas de
resistencia que tuvieron lugar hacia 1740 en Londres, cuando
un atleta corrió la distancia de 17,300 m en una hora.

Los 5000 m es una adaptación de las tres millas (4828 m) y
los 10 000 m, seis millas (9656 m) que realizaban los
británicos.​ Estas pruebas se realizan en su totalidad en la
pista del estadio de atletismo. La resistencia a la fatiga
y el dolor, asociada con una buena aceleración final son
cualidades necesarias para los fondistas.
""")
      
c2 = ("""   3.2) Carreras en ruta:

Estas carreras tienen como punto común que se realizan fuera
del estadio de atletismo, generalmente por carreteras o
entre las calles de ciudades y pueblos.

La maratón no figuraba en el programa de los Juegos Olímpicos
Antiguos, pero su leyenda señala a las diversas historias de
la mitología griega, como la historia del soldado Filípides,
que corrió la distancia entre el campo de batalla hasta la ciudad
de Atenas, a donde llevó la noticia de la victoria. En 1895, el
francés Michel Bréal convenció a su amigo Pierre de Coubertin
para aprovecharse del mito y adaptarlo a los Juegos Olímpicos
modernos. Así, en los primeros Juegos de 1896, veinticuatro
competidores se reunieron en Maratón. El pastor griego Spiridon
Louis se convirtió en el primer ganador de esta nueva prueba.

En los Juegos de Londres en 1908, la familia real británica
quiso que la carrera comenzase en el castillo de Windsor y que
finalizara frente al palco real del Estadio Olímpico. El trayecto
medía precisamente 42,195 kilómetros y posteriormente se
convirtió en la distancia de la maratón oficial. Esta carrera
de resistencia se disputa por camino duro, sobre todo por las
calles y en un recorrido llano.

Algunas competiciones se desarrollan sobre distancias intermedias,
como los 21,097 kilómetros de la media maratón. El ultrafondo
designa la carrera a pie de gran distancia, es decir, todas las
distancias superiores a los 42,195 km de la maratón. Se aplica
a carreras en solitario y a las carreras o («raids»)
siguientes: 6 horas, 12 horas, 24 horas, 6 días, ultra-trail,
raids por etapas, 100 kilómetros y carreras por etapas.
""")
        
c3 = ("""   3.3) Campo a través:

El campo a través, es una carrera de fondo disputada en un terreno
variado. Aunque esta prueba no es olímpica en la actualidad, si lo
fue en tres Juegos olímpicos desde Estocolmo 1912 hasta París 1924,
y se compitió en dos modalidades: individual y por equipos. La
distancia va de 3 a 15 km, según grupos de edad y sexo. La primera
carrera de este tipo se celebró en Ville d'Avray en 1898, entre
los equipos de Francia e Inglaterra. Otras disciplinas como las
carreras en la naturaleza se realizan en bosques, montañas,
desiertos o en cualquier medio ambiente natural.
""")
       
c4 = ("""   3.4) Carreras de vallas:

Las carreras de obstáculos no parecen tener un origen antiguo
pues faltan referencias sobre ella en la antigüedad. Las primeras
apariciones en la historia son en tierras británicas inspiradas
en pruebas hípicas con obstáculos.

En la historia moderna del atletismo las primeras competiciones
se hicieron sobre una distancia de 120 yardas (109,72 metros)
con diez obstáculos de 3 pies y 6 pulgadas (1,06 m) 110 metros
con vallas que es la altura que todavía se utiliza hoy para la
categoría masculina y 100 para las mujeres. Los 110 metros
vallas, como los 100 metros vallas, su equivalente femenino,
es una prueba de velocidad que consta de diez vallas que hay
que saltar a una distancia de 9,14 m para los hombres y 8,50 m
para las mujeres.37​ Estas distancias y alturas varían según
la categoría de edad de la cometición.

Los 400 metros vallas son la evolución y estandarización de
la prueba de los 440 yardas con vallas cuya primera referencia
se remonta al año 1860 en Oxford. Los 400 metros vallas es una
de las carreas más técnicas y complicadas del atletismo, ya que
requiere la capacidad física de un velocista, control del ritmo
de carrera, control de la zancada y una buena técnica para el
paso de los obstáculos.

Los 3000 m obstáculos combinan la resistencia con el paso de
vallas. Parece ser que tiene su inicio en una apuesta entre
estudiantes, en referencia al deporte ecuestre británico muy
popular a finales del siglo XIX.38​Los atletas tienen que recorrer
en la pista una distancia de 3000 m, y también franquear
diferentes obstáculos no abatibles y una ría por vuelta.
Recientemente, los 3000 m obstáculos se abrieron a la participación
de las mujeres y la prueba apareció por primera vez para las
mujeres en el programa olímpico en el año 2008.
""")
       
c5 = ("""   3.5) Relevos:

El objetivo es cubrir la distancia lo más rápido posible con la
posesión de un cilindro de madera o metal llamado testigo y
transmitido de uno a otro atleta en unas zonas determinadas
llamadas zonas de transición.

Las carreras de relevos tienen su origen en las sociedades
antiguas, donde la velocidad y resistencia de los corredores
para transmitir mensajes de una ciudad a otra eran muy
importantes. Pero en los Estados Unidos la disciplina
adquirió popularidad en una carrera benéfica organizada
por los bomberos de Nueva York.

Las pruebas en las competiciones oficiales de la IAAF son
los 4×100 m y 4×400 m constan de cuatro atletas por equipo. Los
especialistas en estas carreras deben combinar la capacidad
física del atleta con el sentido de la anticipación y la
coordinación para la entrega del testigo. Las dos carreras
de relevos en su forma actual hicieron su primera aparición
olímpica en 1912
""")
      
d = ("""4) Marcha atlética:

La marcha atlética es una prueba de origen británico que data
del siglo XVIII. Entre 1775 y 1800 se celebraron marchas de
seis días, suscitando un gran entusiasmo popular. El primer
campeonato de marcha tuvo lugar en 1866 sobre siete millas,
y 1908 marca el inicio de esta disciplina en el programa de
los Juegos Olímpicos sobre 3500 m.41​ La marcha atlética es
una disciplina deportiva en la que se debe siempre caminar,
nunca correr; es decir, al menos un pie debe estar en
contacto con el suelo (a simple vista), mientras que la
pierna de apoyo debe estar recta (no doblada por la rodilla)
desde el momento en que el pie toca el suelo hasta que la
misma pase por la vertical del busto.

Las distancias oficiales se establecen hoy en distnacias
20 km y 50 km. realizandose competiciones estatales y
regionales en distancias variadas que pueden ser mayores
o mayores como los 100 km marcha. También son populares
realizadas sobre un tiempo determinado principalmente 1
hora o 2 horas marcha.
""")
        
e = ("""5) Saltos: ...""")
       
e1 = ("""   5.1) Salto con pértiga:

El salto con pértiga se remonta a las antiguas sociedades
griegas, pero se desarrolló al final del siglo XVIII en
Alemania durante las competiciones de gimnasia. Encontramos
las huellas de este evento en los Tailtean Games célticos
del siglo IX.42​ Hacia 1850, los miembros del Club de
Cricket de Ulverston en Reino Unido decidieron establecer
la prueba de «salto con garrocha». El salto con pértiga
consiste en franquear con la ayuda de una pértiga una barra
transversal, sin hacerla caer, después de una carrera de
impulso de unos treinta metros.43​ Durante los siglos, la
técnica de salto y los materiales han mejorado mucho. Las
pértigas de bambú utilizadas en los juegos de 1900 se
sustituyeron por pértigas de fibra de vidrio en 1956, y
después por las de fibra de carbono que son las que se
utilizan en la actualidad. La prueba estuvo incluida en
los primeros Juegos Olímpicos en 1896 y no fue incluida
en el calendario para las mujeres hasta los Juegos de
Sídney en el año 2000.
""")
        
e2 = ("""   5.2) Salto de longitud:

El salto de longitud existe en todas las competiciones
desde la Antigüedad. Los griegos la incluían ya en el
programa de los antiguos Juegos. La disciplina se desarrolló
en los países anglosajones a mediados del siglo XIX. El
salto de longitud consiste en saltar desde lo más próximo
a una «plancha de salida», después de una carrera de
impulso.
""")
        
e3 = ("""   5.3) Triple Salto:

El triple salto es una variante del salto de longitud. También
nacido en suelo irlandés, la prueba se desarrolló en
América. Como su nombre indica, el triple salto es llevar a
cabo una serie de tres saltos después del impulso: en primer
lugar sobre un pie, luego un segundo salto, siempre en las
mismas condiciones que el primero, y se completa como en la
longitud.
""")
        
e4 = ("""   5.4) Salto de altura:

El salto de altura es de origen celta y germánico. Ya se
practicaba en los Tailtean Games célticos del siglo IX. Desde
antes de 1470 se conocen concursos de altura y se transcriben
en los canales de la ciudad de Augsburg. Se incorporó a la
competición por primera vez en 1840 y quedó regulado en
1865. La regla es, después de tomar impulso, saltar una
barra horizontal lo más alto posible y sin derribarla. La
toma de impulso se realiza en un solo pie.​ La técnica de
salto se ha desarrollado mucho durante el siglo XX. La tijera
y el rodillo fueron muy utilizados por los atletas hasta
la llegada en 1968 del estilo Fosbury, utilizado por todos
los saltadores en la actualidad.
""")
       
f = ("""6) Lanzamientos:

El lanzamiento tiene lugar en la zona comprendida al
interior de un ovalo. El Discóbolo de Mirón simbolizado
por su famosa escultura del lanzador de disco en el
Pentatlón, nos llega desde temprano como historia real de
los lanzamientos de la antigüedad. El principio mismo de
lanzar se inspira en el gesto ancestral del cazador.
""")
    
f1 = ("""   6.1) Lanzamiento de peso:

El lanzamiento de peso tiene su origen en la mitología griega,
donde Homero describe a los lanzadores de piedras. El primer
evento oficial se disputó en los Estados Unidos en 1876. El
peso que se lanza es de 16 libras (7,257 kilogramos), tomando
como referencia la bala de cañón, y la técnica de lanzamiento
evolucionó entre la posición fija, al lanzamiento con toma
de impulso. La idea es lanzar la bola lo más lejos posible
de un círculo que tiene una línea situada en el área de
lanzamiento que no puede ser sobrepasada por el lanzador.
""")
       
f2 = ("""   6.2) lanzamiento de disco:

El lanzamiento de disco es la prueba atlética mejor descrita
por los griegos. Las técnicas para el lanzamiento y los
distintos discos se explican en la Ilíada. El solo era
un disco con un orificio por el que pasaba una cuerda,
mientras que el discos era plano, hecho de piedra o bronce. La
disciplina se desarrolló en los Estados Unidos al final del
siglo XIX. En 1907, el peso del disco masculino se fijó en 2 kg
y un diámetro de 22 cm.
""")
        
f3 = ("""   6.3) Lanzamiento de martillo:

Se han encontrado rastros de lanzamiento de martillo en las antiguas
leyendas celtas que datan de 829 a. C, y durante la Edad Media, donde
el verdadero martillo de herrero sustituyó a los artes rústicos de la
Antigüedad. Al igual que otras disciplinas de lanzamiento, el martillo
ha evolucionado a lo largo de los siglos, tanto en la forma como en
el peso.50​ Hoy en día, para los hombres, la bola de acero pesa 7,257
kilogramos (16 libras) y está conectada a un cable de acero con un
mango. Autorizadas a competir solo a partir de 1995, las mujeres
lanzan un martillo de 4 kg.
""")
        
f4 = ("""6.4) Lanzamiento de jabalina:

La jabalina, ​herramienta de caza utilizada por las civilizaciones
antiguas, y también un arma usada por muchos ejércitos de la
antigüedad, está en el origen de la disciplina de lanzamiento
de jabalina. Hércules se considera que fue uno de los primeros
lanzadores de jabalina. La prueba figuraba en el programa de
los Juegos Olímpicos Antiguos. Hacia 1780, los escandinavos
adoptaron y desarrollaron la disciplina. La jabalina, incluso,
se convirtió en un símbolo de la independencia nacional en
Finlandia. Las marcas han ido aumentado de manera constante
durante los siglos, tanto es así que la jabalina ha sido
rediseñada varias veces en la década de 1980 para controlar
la seguridad y reducir el tiempo de vuelo. A pesar de estas
medidas, los incidentes siguen produciéndose hoy en día. En
2007, los atletas Roman Šebrle y Salim Sdiri fueron alcanzados
accidentalmente por una jabalina durante las reuniones.
""")

#a1
#b
#c
#c1
#c2
#c3
#c4
#c5
#d
#e
#e1
#e2
#e3
#e4
#f
#f1
#f2
#f3
#f4


def return1():
    
    preguntandoteavos=input('¿Desea definir otro? (si/no) ')
    if preguntandoteavos == "si":
        return definiciones2()
    elif preguntandoteavos == "no":
        print('¿Donde desea volver?')
        print('(A) Atletismo')
        print('(B) Inicio')
        print('(C) Finalizar')
        replanteo = input('Escriba una letra ')
        if replanteo == "A":
            atletismo()
        elif replanteo == "B":
            inicio()
        elif replanteo == "C":
            final()
        else:
            print('escriba algo valido por favor')
            return return1()


            

def definiciones2():

        
    numero = int(input('Número de prueba: '))
    if numero == 1:
        print(a)
        return1()
    else:
        print("probando")

        
def pruebas_atletismo():
    print('¿Desea..?')
    time.sleep(2)
    print('(A) Definir todos')
    time.sleep(2)
    print('(B) Definir 1 en específico')
    definiciones=input('Ingrese una letra ')
    
    if definiciones == "A":
        print(a)
        enter()
        print(a1)
        enter()
        print(b)
        enter()
        print(c)
        enter()
        print(c1)
        enter()
        print(c2)
        enter()
        print(c3)
        enter()
        print(c4)
        enter()
        print(c5)
        enter()
        print(d)
        enter()
        print(e)
        enter()
        print(e1)
        enter()
        print(e2)
        enter()
        print(e3)
        enter()
        print(e4)
        enter()
        print(f)
        enter()
        print(f1)
        enter()
        print(f2)
        enter()
        print(f3)
        enter()
        print(f4)
        enter()


    elif definiciones == "B":
        definiciones2()
    else:
        print('Escriba algo válido')
        print('')
        return pruebas_atletismo()



def enter():
    print('')
    print('Presione enter para continuar')
    input('')

#El saludo de entrada
def saludo():
    print ('Saludos '+str(tunombre)+'')
    time.sleep(.3000)
    print(format)
    print('')
    time.sleep(.3000)
    print ('+----------------------------+')
    print ('| #    #    ##    #     ##   |')
    time.sleep(.3000)
    print ('| #    #   #  #   #    #  #  |')
    time.sleep(.3000)
    print ('| #    #   #  #   #    #  #  |')
    time.sleep(.3000)
    print ('| ######   #  #   #    ####  |')
    time.sleep(.3000)
    print ('| #    #   #  #   #    #  #  |')
    time.sleep(.3000)
    print ('| #    #   #  #   #    #  #  |')
    time.sleep(.3000)
    print ('| #    #    ##    ###  #  #  |')
    time.sleep(.3000)
    print ('+----------------------------+')
    print('')
    time.sleep(2)


    

# Historias

def historia_del_basquet():
    time.sleep(3)
    print(""" Historia del baloncesto

Los orígenes del baloncesto se remontan muchos años atrás.
En la época de los mayas se practicaba el pok-a-pok, un
juego en el que se utilizaba una pelota maciza de caucho
que debía golpearse con los muslos y las caderas, y los
perdedores eran sacrificados para ofrecerlos a los dioses.

No obstante, el básquet, tal y como lo conocemos ahora,
nació en 1891 en Estados Unidos, de la mano de James Naismith,
profesor de Educación Física en la Universidad de YMCA,
Springfield (Massachussets). Naismith quería inventar un
deporte que pudiera practicarse en el gimnasio, para pasar
los duros y fríos días de invierno. Observó los deportes
que había entonces -el rugby, el béisbol, el
fútbol, etc.,- basados principalmente en la fuerza o el
contacto físico y pensó en uno que requiriese más destreza.
""")
    enter()
    print("""
El profesor pidió al conserje unas cajas de 50 centímetros
de diámetro y lo que obtuvo fueron dos cestas de melocotones
que hizo colgar a cada lado de la pista del gimnasio, a
3,05 metros de altura. Fue así como surgió el nombre de
basketball, palabra inglesa que define el objetivo del
juego: introducir la pelota dentro de una cesta. 

Naismith diseñó trece reglas alrededor de este nuevo
deporte. Como tenía 18 alumnos, los equipos de baloncesto
estaban compuestos por nueve jugadores cada equipo. Después
pasaron a ser siete miembros, para acabar siendo cinco.
""")
    enter()
    print("""
Con el tiempo las cestas de melocotones se convirtieron en
aros metálicos con una red sin fondo. Y, también,
surgieron los tableros, donde se colgaban las canastas.

El baloncesto cuajó rápidamente en EEUU y no tardó en
dar el salto a Europa. Fue un deporte de exhibición en
los Juegos Olímpicos de Ámsterdam (1928) y de Los Ángeles
(1932), pero en los Juegos Olímpicos de Berlín (1936) Naismith
tuvo la oportunidad de ver cómo el deporte que él creó se
convertía en categoría olímpica. El baloncesto femenino
tuvo que esperar unos años más, hasta 1976 para ser
admitido como deporte olímpico.

""")
    enter()
    print("""
En 1950 se desarrolló el Primer Campeonato Mundial de
Basquetbol, llamado “Libertador General SanMartín”, en
conmemoración por el centenario de su fallecimiento. Se
llevó a cabo en Buenos Aires, Argentina entre el 22 de
octubre y el 3 de noviembre, todos los partidos se
disputaron en el estadio Luna Park.

En el torneo participaron 10 selecciones nacionales
(8 de una fase de clasificación, una invitada y el
organizador). Estas naciones fueron por América, el
local, Argentina, Brasil, Chile, Ecuador, Estados Unidos
y Perú. Mientras que, por la clasificación de la Eurobasket
de 1949, jugaron, Egipto, España, Francia y Yugoslavia.

""")
    enter()
    print('')
    print("""
Argentina fue la campeona, derrotando en la final a los
Estados Unidos en cifras de 64 a 50 (fue el partido
donde se anotaron la mayor cantidad de puntos).
Así es como poco a poco este deporte fue haciéndose
un hueco a nivel mundial y, actualmente, el baloncesto
cuenta con gran difusión en diferentes países, siendo
uno de los deportes con más participantes y competiciones
regulares en distintas zonas del mundo.
""")
    time.sleep(5)
    
    
    def historiabasquet():
        sabermas=input(''+str(tunombre)+', ¿Desea saber la historia del Mini Básquet?')
        
        if sabermas == "sí":
            print("""Historia del mini basquetbol:

Jay Archer sería quien le diera inicio a esta disciplina,
quien nació en año 1912 en la ciudad de Soranton, en
Pensylvania. 

Estudió en la universidad de Stroudsbourg en el estado
de Pensylvania, en ésta se graduó de educación física
siendo de alguna manera influenciado por la pedagogía
la escuela, de algún modo empezó a preocuparse por los
problemas que atravesaban los niños y planteaba la
necesidad de la creación de nuevos deportes que estuviesen
adaptados a los más pequeños y sus necesidades ya que según
el, existían pocos deportes que los ayudaran con su desarrollo.
 """)
            enter()
            print("""
Entonces, decidió crear el Biddy Basket, en el año 1950,
su nombre tal vez es un poco peculiar pero este se debe
a un antojo de su hija ya que un día pidió «biddy» que
en la correcta traducción significara torta pequeño, y
debido a esto se le ocurrió utilizar esta palabra en
algo muy nuevo y que de cierta manera no tenía nada que ver.

Al principio se desarrolló, a diferencia de como se
venía realizando en la historia del basquetbol, con
balones más pequeños y aros más bajos ( 2.60mts) que
de alguna manera pudiesen hacer que los niños se
desempeñaran de manera más fácil en el juego.
""")
            enter()
            print("""
Debía ser un juego que los divirtiera, los alegrara y
sobre todo que los motivara a continuar y a seguir
creciendo en el deporte. La intención era que se
introdujeran en el deporte bajo su tecnicidad y
bajo el cumplimiento de sus reglas.

De pronto, empezó a tener una rápida difusión. Se
interesaron pues en esa nueva modalidad de juego,
haciendo de una vez una amplia difusión por televisión,
procurándose de que fuese en el canal más importante de
Nueva York para que su difusión fuese más certera. .
""")
            enter()
            print("""
LLegaría para cambiar el rumbo de este deporte. Tuvo
una importante evolución en la década de los años
setenta en la cual sería una importante fuente de
jugadores profesionales.

A nuestro país llega en el añon1964, rápidamente se
comienza a difundir y a adaptarse al medio. Lo
importante de este nuevo movimiento es de qué se
trataba precisamente de UN JUEGO PARA NIÑOS.
""")
            enter()
            print("""
La filosofía de sus reglas así lo indican, donde uno
de sus objetivos principales es que todos los integrantes
participen al menos de un cuarto y como máximo en dos
de ellos.""")
            enter()


            return basquet()
        
        if sabermas == "no":
            return basquet()
        else:
            print('Escriba "sí" o "no".')
            return historiabasquet()
        
    historiabasquet()
 



    

    






#Reglas




def reglasbasquet():
    print('')
    print('REGLAS')
    time.sleep(2)
    print("""
La Federación Internacional de Baloncesto (en francés,
Fédération Internationale de Basket-ball, FIBA) es el organismo
que se dedica a regular las normas del baloncesto mundialmente,
así como de celebrar periódicamente competiciones y eventos en
sus dos disciplinas.

Fue fundada en 1932 y tiene su sede actual en Mies (Suiza).
Cuenta en 2018 con la afiliación de 213 federaciones nacionales,
​divididas a su vez en 5 federaciones continentales, que
son: África, América, Asia, Europa y Oceanía. El argentino
Horacio Muratore es el presidente de la FIBA desde 2014.
""")
    enter()
    print('Son 13 reglas bien descritas')
    print('')
        
    print("""1- El balón puede ser lanzado en cualquier dirección
con una o ambas manos.
""")
    time.sleep(3)
    print("""2- El balón puede ser golpeado en cualquier dirección
con una o ambas manos, pero nunca con el puño.
""")
    time.sleep(3)
    print("""3- Un jugador no puede correr con el balón. El jugador debe
lanzarlo desde el lugar donde lo toma.
""")
    time.sleep(3)
    print("""4- El balón debe ser sujetado con o entre las manos. Los
brazos o el cuerpo no pueden usarse para sujetarlo.
""")
    time.sleep(3)
    print("""
5- No se permite cargar con el hombro, agarrar, empujar,
golpear o zancadillear a un oponente. La primera infracción a esta
norma por cualquier persona contará como una falta, la segunda lo
descalificará hasta que se consiga una canasta, o, si hay una
evidente intención de causar una lesión, durante el resto del
partido. No se permitirá la sustitución del infractor.
""")
    enter()
    print("""6- Se considerará falta golpear el balón con el puño, las
violaciones de las reglas 3 y 4, y lo descrito en la regla 5.
""")
    time.sleep(4)
    print("""7- Si un equipo hace tres faltas consecutivas (sin que el
oponente haya hecho ninguna en ese intervalo), se contará un punto
para sus contrarios.
""")
    time.sleep(4)
    print("""8- Los puntos se conseguirán cuando el balón es lanzado o
golpeado desde la pista, cae dentro de la canasta y se queda allí. Si
el balón se queda en el borde y un contrario mueve la cesta, contará
como un punto.
""")
    time.sleep(4)
    print("""9- Cuando el balón sale fuera de banda, será lanzado dentro del
campo y jugado por la primera persona en tocarlo. En caso de duda, el árbitro
lanzará el balón en línea recta hacia el campo. El que saca dispone de cinco
segundos. Si tarda más, el balón pasa al oponente.
""")
    enter()
    print("""10- El árbitro auxiliar, "umpire", sancionará a los jugadores
y anotará las faltas, avisará además al "referee" (árbitro principal, véase
el siguiente punto) cuando un equipo cometa tres faltas consecutivas.
Tendrá poder para descalificar a los jugadores conforme a la regla 5.
""")
    time.sleep(4)
    print("""11- El árbitro principal, "referee", jugará el balón y decide
cuando está en juego, dentro del campo o fuera, a quién pertenece, y
llevará el tiempo. Decidirá cuando se consigue un punto, llevará el marcador
y cualquier otra tarea propia de un árbitro.
""")
    time.sleep(4)
    print("""12- El tiempo será de dos mitades de 15 minutos con un descanso
de 5 minutos entre ambas.
""")
    time.sleep(3)
    print("""13- El equipo que consiga más puntos será el vencedor
""")
    time.sleep(2)
    
    final()

     
def reglasrugby():
    print('')
    print ('REGLAS BÁSICAS')
    time.sleep(2)
    print("""EL JUEGO:
En el rugby se enfrentan dos equipos de quince jugadores
cada equipo (aunque hay una variación para un juego de siete).
""")
    enter()
    print ("""- No se permite pasar el balón hacia adelante. Tampoco se permite
que el balón caiga hacia adelante, lo cual se denomina knock-on
""")
    enter()
    print('')
    print('- El balón sólo puede avanzar llevándolo o pateándolo hacia adelante')
    time.sleep(3)
    print("""- Cualquier jugador en el campo de juego puede avanzar con el balón.
""")
    enter()
    print("""- Un jugador placado o tacleado (derribado) debe pasar o soltar
inmediatamente el Balón. El jugador que taclea debe también soltar
inmediatamente al jugador tacleado.
""")
    time.sleep(7)    
    print("""- El rugby es un deporte continuo. No se prevé
interrupciones (a menos que haya una lesión.).
""")
    time.sleep(3)    
    print("""- Una scrum reinicia el juego después de un pase hacia adelante
o un knock-on. También se forma una  scrum en otras ocasiones
menos frecuentes.
""")
    time.sleep(5)    
    print("""- Cuando a un jugador se le cae la pelota hacia adelante (no la
pudo recepcionar bien y se le cae, o le golpea en alguna parte
del cuerpo-de la cintura hacia arriba- y se le cae,), se cobra
una infracción para el otro equipo, denominándose pase forward.
""")
    enter()    
    print("""- Un line-out reinicia el juego cuando el balón sale del
terreno de juego, por medio de algún jugador, o el portador
de la pelota pisa la línea de touch.
""")
    time.sleep(5)    
    print("""-Un Try es otorgado cuando el balón es llevado más
allá la línea de in goal (zona de anotación) y apoyado
en el suelo.
""")
    enter()    
    print("""   - 5 puntos se otorgan al realizar un try.""")
    time.sleep(3)    
    print("""   - 2 puntos se otorgan al convertir la patada adicional después
    de un try.
""")
    time.sleep(3)    
    print("""   - 3 puntos se otorgan al convertir un penal de campo
    (golpe) después de cometida una infracción.
""")
    time.sleep(5)    
    print("""   - 3 puntos se otorgan al convertir un drop (patada de sobre pique)
    en juego abierto.
    """)
    enter()    
    print("""- Después de que se convierte un try o un penal, el balón es
pateado hacia el equipo anotador, desde mitad de cancha,
mediante un drop.
""")
    time.sleep(7)    
    print("""- El árbitro es el responsable de hacer respetar el reglamento.""")
    time.sleep(5)    
    print("""- Se juega en dos tiempos continuos de 40 minutos cada uno
con un intermedio de 5 minutos.""")
    time.sleep(5)    
    print("""- El tiempo lo lleva el árbitro principal y debe detenerlo
solamente cuando haya lesiones.
""")
    enter()    
    print("""- Hay dos jueces de línea que ayudan a indicar cuándo
el balón o la persona que lo lleva salen del campo de juego.
""")
    time.sleep(5)
    print("""
CAMPO DE JUEGO:
Un campo de juego es rectangular, y no debe exceder de 95 metros
de largo por 65 metros de ancho.13​ Las líneas laterales
(denominadas "líneas de touch") del campo de juego no forman
parte de este. A continuación de cada uno de los lados menores
del rectángulo hay una zona de anotación (o de ensayo), denominada
"in-goal", con una longitud de entre 10 y 22 m
""")
    enter()
    print('OJO... no confundir Rugby con futbol americano (el fútbol yanqui)')
    time.sleep(2)

    final()



    
def reglasfutbol():

    
    print('')
    print ('REGLAS')
    time.sleep(2)
    print("""
Las reglas del fútbol, también conocidas como
las reglas de juego son las reglas que rigen el fútbol
en todo el mundo. Los cambios asociados en las mismas están
a cargo de la International Football Association Board, la cual
está conformada por la FIFA y las cuatro asociaciones de fútbol
del Reino Unido.
""")
    time.sleep(10)
    print('- El balón será de cuero o cualquier otro material adecuado')
    time.sleep(2)
    print('- Tendrá una circunferencia no superior a 70 cm y no inferior a 68 cm.')
    time.sleep(2)
    print('- Su peso no será superior a 450g y no inferior a 410g al comienzo del partido')
    time.sleep(2)
    print('- Tendrá una presión equivalente a 0,6–1,1 atmósferas al nivel del mar')
    time.sleep(7)
    print("""
- CAMPO DE JUEGO:
El terreno de juego debe ser de campo natural o artificial, aunque
esta opción puede depender del reglamento de la competición. El
terreno tendrá forma rectangular, siendo su largo entre 90 y 120m
(de 100 a 110 m para partidos internacionales), y su ancho entre
45 y 90 m (de 64 a 75 m para partidos internacionales)
""")
    time.sleep(7)
    print("""- JUGADORES:
Cada uno de los dos equipos que juegan un partido podrá tener
un máximo de 11 jugadores {contando con el arquero}, dentro
del terreno, de los cuales uno jugará como portero, y no menos
de 7 por equipo. Si se llega a este número de jugadores, se
termina el partido, dando como ganador al equipo contrario,
con un marcador de tres a cero, aunque este último número
puede variar según la competición.
""")
    time.sleep(2)
    print('Éstas fueron lás reglas principales del futbol')
    time.sleep(2)
    
    final()

    
def reglashockey():
    print('')
    print('REGLAS')
    time.sleep(2)
    print('-Acá habrá reglas de hockey')
    time.sleep(2)
    print('- Aca otras reglas...')
    time.sleep(2)
    print('- y otras...')
    time.sleep(2)
    
    final()



#Fin de las reglas )






#Fundamentos(




def fundamentosbasquet():
    print('')
    print('FUNDAMENTOS')
    print('')
    time.sleep(2)
    print('Los fundamentos del Baloncesto son 3')
    time.sleep(2)
    print('1- EL BOTE Y EL DRIBLING')
    time.sleep(2)
    print('2- EL PASE')
    time.sleep(2)
    print('3- EL TIRO A LA CANASTA')
    time.sleep(2)
    print('Los fundamentos para describir es mucho :)')
    
    def variable_fundamentos_basquet():
        masfundamentosbasquet = input(''+str(tunombre)+' ¿Desea que los describa? (si/no) ')
        print('')
        time.sleep(.300)
        if masfundamentosbasquet == "si":
            print('Preparados...')
            time.sleep(2)
            print('Listos...')
            time.sleep(3)
            print('YA!')
            time.sleep(2)
            print("""
1- EL BOTE Y EL DRIBLING

Botar la pelota es la acción de lanzarla con
una mano contra el suelo para que rebote,
repetidamente. Es la manera de avanzar cuando
se está en posesión de la pelota. Hay que dominar
el bote con las dos manos por igual.
""")
            time.sleep(10)
            
            
            print("""
Podemos distinguir distintos tipos de bote:

Bote de protección:
Se utiliza cuando tenemos un defensa
cerca que nos impide progresar con la pelota. La pelota
ha de botar entre ambos pies, más abajo de la cintura.
Se protege el bote con la pierna y el brazo opuesto

Bote de velocidad:
Se utiliza cuando se quiere avanzar
rápidamente y no hay ningún defensa delante. La pelota
bota en el suelo al lado, por delante del jugador. La
pelota, en el rebote, puede subir un poco por encima
de la cintura.""")

            enter()
            print("""
2- EL PASE

Es la acción de pasar la pelota a un compañero con
seguridad y precisión, para poder continuar la
jugada de ataque. Es la manera más rápida de
avanzar en posesión de la pelota. Los hay de
varios tipos:
""")
            time.sleep(10)
            print("""

Pase de pecho:
Es el pase más utilizado en el
baloncesto, en distancias cortas y medias. Se
inicia desde la posición básica. Con los brazos
flexionados a la altura del pecho, se lanza
la pelota mediante la extensión de los brazos
y con un movimiento de muñeca final.
La trayectoria ha de ser recta y rápida
para sorprender al adversario.
""")
            enter()
            
            print("""
Pase picado:
Se ejecuta igual que el pase de
pecho, pero los brazos van en la misma
dirección que la pelota, hacia el suelo. La
pelota no ha de botar demasiado lejos del
receptor para que éste pueda recibirla a la
altura de la cintura. También se realiza
con una mano.
""")
            time.sleep(15)
            print("""
Pase por encima de la cabeza:
Manteniendo la pelota
por encima de la cabeza, los brazos se extienden en
la misma dirección hacia donde queremos que vaya
la pelota y, en el último instante, se le da un
golpe seco con las muñecas.
""")
            enter()
            print("""
Pase de béisbol:
Sujetamos la pelota con las dos
manos a la altura de la oreja. Tiene la misma
mecánica que el lanzamiento de una piedra o
una pelota de béisbol. Sirve para efectuar
un pase a larga distancia, sobre todo en los
contraataques. También puede ser picada
mediante un bote en su trayectoria.
""")
            enter()
            print("""
Pase de mano a mano:
Se realiza cuando tenemos al
compañero receptor muy cerca, de manera que
recibe la pelota casi de manos del pasador.
En el momento del pase, la mano que sirve la
pelota, le da un pequeño impulso para que el
otro jugador pueda recibirla y continuar con
la jugada.
""")
            time.sleep(15)
            print("""
3- EL TIRO A LA CANASTA

El tiro es el lanzamiento de la pelota a
canasta con el objetivo de que entre por
el centro del aro. Con este elemento fundamental
del baloncesto culmina el juego de ataque.
""")
            time.sleep(7)
            print("""
Hay, también, diferentes tipos de lanzamiento
a canasta:

Tiro libre o lanzamiento personal:
Es un lanzamiento estático. Se concede como
penalización de las faltas personales del
equipo contrario. En posición básica, detrás
de las líneas de tiros libres, se coloca la
pelota por delante de la cara y se tira a
canasta con una mano, mientras la otra sirve
de acompañamiento.
""")
            enter()
            print("""
Lanzamiento en suspensión:
Se ejecuta igual que el personal, pero con un
salto incluido. Cuando el cuerpo está en el
aire, se realiza el lanzamiento a canasta,
con un golpe final de muñeca.

Hay cuatro fases: salto, suspensión, lanzamiento y caída.
""")
            time.sleep(15)
            print("""
Lanzamiento en bandeja:
Se realiza muy cerca del aro. Este tiro debe
dominarse tanto con la mano derecha como con
la izquierda, pues es conveniente que el
lanzamiento se ejecute con la mano más alejada
del defensor. La pelota debe quedar casi
amortiguada sobre la canasta, como si se dejara
en bandeja. Puede ser el tiro resultante de una
jugada de entrada a canasta, de un rebote ofensivo
cerca del aro, de una asistencia a un compañero
cercano a la canasta o de una finta de algún
pívot. Es un lanzamiento muy efectivo.
""")
            enter()
            print("""
Entrada a canasta:
Es un enceste con una carrera previa. Si nos
dirigimos a la canasta por el lado derecho,
botaremos la pelota y la lanzaremos con la mano
derecha; si vamos por el lado izquierdo, la
botaremos y lanzaremos con la mano izquierda. Los
dos últimos pasos de la carrera sirven para
aproximarse a la canasta e impulsarse hacia arriba,
con le fin de dejar la pelota la más cerca posible
del aro.
""")
            enter()
            print("""
Clavada o mate:
Es una manera de encestar muy espectacular, que ha
dado lugar a competiciones específicas (concurso
de clavadas). Los jugadores de la NBA son grandes
especialistas en mates. Consiste en impulsar la
pelota directamente dentro de la canasta, con una
mano o con las dos, por encima del aro. Requiere un
gran salto y un fuerte golpe de muñeca.


""")
            enter()
            print("""ufff espero no haberte agotado""")
            time.sleep(2)
            print('quería que fuese lo más explícito posible, '+str(tunombre)+'')
        elif masfundamentosbasquet == "no":
            time.sleep(2)
        else:
            print('Escriba si o no')
            time.sleep(1)
            return variable_fundamentos_basquet()

    variable_fundamentos_basquet()
    
    final()






def fundamentosfutbol():

    
    print('')
    print('FUNDAMENTOS')
    time.sleep(2)
    print('Los fundamentos del fútbol son 4')
    time.sleep(2)
    print('1- Controlar el balón')
    time.sleep(2)
    print('2- Conducir el balón')
    time.sleep(2)
    print('3- Pasar el balón')
    time.sleep(2)
    print('4- Disparar')
    time.sleep(2)
    
    def variable_fundamentos_futbol():
        masfundamentosfutbol = input(''+str(tunombre)+' ¿Desea que los describa? (si/no) ')
        print('')
        time.sleep(.300)
        if masfundamentosfutbol == "si":
             print("""1- CONTROLAR EL BALÓN:
Es la acción técnica mediante la cual el jugador adquiere la posesión
del balón dejándolo en condiciones para la siguiente acción
técnico-táctica.
""")
             time.sleep(7)
             print("""2- CONDUCIR EL BALÓN:
Consiste en conducir el balón libremente, Conducir bien el balón
significa ser su dueño en todo  momento esto requiere un excelente
dominio. es necesario  aprender a conducir el balón con la cabeza
levantada esto permite a realizar correctamente la jugada requerida.
""")
             time.sleep(5)
             print("""3- PASAR EL BALÓN:
El pase es el punto de poseer y luego transferir
el balón  de un compañero a otro....
Esto tiene como objetivo:
       

          - Preparar los ataques
          - Armar las jugadas
          - Poseer el balón en equipo
          - Contraatacar
          - Dar ultimo pase o Pase de gol.
""")
             enterr()
             print("""4- DISPARAR:
Para chutar a portería el jugador se debe colocar detrás de la
pelota y poner su pie de apoyo justo al lado de la misma.
Posteriormente tendrá que llevar hacia atrás la pierna con la
cual va a chutar y golpear el balón con una de las superficies
de contacto del pie anteriormente descritas.
""")
             time.sleep(5)

    
        elif masfundamentosfutbol == "no":
            time.sleep(2)
        else:
            print('Escriba si o no')
            time.sleep(1)
            return variable_fundamentos_futbol()

    variable_fundamentos_futbol()
    
    final()




    
def fundamentosrugby():
    print('')
    print('FUNDAMENTOS')
    time.sleep(1)
    print('acá irán los fundamentos')
    time.sleep(1)
    print('de')
    time.sleep(1)
    print('rugby')
    time.sleep(2)
    
    final()



def fundamentoshockey():
    print('')
    print('FUNDAMENTOS')
    time.sleep(2)
    print('-Acá estarán los fundamentos del hockey')
    time.sleep(2)
    print('- y Aca otros fundmanentos...')
    time.sleep(2)
    print('- y y otros...')
    time.sleep(2)

    final()
    




#Fin de los fundamentos )


 
def pruebasatletismo():
    print('')
    print("""PRUEBAS""")
    time.sleep(3)
    print("""1) Carreras a pie:""")
    time.sleep(3)
    print("""   1.1) Carrera de velocidad""")
    time.sleep(3)
    print("""2) Carreras de medio fondo """)
    time.sleep(2)
    print("""3) Larga distancia (fondo) """)
    time.sleep(3)
    print("""   3.1) Carreras de fondo""")
    time.sleep(3)
    print("""   3.2) Carreras en ruta""")
    time.sleep(3)
    print("""   3.3) Campo a través""")
    time.sleep(3)
    print("""   3.4) Carreras de vallas""")
    time.sleep(3)
    print("""   3.5) Relevos""")
    time.sleep(3)
    print("""4) Marcha atlética""")
    time.sleep(3)
    print("""5) Saltos""")
    time.sleep(3)
    print("""   5.1) Salto con pértiga""")
    time.sleep(3)
    print("""   5.2) Salto de longitud""")
    time.sleep(3)
    print("""   5.3) Triple Salto""")
    time.sleep(3)
    print("""   5.4) Salto de altura""")
    time.sleep(3)
    print("""6) Lanzamientos""")
    time.sleep(3)
    print("""   6.1) Lanzamiento de peso""")
    time.sleep(3)
    print("""   6.2) lanzamiento de disco""")
    time.sleep(3)
    print("""   6.3) Lanzamiento de martillo""")
    time.sleep(3)
    print("""   6.4) Lanzamiento de jabalina""")
    time.sleep(3)
    print("""7) Pruebas combinadas""")
    time.sleep(2)
    pruebas_atletismo()
    

def atletismo():
                #atletismo preguntas
    print ('Bienvenido a atletismo, '+str(tunombre)+'.')
    time.sleep(1)
    print("""Aquí, el atletismo comprende un conjunto de prácticas
deportivas o mejor dicho "pruebas""")
    time.sleep(2)
    print('Que son las siguientes')
    pruebasatletismo()



def natación():
        
                #Aprender de natación
    print('')
    print('')
    print('')
    print ('Bienvenido a Natación, '+str(tunombre)+'.')
    time.sleep(1)
    print('¿Qué desea aprender?')
    time.sleep(2)
    print('¿Qué desea aprender?')
    time.sleep(2)
    print('(A) Reglas')
    time.sleep(2)
    print('(B) Fundamentos')
    time.sleep(2)
    print('(C) Historia de la Natación')
    pregunta1=input('Escriba una letra')
    if pregunta1 == "A":
        reglasnatación()
    elif pregunta1 == "B":
        fundamentosnatacion()
    elif pregunta1 == "C":
        historia_de_la_natacion()
    else:
        print('Escríbalo como está en la consola')
        return natacion()
                




#Aprende de deportes abiertos de campo


#cátedra 1
def deportesdecampo():
        print('')
        print('')
        print('')
        time.sleep(2)
        print('Bienvenido a Deportes Abiertos de Campo')
        time.sleep(2) 
        print('¿Sobre qué deporte le gustaría aprender, '+str(tunombre)+'?: ')
        time.sleep(2)
        print('')
        print('(A) Rugby')
        time.sleep(2)
        print('(B) Fútbol')
        time.sleep(2)
        print('(C) Hockey sobre césped')
        time.sleep(2)
        print('(D) Softbol')
        time.sleep(2)
        print('(E)')
        time.sleep(2)
        print('')
        aprender = input('Escriba una letra por favor. ')
        time.sleep(1)

        
        if aprender == "A":
        
            def rugby():
                #rugby preguntas
                print ('Bienvenido a Rugby, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                time.sleep(2)
                def preguntarugby():
                    
                    pregunta=input('reglas, fundamentos, tacticas? ')
                    if pregunta == "reglas":
                        reglasrugby()
                    elif pregunta == "fundamentos":
                        fundamentosrugby()
                    elif pregunta == "tacticas":
                        tacticasrugby()
                    else:
                        print('Escríbalo como está en la consola')
                        return preguntarugby()
                    
                preguntarugby()
                
            rugby()


        elif aprender == "B":
            
            
            def futbol():
        #futbol preguntas
                print ('Bienvenido a Fútbol, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                print('')
                time.sleep(2)
                print('(A) Reglas')
                time.sleep(2)
                print('(B) Fundamentos')
                time.sleep(2)
                print('(C) Historia del fútbol')
                time.sleep(2)

                
                def preguntafutbol():
                    
                    pregunta1=input('Escriba una letra: ')
                    if pregunta1 == "A":
                        reglasfutbol()
                    elif pregunta1 == "B":
                        fundamentosfutbol()
                    elif pregunta1 == "C":
                        historia_del_futbol()
                    else:
                        print('Escriba una letra: "A", "B", o "C" (Mayúscula): ')
                        return preguntafutbol()
                
                preguntafutbol()
                
            futbol()


        elif aprender == "C":

            
            def hockey():
                #hockey preguntas
                print ('Bienvenido a Hockey sobre Césped, '+str(tunombre)+'.')
                time.sleep(1)
                print('Que desea aprender?')
                time.sleep(2)
                
                def preguntahockey():
                    pregunta=input('reglas, fundamentos, tacticas? ')
                    if pregunta == "reglas":
                        reglashockey()
                    elif pregunta == "fundamentos":
                        fundamentoshockey()
                    elif pregunta == "tacticas":
                        tacticashockey()
                    else:
                        print('Escriba una letra: "A", "B", o "C" (Mayúscula):')
                        return preguntahockey()
                    
                preguntahockey()
                
            hockey()
            
        elif aprender == "D":


                        
            def softbol():
                #hockey preguntas
                print ('Le doy la bienvenida a SOFTBOL, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                time.sleep(2)
                print('(A) Reglas')
                time.sleep(2)
                print('(B) Fundamentos')
                time.sleep(2)
                print('(C) Tácticas')
                time.sleep(2)
                print('(D) ¿Qué es softbol? :v')
                
                def preguntasoftbol():
                    pregunta=input('Escriba una letra: ')
                    if pregunta == "A":
                        reglassoftbol()
                    elif pregunta == "B":
                        fundamentossoftbol()
                    elif pregunta == "C":
                        tacticassoftbol()
                    elif pregunta == "D":
                        que_es_softbol()
                    else:
                        print('Escriba una letra: "A", "B", o "C" (Mayúscula): ')
                        return preguntasoftbol()
                    
                preguntasoftbol()
                
            softbol()
            
        else:
            print('Escríbalo como está en la consola')
            time.sleep(1)
            return deportesdecampo()



    

#Aprende de deportes abiertos de gym
#cátedra 2
def deportesdegimnasio():
        print('')
        print('')
        print('')
        time.sleep(2)
        print('Bienvenido a Deportes de gimnasio')
        time.sleep(2)
        print('¿Sobre qué deporte le gustaría aprender, '+str(tunombre)+'?: ')
        time.sleep(2)
        print('')
        print('(A) Handball')
        time.sleep(2)
        print('(B) voley')
        time.sleep(2)
        print('(C) Básquet')
        print('')
        time.sleep(2)
        aprender = input('Escriba una letra por favor. ')
        time.sleep(2)
        
        if aprender == "A":
        
            def handball():
                #rugby preguntas
                print ('Bienvenido a Handball, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                time.sleep(2)
                print('(A) Reglas')
                time.sleep(2)
                print('(B) Fundamentos')
                time.sleep(2)
                print('(C) Historia del Handball')
                print('')
                pregunta=input('Escriba una letra por favor')
                if pregunta == "A":
                    reglashandball()
                elif pregunta == "B":
                    fundamentoshandball()
                elif pregunta == "C":
                    historia_del_handball()
                else:
                    print('Escriba una letra: "A", "B", o "C", (Mayúscula)')
                    return handball()
            handball()

        elif aprender == "B":
            
            def voley():
                
                #Aprender de voley
                print ('Bienvenido a Voley, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                time.sleep(2)
                print('(A) Reglas')
                time.sleep(2)
                print('(B) Fundamentos')
                time.sleep(2)
                print('(C) Historia del Voley')
                print('')
                pregunta1=input('Escriba una letra por favor')
                if pregunta1 == "A":
                    reglasvoley()
                elif pregunta1 == "B":
                    fundamentosvoley()
                elif pregunta1 == "C":
                    historia_del_voley()
                else:
                    print('Escríbalo como está en la consola')
                    return voley()
                
            voley()

        elif aprender == "C":
            
            def basquet():
                
                #Aprender de basquet
                print('')
                print('')
                print('')
                print ('Bienvenido a Básquet, '+str(tunombre)+'.')
                time.sleep(1)
                print('¿Qué desea aprender?')
                time.sleep(2)
                print('(A) Reglas')
                time.sleep(2)
                print('(B) Fundamentos')
                time.sleep(2)
                print('(C) Historia del Básquet')
                pregunta=input('Escriba una letra: ')
                if pregunta == "A":
                    reglasbasquet()
                elif pregunta == "B":
                    fundamentosbasquet()
                elif pregunta == "C":
                    historia_del_basquet()

                else:
                    print('Escríbalo como está en la consola')
                    return basquet()
           
            basquet()
        else:
            print('Escríbalo como está en la consola')
            time.sleep(1)
            return deportesdegimnasio()



#Aprende de deportes abiertos cerrados
#cátedra 3
        
def deportescerrados():



    
        print('')
        print('')
        print('')
        time.sleep(2)
        print('Bienvenido a Deportes cerrados')
        time.sleep(2)
        print('¿Sobre qué deporte le gustaría aprender, '+str(tunombre)+'?: ')
        time.sleep(2)
        print('(A) Atletismo')
        time.sleep(2)
        print('(B) Natación')
        time.sleep(2)
        print('(C) otros')
        time.sleep(2)
        print('')
        aprender = input('Escriba una letra por favor: ')
        time.sleep(2)
        
        if aprender == "A":
        

            atletismo()

        elif aprender == "B":
            

            natación()

        elif aprender == "C":
            print('hola')
            
           
        else:
            print('Escríbalo como está en la consola')
            time.sleep(1)
            return deportesdegimnasio()




#Pregunta que desencadena todo
def preguntainicial():
    

    print('¿Sobre que cátedra desea aprender, '+str(tunombre)+'?')
    print('')
    time.sleep(2)
    print('(A) Deportes Abiertos de Campo')
    time.sleep(2)
    print('(B) Deportes de Abiertos Gimnasio')
    time.sleep(2)
    print('(C) Deportes Cerrados')
    print('')
    time.sleep(1)
    aprenderasdedeportes = input ('Escriba una letra ')
    if aprenderasdedeportes == "A":
        deportesdecampo()
    elif aprenderasdedeportes == "B":
        deportesdegimnasio()
    elif aprenderasdedeportes == "C":
        deportescerrados()
    else:
        print('Escriba una letra (Mayúscula): "A", "B", o "C". ')
        return preguntainicial()
        




def inicio():
    print('')
    time.sleep(.300)
    print ('+--------------------------------------------------+')
    time.sleep(.300)
    print ('|  #####  #     #  #####    ####    #####   ####   |')
    time.sleep(.300)
    print ('|    #    ##    #    #     #    #     #    #    #  |')
    time.sleep(.300)
    print ('|    #    # #   #    #    #           #    #    #  |')
    time.sleep(.300)
    print ('|    #    #  #  #    #    #           #    #    #  |')
    time.sleep(.300)
    print ('|    #    #   # #    #    #           #    #    #  |')
    time.sleep(.300)
    print ('|    #    #    ##    #     #    #     #    #    #  |')
    time.sleep(.300)
    print ('|  #####  #     #  #####    ####    #####   ####   |')
    time.sleep(.300)
    print ('+--------------------------------------------------+')
    time.sleep(3)
    print('')
    preguntainicial()




    
#para finalizar todo el ciclo         
def final():
    print('')
    print('Bueno, para ir finalizando...')
    time.sleep(1)
    fin = input('Desea volver al inicio? (si/no) ')
    if fin == "si":
        time.sleep(1)
        print('')
        print('A volver se ha dicho')
        print('')
        time.sleep(1)
        return inicio()
    elif fin == "no":
        time.sleep(1)
        print('Ok :)')
        time.sleep(2)
        print('- Espero le haya gustado, '+str(tunombre)+'.')
        time.sleep(2)
        print('- CHAUUU')
        time.sleep(2)
        input('FIN ')
    
        time.sleep(1)
    else:
        print(''+str(tunombre)+', escriba "si" o "no" por favor')
        time.sleep(1)
        return final()


#bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida
    
#EL SALUDO DEL "HOLA" GIGANTE. De acá empieza todo

time.sleep(.300)

tunombre = input('Ingrese su nombre: ')
time.sleep(.300)
tuedad=int(input('Ingrese su edad: '))
print('')
saludo()

#bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida #bienvenida


def inicializar():
    time.sleep(2)
    print('Le doy la bienvenida al aprendedeportes 2.9')
    time.sleep(2)
    print("""Éste es el contenido de la aplicación:""")
    time.sleep(2)
    print("""

DEPORTES DE CAMPO
    - Fútbol
    - Rugby
    - Hockey sobre cesped
""")
    time.sleep(4)
    print("""
DEPORTES DE GIMNASIO
    - Handball
    - Voley
    - Básquet
""")
    time.sleep(4)
    print("""
DEPORTES CERRADOS
    - Atletismo
    - Natación
    - otros...
""")
    time.sleep(4)
    

    inicio()
    

inicializar()
