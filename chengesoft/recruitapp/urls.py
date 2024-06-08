from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('register/',views.register,name='register'),
    path('recruit/',views.recruit,name='recruit'),
    path('practicaltest/<int:id>',views.practicaltest,name='practicaltest'),
    path('compiler',views.compiler,name='compiler'),
    path('createtest/',views.createtest,name='createtest'),
    path('maketheory/',views.maketheory,name='maketheory'),
    path('theorytest/',views.theorytest,name='theorytest'),
    path('mytest/',views.mytest),
]
