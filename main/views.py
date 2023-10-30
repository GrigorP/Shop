from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

class HomePageListView(generic.ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():
        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        collections_right = Collection.objects.all()[:1]
        collections_left = Collection.objects.all()[1:]
        trandy_products = TrandyProduct.objects.get().products.all()
        products = Product.objects.all()
        general_slider_active = GeneralSlider.objects.first()
        general_slider = GeneralSlider.objects.all()[1:]
        vendor_slider_active = VendorSlider.objects.all()[:6]
        vendor_slider = VendorSlider.objects.all()[6:]
        just_arrived = Product.objects.order_by('-date_time')[:8]

        for sub_cat in sub_categories:
            sub_cat.quantity = 0
            for product in products:
                if product.category == sub_cat:
                    sub_cat.quantity += 1


        for product in trandy_products:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for product in just_arrived:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)


        context = {
            'navbar': 'home',
            'products': products,
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
            'collections_left': collections_left,
            'collections_right': collections_right,
            'trandy_products': trandy_products,
            'general_slider':general_slider,
            'general_slider_active':general_slider_active,
            'just_arrived':just_arrived,
            'vendor_slider_active': vendor_slider_active,
            'vendor_slider': vendor_slider,
        }

        return context

    def get(self, request):
        
        context = self.__extract_all_data()

        return render(request, self.template_name, context)
    
    def post(self, request):
        form = StayUpdatedForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = StayUpdatedForm()
            
        form_news = NewsLetterForm(request.POST)
        
        if form_news.is_valid():
            form_news.save()
        else:
            form_news = NewsLetterForm()
        
        context = self.__extract_all_data()
        context.update({'form':form})
        context.update({'form_news':form_news})

        return render(request, self.template_name, context)


class CartPageListView(generic.ListView):
    template_name = 'cart.html'

    def get(self, request):

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()

        context = {
            'navbar': 'cart',
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
        }

        return render(request, self.template_name, context)
    

class CheckoutPageListView(generic.ListView):
    template_name = 'checkout.html'

    def get(self, request):
        
        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        
        context = {
            'navbar': 'checkout',
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
        }

        return render(request, self.template_name, context)
    
    def post(self, request):

        form_address = BillingAddressForm(request.POST)

        if form_address.is_valid():
            form_address.save()
        else:
            form_address = BillingAddressForm()

        form_shipping = ShippingAddressForm(request.POST)

        if form_shipping.is_valid():
            form_shipping.save()
        else:
            form_shipping = ShippingAddressForm()

        context = {
            'navbar': 'checkout',
            'form_address': form_address,
            'form_shipping': form_shipping,
        }

        return render(request, self.template_name, context)
    

class ContactPageListView(generic.ListView):
    template_name = 'contact.html'

    @staticmethod
    def __extract_all_data():

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        get_it_touch = GetInTouch.objects.get()
        store_one = StoreOne.objects.get()
        store_two = StoreTwo.objects.get()

        context = {
            'navbar': 'contact',
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
            'get_it_touch': get_it_touch,
            'store_one': store_one,
            'store_two': store_two,
        }

        return context

    def get(self, request):

        context = self.__extract_all_data()
        
        return render(request, self.template_name, context)
    
    def post(self, request):

        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()

        context = self.__extract_all_data()
        context.update({'form':form})

        return render(request, self.template_name, context)


class ShopPageListView(generic.ListView):
    template_name = 'shop.html'

    def get(self, request):

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        ourshop = OurShop.objects.get().product.all()
        latest = Product.objects.order_by('-date_time')[:8]
        for product in ourshop:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for product in latest:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        context = {
            'navbar': 'shop',
            'ourshop': ourshop,
            'categories': categories,
            'sub_categories_dresses': sub_categories_dresses,
            'sub_categories': sub_categories,
            'latest': latest,
        }

        return render(request, self.template_name, context)
    

class ProductDetailView(generic.DetailView):
    template_name = 'detail.html'

    # @staticmethod
    # def __extract_all_data():

        

    #     return context

    

    def get(self, request, id):

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        additional_information_text = AdditionalInformation.objects.first()
        additional_information_char_1 = AdditionalInformation.objects.get().char.all()[:4]
        additional_information_char_2 = AdditionalInformation.objects.get().char.all()[4:]
        reviews = ReviewFor.objects.get().review.all().order_by('-date_time')[:4]
        you_may_also_like_active = YouMayAlsoLike.objects.get().product.all()[:4]
        you_may_also_like = YouMayAlsoLike.objects.get().product.all()[4:]

        product = Product.objects.get(pk=id)
        product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for prod in you_may_also_like_active:
            prod.discount_price = round(prod.price * (1 - prod.discount / 100), 2)

        for prodd in you_may_also_like:
            prodd.discount_price = round(prodd.price * (1 - prodd.discount / 100), 2)

        context = {
            'navbar': 'detail',
            'product': product,
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
            'additional_information_text': additional_information_text,
            'additional_information_char_1': additional_information_char_1,
            'additional_information_char_2': additional_information_char_2,
            'reviews': reviews,
            'you_may_also_like_active': you_may_also_like_active,
            'you_may_also_like': you_may_also_like,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id):

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        additional_information_text = AdditionalInformation.objects.first()
        additional_information_char_1 = AdditionalInformation.objects.get().char.all()[:4]
        additional_information_char_2 = AdditionalInformation.objects.get().char.all()[4:]
        reviews = ReviewFor.objects.get().review.all().order_by('-date_time')[:4]
        you_may_also_like_active = YouMayAlsoLike.objects.get().product.all()[:4]
        you_may_also_like = YouMayAlsoLike.objects.get().product.all()[4:]

        product = Product.objects.get(pk=id)
        product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for prod in you_may_also_like_active:
            prod.discount_price = round(prod.price * (1 - prod.discount / 100), 2)

        for prodd in you_may_also_like:
            prodd.discount_price = round(prodd.price * (1 - prodd.discount / 100), 2)

        form = LeaveReviewForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = LeaveReviewForm()

        context = {
            'navbar': 'detail',
            'form': form,
            'product': product,
            'categories': categories,
            'sub_categories': sub_categories,
            'sub_categories_dresses': sub_categories_dresses,
            'additional_information_text': additional_information_text,
            'additional_information_char_1': additional_information_char_1,
            'additional_information_char_2': additional_information_char_2,
            'reviews': reviews,
            'you_may_also_like_active': you_may_also_like_active,
            'you_may_also_like': you_may_also_like,
        }

        



        return render(request, self.template_name, context)


class ShopPageLatestListView(generic.ListView):
    template_name = 'shoplatest.html'

    def get(self, request):

        categories = Category.objects.all()[1:]
        sub_categories_dresses = SubCategory.objects.all()[:3]
        sub_categories = SubCategory.objects.all()
        ourshop = OurShop.objects.get().product.all()
        latest = Product.objects.order_by('-date_time')[:8]
        for product in ourshop:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for product in latest:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        context = {
            'navbar': 'shop',
            'ourshop': ourshop,
            'categories': categories,
            'sub_categories_dresses': sub_categories_dresses,
            'sub_categories': sub_categories,
            'latest': latest,
        }

        return render(request, self.template_name, context)












