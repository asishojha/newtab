from django.shortcuts import render
from django.http import HttpResponse #temporary
from django.db.models import Count, Case, When, IntegerField
from .models import *

def index(request):
	pass

def check_absent_students(request):
	students = Student.objects.all()
	for student in students:
		student_subject_count = Subject.objects.filter(student=student).exclude(sub='').exclude(sub=None).count()
		student_tth_absent_count = Mark.objects.filter(student=student, tth='AB').count()
		if student_subject_count == student_tth_absent_count:
			student.result.ab_code = '4'
		elif student_tth_absent_count > 0 and student_subject_count != student_tth_absent_count:
			student.result.ab_code = '5'
		else:
			student.result.ab_code = None
		student.result.save()
	return HttpResponse('Absent check Complete')

def check_incomplete_students(request):
	students = Student.objects.all()
	for student in students:
		student_tth_inc_count = Mark.objects.exclude(subject__sub='').filter(student=student, tth=None).count()
		if student_tth_inc_count > 0:
			student.result.in_code = 1
			student.result.save()
	return HttpResponse('Incomplete Check Complete')

def raw_results(request):
	appeared_students = Student.objects.exclude(result__ex_code__in = [1,2,3])
	appeared_student_count = appeared_students.count()
	
	stream1_appeared_students = appeared_students.filter(stream='1')
	stream1_appeared_student_count = stream1_appeared_students.count()
	stream2_appeared_students = appeared_students.filter(stream='2')
	stream2_appeared_student_count = stream2_appeared_students.count()
	stream3_appeared_students = appeared_students.filter(stream='3')
	stream3_appeared_student_count = stream3_appeared_students.count()

	passed_count = appeared_students.filter(all_passed=True).count()
	stream1_passed_count = appeared_students.filter(all_passed=True, stream='1').count()
	stream2_passed_count = appeared_students.filter(all_passed=True, stream='2').count()
	stream3_passed_count = appeared_students.filter(all_passed=True, stream='3').count()

	print('Total Passed Students', passed_count)
	print('Total Appeared Students :', appeared_student_count)

	print('Stream One Passed Students: ', stream1_passed_count)
	print('Stream One Appeared Students :', stream1_appeared_student_count)

	print('Stream Two Passed Students: ', stream2_passed_count)
	print('Stream Two Appeared Students :', stream2_appeared_student_count)

	print('Stream Three Passed Students: ', stream3_passed_count)
	print('Stream Three Appeared Students :', stream3_appeared_student_count)
	return HttpResponse('Trial Going on')

def sub_summary(request):
	sbj_appeared = Mark.objects.values('subject__sub').annotate(appeared_count=Count('subject__sub'))
	sbj_passed = Mark.objects.values('subject__sub').annotate(passed_count=Count(Case(When(raw_passed=True, then=1), output_field=IntegerField(),)))

	print('sbj_appeared\n', sbj_appeared)
	print('sbj_passed\n', sbj_passed)

	return HttpResponse('Subject Summaries')

