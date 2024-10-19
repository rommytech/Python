items = [1,2,3,4,5]

for e in items:
    if e < 4:
        continue #< El ciclo salte al sgte
    elif e == 5:
        break #Detiene todas iteraciones
    print(e)


