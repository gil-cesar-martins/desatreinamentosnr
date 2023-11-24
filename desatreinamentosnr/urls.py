from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from app.views import home,treinamentos,treinamentos01,treinamentos06,treinamentos12,treinamentos18andaimes,treinamentos18soldagem,treinamentos20,treinamentos33,treinamentos35,store,painel,videos01,videos06,videos12,videos18andaimes,videos18soldagem,videos20,videos33,videos35,slides01,slides06,slides12,slides18andaimes,slides18soldagem,slides20,slides33,slides35,dologin,dashboard,logouts

urlpatterns = [
    path('painelcontrole/', admin.site.urls),
    path('', home),
    path('treinamentos/', treinamentos),
    path('treinamentos01/', treinamentos01),
    path('treinamentos06/', treinamentos06),
    path('treinamentos12/', treinamentos12),
    path('treinamentos18-andaimes/', treinamentos18andaimes),
    path('treinamentos18-soldagem/', treinamentos18soldagem),
    path('treinamentos20/', treinamentos20),
    path('treinamentos33/', treinamentos33),
    path('treinamentos35/', treinamentos35),
   
    path('store/', store),
    path('painel/', painel),
    path('videos01/', videos01),
    path('videos06/', videos06),
    path('videos12/', videos12),
    path('videos18-andaimes/', videos18andaimes),
    path('videos18-soldagem/', videos18soldagem),
    path('videos20/', videos20),
    path('videos33/', videos33),
    path('videos35/', videos35),
    
    path('slides01/', slides01),
    path('slides06/', slides06),
    path('slides12/', slides12),
    path('slides18-andaimes/', slides18andaimes),
    path('slides18-soldagem/', slides18soldagem),
    path('slides20/', slides20),
    path('slides33/', slides33),
    path('slides35/', slides35),
  
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
    path('painel/', painel),
]

admin.AdminSite.site_header = 'Treinamentos DESA Engenharia'
admin.AdminSite.site_title = 'Treinamentos DESA'
admin.AdminSite.index_title = 'DESA ENGENHARRIA'
