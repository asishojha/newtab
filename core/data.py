import csv
from .models import *

PASSING_THEORY_MARKS = {"01":"26",	"02":"26",	"03":"26",	"04":"26",	"05":"26",	"06":"26",	"11":"23",	"12":"23",	"13":"26",	"14":"23",	"15":"26",	"16":"23",	"17":"23",	"18":"23",	"19":"23",	"20":"23",	"21":"26",	"22":"26",	"23":"26",	"24":"26",	"25":"26",	"26":"26",	"27":"23",	"28":"15",	"29":"26",	"30":"26"}

def load_data():
	file_name = input("\nEnter the name of the file (CASE-SENSITIVE): \n")
	compulsory_subject_count = input("\nEnter the number of compulsory subjects required: \n")

	for k, v in PASSING_THEORY_MARKS.items():
		pass_mark, pass_mark_created = PassingMarkSchema.objects.get_or_create(sub=k, passing_marks=v)

	with open(file_name, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		for l in csv_reader:
			school, school_created = School.objects.get_or_create(index = l[1])
			student, student_created = Student.objects.get_or_create(
				school = school,
				name = l[2],
				sex = l[3],
				rlg = l[4],
				cast = l[5],
				fname = l[6],
				mname = l[7],
				yfa = l[8],
				l_roll = l[9],
				dist = l[85],
				sex_1 = l[86],
				ctg = l[87],
				sylb = l[88],
				ct = l[89],
				roll_no = l[90],
				cen = l[91],
				del_ind = l[93],
				reg_no = l[95],
				reg_yr = l[96],
				enr_no = l[97],
				enr_yr = l[98],
				stream = l[99],
				ind_1 = l[100],
				ind_2 = l[101],
				ind = l[102],
				serial = l[103],
			)
			sub_count = 0
			for i in range(1, 8):
				subject, subject_created = Subject.objects.get_or_create(
					subject_code = i, # this will be moved from subject to student table
					sub = l[(9*i) + 1],
					sub_n = l[(9*i) + 2],
				)
				student.subjects.add(subject)
				if l[(9*i) + 1] and l[(9*i) + 1] != '' and sub_count <= int(compulsory_subject_count):
					student.compulsory_subjects.add(subject)
					sub_count += 1

				mark, marks_created = Mark.objects.get_or_create(
					student=student,
					subject=subject,
					tth = l[(9*i) + 3],
					pr = l[(9*i) + 4],
					aw_sub = l[(9*i) + 5],
					ppr_sub = l[(9*i) + 6],
					total_sub = l[(9*i) + 7],
					grade_sub = l[(9*i) + 8],
				)
			student.save()

			result, result_created = Result.objects.get_or_create(student=student)

	return print('Data Load Complete')

