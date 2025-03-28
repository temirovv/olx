from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from .models import SellerAccount, RegistrationForm, Document


@register(SellerAccount)
class SellerAccountAdmin(ModelAdmin):
    pass


class DocumentTabularInline(TabularInline):
    model = Document


@register(RegistrationForm)
class RegistrationFormAdmin(ModelAdmin):
    inlines = [DocumentTabularInline]
