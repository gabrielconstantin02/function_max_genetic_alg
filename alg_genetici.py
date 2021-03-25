import math
import random
from decimal import Decimal


def f(x, a, b, c):
    return a*(x**2)+b*x+c


def build_x(chromosome, length, a, b):
    x = 0
    for i in range(length-1, -1, -1):
        x += ((2**i)*chromosome[length-i-1])
    return float((b-a)*x/((2**length)-1)+a)


inp = open("date.txt", "r")
# dimensiune populatie
pop_dimension = int(inp.readline())
print(pop_dimension)
# domeniu de definitie al functiei
domain = inp.readline().split()
d, e = float(domain[0]), float(domain[1])
print(d, e)
# parametrii functie de grad 2
param = inp.readline().split()
a, b, c = float(param[0]), float(param[1]), float(param[2])
print(a, b, c)
# precizie
precision = int(inp.readline())
print(precision)
# probabilitare recombinare
pr = float(inp.readline())
print(pr)
# probabilitate mutatie
pm = float(inp.readline())
print(pm)
# nr etape
nr_e = int(inp.readline())
print(nr_e)

inp.close()

# lungime cromozom
l = math.ceil(math.log((e-d)*(10**precision), 2))
print(l)

#ca sa obtin acelasi random -- doar pentru testare
random.seed(123)

# matrice cu cromozomi generati
m = [[random.randint(0, 1) for i in range(l)] for j in range(pop_dimension)]
print(m)

# test x and f
temp = [0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1]
x=build_x(temp,l,d,e)
print(build_x(temp,l,d,e))
print(f(x,a,b,c))
# end of test


# Afisare populatie initiala
x = [0.0 for i in range(pop_dimension)]
fn = [0.0 for i in range(pop_dimension)]
g = open("evolutie.txt", "w")
g.write("Populatia initiala\n")
for i in range(pop_dimension):
    g.write(str(i+1)+": ")
    for j in m[i]:
        g.write(str(m[i][j]))
    x[i] = build_x(m[i], l, d, e)
    fn[i] = f(x[i], a, b, c)
    g.write(" x= " + str(x[i]) + " f= " + str(fn[i]) + "\n")


# probabilitati selectie pentru fiecare cromozom
p = [fn[i]/sum(fn) for i in range(pop_dimension)]
# afisare prob selectie
g.write("\nProbabilitati selectie\n")
for i in range(pop_dimension):
    g.write("cromozom " + str(i+1) + " probabilitate " + str(p[i]) + "\n")
# print(p)

# intervale de selectie
q = [0.0 for i in range(pop_dimension)]
q[0] = p[0]
for i in range(1,pop_dimension):
    q[i] = q[i-1]+p[i]

# afisare intervale probabilitati selectie
g.write("\nIntervale probabilitati selectie\n")
for i in range(pop_dimension):
    g.write(str(q[i]) + " ")

# daca probabilitatea de selectie p[i] e 0 atunci si q[i] trebuie sa fie 0
# defapt cred ca nici nu ne trebuie asta ca oricum face >= si < decat acelasi lucru si crapa
# for i in range(pop_dimension):
#    if p[i] == 0:
#        q[i] = 0
# print(q)
g.close()
