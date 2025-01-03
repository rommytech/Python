from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Filtro personalizado por año de fabricación
class FabricacionYearFilter(admin.SimpleListFilter):
    title = 'Año de fabricación'
    parameter_name = 'f_fabricacion'

    def lookups(self, request, model_admin):
        # Devuelve una lista de tuplas con los años disponibles
        years = set(Producto.objects.values_list('f_fabricacion', flat=True))
        return [(year, year) for year in years]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(f_fabricacion=self.value())
        return queryset


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'get_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', FabricacionYearFilter)  # Añadimos el filtro aquí
    search_fields = ('nombre', 'laboratorio__nombre')
    list_editable = ('p_costo', 'p_venta')

    def get_fabricacion(self, obj):
        return obj.f_fabricacion
    get_fabricacion.short_description = 'Año de fabricación'
