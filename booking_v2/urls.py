from django.urls import path
from booking_v2.views import SignupView
urlpatterns =[
   path('v2/booking/',SignupView.as_view()),                                 
]