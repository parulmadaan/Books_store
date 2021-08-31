from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('registration/', views.registration_view,name="registration"),
    path('login/', views.login_view,name="login"),
    path('logout/', views.logout_link, name='logout'),
    path('userhome/',views.index, name="userhome"),
    path('home/',views.home_page, name="home"),
    path('profile/',views.profile_page, name="profile"),
    # path('email/',views.registration_view, name="email"),

]
