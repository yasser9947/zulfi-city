from django.db import models
from django.contrib import admin
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# header us
class header(models.Model):
    main_header = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف عنوان رئيسي", verbose_name="العنوان الرئيسي")
    sub_header = models.TextField(null=True, blank=True, help_text="اضف عنوان ثانوي", verbose_name="الوصف")

    def __str__(self):
        return self.main_header

    class Meta:
        verbose_name = _("العناوين الاولية")
        verbose_name_plural = _("العناوين الاولية")

choices = [('عرض كبير' , 'عرض كبير') , ('عرض عادي' , 'عرض عادي ')]
class News(models.Model):
    main_header = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف عنوان رئيسي", verbose_name="العنوان الرئيسي")
    sub_header = models.TextField(null=True, blank=True, help_text="اضف عنوان ثانوي", verbose_name="الوصف")
    date = models.DateField(default=timezone.now())
    hight = models.CharField(max_length=200 , choices=choices, null=True, blank=True, help_text="لعرض المحتوى ", verbose_name="طريقه العرض" )

    def __str__(self):
        return self.main_header

    class Meta:
        verbose_name = _("الأخبار")
        verbose_name_plural = _("الأخبار")

class Image2(models.Model):
    news = models.OneToOneField(News ,null=True ,on_delete=models.CASCADE ,default=None, related_name="image")
    image = models.ImageField(upload_to='zulfiapp/static/image')
    
    def __str__(self):
        return str(self.image).split('static')[1]


class Image(models.Model):
    header = models.OneToOneField(header ,null=True ,on_delete=models.CASCADE ,default=None, related_name="image")
    image = models.ImageField(upload_to='zulfiapp/static/image')
    
    def __str__(self):
        return str(self.image).split('static')[1]
    

class InlineImage(admin.TabularInline):
    model = Image
class InlineImage2(admin.TabularInline):
    model = Image2

class headerAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

class newsAdmin(admin.ModelAdmin):
    inlines = [InlineImage2]

# about us
class AboutUs(models.Model):
    main_header = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف عنوان رئيسي", verbose_name="العنوان الرئيسي")
    sub_header = models.TextField(null=True, blank=True, help_text="اضف عنوان ثانوي", verbose_name="الوصف")

    def __str__(self):
        return self.main_header

    class Meta:
        verbose_name = _("من نحن")
        verbose_name_plural = _("من نحن")


class OurPortfolio(models.Model):
    name = models.CharField(max_length=200 , null=True, blank=True, help_text="اضف الفرع", verbose_name="الفرع")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("أعمالنا")
        verbose_name_plural = _("أعمالنا")

class Image3(models.Model):
    portfolio = models.ForeignKey(OurPortfolio ,null=True ,on_delete=models.CASCADE ,default=None, related_name="image")
    image = models.ImageField(upload_to='zulfiapp/static/image')
    
    def __str__(self):
        return str(self.image).split('static')[1]
class InlineImage3(admin.TabularInline):
    model = Image3

class OurPortfolioAdmin(admin.ModelAdmin):
    inlines = [InlineImage3]