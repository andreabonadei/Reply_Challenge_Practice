xfine = yfine=0
S = []  # start
E = []  # end
ostacoli = []
cache = {}  # contiene true se il punto appartiene a un ostacolo
direzioni = ["N","NE","E","SE","S","SO","O","NO"]

def leggiFile(input):
    """ return xinizio, yinizio, xfine, yfine, lista di ostacoli"""
    fin = open(input, "r")
    x_s, y_s, x_e, y_e = fin.readline().split()
    S.append(int(x_s))
    S.append(int(y_s))
    E.append(int(x_e))
    E.append(int(y_e))
    n = int(fin.readline())  # numero ostacoli
    global ostacoli
    for i in range(n):
        elementi = fin.readline().split()
        punto = []
        tmp=[]
        punto.append(int(elementi[0]))
        punto.append(int(elementi[1]))
        tmp.append(punto)
        punto=[]
        punto.append(int(elementi[2]))
        punto.append(int(elementi[3]))
        tmp.append(punto)
        punto=[]
        punto.append(int(elementi[4]))
        punto.append(int(elementi[5]))
        tmp.append(punto)
        ostacoli.append(tmp)


def sign (p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def pointInTriangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) < 0.0
    b2 = sign(pt, v2, v3) < 0.0
    b3 = sign(pt, v3, v1) < 0.0
    return b1 == b2 and b2 == b3

def muoviVersoFine(now):  # prima mi muovo in orizzontale e poi in verticale
    tmp = now
    #scelta=""
    if E[1] > now[1]:
        tmp[1] += 1
    elif E[1] < now[1]:
        tmp[1] -= 1
    if E[0] < now[0]:
        tmp[0] -= 1
    elif E[0] > now[0]:
        tmp[0] += 1
    if not isOstacolo(tmp):
        now[0] = tmp[0]
        now[1] = tmp[1]
        return "Spostato1"
    else:
        return muovi2(now,tmp)


def isOstacolo(p):
    global cache
    if (str(p))in cache:
        return cache[str(p)]
    else:
        isdentro = False
        for o in ostacoli:
            if pointInTriangle(p, o[0], o[1], o[2]):
                isdentro = True
                break
        cache[str(p)] = isdentro
        return isdentro

def muovi2(now, ost):
    tmp = now
    scelta = ""
    if ost[1] > now[1]:
        scelta += "N"
    elif ost[1] < now[1]:
        scelta += "S"
    if ost[0] < now[0]:
        scelta += "O"
    elif E[0] > now[0]:
        scelta += "E"
    indice = direzioni.index(scelta)
    for i in range(1,4): # non torna in indietro
        nuovaScelta = direzioni[indice+i]
        tmp2 = spostaVerso(tmp, nuovaScelta)
        if not isOstacolo(tmp2):
            break
        else:
            nuovaScelta = direzioni[indice-i]
            tmp2 = spostaVerso(tmp, nuovaScelta)
            if not isOstacolo(tmp2):
                break
    if tmp2 == now:
       return "IMPOSSIBLE"
    else:
        return "%d %d" %(tmp2[0],tmp2[1])




def spostaVerso(punto, scelta):
    if "N" in scelta:
        punto[1] += 1
    if "E" in scelta:
        punto[0] += 1
    if "S" in scelta:
        punto[1] -= 1
    if "O" in scelta:
        punto[0] -= 1
    return punto


if __name__ == '__main__':
    q = input("Inserisci numero file:")
    leggiFile("input_%s.txt" % q)
    pt = S
    continua = True
    fout = open("out_%s.txt" % q, "w")
    fout.close()
    lista = []
    lista.append(0)
    fout = open("out_%s.txt" % q, "a")
    while continua:
        s = muoviVersoFine(pt)
        print(s)
        if s == "IMPOSSIBLE":
            print("Impossibile")
            continua=False
        elif s != "Spostato1":
            r = s.split()
            pt[0] = int(r[0])
            pt[1] = int(r[1])
            lista[0] += 1
            lista.append(s)

            print("Passo fatto")
            if pt == E:
                print("Arrivato")
                continua = False
    for riga in lista:
        fout.write(str(riga) + "\n")
    fout.close()