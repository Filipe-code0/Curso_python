def printfl(fl):
    try:
        f = open(fl, 'r')
        print(f.read())
        f.close()
    except:
        return False
    else:
        return True

def appendfl(fl,nome='None',idade=0,criterio=''):
    try:
        f = open(fl, 'a')
        f.write(f'{' '}{nome:<20}{idade:>5} {criterio}\n')
        f.close()
    except:
        return False
    else:
        return True
