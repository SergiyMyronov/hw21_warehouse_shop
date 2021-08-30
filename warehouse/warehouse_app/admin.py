from django.contrib import admin

from warehouse_app.models import Book, Order, OrderLine


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 2


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
            'ISBN',
            'author_name',
            'title',
            'price',
            'quantity',
        ]}),
    ]
    list_display = [
        'order',
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
            'serial_num',
            'author_name',
            'title',
            'pages',
            'price',
            'pubdate',
            'status',
            'order_num',
            'update_date'
        ]}),
    ]
    list_display = [
        'ISBN',
        'serial_num',
        'author_name',
        'title',
        'pages',
        'price',
        'pubdate',
        'status',
        'order_num',
        'update_date'
    ]
    list_filter = ['ISBN', 'author_name']
    search_fields = ['title']


admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
