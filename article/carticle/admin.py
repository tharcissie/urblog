from django.contrib import admin
from .models import Article, College,  Comment



#####################     registering college model on admin dashboard    ######################


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name','description',)
    search_fields = ('name','description',)

admin.site.register(College, CollegeAdmin)

#####################     registering comment model on admin dashboard    ######################

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','user','reply','content','timestamp',)

admin.site.register(Comment, CommentAdmin)

#####################     registering college model on admin dashboard    ######################

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('subject','message','created_at','updated_at','author','college',)
    
admin.site.register(Article, ArticleAdmin)






