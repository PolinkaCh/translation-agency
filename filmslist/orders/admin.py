from django.contrib import admin
from .models import Translators, TranslationTypes, MovieType, LanguagePairs, Order, Post


admin.site.register(TranslationTypes)
admin.site.register(MovieType)
admin.site.register(LanguagePairs)
admin.site.register(Post)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'episode', 'receipt_date', 'deadline', 'translator', 'status')

@admin.register(Translators)
class TranslatorsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'languages', 'admission')
    list_filter = ('admission', 'languages')