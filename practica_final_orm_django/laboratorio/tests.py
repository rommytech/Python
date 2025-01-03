from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

# Clase de Pruebas Unitarias
class LaboratorioModelTest(TestCase):

    # Se ejecuta antes de cada prueba
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio Test',
            ciudad='Ciudad Test',
            pais='Pais Test'
        )

    # 1. Verifica que los datos del laboratorio coincidan
    def test_laboratorio_data(self):
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, 'Laboratorio Test')
        self.assertEqual(laboratorio.ciudad, 'Ciudad Test')
        self.assertEqual(laboratorio.pais, 'Pais Test')

    # 2. Prueba que la URL de listar laboratorios devuelve un HTTP 200
    def test_laboratorio_list_view(self):
        response = self.client.get(reverse('mostrar_laboratorios'))
        self.assertEqual(response.status_code, 200)

    # 3. Verifica que la plantilla correcta se esté usando
    def test_laboratorio_list_template(self):
        response = self.client.get(reverse('mostrar_laboratorios'))
        self.assertTemplateUsed(response, 'laboratorio/mostrar.html')
        self.assertContains(response, 'Información de Laboratorios')
