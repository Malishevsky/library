from django.contrib import admin
from .models import LibraryClient, OwnedBook , ClientAdress

class ClientAdressAdminInline(admin.TabularInline):
    model = ClientAdress

@admin.register(LibraryClient)
class LibraryClientAdmin(admin.ModelAdmin):
    model = LibraryClient
    list_display = 'family_name','name','middle_name','date_of_bitrh'
    inlines = [ClientAdressAdminInline]


    
@admin.register(ClientAdress)
class ClientAdressAdmin(admin.ModelAdmin):
    model =  ClientAdress
    list_display = 'country','city','street','home_number','apartment_number'


@admin.register(OwnedBook)
class OwnedBookAdmin(admin.ModelAdmin):
    list_display = 'owneded_book','client'

    