from django.db import models
from django.contrib import admin
# Create your models here.
from django.utils.translation import gettext_lazy as _

class header(models.Model):
    main_header = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف عنوان رئيسي", verbose_name="العنوان الرئيسي")
    sub_header = models.TextField(null=True, blank=True, help_text="اضف عنوان ثانوي", verbose_name="الوصف")

    def __str__(self):
        return self.main_header

    class Meta:
        verbose_name = _("العناوين الاولية")
        verbose_name_plural = _("العناوين الاولية")


class Image(models.Model):
    header = models.OneToOneField(header ,null=True ,on_delete=models.CASCADE , related_name="image")
    image = models.ImageField(upload_to='zulfiapp/static/image')
    def __str__(self):
        return str(self.image).split('static')[1]
    

class InlineImage(admin.TabularInline):
    model = Image


class headerAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

class AboutUs(models.Model):
    main_header = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف عنوان رئيسي", verbose_name="العنوان الرئيسي")
    sub_header = models.TextField(null=True, blank=True, help_text="اضف عنوان ثانوي", verbose_name="الوصف")

    def __str__(self):
        return self.main_header

    class Meta:
        verbose_name = _("من نحن")
        verbose_name_plural = _("من نحن")