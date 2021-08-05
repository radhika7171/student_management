from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Certificate, CertificateAdmin)
