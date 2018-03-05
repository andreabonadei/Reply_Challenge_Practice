
def rettangolizza(ostacolo):
    minx = min(ostacolo[::2])
    maxx = max(ostacolo[::2])
    miny = min(ostacolo[1::2])
    maxy = max(ostacolo[1::2])
    return (maxx,maxy,minx,miny)


def leggiFile(input):
    """ return xinizio, yinizio, xfine, yfine, lista di ostacoli"""
    fin = open(input, "r")
    x_s, y_s, x_e, y_e = fin.readline().split()
    n = int(fin.readline())  # numero ostacoli
    ostacoli = []
    min = 2000000
    max = -200000
    for i in range(n):
        coord = []
        elementi = fin.readline().split()
        for j in range(len(elementi)):
            if min>int(elementi[j]):
                min = int(elementi[j])
            if max<int(elementi[j]):
                max = int(elementi[j])
            coord.append(int(elementi[j]))
        ostacoli.append(coord)
    griglia = []
    riga = []
    for j in range(max - min):
        riga.append(0)
    for i in range(max-min):
        griglia.append(riga)
    for i in range(len(ostacoli)):
        maxx,maxy,minx,miny = rettangolizza(ostacoli[i])
        for j in range(minx,maxx):
            for k in range(miny,maxy):
                griglia[k][j] = 1
    print(griglia)
    return x_s, y_s, x_e, y_e, ostacoli

if __name__ == '__main__':
    x1, y1,x2,y2, ostacoli = leggiFile("input_1.txt")
    rettangolizza(ostacoli[0])
