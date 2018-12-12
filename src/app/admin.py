from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Currencie, Symbol, Balance, Certification, Account, Biz
from .models import OrderSide, OrderType, OrderRule, TradingStrategy


class CurrencieAdmin(admin.ModelAdmin):
    fields = ('name', 'created_at')
    list_display = ('name', 'created_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']
    readonly_fields = [field.name for field in Currencie._meta.fields]

    def get_ordering(self, request):
        return ['name']

    def has_add_permission(self, request):
        return False
  
    def has_delete_permission(self, request, obj=None):
        return False

class SymbolAdmin(admin.ModelAdmin):
    fields = ('name', 'base_currency', 'quote_currency', 'price_decimal', 'amount_decimal', 'created_at', 'updated_at')
    list_display = ('name', 'base_currency', 'quote_currency', 'price_decimal', 'amount_decimal', 'created_at', 'updated_at')
    list_filter = [
        'quote_currency',
        'price_decimal',
        'amount_decimal',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name', 'base_currency', 'quote_currency']
    readonly_fields = [field.name for field in Symbol._meta.fields]

    def get_ordering(self, request):
        return ['name']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class BalanceAdmin(admin.ModelAdmin):
    fields = ('currency', 'category', 'available', 'frozen', 'balance', 'created_at', 'updated_at')
    list_display = ('currency', 'category', 'available', 'frozen', 'balance', 'created_at', 'updated_at')
    list_filter = [
        'category',
        'created_at',
        'updated_at',
    ]
    search_fields = ['currency']
    readonly_fields = [field.name for field in Balance._meta.fields]

    def get_ordering(self, request):
        return ['-balance', 'currency']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'key', 'secret', 'created_at', 'updated_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class AccountAdmin(admin.ModelAdmin):
    list_display = ('certification', 'created_at', 'updated_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = []

    def get_ordering(self, request):
        return ['updated_at']


class BizAdmin(admin.ModelAdmin):
    fieldsets = (
        ('base', {
          'fields': ('order_symbol', 'order_side', 'order_type', 'order_price', 'order_amount')
        }),
        ('extra', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('order_state', 'order_executed_value', 'order_filled_amount', 'order_fill_fees', 'order_created_at', 'order_source',),
        }),
    )

    readonly_fields = ('order_state', 'order_executed_value', 'order_filled_amount', 'order_fill_fees', 'order_created_at', 'order_source',)

    list_display = (
        'order_id',
        'order_symbol', 
        'order_side', 
        'order_type', 
        'order_price', 
        'order_amount', 
        'order_state', 
        'order_executed_value', 
        'order_filled_amount', 
        'order_fill_fees', 
        'order_created_at', 
        'order_source', 
        'created_at',
        'updated_at'
    )
    list_filter = [
        'order_side', 
        'order_type', 
        'order_state', 
        'order_created_at', 
        'order_source', 
        'created_at',
        'updated_at',
    ]
    list_display_links = ('order_id', 'order_symbol')
    search_fields = ['order_symbol']

    def get_ordering(self, request):
        return ['order_created_at']


class OrderSideAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class OrderRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class TradingStrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price', 'order_rule', 'order_side', 'amount', 'total', 'interval', 'enable', 'username', 'created_at', 'updated_at',)
    list_filter = [
        'order_rule',
        'username',
        'enable',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']
    list_editable = ('enable',)

    def get_ordering(self, request):
        return ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'price', 'symbol', 'order_rule', 'order_side', 'amount', 'total', 'interval', 'enable', 'username']
        else:
            return []

    def get_actions(self, request):
        return []

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):           
        if db_field.name == 'username':                                                
            kwargs['initial'] = request.user.id                                     
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        if db_field.name == 'symbol':                                                
            kwargs['initial'] =  Symbol.objects.get(name='fteth').id                                 
            kwargs['queryset'] = Symbol.objects.filter(Q(name='fteth') | Q(name='ethusdt'))
        return super(TradingStrategyAdmin, self).formfield_for_foreignkey(                     
            db_field, request, **kwargs                                             
        )   


admin.site.register(Currencie, CurrencieAdmin)
admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Biz, BizAdmin)
admin.site.register(OrderType, OrderTypeAdmin)
admin.site.register(OrderSide, OrderSideAdmin)
admin.site.register(OrderRule, OrderRuleAdmin)
admin.site.register(TradingStrategy, TradingStrategyAdmin)

admin.site.site_title = 'Business & Operation Support System'
admin.site.site_header = 'Business & Operation Support System'
