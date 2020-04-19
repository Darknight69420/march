from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.core.mail import send_mail
from emails.models import Employee, Staff_Position


def home(request):

    return render(request, 'home.html')

def Initial_Report(request):

    #Gets the noc and customer services email addresses
    noc_emails = Employee.objects.exclude(Position__Position__contains='Customer').values_list('Email', flat=True)
    cs_emails = Employee.objects.filter(Position__Position__contains = 'Customer').values_list('Email', flat=True)

    noc_message = ('Initial Outage Report', 'This is a new outage report ,The information is in the document', 'from@example.com', noc_emails)
    cs_message = ('Initial Outage Report', 'This is a new outage report ,The information is in the document', 'from@example.com', cs_emails)
    send_mass_mail((noc_message,cs_message), fail_silently=False)

    return render(request,'InitialReport.html')
        


def Update_Report(request):

    noc_emails = Employee.objects.exclude(Position__Position__contains='Customer').values_list('Email', flat=True)
    cs_emails = Employee.objects.filter(Position__Position__contains = 'Customer').values_list('Email', flat=True)

    noc_message = ('Updated Outage Report', 'This is an updated outage report, The information is in the document', 'from@example.com', noc_emails)
    cs_message = ('Updated Outage Report', 'This is an updated outage report, The information is in the document', 'from@example.com', cs_emails)
    send_mass_mail((noc_message,cs_message), fail_silently=False)
    
    return render(request,'UpdateReport.html')

def Closing_Report(request):

    noc_emails = Employee.objects.exclude(Position__Position__contains='Customer').values_list('Email', flat=True)
    cs_emails = Employee.objects.filter(Position__Position__contains = 'Customer').values_list('Email', flat=True)

    noc_message = ('Closing Outage Report', 'This is the final outage report, The outage has been fixed,  The information is in the document', 'from@example.com', noc_emails)
    cs_message = ('Closing Outage Report', 'This is the final outage report, The outage has been fixed,  The information is in the document', 'from@example.com', cs_emails)
    send_mass_mail((noc_message,cs_message), fail_silently=False)
    
    return render(request,'ClosingReport.html')