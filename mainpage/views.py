
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


import altair as alt
import pandas as pd

import os.path



from mainpage.forms import *
from mainpage.functions.functions import *
# Create your views here.
def new(request):
    return render(request,'Home.html')

def Login(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        password=request.POST["password"]

        user=auth.authenticate(username=uname, password=password)

        if user is not None:    #valid user
            auth.login(request,user)
            return redirect('FileUpload')
        else:                                     #invalid user
            messages.info(request,'Username OR password is incorrect')    
            return redirect('Login')

    else:
        return render(request,'Login.html')

def Logout(request):
    auth.logout(request)
    return redirect('Login')
    

def index(request):
    return render(request,'index.html')

def FileUpload(request):
    mesg=""
    file_names=[]
    form=UploadFileForm()
    if request.method=="POST":
        if "OP Consultation" in request.POST:
            filename="OPConsultation.xlsx"
        elif "Discharge TAT" in request.POST:
            filename="DischargeTAT.xlsx"
        elif "Discharge Analysis" in request.POST:
            filename="DischargeAnalysis.xlsx"
        elif "Doctorwise" in request.POST:
            filename="Doctorwise.xlsx"
        elif "Admission Analysis" in request.POST:
            filename="AdmissionAnalysis.xlsx"
        elif "Pharmacy" in request.POST:
            filename="Pharmacy.xlsx"
        elif "Surgery Analysis" in request.POST:
            filename="SurgeryAnalysis.xlsx"
        elif "Demographic Analysis" in request.POST:
            filename="DemographicAnalysis.xlsx"     
        elif "Radiology" in request.POST:
            filename="Radiology.xlsx"  
        elif "Top 100 Medicines" in request.POST:
            filename="Top100Medicines.xlsx"  
        
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            for x in request.FILES.getlist("file"):
                handle_file(x,filename)
                file_names.append(x.name)
            mesg='Files uploaded successfully'
        else:
            mesg='Files were not uploaded'
    
    return render(request,'FileUpload.html',{'form':form,'mesg':mesg,'fname':file_names})


def MainObjectives(request):
    return render(request,'MainObjectives.html')

def DemoObjectives(request):
    return render(request,'DemoObjectives.html')

def PharmObjectives(request):
    return render(request,'PharmObjectives.html')

def OPObjectives(request):
    return render(request,'OPObjectives.html')

############## Anisha's team   ##########################################################################################

def DischargeObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/DischargeAnalysis.xlsx")==False ):
        message='Discharge Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,'DischargeObjectives.html')

def ApptObjectives(request):
    return render(request,'ApptObjectives.html')

def BedObjectives(request):
    return render(request,'BedObjectives.html')

def DocObjectives(request):
    return render(request,'DocObjectives.html')

def MLCObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/DischargeAnalysis.xlsx")==False ):
        message='Discharge Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,'MLCObjectives.html')

def SpecObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/DischargeAnalysis.xlsx")==False ):
        message='Discharge Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,'SpecObjectives.html')

def WaitObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/OPConsultation.xlsx")==False ):
        message='OP Consultation File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,'WaitObjectives.html')

def WalkInObjectives(request):
    return render(request,'WalkInObjectives.html')

def WardObjectives(request):
    return render(request,'WardObjectives.html')


def EachWardBed(request):
    category='EachWardBed'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=discharges_analysis(category,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})

    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def AllWardBed(request):
    category='AllWardBed'
    form=DateFilter()
    if request.method=="POST":
        
        form=DateFilter(request.POST)
        
        if form.is_valid():
            
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date > to_date):
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
            else:               
                g_json=discharges_analysis(category,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})

    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def SpecificWardBed(request):
    form1=Form3()
    form2=DateFilter()
    if request.method=="POST":
        
        form1=Form3(request.POST)
        form2=DateFilter(request.POST)
        if form1.is_valid() and form2.is_valid():
            wardname=request.POST['wardname']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=specific_discharge_analysis(wardname,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2, 'message':message})

            
    else:
        return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2})


def SpecDocBed(request):
    form1=Form5()
    form2=DateFilter()
    
    if request.method=="POST":
        
        form1=Form5(request.POST)
        form2=DateFilter(request.POST)
        
        if form1.is_valid() and form2.is_valid():
            doctor=request.POST['doctor']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):                
                g_json=spec_doc_bed(doctor,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else: 
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2, 'message':message})
            
    else:
        return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2})



