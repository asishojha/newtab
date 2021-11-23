import csv
from .models import *

SUBJECT_SHORT_CODE = {"":"", "01":"ENGB", "02":"BNGA", "03":"KOK", "04":"HINA", "05":"MIZA", "06":"A", "11":"PHYS", "12":"CHEM", "13":"MATH", "14":"BIOS", "15":"ECON", "16":"CPSC", "17":"GEOY", "18":"STAT", "19":"PSYL", "20":"HOME", "21":"ACCY", "22":"BST", "23":"POLS", "24":"EDCN", "25":"PHIL", "26":"HIST", "27":"NUTN", "28":"MUSE", "29":"SOCY", "30":"SANS"}
PASSING_THEORY_MARKS = {"":"", "01":"26", "02":"26", "03":"26",	"04":"26", "05":"26", "06":"26", "11":"23",	"12":"23", "13":"26", "14":"23", "15":"26", "16":"23", "17":"23", "18":"23", "19":"23",	"20":"23", "21":"26", "22":"26", "23":"26",	"24":"26", "25":"26", "26":"26", "27":"23",	"28":"15", "29":"26", "30":"26"}
PASSING_PRAC_MARKS = {"":"", "01":"7", "02":"7", "03":"7", "04":"7", "05":"7", "06":"7", "11":"10", "12":"10", "13":"7", "14":"10", "15":"7", "16":"10", "17":"10", "18":"10", "19":"10", "20":"10", "21":"7", "22":"7", "23":"7", "24":"7", "25":"7", "26":"7", "27":"10", "28":"18", "29":"7", "30":"7"}
MAX_THEORY_MARKS = {"":"", "01":"80", "02":"80", "03":"80", "04":"80", "05":"80", "06":"80", "11":"70", "12":"70", "13":"80", "14":"70", "15":"80", "16":"70", "17":"70", "18":"70", "19":"70", "20":"70", "21":"80", "22":"80", "23":"80", "24":"80", "25":"80", "26":"80", "27":"70", "28":"45", "29":"80", "30":"80"}
MAX_PRAC_MARKS = {"":"", "01":"20", "02":"20", "03":"20", "04":"20", "05":"20", "06":"20", "11":"30", "12":"30", "13":"20", "14":"30", "15":"20", "16":"30", "17":"30", "18":"30", "19":"30", "20":"30", "21":"20", "22":"20", "23":"20", "24":"20", "25":"20", "26":"20", "27":"30", "28":"55", "29":"20", "30":"20"}

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
			sub_codes = []
			for i in range(1, 8):
				subject, subject_created = Subject.objects.get_or_create(
					sub = l[(9*i) + 1],
					sub_n = SUBJECT_SHORT_CODE[l[(9*i) + 1]],
					passing_th_marks = PASSING_THEORY_MARKS[l[(9*i) + 1]],
					passing_pr_marks = PASSING_PRAC_MARKS[l[(9*i) + 1]],
					max_th_marks = MAX_THEORY_MARKS[l[(9*i) + 1]],
					max_pr_marks = MAX_PRAC_MARKS[l[(9*i) + 1]]
				)
				student.subjects.add(subject)
				if l[(9*i) + 1] and sub_count < int(compulsory_subject_count):
					student.compulsory_subjects.add(subject)
					sub_count += 1
				if l[(9*i) + 1]:
					sub_codes.append(i)

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
				if mark.is_passed_in_tth:
					mark.raw_passed = True
					mark.save()

				for sub in student.compulsory_subjects.all():
					sub_mark = Mark.objects.get(student=student, subject=sub)
					if sub_mark.raw_passed:
						student.all_passed = True
					else:
						student.all_passed = False
						break

			student.subject_codes = ','.join(map(str, sub_codes))
			student.save()

			result, result_created = Result.objects.get_or_create(student=student)

	return print('Data Load Complete')

