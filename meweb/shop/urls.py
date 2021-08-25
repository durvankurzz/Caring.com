from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="Tracker"),
    path("search/",views.search,name="Search"),
    path("productview/<int:myid>",views.productview,name="ProductView"),
    path("checkout/",views.checkout,name="CheckOut"),
    # path("handlerequest/",views.handlerequest,name="HandleRequest"),
    path("signup/",views.handleSignUp,name="handleSignUp"),
    path("login/",views.HandleLogin,name="HandleLogin"),
    path("logout/",views.HandleLogout,name="HandleLogout"),
]