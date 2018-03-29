from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', login, {'template_name': 'registration/login.html'}, name='login-main'),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^Internal/$', views.Internal_Pressure, name='Internal'),
    url(r'^Internal_results/$', views.Internal_Pressure_Results, name='Internal_results'),
    url(r'^External/$', views.External_Pressure, name='External'),
    url(r'^External_results/$', views.External_Pressure_Results, name='External_results'),
    url(r'^selection/$', views.selection, name='selection'),
    url(r'^material/$', views.Materials, name='material'),
    url(r'^material/edit/$', views.Materials, name='material-edit'),
    url(r'^material/delete/(?P<pk>\d+)/$', views.Material_delete, name='material-delete'),
    url(r'^AddMaterial/$', views.AddMaterial, name='AddMaterial'),
    url(r'^head/$', views.Heads, name='head'),
    url(r'^head/delete/(?P<pk>\d+)/$', views.Head_delete, name='head-delete'),
    url(r'^AddHead/$', views.AddHead, name='AddHead'),
    #url(r'^.*$', RedirectView.as_view(pattern_name='login', permanent=False)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
