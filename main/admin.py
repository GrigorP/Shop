from django.contrib import admin
from .models import (
    Category, SubCategory,
    Collection, Product,
    TrandyProduct, StayUpdated,
    OurShop, BillingAddress, 
    ShippingAddress, ContactUs, 
    GeneralSlider, VendorSlider,
    NewsLetter, AddChar, 
    AdditionalInformation, LeaveReview, 
    ReviewFor, YouMayAlsoLike, 
    GetInTouch, StoreOne, 
    StoreTwo, 
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(TrandyProduct)
admin.site.register(StayUpdated)
admin.site.register(OurShop)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(ContactUs)
admin.site.register(GeneralSlider)
admin.site.register(VendorSlider)
admin.site.register(NewsLetter)
admin.site.register(AddChar)
admin.site.register(AdditionalInformation)
admin.site.register(LeaveReview)
admin.site.register(ReviewFor)
admin.site.register(YouMayAlsoLike)
admin.site.register(GetInTouch)
admin.site.register(StoreOne)
admin.site.register(StoreTwo)

