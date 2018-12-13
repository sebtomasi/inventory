from django.contrib import admin
from .models import Hardware, Category

admin.site.register(Category)


def convert_price_chf_eur(modeladmin, request, queryset):
    for hardware in queryset:
        hardware.price = 0.93 * hardware.price
        hardware.save()


def convert_price_eur_chf(modeladmin, request, queryset):
    for hardware in queryset:
        hardware.price = hardware.price * 1 / 0.93
        hardware.save()


convert_price_chf_eur.short_description = "Conversion des prix de CHF en EUR"
convert_price_eur_chf.short_description = "Conversion des prix de EUR en CHF"


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ('category', 'buy_date', 'price','is_deleted')
    list_filter = ('category','is_deleted')
    actions = [convert_price_chf_eur, convert_price_eur_chf]
