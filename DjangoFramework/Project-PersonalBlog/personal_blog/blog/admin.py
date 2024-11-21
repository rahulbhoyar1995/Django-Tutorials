from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')  # Ensure 'published_date' exists in Post
    list_filter = ('category', 'published_date')  # Ensure 'published_date' is valid
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content', 'created_date')  # Ensure 'created_date' exists in Comment
    list_filter = ('created_date',)  # Add filters if needed
