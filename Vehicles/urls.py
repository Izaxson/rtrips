from django import views
from django.urls import include, path 
# from Vehicles import settings
from .views import   TripListView , ExpenseListView
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
      
   #  path('', admin.site.login, name='login'),
    path('', TripListView.as_view(), name='home'),
    path('trips/', TripListView.as_view(), name='trips'),
    # path('dashboard/', views.dashboard, name='dashboard'),

  
    path('expense/', ExpenseListView.as_view(), name='expense'),
   #  path('expense/', ExpenseListView.as_view(), name='expense'),
    # path('about/', AboutListView.as_view(), name='about'),
    # path('contact/', ContactView.as_view(), name='contact'),
    # path('article/<str:slug>', ArticleDetailView.as_view(), name='full-article'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # path('post/int<pk>', views.post ,name="full-article"),
    # path('contact/', views.contact ,name="contact"),
    # path('', views.home ,name="home"),
    # path('about/', views.about ,name="about"),
    
 ]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
