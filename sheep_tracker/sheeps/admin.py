from django.contrib import admin

# Register your models here.

from .models import *


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


admin.site.register(Contact, ContactAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Address, AddressAdmin)

admin.site.register(Cell, CellAdmin)
admin.site.register(Person, PersonAdmin)



