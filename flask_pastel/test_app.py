import pytest
from models.pedido import Pedido


def test_validar_fecha_01():
    '''
        Si la fecha es pasada, debe retornar
        un array con errores.
    '''
    mi_pedido = Pedido("leo rojas", "Producto x", "2021-02-02", "Descripcion")
    
    resultado = mi_pedido.is_valid()
    assert len(resultado) == 1
    assert resultado[0] == "Ingrese una fecha correcta"
    
def test_validar_fecha_02():
    '''
        Si la fecha es futura, debe retornar
        un array vacío.
    '''
    mi_pedido = Pedido("Carol Rojas", "Producto y", "2025-12-12", "Descrip")
    resultado = mi_pedido.is_valid()
    assert len(resultado) == 0
    
