from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from djob_profile.models import Profile, Education, Experience
from .models import User


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class EducationInline(admin.StackedInline):
    model = Education
    can_delete = True
    verbose_name_plural = 'Education'
    fk_name = 'user'
    extra = 0

class ExperienceInline(admin.StackedInline):
    model = Experience
    can_delete = True
    verbose_name_plural = 'Experience'
    fk_name = 'user'
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, EducationInline, ExperienceInline )

    def get_inline_instances(self, request, obj=None):
        """
        Args:
            request:
            obj:
        """
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)