from visual import*#maybe not needed
G=6.6e-11
def grav(r,m1,m2):
    f=(-G*m1*m2*norm(r)) / (abs(r)**2)
    return f

