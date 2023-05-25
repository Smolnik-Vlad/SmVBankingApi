from django.contrib import admin

from credits_deposites.models import Credit, Deposit


# Register your models here.
class CreditsDepositesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'interest_rate', 'start_date', 'end_date', 'is_active')
    empty_value_display = "undefined"
    list_editable = ('amount', 'interest_rate', 'start_date', 'end_date', 'is_active')


admin.site.register(Credit, CreditsDepositesAdmin)
admin.site.register(Deposit, CreditsDepositesAdmin)
