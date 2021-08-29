from django.contrib import admin

from store_app.models import Book, Order, OrderLine, Store


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 2


class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'store_num',
            'name',
            'last_update_date',
        ]}),
    ]
    list_display = [
        'store_num',
        'name',
        'last_update_date',
    ]
    search_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'order_num',
            'order_date',
            'store_num',
            'store_name',
            'customer_name',
            'customer_mail',
            'status',
        ]}),
    ]
    list_display = [
        'order_num',
        'order_date',
        'store_num',
        'store_name',
        'customer_name',
        'customer_mail',
        'status',
    ]
    search_fields = ['order_num']
    inlines = [OrderLineInline]


class OrderLineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'order',
            'book',
            'ISBN',
            'author_name',
            'title',
            'price',
            'quantity',
        ]}),
    ]
    list_display = [
        'order',
        'book',
        'ISBN',
        'author_name',
        'title',
        'price',
        'quantity',
    ]
    search_fields = ['ISBN', 'title']


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'ISBN',
            'author_name',
            'title',
            'pages',
            'price',
            'pubdate',
            'quantity',
        ]}),
    ]
    list_display = [
        'ISBN',
        'author_name',
        'title',
        'pages',
        'price',
        'pubdate',
        'quantity',
    ]
    list_filter = ['author_name']
    search_fields = ['ISBN', 'title']


admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Store, StoreAdmin)
