class Polynome:
    pass


class Polynome(list):
    "Classe Polynome par héritage de list"
    def __init__(self, values: int | float | tuple | list = None, deg: int = None) -> None:

        if deg == None:
            if values == None:
                list.__init__(self)
            else:
                if isinstance(values, (int, float)):  # Si une valeur unique est fournie
                    super().__init__((values,))  # retourne values X^0
                elif isinstance(values, (list, tuple)):  # Si une séquence est fournie
                    super().__init__(values)
                else:
                    pass
        else:
            if isinstance(values, (int, float)):  # Si une valeur unique est fournie
                super().__init__([0]*deg)
                self.append(values)  # retourne values X^deg
            elif isinstance(values, (list, tuple)):  # Si une séquence est fournie
                super().__init__(values)
            else:
                pass

        if self:
            while (self[-1] == 0) and (len(self) > 1):
                self.pop()  # Retire les coefficients nuls des degrés supérieurs

    def deg(self) -> int:
        "Degré du polynome"
        if self:
            return (len(self)-1)
        else:
            return (0)

    def __str__(self) -> str:
        " Opérateur string "
        def ex(n: int) -> str:
            " Affiche des exposants"
            t = {"0": 0x2070, "1": 0x00B9, "2": 0x00B2, "3": 0x00B3, "4": 0x2074,
                 "5": 0x2075, "6": 0x2076, "7": 0x2077, "8": 0x2078, "9": 0x2079}
            ret = ""
            for i in str(n):
                ret = ret+chr(t[i])
            return (ret)

        def monome_to_string(i: int):
            "Affiche un monome"
            c = self[i]
            if c == 0:  # Si le coef est nul,
                if i == 0:  # Affichage si le deg est 0
                    return ("0")
                else:  # pas d'affichage sinon
                    return ("")
            elif (i == 0):  # Si le degré est nul, c'est une constante
                return ("{:+}".format(c))
            elif (i == 1):  # Si le degré est 1, on n'affiche pas la puissance de x
                if (c == 1):
                    return ("+x")
                elif (c == -1):
                    return ("-x")
                else:
                    return ("{:+}x".format(c))
            elif (c == 1):  # Si le coefficient est 1, on affiche que la puissance de x
                return ("+x{}".format(ex(i)))
            elif (c == -1):
                return ("-x{}".format(ex(i)))
            else:  # Cas général
                return ("{:+}x{}".format(c, ex(i)))

        if not self:
            return ""

        ret = ""
        for i in range(self.deg()+1):
            ret = monome_to_string(i)+ret
        if ret[0] == "+":
            ret = ret[1:]  # Si le premier caractère est un +, on l'efface
        if len(ret) > 1 and ret[-1] == "0":
            # Si le dernier caractère est un 0 et que le polynome est de deg >0, on l'efface
            ret = ret[:-1]
        return (ret)

    def __add__(self, other: Polynome) -> Polynome:
        " Opérateur addition "
        if not self:
            return (other)
        if not other:
            return (self)

        ret = Polynome()
        M = max(self.deg(), other.deg())
        m = min(self.deg(), other.deg())
        for i in range(M+1):
            if (i <= m):
                ret.append(self[i]+other[i])
            elif other.deg() >= self.deg():
                ret.append(other[i])
            else:
                ret.append(self[i])

        while (ret[-1] == 0) and (len(ret) > 1):
            ret.pop()  # Retire les coefficients nuls des degrés supérieurs
        return (ret)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Polynome(other) + self

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Polynome(other) - self

    def __mul__(self, other: int | float | Polynome) -> Polynome:
        """ 
        Opérateur multiplication.
        Accepte les entiers/float et d'autres Polynome 
        """
        # ret = Polynome()
        if isinstance(other, (int, float)):
            ret = Polynome([x*other for x in self])
            return (ret)
        elif isinstance(other, Polynome):
            list_to_ret = [0]*(self.deg()+other.deg()+1)
            for i in range(self.deg()+1):
                for j in range(other.deg()+1):
                    list_to_ret[i+j] += self[i]*other[j]
            return (Polynome(list_to_ret))
        else:
            raise AttributeError(
                'muliply by ' + type(other) + ' is not supported')

    def __rmul__(self, other):
        # Cela permet la multiplication  à gauche
        if isinstance(other, (int, float)):
            return self * other

    def __sub__(self, other: Polynome) -> Polynome:
        " Opérateur soustraction "
        return (self+other*(-1))

    def __neg__(self) -> Polynome:
        " Opérateur opposé "
        return (self*(-1))

    def enter(self):
        "Entre un polynome"
        d = int(input("deg: "))
        self = Polynome()
        for i in range(d+1):
            a = input("x^"+str(i)+": ")
            self.append(float(a))
        while (self[-1] == 0) and (len(self) > 1):
            self.pop()  # Retire les coefficients nuls des degrés supérieurs

    def div(self, d: Polynome) -> tuple:
        """ 
        Division Euclidienne.
        S'arrête quand le deg(r) = deg(d)-1
        """
        if self.deg() <= d.deg():
            raise ValueError
        D = Polynome(self)
        r = Polynome(D)
        q = Polynome()
        i = self.deg()-d.deg()
        while D.deg() >= d.deg():
            #print(f"deg(D)={D.deg()}, deg(d)={d.deg()}, i={i},")
            if D.deg() < i + d.deg():
                i -= 1
                continue
            s = -D[-1] / d[-1]
            if s-int(s) == 0.0:
                s = int(s)
            m = Polynome(1, deg=i)*s
            q = q-m
            r = d*m+D
            # print(f"({D}) = ({d}) ({-m}) + ({r})")
            # print(f"deg(D)={D.deg()}, deg(d)={d.deg()}, deg(q)={q.deg()}, deg(r)={r.deg()}, i={i},")
            D = Polynome(r)
            i -= 1
        return (q, r)

    def __floordiv__(self, d: Polynome) -> Polynome:
        " Opérateur Division entière "
        return (self.div(d)[0])

    def __mod__(self, d: Polynome) -> Polynome:
        " Opérateur modulo ou reste"
        return (self.div(d)[1])
