# from django.contrib import admin

from .models import CustomUser
from .models import Category, Subcategory, Product, Age, Brand ,WishlistItem
# Register your models here.
# admin.site.register(CustomUser)

# Register your models here.



# new
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class SuperuserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return User.objects.filter(is_superuser=False)

# Register the custom admin class
admin.site.register(User, SuperuserAdmin)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Age)
admin.site.register(Product)
admin.site.register(WishlistItem)

from .models import  Cart, CartItem, Order, OrderItem

# admin.site.register(Profile)

admin.site.register(CartItem)
admin.site.register(Cart)

admin.site.register(Order)
admin.site.register(OrderItem)