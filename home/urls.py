from django.urls import path

from . import views

urlpatterns = [
    path("card/", views.HomeCardList.as_view(), name="card-list"),
    path("card/<int:pk>", views.HomeCardDetail.as_view(), name='card-detail'),
    path("slide", views.HomeSlideList.as_view(), name='slide-list'),
    path("slide/<int:pk>", views.HomeSlideDetail.as_view(), name='slide-detail'),
]
