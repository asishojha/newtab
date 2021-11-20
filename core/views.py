from django.shortcuts import render
from django.http import HttpResponse #temporary
from .models import *

PASSING_THEORY_MARKS = {
	"01":"26",
	"02":"26",
	"03":"26",
	"04":"26",
	"05":"26",
	"06":"26",
	"11":"23",
	"12":"23",
	"13":"26",
	"14":"23",
	"15":"26",
	"16":"23",
	"17":"23",
	"18":"23",
	"19":"23",
	"20":"23",
	"21":"26",
	"22":"26",
	"23":"26",
	"24":"26",
	"25":"26",
	"26":"26",
	"27":"23",
	"28":"15",
	"29":"26",
	"30":"26"
}

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
		# student_subject_count = Subject.objects.filter(student=student).exclude(sub='').exclude(sub=None).count()
		student_tth_inc_count = Mark.objects.exclude(subject__sub='').filter(student=student, tth=None).count()
		if student_tth_inc_count > 0:
			student.result.in_code = 1
			student.result.save()
	return HttpResponse('Incomplete Check Complete')


def raw_results(request):
	students = Student.objects.all()
	appeared_student_count = students.exclude(result__ex_code__in = [1,2,3]).count()

	eligible_students = Student.objects.exclude(subject__sub='').count()
	# eligible_students = Subject.objects.exclude(sub='').exclude(sub=None).values_list('student', flat=True).distinct()
	print(eligible_students)

	# passed_count = 0

	# for student in students:
	# 	# student_subject_count = Subject.objects.filter(student=student).exclude(sub='').exclude(sub=None).count()

	# 	passed_count1 = 0

	# 	for m in student.mark_set.all():

	# 		if m.subject.sub != '' and m.subject.sub is not None and m.tth != 'AB' and m.tth != '' and m.tth is not None and m.tth >= PASSING_THEORY_MARKS[m.subject.sub]:
	# 			print(m.tth)
	# 			print(PASSING_THEORY_MARKS[m.subject.sub])
	# 			passed_count1 += 1
	# 		else:
	# 			continue

	# 	if passed_count1 == 5:
	# 		passed_count += 1

	# 	# print('Student Passed Count', passed_count1)

	# print('student_count', appeared_student_count)
	# print('passed_count', passed_count)

	return HttpResponse('Trial Going on')