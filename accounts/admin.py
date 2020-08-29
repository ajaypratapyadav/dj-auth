# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from .form import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser, InvestorInfo, InvestorGroups
#
#
# class CustomUserAdmin(UserAdmin):
#     """
#     This class create custom user form on with mentioned field on the admin dashboard.
#     Here i removed the username field and replace it with email values.
#     """
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('DeatilInfo', {'fields': ('first_name', 'last_name', 'user_type', 'score')}),
#         ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#          ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)  # registered Custom user table
# admin.site.register(InvestorInfo)  # registered InvestorInfo table
# admin.site.register(InvestorGroups)  # registered InvestorGroups table
