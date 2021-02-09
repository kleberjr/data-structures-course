#############################################################################
# ------------------------------ Functions -------------------------------- #
#############################################################################
#
#
def gcd(m, n):              # Greather common divisor
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n
#
#
#
#############################################################################
# -------------------------------- Classes -------------------------------- #
#############################################################################
#
class Fraction():
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(f'{self.num}/{self.den}')

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
        # Ao definirmos um método __str__, possibilitamos que o número seja printa-
        # do no console; seja representável visualmente.

    def __add__(self,other):        
        
        new_den = (self.den * other.den)
        new_num = (self.num * other.den) + (self.den * other.num)
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)  
        # Ao definirmos um método __add__, o programa possibilita o uso do operador de adição
        # para chamar esse método.

    def __sub__(self, other):
        
        new_den = (self.den * other.den)
        new_num = (self.num * other.den) - (self.den * other.num)
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)  
        # Ao definirmos um método __sub__, o programa possibilita o uso do operador de subtração
        # para chamar esse método.
    
    def __mul__(self, other):
        new_num = (self.num * other.num)
        new_den = (self.den * other.den)
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)
        # Ao definirmos um método __mul__, o programa possibilita o uso do operador de multi-
        # plicação para chamar esse método.

    def __truediv__(self, other):
        new_num = (self.num * other.den)
        new_den = (self.den * other.num)
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)
        # Ao definirmos um método __truediv__, o programa possibilita o uso do operador de 
        # divisão para chamar esse método.

    def __eq__(self, other):
        return (self.num * other.den) == (self.den * other.num)
    # Possibilita o uso dos operador relacional booleano '==' para atestar se 2 objetos
    # diferentes possuem uma Deep Equality (Igualdade por Valor) e não uma Shallow Equality
    #(Igualdade por Referência).

    def __gt__(self, other):
        return True if ((self.num / self.den) > (other.num / other.den)) else False
    # Possibilita o uso dos operador relacional booleano '>' para atestar se 2 objetos
    # possuem valores maiores que o outro.

    def __lt__(self, other):
        return True if ((self.num / self.den) < (other.num / other.den)) else False    
    # Possibilita o uso dos operador relacional booleano '<' para atestar se 2 objetos
    # possuem valores menores que o outro.
#
#
#
##########################################################################################
# -------------------------------- Main Function --------------------------------------- #
##########################################################################################
#
a, b = [int(x) for x in input('Insert here the first fraction (a/b): ').split("/")]
f1 = Fraction(a, b)
a, b = [int(x) for x in input('Insert here the second fraction (a/b): ').split("/")]
f2 = Fraction(a, b)

print("\n----------- Fraction Class Demonstration -----------")
print(f"First fraction: {f1}")
print(f"Second fraction: {f2}")
print("------------------- Operations ---------------------")
print(f'Sum: {f1 + f2}')
print(f'Sub: {f1 - f2}')
print(f'Mul: {f1 * f2}')
print(f'Div: {f1 / f2}')
print("Are the object's value equal?", f1 == f2)
print("Are f1 greater than f2?", f1 > f2)
print("Are f1 less than f2?", f1 < f2, "\n")


