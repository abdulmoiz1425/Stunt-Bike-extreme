from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('name', 'email', 'body', 'approved', 'created_at')
    readonly_fields = ('name', 'email', 'body', 'created_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_published', 'reading_time_display', 'comment_count')
    list_filter = ('is_published', 'author', 'publish_date')
    list_editable = ('is_published',)
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'author', 'featured_image', 'excerpt', 'content')}),
        ('Publishing', {'fields': ('is_published', 'publish_date')}),
        ('SEO', {'fields': ('meta_title', 'meta_description')}),
    )

    def reading_time_display(self, obj):
        return f'{obj.reading_time} min'
    reading_time_display.short_description = 'Read Time'

    def comment_count(self, obj):
        total = obj.comment_set.count()
        approved = obj.comment_set.filter(approved=True).count()
        return format_html('{} <small style="color:#888">({} approved)</small>', total, approved)
    comment_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    list_editable = ('approved',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'reject_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = 'Approve selected comments'

    def reject_comments(self, request, queryset):
        queryset.update(approved=False)
    reject_comments.short_description = 'Reject selected comments'
