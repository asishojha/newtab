import csv
from .models import *


def load_data():
	file_name = input("\nEnter the name of the file (CASE-SENSITIVE): \n")
	compulsory_subject_count = input("\nEnter the number of compulsory subjects required: \n")

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
				if l[(9*i) + 1] and l[(9*i) + 1] != '' and sub_count <= int(compulsory_subject_count):
					compulsory = 'c'
					sub_count += 1
				else:
					compulsory = l[(9*i) + 9]
				subject, subject_created = Subject.objects.get_or_create(
					student = student,
					subject_code = i,
					sub = l[(9*i) + 1],
					sub_n = l[(9*i) + 2],
					compulsory = compulsory,
				)
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

			result, result_created = Result.objects.get_or_create(student=student)

	return print('Data Load Complete')

