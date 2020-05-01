###
# Approximation d'intégrales par la méthode des rectangles
###

## Fonction f continue, positive dont on veut approcher l'aire sur un intervalle donné
def f(x):
    return x**2

## Renvoie un couple de nombre qui permet d'encadrer l'intégrale de f sur [a;b], à l'aide de la méthode des rectangles, avec n itérations.
def methode_rectangle(a,b,n):
    h = ...#à remplir
    x = a
    I = 0#somme des rectangles inférieurs pour une fonction croissante
    S = 0#somme des rectangles supérieurs pour une fonction croissante
    for i in range(n):
        I = #à remplir
        S = #à remplir
        x = #à remplir
    return (I,S)
