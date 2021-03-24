import math
import random


def f(x, a, b, c):
    return a*(x**2)+b*x+c


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
# matrice cu cromozomi generati
m = [[random.randint(0, 1) for i in range(l)] for j in range(pop_dimension)]
print(m)

# x


g = open("evolutie.txt", "w")
#f.write("id,label\n")
#i = 0
#for img in list:
#    f.write(img+","+str(predictions[i])+"\n")
#    i += 1
g.close()