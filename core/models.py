from django.db import models

class School(models.Model):
	index = models.CharField(max_length=5, null=True)

	def __str__(self):
		return self.index

class Subject(models.Model):
	sub = models.CharField(max_length=2, null=True)
	sub_n = models.CharField(max_length=4, null=True)
	passing_th_marks = models.CharField(max_length=3)
	passing_pr_marks = models.CharField(max_length=2, null=True)
	max_th_marks = models.CharField(max_length=2, null=True)
	max_pr_marks = models.CharField(max_length=2, null=True)

	def __str__(self):
		return self.sub

class Student(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	name = models.CharField(max_length=35)
	sex = models.CharField(max_length=1)
	rlg = models.CharField(max_length=1)
	cast = models.CharField(max_length=2, null=True)
	fname = models.CharField(max_length=35, null=True)
	mname = models.CharField(max_length=35, null=True)
	yfa = models.CharField(max_length=2)
	l_roll = models.CharField(max_length=15, null=True)
	dist = models.CharField(max_length=6)
	sex_1 = models.CharField(max_length=2)
	ctg = models.CharField(max_length=8)
	sylb = models.CharField(max_length=3)
	ct = models.CharField(max_length=1, null=True)
	roll_no = models.CharField(max_length=12)
	cen = models.CharField(max_length=2)
	del_ind = models.CharField(max_length=1, null=True)
	reg_no = models.CharField(max_length=5)	
	reg_yr = models.CharField(max_length=4)	
	enr_no = models.CharField(max_length=10)	
	enr_yr = models.CharField(max_length=4)	
	stream = models.CharField(max_length=1)
	ind_1 = models.CharField(max_length=1, null=True)
	ind_2 = models.CharField(max_length=1, null=True)
	ind = models.CharField(max_length=1, null=True)
	serial = models.CharField(max_length=6, null=True)
	subjects = models.ManyToManyField(Subject, related_name='subjects')
	compulsory_subjects = models.ManyToManyField(Subject, related_name='compulsory_subjects')
	subject_codes = models.CharField(max_length=50)

	def __str__(self):
		return self.school.index + ' ' + self.name + '(' + self.roll_no + ')'

class Mark(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	tth = models.CharField(max_length=3, null=True)
	pr = models.CharField(max_length=3, null=True)
	aw_sub = models.CharField(max_length=2, null=True)
	ppr_sub = models.CharField(max_length=2, null=True)
	total_sub = models.CharField(max_length=3, null=True)
	grade_sub = models.CharField(max_length=2, null=True)

	class Meta:
		unique_together = (('student', 'subject'), )

	def __str__(self):
		return self.student.roll_no + ' - ' + self.subject.subject_code

	@property
	def is_passed_in_tth(self):
		if self.tth != 'AB':
			return int(self.tth) >= int(PASSING_THEORY_MARKS[self.subject.sub])
		return False

class Result(models.Model):
	student = models.OneToOneField(Student, on_delete=models.CASCADE, unique=True)
	we_tot = models.CharField(max_length=2, null=True) 
	we_gr = models.CharField(max_length=2, null=True)
	env = models.CharField(max_length=2, null=True)
	aggr = models.CharField(max_length=3, null=True)
	status = models.CharField(max_length=1, null=True)
	div = models.CharField(max_length=1, null=True)
	ex_code = models.CharField(max_length=1, null=True)
	ab_code = models.CharField(max_length=1, null=True)
	in_code = models.CharField(max_length=1, null=True)
	comp_1 = models.CharField(max_length=1, null=True)
	comp_2 = models.CharField(max_length=1, null=True)
	ovgr = models.CharField(max_length=2, null=True)
	crt_no = models.CharField(max_length=5, null=True)	
	marksheet_no = models.CharField(max_length=5, null=True)

	def __str__(self):
		return self.student.roll_no