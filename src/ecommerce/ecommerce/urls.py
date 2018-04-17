"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView


import accounts.views
import addresses.views
import analytics.views
import billing.views
import carts.views
import marketing.views
import orders.views
import ecommerce.views

urlpatterns = [
    url(r'^$', ecommerce.views.home_page, name='home'),
    url(r'^about/$', ecommerce.views.about_page, name='about'),
    #url(r'^accounts/login/$', RedirectView.as_view(url='/login')),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^account/', include(("accounts.urls", 'account'))),
    url(r'^address/$', RedirectView.as_view(url='/addresses')),
    url(r'^addresses/$', addresses.views.AddressListView.as_view(), name='addresses'),
    url(r'^addresses/create/$', addresses.views.AddressCreateView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>\d+)/$', addresses.views.AddressUpdateView.as_view(), name='address-update'),
    url(r'^analytics/sales/$', analytics.views.SalesView.as_view(), name='sales-analytics'),
    url(r'^analytics/sales/data/$', analytics.views.SalesAjaxView.as_view(), name='sales-analytics-data'),
    url(r'^contact/$', ecommerce.views.contact_page, name='contact'),
    url(r'^login/$', accounts.views.LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', addresses.views.checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', addresses.views.checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', accounts.views.GuestRegisterView.as_view(), name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', carts.views.cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include(("carts.urls", 'cart'))),
    url(r'^billing/payment-method/$', billing.views.payment_method_view, name='billing-payment-method'),
    url(r'^billing/payment-method/create/$', billing.views.payment_method_createview, name='billing-payment-method-endpoint'),
    url(r'^register/$', accounts.views.RegisterView.as_view(), name='register'),
    #url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^library/$', orders.views.LibraryView.as_view(), name='library'),
    url(r'^orders/', include(("orders.urls", 'orders'))),
    url(r'^products/', include(("products.urls", 'products'))),
    url(r'^search/', include(("search.urls", 'search'))),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^settings/email/$', marketing.views.MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    url(r'^webhooks/mailchimp/$', marketing.views.MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
