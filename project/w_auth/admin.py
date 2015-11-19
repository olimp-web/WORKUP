from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'created', 'last_login')
    fieldsets = (
        (None, {
            'fields': ('email', 'password', ('created', 'last_login'))
        }),
        ('Статус учетной записи', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Разрешенные действия и группы', {
            'fields': ('groups', 'user_permissions'),
            'classes': ('collapse', 'wide')
        })
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('created',)
    readonly_fields = ('created', 'last_login')
    search_fields = ('email', 'created')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

admin.site.register(Account, AccountAdmin)
