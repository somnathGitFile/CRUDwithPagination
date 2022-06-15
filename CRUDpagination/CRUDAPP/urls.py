from django.urls import path
from.import views

urlpatterns=[
    path('SC/',views.ShowCustomer.as_view(), name='showCust_url'),
    path('AC/',views.AddCustomer.as_view(), name='addCust_url'),
    path('UC/<int:pk>/',views.UpdateCustomer.as_view(),name='updateCust_url'),
    path('DC/<int:pk>/', views.DeleteCustomer.as_view(),name='deleteCust_url'),
    path('pdf/<int:pk>/',views.perticularData, name='pdf2_url'),
    path('pdf/',views.GenaratePDF, name='pdf_url'),
]