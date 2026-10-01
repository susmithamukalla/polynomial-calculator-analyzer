#Polynomial Calculator Using linked Lists
class Node:
    def __init__(self,coefficient,exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    #insert a term
    def insert(self,coefficient,exponent):
        if coefficient == 0:
            return

        new_node = Node(coefficient,exponent)

        #insert at beginning
        if self.head is None or exponent>self.head.exponent:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        previous = None

        while current and current.exponent>exponent:
            previous = current
            current = current.next

        #if exponent already exists
        if current and current.exponent ==exponent:
            current.coefficient += coefficient         

            if current.coefficient == 0:
                if previous:
                    previous.next = current.next
                else:
                   self.head = current.next

        else:
           new_node.next = current
           previous.next = new_node

    #Display polynomial
    def display(self):
        if self.head is None:
            return "0" 

        terms = []                      
        current = self.head

        while current:
            c = current.coefficient
            e = current.exponent

            if e == 0:
                term = str(abs(c))
            elif e == 1:
                term = (""if abs(c) == 1 else str(abs(c))) +"X"
            else:
                term = (""if abs(c) == 1 else str(abs(c))) + f"X^{e}"    

            if not terms:
                terms.append(("-"if c<0 else"")+ term)
            else:
                terms.append(("-"if c<0 else"+")+ term)
            current = current.next
        return"".join(terms)

    # Add two polynomials
    def add(self,other):
        result = Polynomial()

        p = self.head
        q = other.head

        while p:
            result.insert(p.coefficient,p.exponent)
            p = p.next

        while q:
            result.insert(q.coefficient,q.exponent)
            q = q.next

        return result

    #subtract two polynomials
    def subtract(self,other):
        result = Polynomial()

        p = self.head
        q = other.head

        while p:
            result.insert(p.coefficient,p.exponent)
            p = p.next

        while q:
            result.insert(-q.coefficient,q.exponent)
            q = q.next
        return result

    #multiply two polynomials
    def multiply(self,other):
        result = Polynomial()

        p = self.head

        while p:
            q = other.head
            while q:
                coefficient = p.coefficient*q.coefficient
                exponent = p.exponent+q.exponent

                result.insert(coefficient,exponent)

                q = q.next

            p = p.next

        return result

    #Evaluate polynomial
    def evaluate(self,X):
        result = 0
        current = self.head

        while current:
            result += current.coefficient*(X** current.exponent)
            current = current.next
        return result
#Foundation to create polynomial
def create_polynomial():
    polynomial = Polynomial()

    n = int(input("Enter number of terms:"))

    for i in range(n):
        coefficient = int(input(f"Enter coefficient for term {i+1}:"))
        exponent = int(input(f"Enter exponent for term {i+1}:"))

        polynomial.insert(coefficient,exponent)

    return polynomial

#main program
print("===== POLYNOMIAL CALCULATOR =====")

print("\nEnter Polynomial 1")
p1 = create_polynomial()

print("\nEnter Polynomial 2")
p2 = create_polynomial()

print("\n Polynomial 1:",p1.display())
print("Polynomial 2:",p2.display())

while True:
    print("\n===== MENU =====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Evaluate Polynomial 1")
    print("5.Evaluate Polynomial 2")
    print("6.Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        result = p1.add(p2) 
        print("Result:",result.display())

    elif choice == 2:
        result = p1.subtract(p2)
        print("Result:",result.display())

    elif choice == 3:
        result = p1.multiply(p2)
        print("Result:",result.display())

    elif choice == 4:
        X = int(input("Enter value of X:"))
        print("Value = ",p1.evaluate(X))

    elif choice == 5:
        X = int(input("Enter value of X:"))
        print("Value = ",p2.evaluate(X))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("invalid choice!")
