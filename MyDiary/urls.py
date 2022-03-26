
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views as user_views
from users import views
from . import views as d_views


admin.site.site_header = "My notes"
admin.site.site_title = "Admin Portal || My notes"
admin.site.index_title = "Welcome to My notes admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mynotes/',d_views.mynotes,name='home'),
    path('sort_by/', d_views.sort_by, name="sort-by"),
    path('pdf/<slug:slug>',d_views.GeneratePdf,name='pdf'),

  
    path('',d_views.home,name='landing-page'),
    path('search',d_views.search,name='search'),
    path('tagged/<slug:slug>',d_views.tagged,name='tagged'),
    path('note/',include('note.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.llogin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
