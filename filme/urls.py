#url - view  - template -------pra cada link ,tem que  criar essas 3 coisas


from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme

# urlpatterns = [
#     path('', homepage),
#     path('filmes/', homefilmes), ]


app_name= 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name ='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme')

]