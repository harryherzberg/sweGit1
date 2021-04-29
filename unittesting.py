
import unittest
#forced = input("   press 1 to add, 2 to subtract, 3 to multiply, 4 to devide:           ")
forced = 5
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
#checks to see if whatever you added, multiplied, or devided = 6 since 6 is a fantastic number
class myTest(unittest.TestCase):
  def test_volume(self):
     self.assertEqual(multiply(),6)
     self.assertEqual(devide(),6)
     self.assertEqual(adder(),6)
     self.assertEqual(subtractor(),6)
a=myTest()
a.test_volume()
