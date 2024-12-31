from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User, Company, Auditor, Audit, Payment, LeaveApplication


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput,
        help_text="Password must contain at least 6 alphanumeric characters and/or special symbols"
    )
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "phone"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        if len(password1) < 6:
            raise ValidationError("Passwords can't be less than 6 characters")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput, required=False
    )

    class Meta:
        model = User
        fields = [
            "email", "username", "password", "first_name", "last_name", "phone",  "password1", "password2"
        ]

    def save(self, commit=True):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        user = super().save(commit=False)

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Passwords don't match")
            elif len(password1) < 6:
                raise ValidationError("Passwords can't be less than 6 characters")
            else:
                user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["username", "first_name", "last_name", "email", "phone"]

    fieldsets = [
        (
            None,
            {"fields": ["first_name", "last_name", "phone", "email", "username"]}
        ),
        (
            "Password Change",
            {
                "classes": ["collapse"],
                "fields": ["password1", "password2"]
            }
        )
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["first_name", "last_name", "email", "username", "phone", "password1", "password2"],
            },
        ),
    ]
    search_fields = ['first_name', 'last_name', "email", "phone"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.register([Company])
admin.site.register([Auditor,Payment,Audit, LeaveApplication])