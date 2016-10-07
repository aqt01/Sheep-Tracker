from django.contrib import admin

# Register your models here.

from .models import *

'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)
    search_fields = ['question']

'''

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AddressAdmin(admin.ModelAdmin):
    pass
class PersonAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass




admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Address, AddressAdmin)

admin.site.register(Location, LocationAdmin)
admin.site.register(Person, PersonAdmin)