def EachDoc(request):
    category='EachDoc'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=discharges_analysis(category,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def EachSpec(request):
    category='EachSpec'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=discharges_analysis(category,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def SpecificSpecBed(request):
    form1=Form4()
    form2=DateFilter()
    if request.method=="POST":
        form1=Form4(request.POST)
        form2=DateFilter(request.POST)
        if form1.is_valid() and form2.is_valid():
            specialty=request.POST['specialty']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=specific_spec_bed(specialty,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2, 'message':message})
            
    else:
        return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2})


def SpecificDocSpecificSpec(request):
    form1=Form4()
    form2=Form5()
    form3=DateFilter()
    if request.method=="POST":
        form1=Form4(request.POST)
        form2=Form5(request.POST)
        form3=DateFilter(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            doctor=request.POST['doctor']
            specialty=request.POST['specialty']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=spec_doc_and_spec(doctor, specialty, from_date, to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormThree.html', {'form1':form1, 'form2':form2, 'form3':form3, 'message':message})
            
    else:
        return render(request,'FilterFormThree.html', {'form1':form1, 'form2':form2, 'form3':form3})



def EachWard(request):
    category='EachWard'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=discharges_analysis(category,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


def SpecificWardSpecificSpec(request):
    form1=Form3()
    form2=Form4()
    form3=DateFilter()
    if request.method=="POST":
        form1=Form3(request.POST)
        form2=Form4(request.POST)
        form3=DateFilter(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            wardname=request.POST['wardname']
            specialty=request.POST['specialty']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=spec_ward_and_spec(wardname,specialty,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormThree.html', {'form1':form1, 'form2':form2, 'form3':form3, 'message':message})
            
    else:
        return render(request,'FilterFormThree.html', {'form1':form1, 'form2':form2, 'form3':form3})


def SpecWardSpecSpecSpecDoc(request):
    form1=Form3()
    form2=Form4()
    form3=Form5()
    form4=DateFilter()
    if request.method=="POST":
        form1=Form3(request.POST)
        form2=Form4(request.POST)
        form3=Form5(request.POST)
        form4=DateFilter(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            wardname=request.POST['wardname']
            specialty=request.POST['specialty']
            doctor=request.POST['doctor']
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=spec_ward_and_spec_and_doc(wardname,specialty,doctor,from_date,to_date)
                return render(request,'embed.html',{'g':g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormFour.html', {'form1':form1, 'form2':form2, 'form3':form3,'form4':form4, 'message':message})
    else:
        return render(request,'FilterFormFour.html', {'form1':form1, 'form2':form2, 'form3':form3,'form4':form4})

    
def SpecificWardDay(request):
    form=Form3()
    if request.method=="POST":
        form=Form3(request.POST)
        
        if form.is_valid():
            wardname=request.POST['wardname']
            g_json=spec_ward_day(wardname)
            return render(request,'embed.html',{'g':g_json})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def paymentsFilter(request):
    if (os.path.isfile("mainpage/media/fileupload/DischargeAnalysis.xlsx")==False ):
        
        message='Discharge Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    
    payments_analysis()
    return render(request,'OPObjectives.html')

def MLCWard(request):
    category='MLCWard'
    g_json=mlc_analysis(category)
    return render(request, 'embed.html', {'g' : g_json})

def MLCSpecialty(request):
    category='MLCSpecialty'
    g_json=mlc_analysis(category)
    return render(request, 'embed.html', {'g' : g_json})

def DeptAppt(request):
    category='DeptAppt'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=waitingtime_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def DeptW(request):
    category='DeptW'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=waitingtime_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


def DocAppt(request):
    category='DocAppt'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=waitingtime_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
            
    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


def DocW(request):
    category='DocW'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=waitingtime_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})

    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


############## Amala's team   ##########################################################################################

def NursingStationObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/Pharmacy.xlsx")==False ):
        mesg=""
        message='Pharmacy File NOT present ! Please upload the file first.'
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
            
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
        
    return render(request,'NursingStationObjectives.html')

def TopMovableObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/Top100Medicines.xlsx")==False ):
        mesg=""
        message='Top Movable File NOT present ! Please upload the file first.'
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
            
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
        
    return render(request,'TopMovableObjectives.html')
    
def DrugStockObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/Top100Medicines.xlsx")==False ):
        mesg=""
        message='Drugstock File NOT present ! Please upload the file first.'
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
            
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,'DrugStockObjectives.html')

def SurgeryObjectives(request):
    if ((os.path.isfile("mainpage/media/fileupload/SurgeryAnalysis.xlsx") and (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")))==True):
        return render(request,'SurgeryObjectives.html')
    else:
            mesg=""
            message='Surgery or/and Demographic File NOT present ! Please upload the file first.'
            file_names=[]
            form=UploadFileForm()
            if request.method=="POST":
                message=""
                if "OP Consultation" in request.POST:
                    filename="OPConsultation.xlsx"
                elif "Discharge TAT" in request.POST:
                    filename="DischargeTAT.xlsx"
                elif "Discharge Analysis" in request.POST:
                    filename="DischargeAnalysis.xlsx"
                elif "Doctorwise" in request.POST:
                    filename="Doctorwise.xlsx"
                elif "Admission Analysis" in request.POST:
                    filename="AdmissionAnalysis.xlsx"
                elif "Pharmacy" in request.POST:
                    filename="Pharmacy.xlsx"
                elif "Surgery Analysis" in request.POST:
                    filename="SurgeryAnalysis.xlsx"
                elif "Demographic Analysis" in request.POST:
                    filename="DemographicAnalysis.xlsx"     
                elif "Radiology" in request.POST:
                    filename="Radiology.xlsx"  
                elif "Top 100 Medicines" in request.POST:
                    filename="Top100Medicines.xlsx"  
                
                form=UploadFileForm(request.POST,request.FILES)
                if form.is_valid():
                    for x in request.FILES.getlist("file"):
                        handle_file(x,filename)
                        file_names.append(x.name)
                    mesg='Files uploaded successfully'
                else:
                    mesg='Files were not uploaded'
            return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    


def pharm_priority(request):
    category='Priority'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=pharmacyorders_from_nursing_stations_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

        

def pharm_station(request):
    category='OrderingStation'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=pharmacyorders_from_nursing_stations_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def pharm_overall(request):
    category='Overall'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=pharmacyorders_from_nursing_stations_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def OrdersPerPatient(request):
    if (os.path.isfile("mainpage/media/fileupload/Pharmacy.xlsx")==False ):
        mesg=""
        message='Pharmacy File NOT present ! Please upload the file first.'
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
            
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            g_json=pharmacyorders_per_patient_analysis(from_date,to_date)
            return render(request,'embed.html',{'g':g_json})

    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def topmovable_station(request):
    category='Station'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=topmedicines_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def topmovable_overall(request):
    category='Overall'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=topmedicines_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def drugstock_itemcat(request):
    category= 'Item Catagory'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=drugstock_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def drugstock_overall(request):
    category='Overall'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date'] 
            message=""
            if (from_date <= to_date):
                g_json=drugstock_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def Radiology(request):
    if (os.path.isfile("mainpage/media/fileupload/Radiology.xlsx")==False ):
        mesg=""
        message='Radiology File NOT present ! Please upload the file first.'
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
            
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    else:
        form1=Form6()
        form2=DateFilter()
        if request.method=="POST":
            form1=Form6(request.POST)
            form2=DateFilter(request.POST)
            if form1.is_valid() and form2.is_valid():
                test=request.POST['selected_test']
                from_date=request.POST['from_date']
                to_date=request.POST['to_date']
                message=""
                if (from_date <= to_date):
                    g_json=radiology_analysis(test,from_date,to_date)
                    return render(request, 'embed.html', {'g' : g_json, 'message':message})
                else:
                    message="Please ensure from-date falls before to-date."
                    return render(request,'FilterFormTwo.html', {'form1':form1,'form2':form2,'message':message})
        else:
            return render(request,'FilterFormTwo.html', {'form1':form1, 'form2':form2})

def surgeryname(request):
    category= 'Surgery'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=surgery_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def surgerydept(request):
    category= 'Surgery Department'
    form=DateFilter()
    if request.method=="POST":
        form=DateFilter(request.POST)
        if form.is_valid():
            from_date=request.POST['from_date']
            to_date=request.POST['to_date']
            message=""
            if (from_date <= to_date):
                g_json=surgery_analysis(category,from_date,to_date)
                return render(request, 'embed.html', {'g' : g_json, 'message':message})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
    
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


############## Varsha's team   ##########################################################################################

#def demographic(request):   
#    return render(request,'demographic.html')


def InsuranceObjectives(request):
    if (os.path.isfile("mainpage/media/fileupload/AdmissionAnalysis.xlsx")==False ):
        message='Admission Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    return render(request,"InsuranceObjectives.html")

def insurancedepartment(request):
    category='Department'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def insuranceward(request):
    category='Ward'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def insurancearea(request):
    category='Area'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})




def GenderObjectives(request):
    return render(request,"GenderObjectives.html")


def genderdepartment(request):
    if (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False ):
        message='Demographic Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Department'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def genderward(request):
    if (os.path.isfile("mainpage/media/fileupload/AdmissionAnalysis.xlsx")==False ):
        message='Admission Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Ward'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def genderarea(request):
    if (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False ):
        message='Demographic Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Area'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})
    




    
def AgeObjectives(request):
    return render(request,"AgeObjectives.html")

def agedepartment(request):
    if (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False ):
        message='Demographic Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Department'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def ageward(request):
    if (os.path.isfile("mainpage/media/fileupload/AdmissionAnalysis.xlsx")==False ):
        message='Admission Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Ward'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

def agearea(request):
    if (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False ):
        message='Demographic Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Area'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

    
def ApptDemoObjectives(request):
    return render(request,"ApptDemoObjectives.html")

def appointmentdepartment(request):
    if (os.path.isfile("mainpage/media/fileupload/OPConsultation.xlsx")==False ):
        message='OPConsultation File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Department'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})



def appointmentarea(request):
    if ((os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False) or (os.path.isfile("mainpage/media/fileupload/OPConsultation.xlsx")==False)) :
        message=' Please upload the Demographic Analysis file and OPConsultation file for the required time period. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Area'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})

    
