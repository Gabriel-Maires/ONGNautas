from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = (
        ('Informação Pessoal', {'fields': ('cpf',)}),
        ('Cargos', {'fields': ('is_voluntary', 'is_supporter')}),
    )

    list_display = ('first_name', 'last_name', 'email', 'is_voluntary', 'is_supporter')

    readonly_fields = ['is_voluntary', 'is_supporter', 'cpf']
