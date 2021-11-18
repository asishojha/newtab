# Generated by Django 3.2.9 on 2021-11-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('sex', models.CharField(max_length=1)),
                ('rlg', models.CharField(max_length=1)),
                ('cast', models.CharField(max_length=2, null=True)),
                ('fname', models.CharField(max_length=35, null=True)),
                ('mname', models.CharField(max_length=35, null=True)),
                ('yfa', models.CharField(max_length=2)),
                ('l_roll', models.CharField(max_length=15, null=True)),
                ('dist', models.CharField(max_length=6)),
                ('sex_1', models.CharField(max_length=2)),
                ('ctg', models.CharField(max_length=8)),
                ('sylb', models.CharField(max_length=3)),
                ('ct', models.CharField(max_length=1, null=True)),
                ('roll_no', models.CharField(max_length=12)),
                ('cen', models.CharField(max_length=2)),
                ('del_ind', models.CharField(max_length=1, null=True)),
                ('reg_no', models.CharField(max_length=5)),
                ('reg_yr', models.CharField(max_length=4)),
                ('enr_no', models.CharField(max_length=10)),
                ('enr_yr', models.CharField(max_length=4)),
                ('stream', models.CharField(max_length=1)),
                ('ind_1', models.CharField(max_length=1, null=True)),
                ('ind_2', models.CharField(max_length=1, null=True)),
                ('ind', models.CharField(max_length=1, null=True)),
                ('serial', models.CharField(max_length=6, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.school')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=1)),
                ('sub', models.CharField(max_length=2)),
                ('sub_n', models.CharField(max_length=4)),
                ('compulsory', models.CharField(max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'unique_together': {('student', 'sub', 'sub_n')},
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_tot', models.CharField(max_length=2, null=True)),
                ('we_gr', models.CharField(max_length=2, null=True)),
                ('env', models.CharField(max_length=2, null=True)),
                ('aggr', models.CharField(max_length=3, null=True)),
                ('status', models.CharField(max_length=1, null=True)),
                ('div', models.CharField(max_length=1, null=True)),
                ('ex_code', models.CharField(max_length=1, null=True)),
                ('ab_code', models.CharField(max_length=1, null=True)),
                ('in_code', models.CharField(max_length=1, null=True)),
                ('comp_1', models.CharField(max_length=1, null=True)),
                ('comp_2', models.CharField(max_length=1, null=True)),
                ('ovgr', models.CharField(max_length=2, null=True)),
                ('crt_no', models.CharField(max_length=5, null=True)),
                ('marksheet_no', models.CharField(max_length=5, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tth', models.CharField(max_length=3, null=True)),
                ('pr', models.CharField(max_length=3, null=True)),
                ('aw_sub', models.CharField(max_length=2, null=True)),
                ('ppr_sub', models.CharField(max_length=2, null=True)),
                ('total_sub', models.CharField(max_length=3, null=True)),
                ('grade_sub', models.CharField(max_length=2, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
