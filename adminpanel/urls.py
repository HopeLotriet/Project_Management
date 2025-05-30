from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_books/', views.admin_books, name='admin_books'),
    path('app_kanban/', views.app_kanban, name='app_kanban'),
    path('admin_journals/', views.admin_journals, name='admin_journals'),
    path('admin_ganttchart/', views.admin_ganttchart, name='admin_ganttchart'),
    path('overview/', views.overview, name='overview'),
    path('finance/', views.finance, name='finance'),
    path('admin_kanban/', views.admin_kanban, name='admin_kanban'),
    path('supervisor_dashboard/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('finance/add-cost-centre/', views.add_cost_centre, name='add_cost_centre'),
    path('finance/expenditures/<int:cost_centre_id>/', views.get_expenditures, name='get_expenditures'),
    path('feedback/<int:submission_id>/', views.provide_feedback, name='provide_feedback'),

]
