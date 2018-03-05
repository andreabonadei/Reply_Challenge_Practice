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

    return x_s, y_s, x_e, y_e, ostacoli

def sign (p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def pointInTriangle ( pt, v1, v2, v3):

    b1=False
    b2=False
    b3=False

    b1 = sign(pt, v1, v2) < 0.0
    b2 = sign(pt, v2, v3) < 0.0
    b3 = sign(pt, v3, v1) < 0.0

    return ((b1 == b2) and (b2 == b3))


if __name__ == '__main__':
    x1, y1,x2,y2, ostacoli = leggiFile("input_1.txt")

