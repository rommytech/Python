from empleado import Empleado
from supervisor import Supervisor
from tecnico import Tecnico
from mantenimiento import Mantenimiento
from vehiculo import Vehiculo
from software import Software
# from software import Software  # Descomentar si ha implemenado la clase Software
# from mantenimiento import Mantenimiento # Descomentar si ha implementado la clase Mantenimiento
def traer_supervisor():
    #Retornar una instancia Supervisor
    sor = Supervisor(555, "George Ramirez")
    return sor

def traer_dos_empleados():
# Retornar un array con dos instancias de Empleados
    em1 = Empleado(999, "Leandro Vega")
    em2 = Empleado(333, "Ana Camargo")
    return [em1, em2]

def traer_tecnico_supervisor_empleado():
    # Retornar un array con
    # 1 instancia de un tecnico

    tec = Tecnico(444, "Abelardo Rojas", "Neumaticos")
    # 1 instancia de un supervisor
    sup = Supervisor(111, "Roman Robles")
    # 1 instancia de un empleado
    empl = Empleado(55, "Abel Reyes")

    return [tec, sup, empl]

def traer_n_empleados(num):
    # La funcion debe retornar
    # El numero de instanciar que
    # indica el parametro num
    empls = []
    ### Utilizar for item in range(num)
    for item in range(num):
        ni = Empleado(34, "Leo Rojas")
        empls.append(ni)
    return empls

def traer_software_con_parametros(version):
    # Retornar una instancia
    # de un software con la version
    # que indica el parametro
    software = Software(version, "2012/12/12", "Mejoras")
    return software # Reemplazar esta linea

def traer_mantenimiento_con_tecnico(tecnico_nombre):
    # Retornar una instancia de Mantenimiento
    # con un empleado de nombre, como indica el parametro
    tecnico = Tecnico(44, tecnico_nombre, "Neumaticos")
    vehiculo = Vehiculo("Auto", "4543", "Toyota", "2023", "Sysauto")

    mant = Mantenimiento("2023/12/12", "Revision", tecnico, vehiculo)
    return mant

def traer_mantenimiento_con_vehiculo(modelo_vehiculo):
    # Retornar una instancia de Mantenimiento
    # con un vehiculo de del modelo como indica el parametro
    tecnico = Tecnico(1212, "Leo Rojas", "Neumaticos")
    vehiculo = Vehiculo("Auto", "1234", modelo_vehiculo, "2013", "System")
    mant = Mantenimiento("2012/12/12", "Revision", tecnico, vehiculo)
    return mant

def traer_mantenimiento_con_vehiculo_tecnico(modelo_vehiculo, tecnico_nombre):
    # Retornar una instancia de Mantenimiento
    # con un vehiculo de del modelo como indica el parametro
    tecnico = Tecnico(434, tecnico_nombre, "Neumaticos")
    vehiculo = Vehiculo("Auto", "2323", modelo_vehiculo, "2023", "System")
    mant = Mantenimiento("2012/12/12", "Revision", tecnico, vehiculo) 
    return mant