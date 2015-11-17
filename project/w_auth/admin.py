from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
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
    readonly_fields = ('created', 'last_login', 'password')
    search_fields = ('email', 'created')
#     TODO add 'set password' btn.
#     TODO change create form.
#     Look import django.contrib.auth.admin
