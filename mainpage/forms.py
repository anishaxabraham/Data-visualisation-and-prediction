from django import forms
import pandas as pd

class DateInput(forms.DateInput):
    input_type='date'


class UploadFileForm(forms.Form):    
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True,'class' : 'myfieldclass'}))
    
class DischargesFilter(forms.Form):
    category = forms.ChoiceField(choices = [  ("Ward", "Ward"),("Specialty","Specialty")])


class DateFilter(forms.Form):
    from_date = forms.DateField(widget=DateInput(),label='From Date', input_formats=['%Y-%m-%d'])     #date field to choose from-date
    to_date = forms.DateField(widget=DateInput(),label='To Date', input_formats=['%Y-%m-%d'])   #date field to choose to-date
    
class MLCFilter(forms.Form):
    category = forms.ChoiceField(choices = [  ("Ward", "Ward"),("Specialty","Specialty")])

class WaitingTimeFilter(forms.Form):
    category = forms.ChoiceField(choices = [  ("Docwise-Walkins", "Docwise-Walkins"),("Deptwise-Walkins","Deptwise-Walkins"),("Docwise-Appointments", "Docwise-Appointments"),("Deptwise-Appointments","Deptwise-Appointments")])

class Form3(forms.Form):
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    df=df.drop_duplicates(subset=['Ward Name'])
    df1=pd.DataFrame()
    df1['Ward Name']=df['Ward Name']
    Choice3=[]
    for i,row in df1.iterrows():
        s=df1.loc[i,'Ward Name']
        Choice3.append((s,s))
    Choice3.sort()
    wardname = forms.ChoiceField(choices = Choice3)
   

class Form4(forms.Form):
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    df=df.drop_duplicates(subset=['Primary doctor Specialty'])
    df1=pd.DataFrame()
    df1['Primary doctor Specialty']=df['Primary doctor Specialty']
    Choice4=[]
    for i,row in df1.iterrows():
        s=df1.loc[i,'Primary doctor Specialty']
        Choice4.append((s,s))
    Choice4.sort()
    specialty = forms.ChoiceField(choices = Choice4)

class Form5(forms.Form):
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    df=df.drop_duplicates(subset=['Primary doctor'])
    df1=pd.DataFrame()
    df1['Primary doctor']=df['Primary doctor']
    Choice5=[]
    for i,row in df1.iterrows():
        s=df1.loc[i,'Primary doctor']
        Choice5.append((s,s))
    Choice5.sort()
    doctor = forms.ChoiceField(choices = Choice5)
    





class Form6(forms.Form):
    df=pd.read_excel("mainpage/static/fileupload/Radiology.xlsx",usecols=['RegistrationNo','sex', 'Age','Item Name',"Bill Datetime"],engine='openpyxl')
    df=df.dropna()
    options=df['Item Name'].unique()
    Choice6=[]
    for c in options:
        Choice6.append((c,c))
    Choice6.sort()
    selected_test= forms.ChoiceField(choices = Choice6)

