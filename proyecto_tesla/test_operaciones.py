from supervisor import Supervisor
from empleado import Empleado
from tecnico import Tecnico
from operaciones import traer_n_empleados, \
    traer_software_con_parametros, \
    traer_mantenimiento_con_tecnico, \
    traer_supervisor, traer_dos_empleados, \
    traer_mantenimiento_con_vehiculo, \
    traer_mantenimiento_con_vehiculo_tecnico, \
    traer_tecnico_supervisor_empleado

def test_traer_supervisor():
    sup = traer_supervisor()
    assert isinstance(sup, Supervisor)

def test_traer_dos_empleados():
    empls = traer_dos_empleados()
    assert len(empls) == 2

def test_traer_tecnico_supervisor_empleado():
    rows = traer_tecnico_supervisor_empleado()
    assert len(rows) == 3
    assert isinstance(rows[0], Tecnico)
    assert isinstance(rows[1], Supervisor)
    assert isinstance(rows[2], Empleado)

def test_traer_n_empleados():
    assert len(traer_n_empleados(5)) == 5

def test_traer_software_con_parametros():
    soft = traer_software_con_parametros("v.10.0")
    assert soft.version == "v.10.0"

def test_traer_mantenimiento_con_tecnico():
    mant = traer_mantenimiento_con_tecnico("Juan Carlos")
    assert mant.tecnico.nombres == "Juan Carlos"

def test_traer_mantenimiento_con_vehiculo():
    mant = traer_mantenimiento_con_vehiculo("Toyota XYZ")
    assert mant.vehiculo.modelo == "Toyota XYZ"

def test_traer_mantenimiento_con_vehiculo_empleado():
    mant = traer_mantenimiento_con_vehiculo_tecnico("Roberto Carlos", "Toyota XYZ")
    assert mant.vehiculo.modelo == "Toyota XYZ"
    assert mant.tecnico.nombres == "Roberto Carlos"
