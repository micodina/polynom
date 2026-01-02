from polynom import Polynome

if __name__ == "__main__":
        
    print("Polynome démo")

    import random

    a = Polynome()  # Polynome vide
    print(f"{a}, de degré {a.deg()}")

    a = Polynome(1)  # 1
    print(f"{a}, de degré {a.deg()}")

    a = Polynome((1, 2, 3))  # 3X^2+2X+1
    print(f"{a}, de degré {a.deg()}")

    a = Polynome(3, deg=2)  # 3X^2
    print(f"{a}, de degré {a.deg()}")

    a = Polynome(values=[-1, -1, 1], deg=2)  # X^2-X-1
    print(f"{a}, de degré {a.deg()}")

    a = Polynome((2, 3))  # Un tuple, passage de values
    b = Polynome(2, 3)  # Un coefficient, un degré.
    print(f"{a}, de degré {a.deg()} est différent de {b}, de degré {b.deg()}")

    # a.enter()
    # print(f"{a}, de degré {a.deg()}")

    # Multiplication par un scalaire
    a = Polynome((1, 2, 3))
    print(f"a : {a}, {a} * 10 : {a*10}")
    print(f"a : {a}, 10 * {a} : {a*10}")

    # Multiplication par un polynome
    b = Polynome((2, 4))
    print(f"a : {a}, b : {b}, {a} * {b}: {a*b}")

    # Addition
    print(f"a : {a}, b : {b}, {a} + {b}: {a+b}")

    # Soustraction
    print(f"a : {a}, b : {b}, {a} - {b}: {a-b}")

    # Addition d'un entier
    s = 1
    print(f"s : {s}, b : {b}, {s} + {b}: {s+b}")

    # Soustraction d'un entier
    s = 1
    print(f"s : {s}, b : {b}, {s} - ({b}): {s-b}")

    # Opposé
    print(f"a : {a}, - ({a}) : {-a}")

    # Itérateur
    for t in a:
        print(t, end=' ')
    print()
 
    # Opérateur d'indexation
    print(a[1])
    print(a[-1])

    # Opérateur égalité
    print(a, b)
    print(a == b)  # False
    b = Polynome(a)
    print(a == b)  # True

    # Division euclidienne
    a = Polynome((1, 2, 3, 4))  # va devenir q
    d = Polynome((1, 1, 1))
    b = Polynome((1, 2))  # va devenir r, il doit être de deg = deg(d)-1

    D = a*d+b
    q, r = D.div(d)
    print("Division (D=qd+r) : {} = ({})({}) + {}".format(D, q, d, r))
    print(a == q, b == r)

    a = Polynome([random.randint(-9, 9) for i in range(8)])
    d = Polynome([random.randint(-9, 9) for i in range(4)])
    b = Polynome([random.randint(-9, 9) for i in range(3)])
    D = a*d+b
    q, r = D.div(d)
    print("Division (D=qd+r) : {} = ({})({}) + {}".format(D, q, d, r))
    print(a == q, b == r)

    # PGCD # BUG !!!!
    # a = Polynome((-1, -1, 1))
    # D = a*Polynome([random.randint(-9, 9) for i in range(10)])
    # d = a*Polynome([random.randint(-9, 9) for i in range(3)])
    D = Polynome((1, -2, 0, 1, 1))
    d = Polynome((1, 1, 0, 1))
    D = Polynome((-1, 2, -1, 1, -2, 1))
    d = Polynome((-2, 2, -1, 1))
    while d.deg() > 0:
        (q, r) = D.div(d)
        print("{} = ({})({}) + {}".format(D, q, d, r))
        D = Polynome(d)
        d = Polynome(r)
