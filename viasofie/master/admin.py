from django.contrib import admin
from .models import Pand
from .models import Criteria, PandCriteria, TypeHuis, Fase, Status, Staat
from .models import PandEigenschap, Eigenschap, Criteria, VerbruiksType, Wettelijk
from .models import VerbruiksType, PandVerbruiksType
from .models import Wettelijk, PandWettelijk, Document, PandDocument
from .models import Bezichtiging, PandBezichtiging, PandHitCount, Nieuwsbrief, \
    DynamicPageContent, DynamicPageContent_EN, DynamicPageContent_FR, MainDynamicPageContent
from .models import Supportticket
from django.shortcuts import get_object_or_404
from master.models import Image


class ImageInlineAdmin(admin.TabularInline):
    model = Image


class CriteriaInlineAdmin(admin.TabularInline):
        model = PandCriteria


class EigenschapInlineAdmin(admin.TabularInline):
    model = PandEigenschap


class VerbruikInlineAdmin(admin.TabularInline):
    model = PandVerbruiksType


class WettelijkInlineAdmin(admin.TabularInline):
    model = PandWettelijk

class DocumentInlineAdmin(admin.TabularInline):
    model = PandDocument

# Panden opties


class PandAdmin(admin.ModelAdmin):
    list_display = ('referentienummer', 'inkijker', 'user', 'fase', 'straat', 'postcode', 'stad', 'prijs', 'profiel_foto_img', 'datum')
    fields = (('referentienummer', 'inkijker'), 'user', ('straat_naam', 'huis_nummer'), ('postcode', 'gemeente'), ('stad', 'land'), ('verdieping', 'aantal_kamers'), 'status', ('staat', 'type', 'fase'), 'bouwjaar', 'prijs',
              'beschrijving', ('profiel_foto', 'plattegrond_gelijksvloer', 'plattegrond_eerste_verdiep'))
    search_fields = ('fase__naam', 'postcode', 'stad')
    list_filter = ['datum']
    inlines = [ImageInlineAdmin, DocumentInlineAdmin, CriteriaInlineAdmin, EigenschapInlineAdmin, VerbruikInlineAdmin, WettelijkInlineAdmin]
    ImageInlineAdmin.can_delete = True
    multiupload_form = True
    multiupload_list = False

    def admin_image(self):
        return '<img src="%s"/>' % self.img

    admin_image.allow_tags = True


class PandCriteriaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    list_display = ('pand', 'aantal', 'criteria')
    fields = ('pand', ('aantal', 'criteria'))
    search_fields = ('pand__postcode', 'pand__stad', 'criteria__naam')


class PandEigenschapAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    list_display = ('pand', 'eigenschap', 'oppervlakte', 'eenheid')
    search_fields = ('pand__postcode', 'pand__stad', 'eigenschap__naam')


class PandVerbruiksTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    list_display = ('pand', 'verbruik')
    search_fields = ('pand__postcode', 'pand__stad', 'verbruik__naam')


class PandWettelijkAdmin(admin.ModelAdmin):
    list_display = ('pand', 'wettelijk', 'jaartal')
    fields = ('pand', 'wettelijk', ('oppervlakte', 'eenheid'))
    search_fields = ('pand__postcode', 'pand__stad', 'wettelijk__naam')


class PandBezichtigingAdmin(admin.ModelAdmin):
    list_display = ('pand', 'bezichtiging', 'bezichtigd')
    search_fields = ('pand__postcode', 'pand__stad', 'bezichtiging__voornaam_bezoeker',
                     'bezichtiging__achternaam_bezoeker')


class SupportticketAdmin(admin.ModelAdmin):
    list_display = ('user', 'titel', 'beschrijving', 'gemaakt')
    search_fields = ('titel',)


class NieuwsbriefContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'actief',)
    fields = ('email', 'actief',)

class MainDynamicPageContentAdmin(admin.ModelAdmin):
    list_display = ('page_content_nl', 'page_content_en', 'page_content_fr',)

class PandDocumentAdmin(admin.ModelAdmin):
    list_display = ('pand', 'pand_document', 'document_code',)


class TypeHuisAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class FaseAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class StatusAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class StaatAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class EigenschapAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class CriteriaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class VerbruiksTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class WettelijkAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class DocumentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class DynamicPageContentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class DynamicPageContentAdmin_EN(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class DynamicPageContentAdmin_FR(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class DynamicPageContentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class PandDocumentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
# Register your models here.

# _________PAND___________
admin.site.register(Pand, PandAdmin)
admin.site.register(TypeHuis, TypeHuisAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Staat, StaatAdmin)
admin.site.register(Eigenschap, EigenschapAdmin)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(VerbruiksType, VerbruiksTypeAdmin)
admin.site.register(Wettelijk, WettelijkAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(PandDocument, PandDocumentAdmin)
admin.site.register(DynamicPageContent, DynamicPageContentAdmin)
admin.site.register(DynamicPageContent_FR, DynamicPageContentAdmin_FR)
admin.site.register(DynamicPageContent_EN, DynamicPageContentAdmin_EN)
# _______BEZICHTIGING__________
admin.site.register(PandBezichtiging, PandBezichtigingAdmin)


#Nieuwsbrief
admin.site.register(Nieuwsbrief, NieuwsbriefContactAdmin)

#CONTENT DYNAMIC LOADING
admin.site.register(MainDynamicPageContent, MainDynamicPageContentAdmin)
