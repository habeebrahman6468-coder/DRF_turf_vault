from django.urls import path
from booking_v2.views import SignupView,BookingListCreateiew,BookingRetrieveUpdateDeleteView



urlpatterns =[
   path('signup/',SignupView.as_view()), 

   path('reservation/',BookingListCreateiew.as_view()), 
   path('reservation/<int:pk>/',BookingRetrieveUpdateDeleteView.as_view()),                               
]