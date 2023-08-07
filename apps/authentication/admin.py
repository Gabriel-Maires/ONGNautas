from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Voluntary
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = (
        ('Informações Pessoais', {'fields': ('cpf', 'birthdate',)}),
        ('Informações de Endereço', {'fields': ('address', 'cep', 'complement',)}),
        ('Funções', {'fields': ('is_voluntary', 'is_supporter')}),
    )

    list_display = ('first_name', 'last_name', 'email', 'is_voluntary', 'is_supporter')
    search_fields = ('first_name', 'last_name', 'cpf', 'email')
    list_filter = ('is_voluntary', 'is_supporter')
    ordering = ('first_name', 'last_name')

    readonly_fields = ['cpf', 'birthdate']


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
