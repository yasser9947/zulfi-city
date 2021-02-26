from django.contrib import admin
from .models import header , AboutUs , headerAdmin , newsAdmin , News
# Register your models here.

admin.site.register(header , headerAdmin)
admin.site.register(AboutUs)
admin.site.register(News , newsAdmin)