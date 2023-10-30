from typing import Any
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField('Category name', max_length=254)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    subcat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField('SubCategory Name', max_length=254)
    img = models.ImageField('IMG', upload_to='media')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Collection(models.Model):
    info = models.CharField('Collection info', max_length=254)
    name = models.CharField('Collection name', max_length=254)
    img = models.ImageField('IMG', upload_to='media')

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE , null=True)
    name = models.CharField('Product Name', max_length=254)
    img = models.ImageField('IMG', upload_to='media')
    price = models.DecimalField('Product Price', max_digits=5, decimal_places=2)
    discount = models.DecimalField('Product Discount', max_digits=4, decimal_places=2)
    date_time = models.DateTimeField('DateTime', auto_now=True)
    description = models.TextField('Product Desc')

    def __str__(self) -> str:
        return self.name
    

class TrandyProduct(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return 'TrandyProducts'
    
class StayUpdated(models.Model):
    email = models.EmailField('Email')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'StayUpdated'
        verbose_name_plural = 'StayUpdated'
    
class OurShop(models.Model):

    product = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.product.__str__()
    
    class Meta:
        verbose_name = 'OurShop'
        verbose_name_plural = 'OurShop'


class BillingAddress(models.Model):
    first_name = models.CharField('First Name', max_length=254)
    last_name = models.CharField('Last Name', max_length=254)
    email = models.EmailField('Email')
    phone = PhoneNumberField()
    AddressLine1 = models.CharField('AddressLine1', max_length=254)
    AddressLine2 = models.CharField('AddressLine2', max_length=254)
    city = models.CharField('City', max_length=254)
    state = models.CharField('State', max_length=254)
    zipcode = models.PositiveIntegerField('Zip Code')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'BillingAddress'
        verbose_name_plural = 'BillingAddresses'


class ShippingAddress(models.Model):
    first_name = models.CharField('First Name', max_length=254)
    last_name = models.CharField('Last Name', max_length=254)
    email = models.EmailField('Email')
    phone = PhoneNumberField()
    AddressLine1 = models.CharField('AddressLine1', max_length=254)
    AddressLine2 = models.CharField('AddressLine2', max_length=254)
    city = models.CharField('City', max_length=254)
    state = models.CharField('State', max_length=254)
    zipcode = models.PositiveIntegerField('Zip Code')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'ShippingAddress'
        verbose_name_plural = 'ShippingAddresses'


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=253)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'ConcactUs'
        verbose_name_plural = 'ConcactUs'



class GeneralSlider(models.Model):
    img = models.ImageField('Slider Image', upload_to='media')
    title = models.CharField('Slider Title' , max_length=100)
    slogan = models.CharField('Slider Slugan' , max_length=100)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'GeneralSlider'
        verbose_name_plural = 'GeneralSliders'
        
        
class VendorSlider(models.Model):
    img = models.ImageField('VendorSlider Image', upload_to='media')

    def __str__(self) -> str:
        return 'VendorSlider'
    
    class Meta:
        verbose_name = 'VendorSlider'
        verbose_name_plural = 'VendorSlider'

class NewsLetter(models.Model):
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email')
    
    def __str__(self) -> str:
        return self.email
    
    
    class Meta:
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetter'

class AddChar(models.Model):
    char = models.CharField('Char', max_length=254)

    def __str__(self) -> str:
        return self.char
    
    class Meta:
        verbose_name = 'AddChar'
        verbose_name_plural = 'AddChar'

class AdditionalInformation(models.Model):
    text = models.TextField('Text')
    char = models.ManyToManyField(AddChar)

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Additional Information'
        verbose_name_plural = 'Additional Information'
    
class LeaveReview(models.Model):
    review = models.TextField('Review')
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email')
    date_time = models.DateTimeField('Date Time', auto_now=True)

    def __str__(self) -> str:
        return self.email
    

class ReviewFor(models.Model):

    review = models.ManyToManyField(LeaveReview)

    def __str__(self) -> str:
        return self.review.__str__()
    
class YouMayAlsoLike(models.Model):
    product = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.product.__str__()
    
    class Meta: 
        verbose_name = 'YouMayAlsoLike'
        verbose_name_plural = 'YouMayAlsoLike'

class GetInTouch(models.Model):
    char = models.CharField('Char', max_length=254)

    def __str__(self) -> str:
        return self.char
    
class StoreOne(models.Model):
    address = models.CharField('Address', max_length=254)
    email = models.EmailField('Email')
    phone = PhoneNumberField()

    def __str__(self) -> str:
        return self.address
    
class StoreTwo(models.Model):
    address = models.CharField('Address', max_length=254)
    email = models.EmailField('Email')
    phone = PhoneNumberField()

    def __str__(self) -> str:
        return self.address
    





















    

