from django.urls import path
from .views import listamesa, lancar, fechar, lancando, tranferir, exibir, testes

urlpatterns = [
    path('', listamesa, name='url_listamesa'),
    path('lancar/', lancar, name='url_lancar'),
    path('fechar/', fechar, name='url_fechar'),
    path('lancando/', lancando, name='url_lancando'),
    path('tranferir/', tranferir, name='url_tranferir'),
    path('exibir/', exibir, name='url_exibir'),
    path('testes/', testes, name='url_testes'),
]
