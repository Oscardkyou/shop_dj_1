from django.urls import path
<<<<<<< HEAD
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
=======
from .views import IndexView, AddProductView, ProductView,\
    LogoutUserView, SingUpUserView, SignInUserView, UserProfileView

urlpatterns = [
    path('', IndexView),
    path('add/', AddProductView),
    path('product/', ProductView),
    path('signup/', SingUpUserView),
    path('signin/', SignInUserView),
    path('logout/', LogoutUserView),
    path('profile/', UserProfileView)
>>>>>>> d3bd320 (ShopTestDj)
]