import random
import re
from urllib2 import urlopen

#variables
url_serebii = "http://www.serebii.net/pokedex-sm/"


print "Generando party aleatorea"
for i in range (0,6): #loop de 6 pasos para generar 6 Pokemon
    pkmn_num = random.randint(1,802) # Se genera un numero aleatoreo entre 1 y 802
    if pkmn_num <= 99:# si el numero aleatoreo es igual o menor a 99 se debe de agregar un 0 al incio del numero para que no haya error al momento de cargar la pagina
        new_pkmn_num = "0" + str(pkmn_num)
        urlpokemon = url_serebii + new_pkmn_num + ".shtml"
    else:
        urlpokemon = url_serebii + str(pkmn_num) +".shtml"

    pkmnpage = urlopen(urlpokemon) #Se abre la pagina web de serebii
    pkmn_html_code = pkmnpage.readlines() #Se leen las lineas de codigo de la pagina

    for line in range (0,10):#Se leen solo las primeras 10 lines de codigo porque el nombre del pokemon lo sacamos en la parte de la etiqueta <title> y esa etiqueta siempre es una de las primeras
        if re.match("<title>", pkmn_html_code[line]): #si se encuentra la linea que tiene <title>
            nombre_pkmn = re.match("<title>(\w+\S?\s?\w+)\s", pkmn_html_code[line])
    print "Pokemon No. %d: %d, %s." % (i + 1, pkmn_num, nombre_pkmn.group(1))
