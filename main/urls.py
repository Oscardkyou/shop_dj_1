from django.urls import path
from .views import IndexView, AddProductView, ProductView, CategoryView, CommentView, SignUpUserView, LogoutUserView, SingInUserView

urlpatterns = [
      path('', IndexView),
      path('add/', AddProductView),
      path('product/', ProductView),
      path('category/', CategoryView),
      path('comment/', CommentView),
      path('singin/', SignUpUserView),
      path('singup/', SingInUserView),
      path('logout/', LogoutUserView),
]