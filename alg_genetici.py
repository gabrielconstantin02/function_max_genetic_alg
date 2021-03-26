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


def display_pop(pd, m_tmp, x_tmp, fn_tmp):
    for i in range(pd):
        g.write(str(i + 1) + ": ")
        for j in m_tmp[i]:
            g.write(str(j))
        x_tmp[i] = build_x(m_tmp[i], l, d, e)
        fn_tmp[i] = f(x_tmp[i], a, b, c)
        g.write(" x= " + str(x_tmp[i]) + " f= " + str(fn_tmp[i]) + "\n")


def binary_search(interval, low, high, x):
    mid = (high + low) // 2

    # daca x-ul se afla in interval, iar acel interval nu e primul (ca sa nu iasa mid-1 = -1)
    if mid > 0 and interval[mid - 1] <= x < interval[mid]:
        return mid

    # daca x-ul se afla in primul interval
    if mid == 0 and x < interval[mid]:
        return mid
    
    if interval[mid] > x:
        return binary_search(interval, low, mid - 1, x)
    else:
        return binary_search(interval, mid + 1, high, x)


def crossover(chr, ind):
    i = 0
    # facem perechi pana ne raman 2 sau 3 cromozomi
    while i + 3 < len(chr):
        break_point = random.randint(0, l - 1)
        g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + ":\n")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))
        g.write(" punct " + str(break_point) + "\n")
        # print(chr[i], chr[i+1])
        tmp = chr[i][:break_point]
        chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
        chr[i+1] = tmp + chr[i+1][break_point:]
        g.write("Rezultat     ")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))
        # print(chr[i], chr[i+1])
        i += 2
    #print("\n")
    break_point = random.randint(0, l - 1)
    if i + 3 == len(chr):
        # print(chr[i], chr[i+1], chr[i+2])
        g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + " si cromozomul " + str(ind[i+2]+1) + ":\n")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+2]:
            g.write(str(j))
        g.write(" punct " + str(break_point) + "\n")
        tmp = chr[i][:break_point]
        chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
        chr[i+1] = chr[i+2][:break_point] + chr[i+1][break_point:]
        chr[i+2] = tmp + chr[i+2][break_point:]
        # print(chr[i], chr[i+1], chr[i+2])
        g.write("Rezultat     ")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+2]:
            g.write(str(j))
    else:
        # print(chr[i], chr[i+1])
        g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + ":\n")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))
        g.write(" punct " + str(break_point) + "\n")
        tmp = chr[i][:break_point]
        chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
        chr[i+1] = tmp + chr[i+1][break_point:]
        # print(chr[i], chr[i+1])
        g.write("Rezultat     ")
        for j in chr[i]:
            g.write(str(j))
        g.write(" ")
        for j in chr[i+1]:
            g.write(str(j))


inp = open("date.txt", "r")
# dimensiune populatie
pop_dimension = int(inp.readline())
# print(pop_dimension)
# domeniu de definitie al functiei
domain = inp.readline().split()
d, e = float(domain[0]), float(domain[1])
# print(d, e)
# parametrii functie de grad 2
param = inp.readline().split()
a, b, c = float(param[0]), float(param[1]), float(param[2])
# print(a, b, c)
# precizie
precision = int(inp.readline())
# print(precision)
# probabilitare recombinare
pr = float(inp.readline())
# print(pr)
# probabilitate mutatie
pm = float(inp.readline())
# print(pm)
# nr etape
nr_e = int(inp.readline())
# print(nr_e)

inp.close()

# lungime cromozom
l = math.ceil(math.log((e-d)*(10**precision), 2))
# print(l)

#ca sa obtin acelasi random -- doar pentru testare
random.seed(123)

# matrice cu cromozomi generati
m = [[random.randint(0, 1) for i in range(l)] for j in range(pop_dimension)]
# for i in range(pop_dimension):
#     print(m[i])

# test x and f
# temp = [0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1]
# x=build_x(temp,l,d,e)
# print(build_x(temp,l,d,e))
# print(f(x,a,b,c))
# end of test


# Afisare populatie initiala
x = [0.0 for i in range(pop_dimension)]
fn = [0.0 for i in range(pop_dimension)]
g = open("evolutie.txt", "w")
g.write("Populatia initiala\n")
display_pop(pop_dimension, m, x, fn)
# for i in range(pop_dimension):
#     g.write(str(i+1)+": ")
#     for j in m[i]:
#         g.write(str(j))
#     x[i] = build_x(m[i], l, d, e)
#     fn[i] = f(x[i], a, b, c)
#     g.write(" x= " + str(x[i]) + " f= " + str(fn[i]) + "\n")


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
for i in range(1, pop_dimension):
    q[i] = q[i-1]+p[i]

# afisare intervale probabilitati selectie
g.write("\nIntervale probabilitati selectie\n")
for i in range(pop_dimension):
    g.write(str(q[i]) + " ")

# generare unui numar aleator u si determinarea intervalului caruia apartine
# TODO: nu uita sa implementezi selectia elitista (alegi doar pop_dimension-1 aici)
m_prim = []  # populatia p'
for i in range(pop_dimension):
    u = random.uniform(0, 1)
    poz = binary_search(q, 0, pop_dimension-1, u)
    g.write("\nu=" + str(u) + " selectam cromozomul " + str(poz+1))
    m_prim.append(m[poz])

# dupa selectie avem:
g.write("\nDupa selectie:\n")
x_prim = [0.0 for i in range(pop_dimension)]
fn_prim = [0.0 for i in range(pop_dimension)]
display_pop(pop_dimension, m_prim, x_prim, fn_prim)

# participanti incrucisare
g.write("\nProbabilitate de incrucisare " + str(pr) + "\n")
mix = [] # lista de cromozomi care intra la incrucisare
c_nr = [] # indicele "original" al cromozomilor
for i in range(pop_dimension):
    g.write(str(i + 1) + ": ")
    for j in m_prim[i]:
        g.write(str(j))
    u = random.uniform(0, 1)
    if u < pr:
        c_nr.append(i)
        mix.append(m_prim[i])
    g.write(" u=" + str(u) + (("<" + str(pr) + " participa") if u < pr else "") + "\n")

# incrucisare
crossover(mix, c_nr)

# dupa incrucisare
g.write("\n\nDupa recombinare:\n")
j = 0
for i in c_nr:
    m_prim[i] = mix[j]
    j += 1
display_pop(pop_dimension, m_prim, x_prim, fn_prim)




# daca probabilitatea de selectie p[i] e 0 atunci si q[i] trebuie sa fie 0
# defapt cred ca nici nu ne trebuie asta ca oricum face >= si < decat acelasi lucru si crapa
# for i in range(pop_dimension):
#    if p[i] == 0:
#        q[i] = 0
# print(q)
g.close()
