forced = input("   press 1 to add, 2 to subtract, 3 to multiply, 4 to devide:           ")

def adder():
  num1 = input("number 1? ")
  num2 = input("number 2? ")
  numero = int(num1)+int(num2)
  num = str(numero)
  print(num1+ " + " + num2 + " = " + num)
def subtractor():
  num1 = input("number 1? ")
  num2 = input("number 2? ")
  numero = int(num1)-int(num2)
  num = str(numero)
  print(num1+ " - " + num2 + " = " + num)
def multiply():
  num1 = input("number 1? ")
  num2 = input("number 2? ")
  numero = int(num1)*int(num2)
  num = str(numero)
  print(num1+ " * " + num2 + " = " + num)
def devide():
  num1 = input("number 1? ")
  num2 = input("number 2? ")
  numero = int(num1)/int(num2)
  num = str(numero)
  print(num1+ " / " + num2 + " = " + num)
forced = int(forced)
if forced == 1:
  adder()
if forced ==2:
  subtractor()
if forced == 3:
  multiply()
if forced == 4:
  devide()
