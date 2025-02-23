def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""

    secondes = temps[3]
    secondes += temps[2]*60
    secondes += temps[1]*60*60
    secondes += temps[0]*24*60*60 
    return secondes

temps = (3,23,1,34)
print(type(temps)) 
print(tempsEnSeconde(temps)) 

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

    jours = seconde // (24*60*60)
    heures = seconde // (60*60)
    heures = heures % 24
    minutes = seconde // 60
    minutes = minutes % 60
    Secondes = seconde % 60
    return (jours, heures, minutes, Secondes)
    
temps = secondeEnTemps(100000) #temps = secondeEnTemps 
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes") #print (...)


def affichePluriel(nombre,mot):
    """ affiche le nombre puis le mot en mettant éventuellement le mot au pluriel, n'affiche rien si nombre = 0 """

    if nombre > 1:
        print (nombre, mot+"s",end=' ')
    elif nombre == 1:
        print (nombre,mot,end=' ')
    
    

affichePluriel (2, 'banane')
affichePluriel (1,'pomme')
affichePluriel (0,'poire')
print('')

def afficheTemps(temps):
    """ affichage du temps """
    affichePluriel (temps[0],'jour')
    affichePluriel (temps[1],'heure')
    affichePluriel (temps[2],'minute')
    affichePluriel (temps[3],'seconde')

afficheTemps((2,1,0,8))

print('')

def sommeTemps(temps1,temps2):
    """permet d'additionner des temps"""
    seconde1 = tempsEnSeconde(temps1)
    seconde2 = tempsEnSeconde(temps2)
    secondes = seconde1 + seconde2
    return secondeEnTemps(secondes)

sommeTemps((0,21,27,30),(0,3,59,45))
print(sommeTemps((0,21,27,30),(0,3,59,45)))