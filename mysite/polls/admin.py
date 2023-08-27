from django.contrib import admin
from .models import Analyste, Expert, Capture

class AnalysteAdmin(admin.ModelAdmin):
    list_display = ('id_analyste', 'role', 'department', 'login')  # Les champs à afficher dans la liste des analystes

admin.site.register(Analyste, AnalysteAdmin)

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('id_expert', 'analyste', 'speciality', 'experience_years')  # Les champs à afficher dans la liste des experts


admin.site.register(Expert, ExpertAdmin)

class CaptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'analyst', 'expert')  # Les champs à afficher dans la liste des captures

admin.site.register(Capture, CaptureAdmin)


# from .models import Choice, Question


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

# admin.site.register(Question, QuestionAdmin)

