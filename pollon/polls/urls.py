from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
    path('',views.index,name="index"),
    path('<int:question_id>/',views.details,name="details"),
    path('results/<int:question_id>/',views.results,name="results"),
    path('<int:question_id>/vote/',views.vote,name="vote"),
    path('resultsdata/<str:question_id>',views.resultsData,name="resultsData")
]