def WalkinDemoObjectives(request):
    return render(request,"WalkinDemoObjectives.html")

def walkindepartment(request):
    if (os.path.isfile("mainpage/media/fileupload/OPConsultation.xlsx")==False ):
        message='OPConsultation File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Department'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
            
    else:
        return render(request,'FilterFormOpt.html', {'form':form})



def walkinarea(request):
    if ((os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False) or (os.path.isfile("mainpage/media/fileupload/OPConsultation.xlsx")==False) ):
        message='Please upload the Demographic Analysis file and OPConsultation file for the required time period.'
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    category='Area'
    form=datefilter()
    if request.method=="POST":
        form=datefilter(request.POST)
        if form.is_valid():
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(category,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})


    

def AreaObjectives(request): 
    if (os.path.isfile("mainpage/media/fileupload/DemographicAnalysis.xlsx")==False ):
        message='Demographic Analysis File NOT present ! Please upload the file first. '
        mesg=""
        file_names=[]
        form=UploadFileForm()
        if request.method=="POST":
            message=""
            if "OP Consultation" in request.POST:
                filename="OPConsultation.xlsx"
            elif "Discharge TAT" in request.POST:
                filename="DischargeTAT.xlsx"
            elif "Discharge Analysis" in request.POST:
                filename="DischargeAnalysis.xlsx"
            elif "Doctorwise" in request.POST:
                filename="Doctorwise.xlsx"
            elif "Admission Analysis" in request.POST:
                filename="AdmissionAnalysis.xlsx"
            elif "Pharmacy" in request.POST:
                filename="Pharmacy.xlsx"
            elif "Surgery Analysis" in request.POST:
                filename="SurgeryAnalysis.xlsx"
            elif "Demographic Analysis" in request.POST:
                filename="DemographicAnalysis.xlsx"     
            elif "Radiology" in request.POST:
                filename="Radiology.xlsx"  
            elif "Top 100 Medicines" in request.POST:
                filename="Top100Medicines.xlsx"  
        
            form=UploadFileForm(request.POST,request.FILES)
            if form.is_valid():
                for x in request.FILES.getlist("file"):
                    handle_file(x,filename)
                    file_names.append(x.name)
                mesg='Files uploaded successfully'
            else:
                mesg='Files were not uploaded'
        return render(request,'FileUpload.html', {'form':form,'mesg':mesg,'fname':file_names,'message':message})
    form=areaform()
    if request.method=="POST":
        form=areaform(request.POST)
        if form.is_valid():
            department=request.POST['department']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            message=""
            if (start_date <= end_date):
                g_json=insurance_analysis(department,start_date,end_date)
                return render(request,'embed.html',{'g':g_json})
            else:
                message="Please ensure from-date falls before to-date."
                return render(request,'FilterFormOpt.html', {'form':form, 'message':message})
           
           
    else:
        return render(request,'FilterFormOpt.html', {'form':form})






















