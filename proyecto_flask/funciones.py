def navegador(): #Retorna None
    print("Navegador")
 
def caracteristica(valor):
    print(valor)
 
def traer_navegador(tipo):
    if tipo == 1:
        return "Firefox"
    elif tipo == 2:
        return "Chrome"
    elif tipo == 3:
        return "Safari"
    else:
        return "Navegador x"  
 
navegador()
caracteristica("Bueno")
caracteristica("Bonito")
caracteristica("Barato")

traer_navegador(3)
navegador()
caracteristica("pesado")

for item in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
    navegador()
for item in [0,1,2]:
    print(traer_navegador(1))
for item in [0,1]:
    print(traer_navegador(3))



