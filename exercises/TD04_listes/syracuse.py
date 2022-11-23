def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_nombre = [n]
    while n > 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        liste_nombre.append(n)
    return liste_nombre


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for n in range(1, n_max+1):
        syracuse(n)

    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1


print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = []
    for n in range(1, n_max+1):
        liste.append(tempsVol(n))
# ou : liste = [tempsVol(n) for in range (1,n_max+1)]
    return liste


print(tempsVolListe(100))


print(syracuse(27))

# déterminer quel entier entre 1 et 10 000 à le plus grand temps de vol

listeTV = tempsVolListe(10000)
print(max(listeTV))
print(listeTV.index(261)+1)

# ou :

im = 0
m = 0
for i in range(10000):
    e = listeTV[i]
    if e > m:
        m = e
        im = i
print(m, im)

# déterminer quel entier entre 1 et 10 000 à la plus grande altitude totale


def altitudeMaxListe(n_max):
    """listes des altitudes maximales des nombres de 1 à n_max"""
    liste = []
    for n in range(1, n_max+1):
        liste.append(max(syracuse(n)))
    return liste


listeAM = altitudeMaxListe(10000)
print(max(listeAM))
print(listeAM.index(27114424)+1)
