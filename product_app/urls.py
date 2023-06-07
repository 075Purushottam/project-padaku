from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('product/<str:pk>/',views.productPage,name='product-page'),
    path('enquiry/',views.enquiryPage,name='enquiry-page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
