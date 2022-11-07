from django.urls import path

from . import views

urlpatterns = [
    path("", views.SpecialList.as_view(), name="special-list"),
    path("<int:pk>", views.SpecialDetail.as_view(), name='special-detail'),
]
