from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
	path('check-absent-students/', check_absent_students, name='check_absent_students'),
	path('check-incomplete-students/', check_incomplete_students, name='check_incomplete_students'),
	path('raw-result/', raw_results, name='raw_results'),
	path('subject-summary/', sub_summary, name='sub_summary'),
]