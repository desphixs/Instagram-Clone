from django.contrib import admin
from .models import Profile
# class ProfileAdmin(admin.ModelAdmin):
#     list_filter = ('creator', 'normal_user')

# class PackagePriceAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug":("package_name",)}

admin.site.register(Profile)
# admin.site.register(Contact)
# admin.site.register(Review)
# admin.site.register(GetInTouch)
# # admin.site.register(NewsLetter)
# admin.site.register(PackagePrice, PackagePriceAdmin)
# admin.site.register(AboutUs)
# admin.site.register(FAQs)
# admin.site.register(Announcements)
# admin.site.register(support_and_customerservice)
# admin.site.register(privacy_and_terms)
# admin.site.register(Feedback)
# admin.site.register(ModelNotes)
# admin.site.register(HomePopup)
# # admin.site.register(Creators)
# admin.site.register(Banner)
# admin.site.register(NewsLetter)
# admin.site.register(MailMessage)
