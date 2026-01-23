def printfl(fl, stl=0):
    try:
        f = open(fl, 'r')
    except:
        return False
    else:
        print(f.read())
        f.close()

def appendfl(fl,nome='None',idade=0):
    try:
        f = open(fl, 'a')
        f.write(f'{nome:<20}{idade:>5}\n')
        f.close()
    except:
        return False
    else:
        return True
