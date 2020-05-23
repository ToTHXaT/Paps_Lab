from django.db import models

class Department(models.Model):
    
    name = models.CharField(max_length = 200)
    sub_dep_count = models.IntegerField()

    sup_dep = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"[{self.name}]"

class Worker(models.Model):

    fio = models.CharField(max_length = 200)
    department = models.CharField(max_length = 100)

    login = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return f"<{self.fio} from {self.department}>"

class Client(models.Model):

    pass_id = models.IntegerField(unique=True)
    fio = models.CharField(max_length = 200)
    info = models.CharField(max_length = 500)

    def __str__(self):
        return f"{self.fio} : {self.pass_id}"


class AccessRights(models.Model):
    time_constrait = models.DateTimeField()
    count_constrait = models.IntegerField()

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='pass_id', null=True)

    def __str__(self):
        return f"Access right for {self.client} on {self.department}"




class Report(models.Model):

    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    data = models.TextField()

    def __str__(self):
        return f"Report by {self.worker}\n{self.data}"
