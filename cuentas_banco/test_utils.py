import pytest
from utils import eliminar_archivo
from utils import crear_archivo
from utils import archivo_existe

def test_eliminar_archivo_0(monkeypatch):
    '''
        Tengo un archivo existente
        Y se va a eliminar
    '''
    crear_archivo("temporal.csv") #Escenario
    assert archivo_existe("temporal.csv") == True #Comprobar escenario
    
    monkeypatch.setattr("builtins.input", lambda _: "S") #Simular el input

    eliminar_archivo("temporal.csv") #Acción a probar
    
    assert archivo_existe("temporal.csv") == False #Comprobación después acción

def test_eliminar_archivo_1(capsys):
    '''
        No tengo ningún archivo
        No elimina nada pero muestra alerta
    '''
    eliminar_archivo("temporal.csv") #Acción a probar
    salida, _ = capsys.readouterr() #Capturamos lo impreso en consola

    assert salida == "¡¡Alerta!! El archivo no existe.\n"

