from django.urls import path
from .views import report_view,delete_view,ReportUpdateView,HomeView,SelectView,main_report_summary,render_pdf_view

app_name='reports'

urlpatterns = [

    path('',HomeView.as_view(),name="home"),
    path('reports/',SelectView.as_view(),name="select-view"),
    path('reports/summary/',main_report_summary,name='summary-view'),
    path('reports/<str:production_line>/',report_view,name="report-view"),
    path('reports/delete/<pk>/',delete_view,name='delete-view'),
    path('reports/<str:production_line>/<pk>/update/',ReportUpdateView.as_view(),name="update-view"),
    path('reports/generate/pdf/',render_pdf_view,name='pdf')            
    

]
