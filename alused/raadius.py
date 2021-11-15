import math
while (True):
    radius = input ('sisesta raadius: ')

    ümbermoot = math.pi * float (radius) * 2
    pindala = math.pi * float (radius) * float (radius)

    print ('pindala on: ', round (pindala),"cm2")

    print ('ümbermööt on: ', round ( ümbermoot ),"cm")

