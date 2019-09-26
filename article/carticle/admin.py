from .models import Article, College,  Comment
from django.contrib import admin


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name','description',)

admin.site.register(College, CollegeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','user','reply','content','timestamp',)

admin.site.register(Comment, CommentAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('subject','message','created_at','updated_at','author','college',)
    
admin.site.register(Article, ArticleAdmin)






