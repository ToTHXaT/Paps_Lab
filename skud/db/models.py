from django.db import models

class Department(models.Model):
    
    name = models.CharField(max_length = 200)
    sub_dep_count = models.IntegerField()

    sup_dep = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)


class Worker(models.Model):

    fio = models.CharField(max_length = 200)
    department = models.CharField(max_length = 100)

    login = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)


class Client(models.Model):

    pass_id = models.IntegerField()
    fio = models.CharField(max_length = 200)
    info = models.CharField(max_length = 500)


class AccessRights(models.Model):
    time_constrait = models.DateTimeField()
    count_constrait = models.IntegerField()

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)



class Report(models.Model):

    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    data = models.TextField()
