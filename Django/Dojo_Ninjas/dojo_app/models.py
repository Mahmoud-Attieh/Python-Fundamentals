from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=15)
    

class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.DO_NOTHING)

def create_dojo():
    Dojo.objects.create(first_name = "Mahmoud", city ="Ramallah" , state = "WB" )
    Dojo.objects.create(first_name = "Shireen", city ="Ramallah" , state = "WB" )
    Dojo.objects.create(first_name = "Ahmad", city ="Ramallah" , state = "WB" )
    


