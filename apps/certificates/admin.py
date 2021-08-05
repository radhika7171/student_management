from django.contrib import admin
from .models import Certificate  #,Certificate_test


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)



# class Certificate_testAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     search_fields = ('name',)



admin.site.register(Certificate, CertificateAdmin)
# admin.site.register(Certificate_test, CertificateAdmin)


