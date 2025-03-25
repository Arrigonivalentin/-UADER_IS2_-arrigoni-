#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Definimos el rango de números a verificar (entre 1 y 500 en este caso)
lower = 1
upper = 500

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1): 
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           # Si el número es divisible por cualquier valor de i, no es primo
           if (num % i) == 0:
               break
       else:
           # Si no encontramos divisores, es un número primo y lo imprimimos
           print(num)
