from django.conf.urls import url
from Ligaplusapp import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
   url(r'^(?P<equipo_id>\d+)/$',views.jugadores_equipo, name='jugadores'),
   url(r'^registro$', views.registro, name='registro'),
   url(r'^login$', views.loginpage, name='login'),
   url(r'^logout$', views.logoutpage, name='logout'),
	
		
]
