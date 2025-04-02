from django.contrib import admin
from .models import User, Game, Category, Review, Order, OrderItem

# Регистрация модели User
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)

# Регистрация остальных моделей
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)