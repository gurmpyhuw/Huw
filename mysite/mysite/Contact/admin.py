from django.contrib import admin

#from .models import Book, Author, Publisher
from.models import *

#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')
#    search_fields = ('first_name', 'last_name')

#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_heirarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)

# Register your models here
#admin.site.register(Book, BookAdmin)
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Publisher)
admin.site.register(Title)
admin.site.register(Region)
admin.site.register(Interest)
admin.site.register(Contact)
admin.site.register(Type)
admin.site.register(Relationship)
admin.site.register(JobTitle)
admin.site.register(Source)