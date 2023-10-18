from django.contrib import admin

from .models import Problem

admin.site.register(Problem)

# class TestCaseInline(admin.TabularInline):
#     model = TestCase
#     extra = 1
#
#
# @admin.register(Problem)
# class ProblemAdmin(admin.ModelAdmin):
#     inlines = [TestCaseInline]


# admin.site.register(Tag)
# admin.site.register(TestCase)
