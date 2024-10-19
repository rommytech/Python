import sentry_sdk

sentry_sdk.init(dsn = "https://767f9c5a7948e57595f59abe162048fe@o4507908436590592.ingest.us.sentry.io/4507908911661056",
                traces_sample_rate = 1.0)
class Postulante:

    def __init__(self, nombres, egreso, especialidad):
        self.nombres = nombres
        self.egreso = egreso
        self.especialidad = especialidad
    
    def is_valid(self):
        datos_validos = True
        # Validación del nombre
        try:
            if len(self.nombres) < 4:
                raise ValueError("El nombre es muy corto")
        except Exception as e:
            sentry_sdk.capture_exception(e)

            datos_validos = False
            print("Por favor ingrese un nombre completo")

        # Validación del año de egreso
        try:
            egreso_numero = int(self.egreso)  # Convertimos el texto a número
            if egreso_numero < 1990 or egreso_numero > 2024:
                raise ValueError("Rango de egreso erróneo")
        except Exception as e:
            sentry_sdk.capture_exception(e)
            datos_validos = False
            print("Lo sentimos, el ingreso es incorrecto")
            return False  # Devolvemos False en caso de error

        # Validación de la especialidad
        try:
            if len(self.especialidad) < 4:
                raise ValueError("Especialidad incorrecta")
        except ValueError as e:
            sentry_sdk.capture_exception(e)
            print(e)
            return False  # Devolvemos False en caso de error
        
        print("Formulario válido")  # Si pasa todas las validaciones
        return datos_validos  # Devolvemos True si todo está correcto

    def save(self):
        import csv

        with open("postulantes.csv", mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            if archivo.tell() == 0:
                escritor.writerow(["NOMBRES", "EGRESO", "ESP."])

            escritor.writerow([self.nombres,
                               self.egreso,
                               self.especialidad])
