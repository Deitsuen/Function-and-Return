def add(a, b):
    print"ADDITIONE %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SOUSTRAIRE %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print"MULTIPLIER %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVISE %d / %d" % (a, b)
    return a / b


print "on va faire du calcul avec les fonctions"

age = add(10, 7)#Alors ici sa va juste afficher les addition et soustraction etc
taille = subtract (354, 177)# avec les chiffre qu'on a mis entre paranthese
poids = multiply (40, 2)#sa va pas nous afficher directement les reponse
pointure = divide(84, 2)

print "Age: %d, Taille: %d, Poids %d, Pointure %d" %(age, taille, poids, pointure)
#Mais par exemple dans la phrase ci dessus mettre les variable de script ci dessus dans la
#phrase va afficher les resultat directement plutot que les  addition et soustraction etc
# a faire
print "Un puzzle ??"

what = add(age, subtract(taille, multiply(poids, divide(pointure, 2))))
print "normalement le resultat est",what, "appart si vous avez modifier ;)"

#SOLUCE deja sa va afficher la variable a l'enver sa va commence par le divide

#pour finir par le add important pour la suite, alors on prend le resultat de la

#division donc ici 21 et on va le multiplier le 21 et le resultat de la multiplication

#va etre soustrait et ensuite ce resultat va etre additione et on obtient le resultat

#de cette variable biensur le tous reprend ce que vous avec marque sur les variable

# age,taille,poids,pointure sa peut radicalement changer selon ce que vous mettez

