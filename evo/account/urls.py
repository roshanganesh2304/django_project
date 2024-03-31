from django.urls import path
from .views import *

urlpatterns=[
    path('log',LoginView.as_view(),name="log"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('reg',RegView.as_view(),name="reg"),
    path('rev',ReviewView.as_view(),name="rev"),
    path('car',CarView.as_view(),name="car"),
    path('bike',BikeView.as_view(),name="bike"),
    path('b1',BikerView.as_view(),name="b1")
]