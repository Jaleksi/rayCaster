from math import sqrt

def counterClockWise(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersects(a, b, c, d):
    # Matematiikkakaava jolla lasketaan halkaisevatko kaksi janaa toisensa
    # True / False
    return counterClockWise(a, c, d) != counterClockWise(b, c, d) and\
    counterClockWise(a, b, c) != counterClockWise(a, b, d)




def intersectPoint(rayStart, rayEnd, esteStart, esteEnd):
    # Palauttaa halkaisupisteen koordinaatit [x, y]
    rsx, rsy = rayStart[0], rayStart[1]
    rex, rey = rayEnd[0], rayEnd[1]
    esx, esy = esteStart[0], esteStart[1]
    eex, eey = esteEnd[0], esteEnd[1]

    px1 = (rsx*rey-rsy*rex)*(esx-eex)-(rsx-rex)*(esx*eey-esy*eex)
    px2 = (rsx-rex)*(esy-eey)-(rsy-rey)*(esx-eex)

    py1 = (rsx*rey-rsy*rex)*(esy-eey)-(rsy-rey)*(esx*eey-esy*eex)
    py2 = (rsx-rex)*(esy-eey)-(rsy-rey)*(esx-eex)

    try:
        return [int(px1/px2), int(py1/py2)]
    except ZeroDivisionError:
        return 0

def pointDistance(p1, p2):
    # Etäisyys kahden pisteen välillä
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


if __name__ == "__main__":
    exit()
