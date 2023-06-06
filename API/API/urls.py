from django.contrib import admin
from django.urls import path
from DataScience import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ComputerScience/detail/',views.ComputerScienceView.as_view()),
    path('api/ComputerScience/detailUpdateDelete/',views.ComputerScienceViewUpdateDelete.as_view())
]
