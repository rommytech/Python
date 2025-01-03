from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Modelo para Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    ciudad = models.CharField(max_length=255, default='')  # Nuevo campo
    pais = models.CharField(max_length=255, default='')    # Nuevo campo

    def __str__(self):
        return self.nombre

# Modelo para DirectorGeneral
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255, default='')  # Nuevo campo
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.nombre} - {self.laboratorio.nombre}'

# Modelo para Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE
    )
    
    YEARS_CHOICES = [(year, str(year)) for year in range(2015, datetime.now().year + 1)]
    
    f_fabricacion = models.IntegerField(
        choices=YEARS_CHOICES,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(datetime.now().year)
        ]
    )
    
    p_costo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    p_venta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.nombre} - {self.laboratorio.nombre}'
