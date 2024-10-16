import sympy as sp


def complex_mult(a, b):
    """
    Multiply two complex numbers a, b modulo p, where a = (x1, y1) and b = (x2, y2).
    
    Returns (x, y) such that x ≡ x1*x2 - y1*y2 (mod p) and y ≡ x1*y2 + x2*y1 (mod p).
    """
    (x1, y1) = a
    (x2, y2) = b
    x = (x1 * x2 - y1 * y2) % p
    y = (x1 * y2 + x2 * y1) % p
    return (x, y)

def Circle(p):
    points = [(0,1),(0,p-1),(1,0),(p-1,0)]
    if p<=5:
        return points,(0,1) #points, generator
    points = set(points)
    for x in range(2,p): #for p>=7 any generator must have order at least 6, so cannot belonge to the previous set (which forms a cyclic subgroup of order 4 generate by (0,1)
        


