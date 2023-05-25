from django.contrib import admin

from accounts.models import Account, Transaction


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'account_number', 'balance', 'created_at')
    list_editable = ('balance', 'account_number')
    empty_value_display = "undefined"


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'amount', 'timestamp')
    list_editable = ('amount',)
    empty_value_display = "undefined"


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
