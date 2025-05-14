"""
Definition of urls for HotelFlexProject.
"""

from django.urls import path
import app.views


urlpatterns = [
    path('', app.views.home, name='home'),
    path('contact', app.views.contact, name='contact'),
    path('about', app.views.about, name='about'),
    path('register/', app.views.register, name='register'),
    path('login/', app.views.login, name='login'),
    path('booking/', app.views.booking, name='booking'),
    path('logout', app.views.logout, name='logout'),
    path('roombooking/', app.views.roombooking, name='roombooking'),
    path('single/', app.views.single, name='single'),
    path('forgotpassword/', app.views.forgotpassword, name='forgot'),
    path('double/', app.views.double, name='double'),
    path('luxury/', app.views.luxury, name='luxury'),
    path('deluxe/', app.views.deluxe, name='deluxe'),
    path('executive/', app.views.executive, name='executive'),
    path('presidential/', app.views.presidential, name='presidential'),
    path('bookinghistory/', app.views.bookinghistory, name='history'),
    path('rooms/', app.views.rooms, name='rooms'),
    path('adminruby/', app.views.adminruby, name='adminruby'),
    path('adminlogin/', app.views.adminlogin, name='adminlogin'),
    path('getusers/', app.views.getusers, name='adminlogin'),
    path('adminbooking/', app.views.adminbooking, name='adminbooking'),
    path('salesanalysis/', app.views.salesanalysis, name='salesanalysis'),

    # To enable Django admin (optional):
    # path('admin/', admin.site.urls),
]
