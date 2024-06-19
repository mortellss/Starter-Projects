## FIRST PROJECT



'''
Estructura: pedir input, asegurarse de que el input es lo solicitado, random de las palabras,
comparar resultado con el input, imprimir resultado

Cosas a añadir: que si el input no es correcto vuelva a introducir el input (DONE),
que haya un número de tries, optimiztimizar la comparación de resultados con un 
'''
import random


status = True
TRIES = 3
done = 0

print("Welcome to the Rock, Paper, Scissors game")

while (done < 3):
    
    print("You have " + str(TRIES - done) + " left")
    while (status == True):
        user = str.lower(input("Choose rock , paper, or scissors: "))
    
        if (user == "rock") or (user == "paper") or (user == "scissors"):
            print("Try again")
            status = False
    WORDS = ("rock", "paper", "scissors")
    computer = random.choice(WORDS)
    
    print("You selected: " + user + ". The computer selected: " + computer)
    
    if (user == computer):
        print("Tie!")
    
    if (user == "rock"):
        if (computer == "paper"):
            print("The computer won")
        elif (computer == "scissors"):
            print("You won!")
    elif (user == "paper"):
        if (computer == "scissors"):
            print("The computer won")
        elif (computer == "rock"):
            print("You won!")
    elif (user == "scissors"):
        if (computer == "rock"):
            print("The computer won")
        elif (computer == "paper"):
            print("You won!")
    done += 1
    status = True

print("Thank you for playing!")
