from django.contrib import admin

from authentication.models import Voluntary


@admin.register(Voluntary)
class VoluntaryAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Usuário', {'fields': ('user',)}),
        ('Informações de Contribuição', {'fields': ('hours_worked',)})
    )

    list_display = ('user', 'hours_worked',)
    search_fields = ('user',)
    ordering = ('user',)

    readonly_fields = ('user', 'hours_worked',)
