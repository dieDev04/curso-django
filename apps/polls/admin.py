from django.contrib import admin
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")


# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question']}),
#         ('Choice information', {'fields': ['choice_text', 'votes']}),
#     ]

admin.site.register(models.Question, QuestionAdmin)
# admin.site.register(models.Choice, ChoiceAdmin)
