from django.urls import path
from . import views


urlpatterns=[
    #urls for pages
    path('',views.new,name='home'),
    path('home',views.new,name='home'),
    path('Login', views.Login,name='Login'),
    path('index', views.index,name='index'),
    path('FileUpload', views.FileUpload,name='FileUpload'),
    path('MainObjectives', views.MainObjectives,name='MainObjectives'),
    path('DemoObjectives', views.DemoObjectives,name='DemoObjectives'),
    path('PharmObjectives', views.PharmObjectives,name='PharmObjectives'),
    path('OPObjectives', views.OPObjectives,name='OPObjectives'),
    path('DischargeObjectives', views.DischargeObjectives,name='DischargeObjectives'),
    path('ApptObjectives', views.ApptObjectives,name='ApptObjectives'),
    path('BedObjectives', views.BedObjectives,name='BedObjectives'),
    path('DocObjectives', views.DocObjectives,name='DocObjectives'),
    path('MLCObjectives', views.MLCObjectives,name='MLCObjectives'),
    path('SpecObjectives', views.SpecObjectives,name='SpecObjectives'),
    path('WaitObjectives', views.WaitObjectives,name='WaitObjectives'),
    path('WalkInObjectives', views.WalkInObjectives,name='WalkInObjectives'),
    path('WardObjectives', views.WardObjectives,name='WardObjectives'),

    path('NursingStationObjectives',views.NursingStationObjectives,name='NursingStationObjectives'),
    path('OrdersPerPatient',views.OrdersPerPatient,name='OrdersPerPatient'),
    path('TopMovableObjectives',views.TopMovableObjectives,name='TopMovableObjectives'),
    path('DrugStockObjectives',views.DrugStockObjectives,name='DrugStockObjectives'),
    path('Radiology',views.Radiology,name='Radiology'),
    path('SurgeryObjectives',views.SurgeryObjectives,name='SurgeryObjectives'),


    path('InsuranceObjectives',views.InsuranceObjectives,name='InsuranceObjectives'),
    path('GenderObjectives',views.GenderObjectives,name='GenderObjectives'),
    path('AgeObjectives',views.AgeObjectives,name='AgeObjectives'),
    path('ApptDemoObjectives',views.ApptDemoObjectives,name='ApptDemoObjectives'),
    path('WalkinDemoObjectives',views.WalkinDemoObjectives,name='WalkinDemoObjectives'), 
    path('AreaObjectives',views.AreaObjectives,name='AreaObjectives'),




    path('Login',views.Login,name='Login'),
    path('Logout',views.Logout,name='Logout'),

    #urls for Anisha's visualisations
    path('EachWardBed',views.EachWardBed,name='EachWardBed'),
    path('AllWardBed',views.AllWardBed,name='AllWardBed'),
    path('SpecificWardBed',views.SpecificWardBed,name='SpecificWardBed'),
    path('SpecDocBed',views.SpecDocBed,name='SpecDocBed'),
    path('SpecificSpecBed',views.SpecificSpecBed,name='SpecificSpecBed'),
    path('EachDoc',views.EachDoc,name='EachDoc'),
    path('EachSpec',views.EachSpec,name='EachSpec'),
    path('SpecificDocSpecificSpec',views.SpecificDocSpecificSpec,name='SpecificDocSpecificSpec'),
    path('EachWard',views.EachWard,name='EachWard'),
    path('SpecificWardDay',views.SpecificWardDay,name='SpecificWardDay'),
    path('SpecWardSpecSpecSpecDoc',views.SpecWardSpecSpecSpecDoc,name='SpecWardSpecSpecSpecDoc'),
    path('SpecificWardSpecificSpec',views.SpecificWardSpecificSpec,name='SpecificWardSpecificSpec'),

    path('PaymentsFilter',views.paymentsFilter,name='PaymentsFilter'),

    path('MLCWard',views.MLCWard,name='MLCWard'),
    path('MLCSpecialty',views.MLCSpecialty,name='MLCSpecialty'),

    path('DeptAppt',views.DeptAppt,name='DeptAppt'),
    path('DocAppt',views.DocAppt,name='DocAppt'),
    path('DocW',views.DocW,name='DocW'),
    path('DeptW',views.DeptW,name='DeptW'),



    #urls for Amala's visualisations

    path('PharmacyNursingStation_priority', views.pharm_priority,name='PharmacyNursingStation_priority'), 
    path('PharmacyNursingStation_station', views.pharm_station,name='PharmacyNursingStation_station'), 
    path('PharmacyNursingStation_overall', views.pharm_overall,name='PharmacyNursingStation_overall'),

    path('TopMedicines_station', views.topmovable_station,name='TopMedicines_station'), 
    path('TopMedicines_overall', views.topmovable_overall,name='TopMedicines_overall'),

    path('DrugStock_itemcat', views.drugstock_itemcat,name='DrugStock_itemcat'), 
    path('DrugStock_overall', views.drugstock_overall,name='DrugStock_overall'),

    path('Surgery_surgeryname', views.surgeryname,name='Surgery_surgeryname'), 
    path('Surgery_surgerydept', views.surgerydept,name='Surgery_surgerydept')


    #all urls for varsha team

    path('insurancedepartment',views.insurancedepartment,name='insurancedepartment'),
    path('insuranceward',views.insuranceward,name='insuranceward'),
    path('insurancearea',views.insurancearea,name='insurancearea'),


    path('genderdepartment',views.genderdepartment,name='genderdepartment'),
    path('genderward',views.genderward,name='genderward'),
    path('genderarea',views.genderarea,name='genderarea'),
    
    path('agedepartment',views.agedepartment,name='agedepartment'),
    path('ageward',views.ageward,name='ageward'),
    path('agearea',views.agearea,name='agearea'),

    path('appointmentdepartment',views.appointmentdepartment,name='appointmentdepartment'),
    path('appointmentarea',views.appointmentarea,name='appointmentarea'),

    path('walkindepartment',views.walkindepartment,name='walkindepartment'),
    path('walkinarea',views.walkinarea,name='walkinarea'),



]