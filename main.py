import matplotlib as mpl
mpl.use('Agg')#propre à repl.it pour le tracé
import matplotlib.pyplot as plt
from math import exp
# Méthode d'Euler pour approcher la fonction
# solution de y'=y, f(0)=1 (à adapter pour d'autres)
# Paramètres de la méthode
# Intervalle d'étude de la simulation: [a;b]
a=0
b=1
# Découpage de l'intervalle [a;b]
N = 5
# Pas de la méthode
h = ...#à remplir

# expression de la fonction solution exacte
def f(x):
    return exp(x)

# conditions initiales
x = a
y = f(a)
# On mémorise les résultats dans des listes
X = [x]#abscisses
Y = [y]#images approximées
# Liste des vraies images (pour comparaison)
F = [f(x)]

# Itérations de la méthode
for k in range(N):
    x = ... #à remplir
    # itération d'Euler
    y = ... #à remplir
    # ajout des résultats dans les listes
    # abscisses
    X.append(x)
    # ordonnés valeurs approximées
    Y.append(y)
    # ordonnés valeurs exactes
    F.append(f(x)) 
# tracé de la solution approchée
plt.plot(X, Y, "r-") 
# tracé de la solution exacte
plt.plot(X, F, "b-") 
# mise en forme du graphique
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
# sauvegarde l'image
plt.savefig('graph.png')