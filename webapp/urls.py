from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^calculator/$', views.calculator, name='calculator'),
    url(r'^.*$', RedirectView.as_view(pattern_name='login', permanent=False)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
