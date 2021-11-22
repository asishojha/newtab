from django.shortcuts import render
from django.http import HttpResponse #temporary
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

	passed_count = 0
	stram1_passed_count = 0
	stram2_passed_count = 0
	stram3_passed_count = 0
	
	for student in appeared_students:
		countx = 0
		for m in student.mark_set.exclude(tth='AB').filter(subject__compulsory='c'):
			if m.is_passed_in_tth:
				countx += 1
		if countx == 5 :
			passed_count+=1
			if student.stream == '1':
				stram1_passed_count += 1
			elif student.stream == '2':
				stram2_passed_count += 1
			elif student.stream == '3':
				stram3_passed_count += 1

	print('Total Passed Students: ', passed_count)
	print('Total Appeared Students :', appeared_student_count)

	print('Stream One Passed Students: ', stram1_passed_count)
	print('Stream One Appeared Students :', stream1_appeared_student_count)

	print('Stream Two Passed Students: ', stram2_passed_count)
	print('Stream Two Appeared Students :', stream2_appeared_student_count)

	print('Stream Three Passed Students: ', stram3_passed_count)
	print('Stream Three Appeared Students :', stream3_appeared_student_count)
	return HttpResponse('Trial Going on')

def sub_summary(request):

	# sbj_appeared = Subject.objects.values('sub').annotate(count = Count('sub'))
	# sbj_passed = 0

	# for mark in Mark.objects.all():
	# 	sub_passed = Subject.objects.annotate(numpassed=Count(Case(When(mark__tth__gte=passing_marks, then=1), output_field=IntegerField(),)))
	# return sub_passed
	pass

	# needs to be re designed