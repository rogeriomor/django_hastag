#url - view  - template -------pra cada link ,tem que  criar essas 3 coisas


from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage),
]