from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=15)
    

class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.DO_NOTHING)
    
def createDojo(request):
    Dojo.objects.create(name=request.POST["dojo_name"],city=request.POST["city"],state=request.POST["state"])
    

def createNinja(request):
    return Ninja.objects.create(first_name=request.POST['ninjaname'],last_name=request.POST['lname'], dojo=Dojo.objects.get(id=request.POST['seldojo']))  
    
def display():
    return Dojo.objects.all()

def show():
    return Ninja.objects.all()