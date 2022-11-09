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

    Secondes = seconde % 60
    minutes = seconde // 60
    minutes += seconde % 60
    heures = seconde // 60
    heures += seconde % 60
    jours = seconde // 24
    return (jours, heures, minutes, Secondes)
    
temps = secondeEnTemps(100000) #temps = secondeEnTemps 
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes") #print (...)
