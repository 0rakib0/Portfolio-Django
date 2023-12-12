from django.db import models

# Create your models here.

class AbountUs(models.Model):
    image = models.ImageField(upload_to='profile-pic')
    name = models.CharField(max_length=240)
    email = models.EmailField()
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=150)
    age = models.CharField(max_length=5)
    designation = models.CharField(max_length=120)
    aboutMe = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class ServiceSumarry(models.Model):
    happyClient = models.IntegerField()
    complateProjects = models.IntegerField()
    HourseOfSupport = models.IntegerField()
    awards = models.IntegerField()
    
    
class SkillLevel(models.Model):
    skillName = models.CharField(max_length=160)
    skillParsent = models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.skillName


class Testmonials(models.Model):
    clientPic = models.ImageField(upload_to='client_profile')
    clientName = models.CharField(max_length=160)
    clientDesignation = models.CharField(max_length=160)
    testMonials = models.TextField()
    
    def __str__(self) -> str:
        return self.clientName
    
    
class ProjectExperience(models.Model):
    projectName = models.CharField(max_length=500)
    aboutProject = models.TextField()
    usesTecknology = models.CharField(max_length=500)
    sourceCode = models.URLField()
    
    
    def __str__(self) -> str:
        return self.projectName
class WorkExperience(models.Model):
    rol = models.CharField(max_length=260)
    companyName = models.CharField(max_length=260)
    joinDate = models.DateField()
    regineDate = models.DateField(blank=True, null=True)
    aboutExperience = models.TextField()

    def __str__(self) -> str:
        return self.rol
    

class Education(models.Model):
    degree = models.CharField(max_length=260)
    instituteName = models.CharField(max_length=260)
    duration = models.CharField(max_length=160)
    aboutEducation = models.TextField()


    def __str__(self) -> str:
        return self.instituteName

class Skill(models.Model):
    skillName = models.CharField(max_length=160)
    

    def __str__(self) -> str:
        return self.skillName
    
    
class Service(models.Model):
    serviceName = models.CharField(max_length=160)
    serviceIcon = models.CharField(max_length=260)
    aboutService = models.TextField()
    
    def __str__(self):
        return self.serviceName
    
    
class PortfolioCategory(models.Model):
    categoryName = models.CharField(max_length=160)
    
    def __str__(self) -> str:
        return self.categoryName

class Portfolio(models.Model):
    profolioCategory      = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    projectName           = models.CharField(max_length=260)
    projectImage          = models.ImageField(upload_to='portfolio-pic')
    projectLongImage      = models.ImageField(upload_to='portfolio-pic')
    projectType           = models.CharField(max_length=160)
    projectDetails        = models.TextField()
    usedTecnology         = models.CharField(max_length=500)
    projectFeature1       = models.CharField(max_length=360)
    projectFeature2       = models.CharField(max_length=360)
    projectFeature3       = models.CharField(max_length=360)
    projectFeature4       = models.CharField(max_length=360)
    projectSourceCodeLink = models.CharField(max_length=260, null=True, blank=True)
    projectLiveLink       = models.CharField(max_length=260, null=True, blank=True)

    
    
    def __str__(self) -> str:
        return self.projectName
    
    


    
