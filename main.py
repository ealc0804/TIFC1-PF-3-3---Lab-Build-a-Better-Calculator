# Suma todos los números de la lista
def addmultiplenumbers(numbers):
    return sum(numbers)

# Multiplica cada número con el que sigue.
def multiplymultiplenumbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result *= numbers[i]
    return result

# Dice si un número es par.
def isiteven(num):
    return isinstance(num, int) and num % 2 == 0

# Dice si un número es un entero.
def isitaninteger(num):
    return isinstance(num, int)

def main():
  print("Hello learners!")

  print(addmultiplenumbers([1, 2, 3]))
  print(multiplymultiplenumbers([2, 3, 4]))
  print(isiteven(8))
  print(isitaninteger(5))

if __name__=="__main__":
  main()