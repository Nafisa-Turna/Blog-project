from django.urls import path
from . import views

urlpatterns = [
    path("login",views.bloglogin,name="login"),
    path("logout",views.bloglogout,name="logout"),
    path("",views.dashboard,name="dashboard"),
    path("create_category",views.create_category,name="create_category"),
    path("allcategory",views.allcategory,name="allcategory"),
    path('posts/del/<int:pk>',views.postdelete,name="postdelete"),
    path("posts",views.posts,name="posts"),
    path('posts/<int:pk>',views.updatepost,name="updatepost"),
    path('posts/delete/<int:pk>',views.deletepost,name="deletepost"),
    path("showallposts",views.showallposts,name="showallposts"),
    path("settings",views.settings,name="settings")
]