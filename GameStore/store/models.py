from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Пользователь
class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    groups = models.ManyToManyField(Group, related_name="user_set_custom", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="user_permissions_custom", blank=True)

    def __str__(self):
        return self.username


# Категории (если используем свои, а не из RAWG)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Игры (запрашиваем данные из RAWG API, но храним ID, цену и доп. инфо)
class Game(models.Model):
    rawg_id = models.IntegerField(unique=True)  # ID игры в RAWG API
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Для кеширования данных

    def __str__(self):
        return self.title


# Отзывы (локальные, а не из RAWG API)
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()  # 1-10
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


# Заказ
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('paid', 'Оплачен'),
        ('shipped', 'Отправлен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# Игры в заказе
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.game.title} x {self.quantity}"
