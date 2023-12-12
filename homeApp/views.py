from django.shortcuts import render, redirect
from homeApp.models import AbountUs, ServiceSumarry, SkillLevel, Testmonials, ProjectExperience, WorkExperience, Skill, Education, Service, PortfolioCategory, Portfolio

# Create your views here.
def home(request):
    aboutMe = AbountUs.objects.all()[0]
    service_summary = ServiceSumarry.objects.all()[0]
    skill_level = SkillLevel.objects.all()
    testmonials = Testmonials.objects.all()
    projects = ProjectExperience.objects.all()
    work = WorkExperience.objects.all()
    skill = Skill.objects.all()
    education = Education.objects.all()
    service = Service.objects.all()
    category = PortfolioCategory.objects.all()
    portfolio = Portfolio.objects.all()
    
    context ={
        'aboutMe':aboutMe,
        'service_summary':service_summary,
        'skill_level':skill_level,
        'testmonials':testmonials,
        'projects':projects,
        'work':work,
        'skill':skill,
        'education':education,
        'service':service,
        'category':category,
        'portfolio':portfolio,
        }
    return render(request, 'home.html', context)


def ViewPorfolio (request, id):
    viewPortfolio = Portfolio.objects.get(id=id)        
    return render(request, 'ViewProject.html', context={"viewPortfolio":viewPortfolio})
    