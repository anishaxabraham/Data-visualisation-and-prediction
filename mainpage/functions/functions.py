
import altair as alt
from altair.vegalite.v4.schema.core import JsonDataFormat
import pandas as pd
from altair import datum
from django.shortcuts import render
import re
import numpy as np

def handle_file(f,filename):
    with open('mainpage/media/fileupload/'+filename,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#######    Anisha's team    ################################################################################################

def waitingtime_analysis(category, start_date, end_date):
    if category=="DocW":
        import pandas as pd;
        import altair as alt;
        import matplotlib.pyplot as plt
        import numpy as np
        import re;
        import itertools
        from cmath import rect, phase
        from math import radians, degrees
            
        alt.data_transformers.disable_max_rows()

        df = pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx", sheet_name='WalkInOPConsultation', engine='openpyxl')
        df=df.rename(columns={"Doctor Name": "DoctorName","BillingTime":'Bill Time',"Consultation start Date/Time":"Consult IN"})
        df['date']=pd.to_datetime(df['Consult IN']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]
        if(len(df)!=0):
            docList= df['DoctorName'].values.tolist()
            billList= df['Bill Time'].values.tolist()
            inList= df['Consult IN'].values.tolist()

            #time difference list
            df['diff_seconds'] =df['Consult IN']-df['Bill Time']
            df['diff_seconds']=df['diff_seconds']/np.timedelta64(1,'s')
            diffList=df['diff_seconds'].values.tolist()
            #print(diffList)


            #getting unique values for dept
            unique_doc = []
            for x in docList:
                # check if exists in unique_list or not
                if x not in unique_doc:
                    unique_doc.append(x)
                
            # making dept time total
            counter=0;
            DAvgList=[]
            a=0

            for i in range(len(unique_doc)):
                counter=0
                a=0
                for j in range(len(docList)):
                    if(unique_doc[i]==docList[j]):
                        a=a+diffList[j]
                        counter=counter+1
                        #print("Nice")
                DAvgList.append((a/counter)/3600)



            df2 = pd.DataFrame(list(zip(unique_doc, DAvgList)),
                    columns =['DName', 'AVG'])
       

            bars=alt.Chart(df2,title="Average Waiting time for Each Department(Walkins)", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
            color=alt.value('#5B9AA0'),
            tooltip = [alt.Tooltip('DName'),
                    alt.Tooltip('AVG')]
        
            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Waiting time for Walk-Ins", width=400,height=1500

            )

            g_json=bars.to_json()
            return g_json

    elif category=="DeptW":
        import altair as alt
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import re;
        import itertools
        from cmath import rect, phase
        from math import radians, degrees
        alt.data_transformers.disable_max_rows()
            
        df = pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx", sheet_name='WalkInOPConsultation', engine='openpyxl')
        df=df.rename(columns={"Doctor Name": "DoctorName","BillingTime":'Bill Time',"Consultation start Date/Time":"Consult IN","Speciality":"Dept Name"})
        
        df['date']=pd.to_datetime(df['Consult IN']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]
        if(len(df)!=0):
            deptList= df['Dept Name'].values.tolist()
            billList= df['Bill Time'].values.tolist()
            inList= df['Consult IN'].values.tolist()

            #time difference list
            df['diff_seconds'] =df['Consult IN']-df['Bill Time']
            df['diff_seconds']=df['diff_seconds']/np.timedelta64(1,'s')
            diffList=df['diff_seconds'].values.tolist()
            #print(diffList)


            #getting unique values for dept
            unique_dept = []
            for x in deptList:
                # check if exists in unique_list or not
                if x not in unique_dept:
                    unique_dept.append(x)
                
            # making dept time total
            counter=0;
            DAvgList=[]
            a=0

            for i in range(len(unique_dept)):
                counter=0
                a=0
                for j in range(len(deptList)):
                    if(unique_dept[i]==deptList[j]):
                        a=a+diffList[j]
                        counter=counter+1
                        #print("Nice")
                DAvgList.append((a/counter)/3600)

        

            df2 = pd.DataFrame(list(zip(unique_dept, DAvgList)),
                    columns =['DName', 'AVG'])
        

            bars=alt.Chart(df2,title="Average Waiting time for Each Department(Walkins)", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis(title='Department Name')),
            color=alt.value('#E06377'),
            tooltip = [alt.Tooltip('DName'),
                    alt.Tooltip('AVG')]
        
            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Waiting time for Walk-Ins", width=400,height=800

            )
        
            g_json=bars.to_json()
            return g_json


    elif category=="DocAppt":
        import altair as alt
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import re;
        import itertools
        from cmath import rect, phase
        from math import radians, degrees
        alt.data_transformers.disable_max_rows()
            
        df = pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx", sheet_name='WithAppointmentOP', engine='openpyxl' )
        #df=df.rename(columns={"Doctor Name": "DoctorName","Billing Time":"'Bill Time","Consultation start Date/Time":"Consult IN"})
        
        df['date']=pd.to_datetime(df['Consultation start Date/Time']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]

        if(len(df)!=0):

            docList= df['Doctor Name'].values.tolist()
            billList= df['BillingTime'].values.tolist()
            inList= df['Consultation start Date/Time'].values.tolist()

            #time difference list
            df['diff_seconds'] =df['Consultation start Date/Time']-df['BillingTime']
            df['diff_seconds']=df['diff_seconds']/np.timedelta64(1,'s')
            diffList=df['diff_seconds'].values.tolist()
            #print(diffList)


            #getting unique values for dept
            unique_doc = []
            for x in docList:
                # check if exists in unique_list or not
                if x not in unique_doc:
                    unique_doc.append(x)
                
            # making dept time total
            counter=0;
            DAvgList=[]
            a=0

            for i in range(len(unique_doc)):
                counter=0
                a=0
                for j in range(len(docList)):
                    if(unique_doc[i]==docList[j]):
                        a=a+diffList[j]
                        counter=counter+1
                        #print("Nice")
                DAvgList.append((a/counter)/3600)



            df2 = pd.DataFrame(list(zip(unique_doc, DAvgList)),
                    columns =['DName', 'AVG'])


            bars=alt.Chart(df2,title="Average Waiting time for Each Department(Appointments)", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
            color=alt.value('#FF6361'),
            tooltip = [alt.Tooltip('DName'),
                    alt.Tooltip('AVG')]
        
            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Waiting time for Appointments", width=400,height=1500

            )
            g_json=bars.to_json()
            return g_json
   
    else:
        

        import altair as alt
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import re;
        import itertools
        from cmath import rect, phase
        from math import radians, degrees
            
        alt.data_transformers.disable_max_rows()
        df = pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx", sheet_name='WithAppointmentOP', engine='openpyxl')
        df=df.rename(columns={"Speciality":"Dept Name"})
        
        df['date']=pd.to_datetime(df['Consultation start Date/Time']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]

        if(len(df)!=0):
            deptList= df['Dept Name'].values.tolist()
            billList= df['BillingTime'].values.tolist()
            inList= df['Consultation start Date/Time'].values.tolist()

            #time difference list
            df['diff_seconds'] =df['Consultation start Date/Time']-df['BillingTime']
            df['diff_seconds']=df['diff_seconds']/np.timedelta64(1,'s')
            diffList=df['diff_seconds'].values.tolist()
            #print(diffList)


            #getting unique values for dept
            unique_dept = []
            for x in deptList:
                # check if exists in unique_list or not
                if x not in unique_dept:
                    unique_dept.append(x)
                
            # making dept time total
            counter=0;
            DAvgList=[]
            a=0

            for i in range(len(unique_dept)):
                counter=0
                a=0
                for j in range(len(deptList)):
                    if(unique_dept[i]==deptList[j]):
                        a=a+diffList[j]
                        counter=counter+1
                        #print("Nice")
                DAvgList.append((a/counter)/3600)

        

            df2 = pd.DataFrame(list(zip(unique_dept, DAvgList)),
                    columns =['DName', 'AVG'])
    

            bars=alt.Chart(df2,title="Average Waiting time for Each Department(Appointments)", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
            color=alt.value('#FFA600'),
            tooltip = [alt.Tooltip('DName'),
                    alt.Tooltip('AVG')]
        
            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Waiting time for Appointments", width=400,height=800

            )
   
            g_json=bars.to_json()
            return g_json

        
def mlc_analysis(category):
    import pandas as pd
    import altair as alt
    alt.data_transformers.disable_max_rows()
    df = pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    if(len(df)!=0):
        w=pd.Series(df['Is MLC'].value_counts())
        if category=="MLCSpecialty":
        
            input_dropdown = alt.binding_select(options=df['Primary doctor Specialty'].unique(), name="Specialty Name")  # creates drop-down menu of unique department names
            selection = alt.selection_single(fields=['Primary doctor Specialty'], bind=input_dropdown, name='Select')
            area_chart=alt.Chart(df, title="Number of MLC's", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().transform_filter(selection
                    ).encode(
                    alt.X('Is MLC:N'),
                    alt.Y('count(Is MLC):Q'),
                    color=alt.value('#E985F0'),
                    tooltip = [alt.Tooltip('Is MLC:N'),
                            alt.Tooltip('count(Is MLC):Q'),
                            alt.Tooltip('Primary doctor Specialty')
                            ]
                            
                        
                #).interactive(# zoom
                ).add_selection(selection
                    ).configure_axis(grid=False #interior grid off
            ).configure_view(strokeWidth=0 #exterior grid off
            ).properties(
                width =100, #width and height of bars
                height =300,
        
            ).configure_title(
                fontSize=15,
                font='Arial',
                anchor='middle',#center title
                color='black'
            ).configure_axis(
                domainWidth=2,
                domainColor='black',#domain is axis...axis width and color
                labelFontSize=15,
                titleFontSize=15,

            )
            g_json=area_chart.to_json()
            return g_json

        else:
            input_dropdown = alt.binding_select(options=df['Ward Name'].unique(),name="Ward Name")  # creates drop-down menu of unique department names
            selection = alt.selection_single(fields=['Ward Name'], bind=input_dropdown, name='Select')
            area_chart=alt.Chart(df, title="Number of MLC's", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().transform_filter(selection
                    ).encode(
                    alt.X('Is MLC:N'),
                    alt.Y('count(Is MLC):Q'),
                    color=alt.value('#85F095'),
                    tooltip = [alt.Tooltip('Is MLC:N'),
                            alt.Tooltip('count(Is MLC):Q'),
                            alt.Tooltip('Ward Name')
                            ]
                        
                #).interactive(# zoom
                ).add_selection(selection
                    ).configure_axis(grid=False #interior grid off
                ).configure_view(strokeWidth=0 #exterior grid off
                ).properties(
                    width =100, #width and height of bars
                    height =300,
        
            ).configure_title(
                fontSize=15,
                font='Arial',
                anchor='middle',#center title
                color='black'
            ).configure_axis(
                domainWidth=2,
                domainColor='black',#domain is axis...axis width and color
                labelFontSize=15,
                titleFontSize=15,
        
            )
            g_json=area_chart.to_json()
            return g_json
        


def discharges_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    if category=='EachWard':
        df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        data = [df['Discharge Date & Time '], df['Ward Name']]

        headers = ['Discharge','Wardname']

        df2 = pd.concat(data, axis=1, keys=headers)
        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]
        if(len(df2)!=0):
            gk=df2.groupby(by=['Wardname']).count().reset_index()

            gk=gk.rename(columns={'Discharge':'Count'})

            area_chart=alt.Chart(gk, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Wardname:N',axis=alt.Axis(title=None)),
            color=alt.value('#6056E3'),
            
            tooltip = [

                    alt.Tooltip('Count'),

                    alt.Tooltip('Wardname:N')

                    ]

            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Number of discharges from each ward",
            width = 400, #width and height of bars
            height = 400

            )


            g_json=area_chart.to_json()
            return g_json
    elif category=='EachWardBed':
        df1=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        #alt.data_transformers.disable_max_rows()
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]     #selecting data frame rows in the desired date range
        if(len(df1)!=0):
            area_chart=alt.Chart(df1).mark_bar(size=15).encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

            alt.Y('Billable Bed Type:N',axis=alt.Axis(title=None)),

            alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

            tooltip = [

                    alt.Tooltip('count(Billable Bed Type)'),

                    alt.Tooltip('Billable Bed Type')

                    ]

            ).facet(row=alt.Row('Ward Name:N', header=alt.Header(title='Ward Name',labelOrient='top',labelAngle=0)) #categorize orders based on ordering station

        
            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Number of discharges from each ward: Bed-wise"
            )

            g_json=area_chart.to_json()
            return g_json
    elif category=='AllWardBed':
        df1=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]     #selecting data frame rows in the desired date range
        if(len(df1)!=0):
            bars=alt.Chart(df1, title='Number of discharges from all wards: Bed-wise', padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=15).encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

            alt.Y('Billable Bed Type:N',axis=alt.Axis(title=None)),

            alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),
        

            tooltip = [

                    alt.Tooltip('count(Billable Bed Type)'),

                    alt.Tooltip('Billable Bed Type')

                    ]


            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Number of discharges",width=300,height=300

            )

       
            g_json=bars.to_json()
            return g_json
    elif category=='EachSpec':
        df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        data = [df['Discharge Date & Time '], df['Primary doctor Specialty']]

        headers = ['Discharge','Specialty']

        df2 = pd.concat(data, axis=1, keys=headers)

        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format


        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]
        if(len(df2)!=0):
            gk=df2.groupby(by=['Specialty']).count().reset_index()

            gk=gk.rename(columns={'Discharge':'Count'})

            area_chart=alt.Chart(gk, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Specialty:N',axis=alt.Axis(title=None)),
            color=alt.value('#82DC1C'),
            tooltip = [

                    alt.Tooltip('Count'),

                    alt.Tooltip('Specialty:N')

                    ]

            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Number of discharges from each ward",width=400,height=600
            )
            g_json=area_chart.to_json()
            return g_json
    elif category=='EachDoc':
        
        df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        data = [df['Discharge Date & Time '], df['Primary doctor']]

        headers = ['Discharge','Doctor']

        df2 = pd.concat(data, axis=1, keys=headers)

        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format


        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]
        if(len(df2)!=0):
            gk=df2.groupby(by=['Doctor']).count().reset_index()

            gk=gk.rename(columns={'Discharge':'Count'})

            area_chart=alt.Chart(gk,padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=15).encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Doctor:N',axis=alt.Axis(title=None)),
            color=alt.value('#EF5F8A'),
            tooltip = [

                    alt.Tooltip('Count'),

                    alt.Tooltip('Doctor:N')

                    ]

            ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
            ).properties(title="Number of discharges",width=400,height=1000

            )

        

            g_json=area_chart.to_json()
            return g_json

    elif category=='BedEachWard':
        df1=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows() #to allow more than 5000 rows in display
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]
        if(len(df1)!=0):
            area_chart=alt.Chart(df1, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

            alt.Y('Billable Bed Type:N',axis=alt.Axis(title=None)),

            alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),
            

            tooltip = [

                    alt.Tooltip('count(Billable Bed Type)'),

                    alt.Tooltip('Billable Bed Type')

                    ]

            ).facet(row=alt.Row('Ward Name:N', header=alt.Header(title='Ward Name',labelOrient='top',labelAngle=0)) #categorize orders based on ordering station

            ).properties(title='Number of discharges from each ward: Bed-wise'

            ).configure_axis(grid=False #interior grid off
            ).configure_view(strokeWidth=0 #exterior grid off
            ).properties(
                width =200, #width and height of bars
                height =700,
        
            ).configure_title(
                fontSize=15,
                font='Arial',
                anchor='middle',#center title
                color='black'
            ).configure_axis(
                domainWidth=2,
                domainColor='black',#domain is axis...axis width and color
                labelFontSize=10,
                titleFontSize=10,
        
            )
            g_json=area_chart.to_json()
            return g_json

    elif category=='BedAllWard':
        df1=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows() #to allow more than 5000 rows in display
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]
        if(len(df)!=0):
            bars=alt.Chart(df1, title='Number of discharges from all wards: Bed-wise', padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

            alt.Y('Billable Bed Type:N',axis=alt.Axis(title=None)),

            alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),
            

            tooltip = [

                    alt.Tooltip('count(Billable Bed Type)'),

                    alt.Tooltip('Billable Bed Type')

                    ]


            )
            text=alt.Chart().mark_text(align='center', baseline='middle', dx=9).encode(
            y=alt.Y('Billable Bed Type', title=None),
            x='count(Billable Bed Type)',
            text='count(Billable Bed Type)')


            area_chart=alt.layer(bars, text, data=df1)
            g_json=area_chart.to_json()
            return g_json
def spec_ward_day(wardname):
    category=wardname
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name']]
    headers = ['Discharge','Wardname']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Wardname']==category)]
    if(len(df3)!=0):
        df3['date']=pd.to_datetime(df3['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    
    
        t1=pd.Series(df3['date'].value_counts())
        pdf1=t1.to_frame()
        pdf1=pdf1.reset_index()
        pdf1=pdf1.rename(columns={"index":"date", "date":"count"})
        print(sum(pdf1['count']))
        area_chart=alt.Chart(pdf1, title="Number of patients discharged from ("+category+")", padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar().encode(
        alt.X('count'),
        alt.Y('date'),
        color=alt.value('#935FEF'),
        tooltip = [alt.Tooltip('count'),
                alt.Tooltip('date')
                ]
                
        #).interactive(# zoom
        ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(width=300,height=600

            )
    
        g_json=area_chart.to_json()
        return g_json

def spec_doc_and_spec(doctor,specialty,start_date,end_date):
    category1=specialty
    category2=doctor
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Billable Bed Type'], df['Primary doctor Specialty'], df['Primary doctor']]

    headers = ['Discharge', 'BedType', 'Speciality', 'Doctor']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category1) & (df2["Doctor"]==category2)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    if(len(gk)!=0):
        area_chart=alt.Chart(gk, padding={"left": 180, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#8DEF5F'),

        

        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="("+category1+") speciality: Doctor ("+category2+")",width=300,height=300

            )

        g_json=area_chart.to_json()
        return g_json

def specific_spec_bed(specialty,start_date,end_date):
    category=specialty
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty']]

    headers = ['Discharge','Wardname', 'BedType', 'Speciality']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    if(len(gk)!=0):

        area_chart=alt.Chart(gk, padding={"left": 150, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#EF935F'),
        #alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="Number of discharges from ("+category+"): Bed-wise", width=300,height=300

            )
    
        g_json=area_chart.to_json()
        return g_json

def specific_discharge_analysis(wardname,start_date,end_date):
    category=wardname
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type']]

    headers = ['Discharge','Wardname', 'BedType']

    df2 = pd.concat(data, axis=1, keys=headers)
   
    df3= df2[(df2['Wardname']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    if(len(gk)!=0):
        area_chart=alt.Chart(gk, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#8971A3'),
        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="Number of discharges from ("+category+"): Bed-wise",
            width=300,height=300

        )
    
        g_json=area_chart.to_json()
        return g_json

def spec_doc_bed(doctor, start_date, end_date):
    category=doctor
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Primary doctor'], df['Billable Bed Type']]
    headers = ['Discharge','Primary doctor', 'BedType']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Primary doctor']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    if(len(gk)!=0):
        area_chart=alt.Chart(gk, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#D265B1'),

        #alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=25,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="Number of discharges by ("+category+"): Bed-wise",width=300,height=300

            )
        g_json=area_chart.to_json()
        return g_json




def spec_ward_and_spec_and_doc(wardname, specialty, doctor,start_date,end_date):
    category1=wardname
    category2=specialty
    category3=doctor
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty'], df['Primary doctor']]
    headers = ['Discharge','Wardname', 'BedType', 'Speciality', 'Doctor']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category2) & (df2['Wardname']==category1) & (df2["Doctor"]==category3)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range

    if(len(gk)!=0):
        area_chart=alt.Chart(gk, padding={"left": 150, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#3D95AF'),
        #alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=20,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="("+category1+") ward: ("+category2+") speciality: Doctor ("+category3+")",width=300,height=300

            )


        g_json=area_chart.to_json()
        return g_json


def spec_ward_and_spec(wardname, specialty,start_date,end_date):
    category1=wardname
    category2=specialty
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty']]

    headers = ['Discharge','Wardname', 'BedType', 'Speciality']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category2) & (df2['Wardname']==category1)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    if(len(gk)!=0):
        area_chart=alt.Chart(gk, padding={"left": 200, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
        color=alt.value('#7FB47D'),
        #alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

        tooltip = [

                alt.Tooltip('count(BedType)'),

                alt.Tooltip('BedType:N')

                ]

        ).configure_title(
                        fontSize=20,
                        font='Arial',
                        anchor='middle',#center title
                        color='black'
                    ).configure_axis(
                        domainWidth=2,
                        domainColor='black',#domain is axis...axis width and color
                        labelFontSize=10,
                        titleFontSize=15,    
        ).properties(title="("+category1+") ward: ("+category2+") speciality",width=300,height=300

            )
            
        g_json=area_chart.to_json()
        return g_json



def payments_analysis():
    import matplotlib.pyplot as plt
    df=pd.read_excel("mainpage/media/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')

    a=df['PaymentType'].str.count("Cash").sum()
    b=df['PaymentType'].str.count("Credit").sum()
    labels = ['Cash','Credit']
    explodeTuple = (0.1,0.1)
    sizes=[a,b]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True,explode=explodeTuple)
    ax1.axis('equal')
    ax1.set_title("Payment type")
    ax1.text(-1.5, 0.7, a, bbox=dict(facecolor='blue', alpha=0.5))
    ax1.text(-2.0, 0.7, "Cash" )
    ax1.text(-1.5, 0.5, b, bbox=dict(facecolor='orange', alpha=1))
    ax1.text(-2.0, 0.5, "Credit" )
    plt.show()

################################## amala's team  #########################################################################################################

def pharmacyorders_from_nursing_stations_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    dip=pd.read_excel("mainpage/media/fileupload/Pharmacy.xlsx",usecols=['OrderId','OrderDateTime','UHId','OrderingStation','PriorityName'],engine='openpyxl')    #create dataframe
    dip["OrderDate"] = pd.to_datetime(dip["OrderDateTime"]).dt.strftime("%Y-%m-%d") #string to date format

    dip=dip.dropna()
    dip=dip.loc[(dip["OrderDate"]>=start_date) & (dip["OrderDate"]<=end_date)]

    if (len(dip)!=0):
        dip2=dip.groupby(['OrderingStation', 'PriorityName']).size().reset_index(name='Counts')
        input_dropdown = alt.binding_select(options=dip['PriorityName'].unique(), name="Select Priority ")  # creates drop-down menu of unique priority names
        selection = alt.selection_single(fields=['PriorityName'], bind=input_dropdown)

        if category=='Priority':
            #Pharmacy Orders From Each Nursing Stations- PRIORITY FILTER
            pharmacy1_chart=alt.Chart(dip2).mark_bar().transform_filter(selection
            ).encode(alt.X('Counts',title='Number of Orders'),
            alt.Y('PriorityName:N',title=None,axis=alt.Axis(labels=False)),
            alt.Color('PriorityName', legend=alt.Legend(title="Priority Name")),
            tooltip = [
                    alt.Tooltip('Counts'),
                    alt.Tooltip('OrderingStation'),
                    alt.Tooltip('PriorityName')
                    ]
            ).facet(row=alt.Row('OrderingStation:N', header=alt.Header(title='Ordering Station',labelOrient='top',labelAngle=0,labelFontSize=15,titleFontSize=20,labelFontStyle='Arial'))
            ).add_selection(selection
            ).configure_title(fontSize=20, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=15, titleFontSize=20,
            ).configure_legend(titleFontSize=15,labelFontSize=15
            ).properties(title='Pharmacy Orders From Each Nursing Station: Priority-wise : '+start_date+" to "+ end_date
            )
            g_json=pharmacy1_chart.to_json()
            return g_json

        elif category=='OrderingStation':
            #Pharmacy Orders From Each Nursing Stations- ORDERING STATION              
            data = pd.read_excel('mainpage/media/fileupload/Pharmacy.xlsx',usecols=['OrderDateTime','OrderId','OrderingStation','PriorityName'])
            data["OrderDate"] = pd.to_datetime(data["OrderDateTime"]).dt.strftime("%Y-%m-%d") #convert to desired date format
            data=data.loc[(data["OrderDate"]>=start_date) & (data["OrderDate"]<=end_date)]
            data.drop("OrderDateTime",axis=1,inplace=True)

            df_stationwise= data.groupby('OrderingStation')

            df=df_stationwise.count() #df has stations and their order counts
            df=df.rename(columns={'OrderId':'OrderCount'})  #No. of orders from each station
            df['Station']=df.index #converting station to column from being index

            df1=data.groupby(['OrderingStation', 'PriorityName']).size().reset_index(name='Counts')  #df1 has stations and their order counts for each priority
            df1=df1.rename(columns={'OrderingStation':'Station'}) #so that matches with station in df 
            df1=df1.dropna()

            select_station = alt.selection(type="single", encodings=['y'])

            station_chart = alt.Chart(df).mark_bar().encode(
                alt.X('OrderCount',title='Number of Orders'), #x-axis
                alt.Y('Station',title='Ordering Station'),
                color=alt.condition(select_station, alt.ColorValue("teal"), alt.ColorValue("grey")),
                tooltip = [
                            alt.Tooltip('OrderCount',title='Number of Orders'),
                            alt.Tooltip('Station',title='Ordering Station'),
                            ]
            ).add_selection(select_station)   #so that we can select a station


            priority_chart = alt.Chart(df1).mark_bar(size=30).encode(
                    alt.Y('Counts',title='Number of Orders'),
                    alt.X("PriorityName",title='Priority'),
                    color=alt.Color('PriorityName',title='Priority', scale=alt.Scale(scheme='tableau10')),
                    tooltip = [
                        alt.Tooltip('PriorityName',title='Priority Name'),
                        alt.Tooltip('Counts',title='Number of Orders'),
                        ]
                ).transform_filter(select_station).properties(width=100)  #apply filter



            pharmacy2_chart = alt.hconcat(station_chart, priority_chart).configure_title(fontSize=20, font='Calibri',dy=-25, anchor='middle', color='black'
                    ).configure_axis(domainWidth=2,
                    domainColor='black',#domain is axis...axis width and color
                    labelFontSize=15, titleFontSize=20,
                    ).configure_legend(titleFontSize=15,labelFontSize=15
                    ).properties(
                title="Pharmacy Orders From Each Nursing Station and Priority-wise: "+start_date+" to "+ end_date
            )
            g_json=pharmacy2_chart.to_json()
            return g_json

        elif category=='Overall':
            #Pharmacy Orders From Each Nursing Stations- OVERALL
            pharmacy3_chart=alt.Chart(dip2).mark_bar().encode(
                alt.X('Counts',title='Number of Orders'),
                alt.Y('PriorityName:N',axis=alt.Axis(title=None)),
                alt.Color('PriorityName', legend=alt.Legend(title="Priority Name")),
                tooltip = [
                        alt.Tooltip('Counts'),
                        alt.Tooltip('OrderingStation'),
                        alt.Tooltip('PriorityName')
                        ]
            ).facet(row=alt.Row('OrderingStation:N', header=alt.Header(title='Ordering Station',labelFontSize=15,titleFontSize=20,labelFontStyle='Arial',labelOrient='top',labelAngle=0)) #categorize orders based on ordering station
            ).configure_title(fontSize=20, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=15, titleFontSize=20,
            ).configure_legend(titleFontSize=15,labelFontSize=15
            ).properties(title='Pharmacy Orders From Each Nursing Station: All Priorities: '+start_date+" to "+ end_date
            )
            g_json=pharmacy3_chart.to_json()
            return g_json

def pharmacyorders_per_patient_analysis(start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/media/fileupload/Pharmacy.xlsx",usecols=['OrderDateTime','UHId'],engine='openpyxl')    #create dataframe
    df["date2"] = pd.to_datetime(df["OrderDateTime"]).dt.strftime("%Y-%m-%d") #string to date format
    #------------creating a dataframe with columns- date, patientcount, ordercount---------

    df1 = pd.DataFrame(df, columns = ['date2','UHId']) #create a df with just these 2 columns
    df1=df1.dropna()
    df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]
    if (len(df1)!=0):
        grouped_patientcount=df1.groupby('date2').UHId.nunique() #df with patient count date-wise
        grouped_ordercount= df1.groupby('date2').count() #df with order count date-wise
        merged=pd.merge(grouped_patientcount,grouped_ordercount,on='date2') # join the dfs using date field
        merged.columns=['PatientCount','OrderCount'] #name columns
        merged['Number of Orders per patient']= (merged['OrderCount']/merged['PatientCount']).round(decimals=2) #add column for no. of orders per patient
        #-----------------------------------------------
        merged=merged.sort_index(ascending=True) #sort df with respect to date
        merged['date2']=merged.index #converting date from being index to column

        orderperpatient_chart=alt.Chart(merged).mark_bar(size=20).encode(
            alt.Y('Number of Orders per patient'),
            alt.X('date2',title='Date'),
            #color=alt.Color('Number of Orders per patient',title='Orders Per Patient'),
            tooltip = [
                    alt.Tooltip('date2',title='Date'),
                    alt.Tooltip('Number of Orders per patient'),
                    alt.Tooltip('OrderCount'),
                    alt.Tooltip('PatientCount')
                    ]
                    
        ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
        ).configure_axis(domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=10, titleFontSize=15,
        ).configure_legend(titleFontSize=15,labelFontSize=15
        ).properties(title='Pharmacy Orders - Number of Orders per Patient per Day: '+start_date+" to "+ end_date,width=300,height=300)
        g_json=orderperpatient_chart.to_json()
        return g_json

def topmedicines_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/media/fileupload/Top100Medicines.xlsx",usecols=['ItemName', 'Quantity','Unit', 'ItemCatagory','Station','BillDateTime'],engine='openpyxl')    #create dataframe
    df["Date"] = pd.to_datetime(df["BillDateTime"]).dt.strftime("%Y-%m-%d") # to desired date format
    df=df.dropna()
    df=df.loc[(df["Date"]>=start_date) & (df["Date"]<=end_date)]
    if (len(df)!=0):
        if category=="Station":
            groups=df.groupby(['Station','ItemName'])['Quantity'].sum().reset_index(name='TotalQty')  #index is Total Quantity now
            groups=groups.sort_values(['Station','TotalQty'], ascending=False)
            groups=groups.reset_index()
            groups=groups.drop(columns=['index'])
            stations=groups['Station'].unique()

            base=alt.Chart(groups).mark_bar(size=15).encode(
                    alt.X('TotalQty',title='Number of units sold'), 
                    alt.Y('ItemName',sort=None), #x-axis
                    color=alt.Color('Station'),
                    tooltip = [
                        alt.Tooltip('TotalQty',title='Number of units sold'),
                        alt.Tooltip('ItemName'),
                        alt.Tooltip('Station'),
                        ]
                    )

            topmedicines_chart1 = alt.vconcat()
            
            for station in stations:
                topmedicines_chart1 &= base.transform_filter(datum.Station == station).properties(title="Top Movable Medicines in "+station+" : "+start_date+" to "+end_date)
            topmedicines_chart1.properties(width=2000,height=500)
            g_json=topmedicines_chart1.to_json()
            return g_json

        elif category=='Overall':
            grouped_df=df.groupby(['ItemName'])['Quantity'].sum().reset_index(name='TotalQty')  #index is Total Quantity now
            dop=grouped_df.nlargest(100,'TotalQty').reset_index()
            dop.drop(columns=['index'])

            topmedicines_chart2=alt.Chart(dop).mark_bar(size=15).encode(
            alt.X('TotalQty',title='Number of units sold'), 
            alt.Y('ItemName', title='Item Name',sort=None), #x-axis
            #color=alt.Color('TotalQty',title='Quantity'),
            tooltip = [
                alt.Tooltip('TotalQty',title='Number of units sold'),
                alt.Tooltip('ItemName',title='Item Name')
                ]
            ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=10, titleFontSize=15,
            ).configure_legend(titleFontSize=15,labelFontSize=15
            ).properties(title='Top 100 Movable Medicines in Hospital: '+start_date+" to "+ end_date,width=800,height=2000)
            g_json=topmedicines_chart2.to_json()
            return g_json
            

def drugstock_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/media/fileupload/Top100Medicines.xlsx",usecols=['ItemName', 'Quantity','Unit', 'ItemCatagory','Station','BillDateTime'],engine='openpyxl')    #create dataframe
    df["Date"] = pd.to_datetime(df["BillDateTime"]).dt.strftime("%Y-%m-%d") # to desired date format
    df=df.dropna()
    df=df.loc[(df["Date"]>=start_date) & (df["Date"]<=end_date)]
    alt.data_transformers.disable_max_rows() 
    if (len(df)!=0):
        if category=='Item Catagory':
            groups=df.groupby(['ItemCatagory','ItemName'])['Quantity'].sum().reset_index(name='TotalQty')  #index is Total Quantity now
            categories=groups['ItemCatagory'].unique()

            base=alt.Chart(groups).mark_bar(size=15).encode(
                    alt.X('TotalQty',title='Quantity'), 
                    alt.Y('ItemName'), #x-axis
                    color=alt.Color('ItemCatagory'),
                    tooltip = [
                        alt.Tooltip('TotalQty',title='Quantity'),
                        alt.Tooltip('ItemName'),
                        alt.Tooltip('ItemCatagory'),
                        ]
                    )

            drug_chart1 = alt.vconcat()

            for category in categories:
                drug_chart1 &= base.transform_filter(datum.ItemCatagory == category).properties(title='Drug Stock Analysis: '+category+" : "+start_date+" to "+ end_date)
            g_json=drug_chart1.to_json()
            return g_json

        elif category=="Overall":
            drug_chart2=alt.Chart(df).mark_bar(size=15).encode(
                alt.X('sum(Quantity)',title='Quantity'), #y-axis
                alt.Y('ItemName',sort='-y'), #x-axis
                color='ItemCatagory', #color bars based on category
                tooltip = [
                        alt.Tooltip('sum(Quantity)'),
                        alt.Tooltip('Unit'),
                        alt.Tooltip('ItemName'),
                        alt.Tooltip('ItemCatagory'),
                        ]
            ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=10, titleFontSize=15,
            ).configure_legend(titleFontSize=15,labelFontSize=15
            ).properties(title='Drug Stock Analysis: '+start_date+" to "+ end_date,width=600)
            g_json=drug_chart2.to_json()
            return g_json


def radiology_analysis(test,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/media/fileupload/Radiology.xlsx",usecols=['RegistrationNo','sex', 'Age','Item Name',"Bill Datetime"],engine='openpyxl')
    df=df.loc[df['Item Name'] == test]

    df=df.dropna()
    df["Date"] = pd.to_datetime(df["Bill Datetime"]).dt.strftime("%Y-%m-%d") # to desired date format
    df=df.loc[(df["Date"]>=start_date) & (df["Date"]<=end_date)]

    if (len(df)!=0):
        #Creating a field Age category
        df.loc[((df.Age >= 0)&(df.Age < 10)),  'Age_Group'] = '0-10'
        df.loc[((df.Age >= 10)&(df.Age < 20)),  'Age_Group'] = '10-20'
        df.loc[((df.Age >= 20)&(df.Age < 30)),  'Age_Group'] = '20-30'
        df.loc[((df.Age >= 30)&(df.Age < 40)),  'Age_Group'] = '30-40'
        df.loc[((df.Age >= 40)&(df.Age < 50)),  'Age_Group'] = '40-50'
        df.loc[((df.Age >= 50)&(df.Age < 60)),  'Age_Group'] = '50-60'
        df.loc[((df.Age >= 60)&(df.Age < 70)),  'Age_Group'] = '60-70'
        df.loc[((df.Age >= 70)&(df.Age < 80)),  'Age_Group'] = '70-80'
        df.loc[(df.Age >= 80),  'Age_Group'] = '80+'

        title='Radiology  (Test wise Analysis) : '+test+' : ' +start_date+' to '+ end_date
        radio_chart = alt.Chart(df,padding={"left": 300, "top": 10, "right": 10, "bottom": 10}).mark_bar(size=15).encode(
                alt.X('sex',title=None), #x-axis
                alt.Y('count(RegistrationNo)',title='Count'), #y-axis
                color=alt.Color('sex',title='Sex',scale=alt.Scale(range=['#c83349','#1f77b4'])),
                column='Age_Group', #creates subcharts based on age group 
                tooltip = [
                        alt.Tooltip('count(RegistrationNo)'),
                        alt.Tooltip('sex'),
                        alt.Tooltip('Age_Group',title='Age Group'),
                        alt.Tooltip('Item Name')
                        ]
                        ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
                ).configure_axis(domainWidth=2,
                domainColor='black',#domain is axis...axis width and color
                labelFontSize=12, titleFontSize=20,
                ).configure_legend(titleFontSize=15,labelFontSize=15
                ).properties(title=title,height=300)

        g_json=radio_chart.to_json()
        return g_json



def surgery_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df1 = pd.read_excel("mainpage/media/fileupload/SurgeryAnalysis.xlsx",usecols=["UHID","SurgeryName","Surgery Department","Date Of Surgery"],engine='openpyxl')
    df2 = pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",usecols=["UHID","AgeYears","Sex"],engine='openpyxl')
    df2 = df2.drop_duplicates('UHID')
    df=pd.merge(df1,df2,on='UHID') # join tables using UHID field
    df=df.dropna()
    df["Date"] = pd.to_datetime(df["Date Of Surgery"]).dt.strftime("%Y-%m-%d") # to desired date format
    df=df.loc[(df["Date"]>=start_date) & (df["Date"]<=end_date)]
    df=df.rename(columns={'AgeYears':'Age'}) #so that matches with age in df 
    #Creating a field Age category
    if (len(df)!=0):
        df.loc[((df.Age >= 0)&(df.Age < 10)),  'Age_Group'] = '0-10'
        df.loc[((df.Age >= 10)&(df.Age < 20)),  'Age_Group'] = '10-20'
        df.loc[((df.Age >= 20)&(df.Age < 30)),  'Age_Group'] = '20-30'
        df.loc[((df.Age >= 30)&(df.Age < 40)),  'Age_Group'] = '30-40'
        df.loc[((df.Age >= 40)&(df.Age < 50)),  'Age_Group'] = '40-50'
        df.loc[((df.Age >= 50)&(df.Age < 60)),  'Age_Group'] = '50-60'
        df.loc[((df.Age >= 60)&(df.Age < 70)),  'Age_Group'] = '60-70'
        df.loc[((df.Age >= 70)&(df.Age < 80)),  'Age_Group'] = '70-80'
        df.loc[(df.Age >= 80),  'Age_Group'] = '80+'
   
        if category=='Surgery':
            input_dropdown = alt.binding_select(options=df['SurgeryName'].unique(), name="Select Surgery Name ")  # creates drop-down menu of unique surgery names
            selection = alt.selection_single(fields=['SurgeryName'], bind=input_dropdown)
            surgery_chart1=alt.Chart(df).mark_bar(size=15).transform_filter(selection
                ).encode(
                alt.X('Age_Group',title='Age Group'),  # x-axis
                alt.Y('count(UHID)',title='Number Of Patients'), # y-axis
                color=alt.Color('Sex',scale=alt.Scale(range=['#c83349','#1f77b4'])),
                column='SurgeryName', #  creates different subcharts for different surgeries
                tooltip = [
                        alt.Tooltip('count(UHID)'),
                        alt.Tooltip('Sex'),
                        alt.Tooltip('Age_Group',title='Age Group'),
                        alt.Tooltip('SurgeryName'),
                        alt.Tooltip('Surgery Department'),
                        ]).add_selection(selection
                ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=12, titleFontSize=15,
            ).configure_legend(titleFontSize=15,labelFontSize=15
                ).properties(title='Surgery - Surgery Name wise analysis: '+start_date+" to "+ end_date,height=300,width=200
            )
            g_json=surgery_chart1.to_json()
            return g_json
            
        elif category=='Surgery Department':
            input_dropdown = alt.binding_select(options=df['Surgery Department'].unique(), name="Select Surgery Department ")  # creates drop-down menu of unique department names
            selection = alt.selection_single(fields=['Surgery Department'], bind=input_dropdown)
        
            surgery_chart2=alt.Chart(df).mark_bar(size=15).transform_filter(selection
                ).encode(
                alt.X('Age_Group',title='Age Group'),  # x-axis
                alt.Y('count(UHID)',title='Number Of Patients'), # y-axis
                color=alt.Color('Sex',scale=alt.Scale(range=['#c83349','#1f77b4'])),
                column='Surgery Department', #  creates subcharts based on department 
                tooltip = [
                        alt.Tooltip('count(UHID)'),
                        alt.Tooltip('Sex'),
                        alt.Tooltip('Age_Group',title='Age Group'),
                        alt.Tooltip('Surgery Department'),
                        ]).add_selection(selection
                ).configure_title(fontSize=25, font='Arial',dy=-25, anchor='middle', color='black'
            ).configure_axis(domainWidth=2,
            domainColor='black',#domain is axis...axis width and color
            labelFontSize=12, titleFontSize=15,
            ).configure_legend(titleFontSize=15,labelFontSize=15
            ).properties(title='Surgery - Department wise analysis : '+start_date+" to "+ end_date,height=300,width=200
            )
            g_json=surgery_chart2.to_json()
            return g_json


################################## varsha's team  ##################################################################################################
#function2.py gender code commented
###################################################



def insurance_analysis(category,start_date,end_date): 
    alt.data_transformers.disable_max_rows()
    count=pd.DataFrame()  
    count=count[0:0]
    if category=='Department':
        h=500
        di=pd.read_excel("mainpage/media/fileupload/AdmissionAnalysis.xlsx",engine='openpyxl')
        dip=pd.DataFrame()
        dip['UHID']=di['UHID']
        dip['Department']=di['Primary doctor Specialty']
        dip['Insurance']=di['InsuranceCompany']

        dip["Date"] = pd.to_datetime(di["Admission Date & Time"]).dt.strftime("%Y-%m-%d") #string to date format

        dip=dip.dropna()
        dip=dip.loc[(dip["Date"]>=start_date) & (dip["Date"]<=end_date)]
        #print(dip)
        #print("end",end_date)
        '''
        dip['Date'] = pd.to_datetime(di['Admission Date & Time']).dt.date
        dip["Date2"] = pd.to_datetime(dip["Date"]).dt.strftime("%Y-%m-%d") 
        dip=dip.dropna()
        
        after_start_date =dip["Date2"] >= start_date
        before_end_date = dip["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dip = dip.loc[between_two_dates]
        '''
        #if (len(dip)!=0):
        s=start_date
        print(s)
        print(len(dip))
        count=dip.groupby(['Department']).size().to_frame(name='Percentage inflow').reset_index()
        sum1=sum(count['Percentage inflow'])

        for i,row in count.iterrows():
                count.loc[i,'Percentage inflow']=count.at[i,'Percentage inflow']/sum1*100        

        #print(df)
    
    elif category=='Ward':
        #read ward file
        h=500
        di=pd.read_excel("mainpage/media/fileupload/AdmissionAnalysis.xlsx",engine='openpyxl')
        dip=pd.DataFrame()
        dip['UHID']=di['UHID']
        dip['Ward']=di['Ward Name']
        dip['Insurance']=di['InsuranceCompany']
        dip=dip.dropna()        

        dip['Date'] = pd.to_datetime(di['Admission Date & Time']).dt.date
        dip["Date2"] = pd.to_datetime(dip["Date"]).dt.strftime("%Y-%m-%d") 
        
        after_start_date =dip["Date2"] >= start_date
        before_end_date = dip["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dip = dip.loc[between_two_dates]

        count=dip.groupby(['Ward']).size().to_frame(name='Percentage inflow').reset_index()
        sum1=sum(count['Percentage inflow'])

        for i,row in count.iterrows():
                count.loc[i,'Percentage inflow']=count.at[i,'Percentage inflow']/sum1*100    
        #print(df)

    elif category=='Area': 
        h=500
        category="District"  
        da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
        df2=pd.DataFrame()
        df2['pincode']=da['pincode']
        df2['District']=da['Districtname']
        df2=df2.drop_duplicates(subset=['pincode'])
        di=pd.read_excel("mainpage/media/fileupload/AdmissionAnalysis.xlsx",engine='openpyxl')
        dip=pd.DataFrame()
        dip['UHID']=di['UHID']
        dip['Insurance']=di['InsuranceCompany']
        dip['City']=di['City']

        dip['Date']= pd.to_datetime(di['Admission Date & Time']).dt.date  
        dip["Date2"] = pd.to_datetime(dip["Date"]).dt.strftime("%Y-%m-%d")  #ymd format date stored in date column of df
        dip=dip.dropna()
        after_start_date =dip["Date2"] >= start_date
        before_end_date = dip["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dip = dip.loc[between_two_dates]

        dip= pd.merge(df2, dip, how='outer',left_on = 'District', right_on = 'City')
        dip['District']=dip['District'].replace(np.NaN,"Other")
        
        count=dip.groupby(['District']).size().to_frame(name='Percentage inflow').reset_index()
        sum1=sum(count['Percentage inflow'])
        for i,row in count.iterrows():
            count.loc[i,'Percentage inflow']=count.at[i,'Percentage inflow']/sum1*100            
    
    count=count.sort_values([category],ascending=False)
    insu_title="Insurance Analysis ("+category+")"+": "+start_date+" to "+end_date

    insu_chart=alt.Chart(count).mark_bar().encode(  

        alt.X('Percentage inflow:Q',axis=alt.Axis(title='Percentage inflow(%)')),                                          
        alt.Y(category,sort=None),
        tooltip = [alt.Tooltip(category), #hover info
                   alt.Tooltip('Percentage inflow:Q',title='Percentage inflow(%)')]

    ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='middle',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20,

    ).properties(
        title=insu_title,
        width = 500, #width and height of bars
        height = h
    )
    g_json=insu_chart.to_json()
    return g_json
    
###########################################gender####################################################

def gender_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    if category=='Department':    
        df=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
               
        df['Date'] = pd.to_datetime(df['visitdate']).dt.date
        df["Date2"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d") 
        df=df.dropna()
        
        after_start_date =df["Date2"] >= start_date
        before_end_date = df["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        df = df.loc[between_two_dates]

        count=df.groupby(['Department', 'Sex']).size().to_frame(name='Percentage').reset_index()
        tot=df.groupby(['Sex']).size()
        
        for i,row in count.iterrows():
            if count.loc[i,'Sex']=='Female':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/tot[0]*100
            else:
                count.loc[i,'Percentage']=count.at[i,'Percentage']/tot[1]*100
    
        count=count.rename(columns={'Sex':'Gender',"Percentage": "Percentage inflow"})
    
    
    elif category=='Ward':
        
        df1=pd.read_excel("mainpage/media/fileupload/AdmissionAnalysis.xlsx",engine='openpyxl')
        gward=pd.DataFrame()
        gward['Ward']=df1['Ward Name']
        gward['Gender']=df1['Gender']  

        gward['Date'] = pd.to_datetime(df1['Admission Date & Time']).dt.date
        gward["Date2"] = pd.to_datetime(gward["Date"]).dt.strftime("%Y-%m-%d") 
        gward=gward.dropna()
        after_start_date =gward["Date2"] >= start_date
        before_end_date = gward["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        gward = gward.loc[between_two_dates]

            
        count=gward.groupby(['Ward','Gender']).size().to_frame(name='Percentage').reset_index()
        totw=gward.groupby(['Gender']).size()
        for i,row in count.iterrows():
            if count.loc[i,'Gender']=='Female':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/totw[0]*100
            else:
                count.loc[i,'Percentage']=count.at[i,'Percentage']/totw[1]*100
        count=count.rename(columns={"Gender": "Gender","Percentage":"Percentage inflow"})    
        
    elif category=='Area':
        category='District'
        df=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
        da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
    
        df2=pd.DataFrame()
        df2['pincode']=da['pincode']
        df2['District']=da['Districtname']
        df2=df2.drop_duplicates(subset=['pincode'])    
    
        dsa=pd.DataFrame()
        dsa['UHID']=df['UHID']
        dsa['pincode']=df['pincode']
        dsa['Gender']=df['Sex']
        dssa=pd.DataFrame()
        dssa = df2.drop_duplicates("pincode")

        dsa['Date'] = pd.to_datetime(df['visitdate']).dt.date
        dsa["Date2"] = pd.to_datetime(dsa["Date"]).dt.strftime("%Y-%m-%d") 
        dsa=dsa.dropna()
        
        after_start_date =dsa["Date2"] >= start_date
        before_end_date = dsa["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dsa = dsa.loc[between_two_dates]

        dsa = pd.merge(dsa, dssa, how='inner',left_on = 'pincode', right_on = 'pincode')
        dsa=dsa.drop_duplicates("UHID")         
        
        count=dsa.groupby(['District', 'Gender']).size().to_frame(name='Percentage').reset_index()
        tot=dsa.groupby(['Gender']).size()
        for i,row in count.iterrows():
            if count.loc[i,'Gender']=='Female':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/tot[0]*100
            else:
                count.loc[i,'Percentage']=count.at[i,'Percentage']/tot[1]*100
        count=count.rename(columns={"Gender": "Gender","Percentage":"Percentage inflow"})    
        
    gender_title="Gender-wise Analysis ("+category+")"+": "+start_date+" to "+end_date
    gender_chart=alt.Chart(count).mark_bar().encode(
        alt.Column(category,header=alt.Header(titleFontSize=20,labelFontSize=13,labelAngle=-90,labelLimit=100,labelAlign='left')),#header for gouped chart -col and row title, label

        alt.Y('Percentage inflow',axis=alt.Axis(title='Percentage inflow(%)')),                                          
        alt.X('Gender',axis=alt.Axis(labels=False,title='')),
        alt.Color('Gender',scale=alt.Scale(range=['#800000', '#020645'])), # maroon, blue
        tooltip = [alt.Tooltip(category), #hover info
                    alt.Tooltip('Gender:O'),
                    alt.Tooltip('Percentage inflow:Q',title='Percentage inflow(%)')]

    ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='middle',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20
    ).properties(
        title=gender_title, 
        width = 30, #width and height of bars
        height = 400
    )
    g_json=gender_chart.to_json()
    return g_json


######################################################### AGE #######################################################################

def age_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    if category=='Department':
        category='Department'
        dag=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
        dag=dag.rename(columns={'AgeYears':'Age'})
        dag=dag.drop_duplicates(subset=['UHID','Department'])

        dag['Date'] = pd.to_datetime(dag['visitdate']).dt.date
        dag["Date2"] = pd.to_datetime(dag["Date"]).dt.strftime("%Y-%m-%d") 
        dag=dag.dropna()
        
        after_start_date =dag["Date2"] >= start_date
        before_end_date = dag["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dag = dag.loc[between_two_dates]

        bins= [0,11,21,31,41,51,61,71,81,91,111]
        labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91 above']
        dag['AgeGroup'] = pd.cut(dag['Age'], bins=bins, labels=labels, right=False)
        count=dag.groupby(['Department','AgeGroup']).size().to_frame(name='Percentage').reset_index()
        sum1=dag.groupby(['AgeGroup']).size()
        
        for i,row in count.iterrows():

            if count.loc[i,'AgeGroup']=='0-10':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[0]*100

            elif count.loc[i,'AgeGroup']=='11-20':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[1]*100

            elif count.loc[i,'AgeGroup']=='21-30':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[2]*100

            elif count.loc[i,'AgeGroup']=='31-40':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[3]*100

            elif count.loc[i,'AgeGroup']=='41-50':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[4]*100

            elif count.loc[i,'AgeGroup']=='51-60':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[5]*100

            elif count.loc[i,'AgeGroup']=='61-70':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[6]*100

            elif count.loc[i,'AgeGroup']=='71-80':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[7]*100

            elif count.loc[i,'AgeGroup']=='81-90':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[8]*100
            elif count.loc[i,'AgeGroup']=='91-110':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[9]*100

            
    elif category=='Ward':
        dd=pd.read_excel("mainpage/media/fileupload/AdmissionAnalysis.xlsx",engine='openpyxl')
        dagw=pd.DataFrame()
        dagw['UHID']=dd['UHID']
        dagw['Age']=dd['Age']
        dagw['Ward']=dd['Ward Name']
        for i,row in dagw.iterrows():
            x=dagw.at[i,'Age']
            dagw.loc[i,'Age']=re.sub('[0-9]* Day','0',x)
        dagw['Age'] = dagw['Age'].str.extract(r'(\d+)', expand=False).astype(int)
        
        dagw['Date'] = pd.to_datetime(dd['Admission Date & Time']).dt.date
        dagw["Date2"] = pd.to_datetime(dagw["Date"]).dt.strftime("%Y-%m-%d") 
        dagw=dagw.dropna()
        after_start_date =dagw["Date2"] >= start_date
        before_end_date = dagw["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dagw = dagw.loc[between_two_dates]


        bins= [0,11,21,31,41,51,61,71,81,91,111]
        labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91 above']
        dagw['AgeGroup'] = pd.cut(dagw['Age'], bins=bins, labels=labels, right=False)
        count=dagw.groupby(['Ward','AgeGroup']).size().to_frame(name='Percentage').reset_index()
        sum1=dagw.groupby(['AgeGroup']).size()

        
        for i,row in count.iterrows():
            if count.loc[i,'AgeGroup']=='0-10':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[0]*100

            elif count.loc[i,'AgeGroup']=='11-20':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[1]*100

            elif count.loc[i,'AgeGroup']=='21-30':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[2]*100

            elif count.loc[i,'AgeGroup']=='31-40':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[3]*100

            elif count.loc[i,'AgeGroup']=='41-50':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[4]*100

            elif count.loc[i,'AgeGroup']=='51-60':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[5]*100

            elif count.loc[i,'AgeGroup']=='61-70':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[6]*100

            elif count.loc[i,'AgeGroup']=='71-80':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[7]*100

            elif count.loc[i,'AgeGroup']=='81-90':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[8]*100
            else:
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[9]*100

       
    elif category=="Area":
        category="District"
        da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
        df2=pd.DataFrame()
        df2['pincode']=da['pincode']
        df2['district']=da['Districtname']
        dag=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
        dag = dag.drop_duplicates(['UHID','Department'])
        dag=dag.rename(columns={'AgeYears':'Age'})
        dssa=pd.DataFrame()
        dssa = df2.drop_duplicates("pincode")

        dag['Date'] = pd.to_datetime(dag['visitdate']).dt.date
        dag["Date2"] = pd.to_datetime(dag["Date"]).dt.strftime("%Y-%m-%d") 
        dag=dag.dropna()
        
        after_start_date =dag["Date2"] >= start_date
        before_end_date = dag["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dag = dag.loc[between_two_dates]

        dag = pd.merge(dag, dssa, how='inner',left_on = 'pincode', right_on = 'pincode')
        bins= [0,11,21,31,41,51,61,71,81,91,111]
        labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91 above']
        dag['AgeGroup'] = pd.cut(dag['Age'], bins=bins, labels=labels, right=False)
        count=dag.groupby(['district','AgeGroup']).size().to_frame(name='Percentage').reset_index()
        sum1=dag.groupby(['AgeGroup']).size()
        for i,row in count.iterrows():
            if count.loc[i,'AgeGroup']=='0-10':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[0]*100
            elif count.loc[i,'AgeGroup']=='11-20':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[1]*100
            elif count.loc[i,'AgeGroup']=='21-30':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[2]*100
            elif count.loc[i,'AgeGroup']=='31-40':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[3]*100
            elif count.loc[i,'AgeGroup']=='41-50':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[4]*100
            elif count.loc[i,'AgeGroup']=='51-60':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[5]*100
            elif count.loc[i,'AgeGroup']=='61-70':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[6]*100
            elif count.loc[i,'AgeGroup']=='71-80':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[7]*100
            elif count.loc[i,'AgeGroup']=='81-90':
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[8]*100
            else:
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1[9]*100
        count=count.rename(columns={"district":"District"})
            
    
    age_title="Age-wise analysis("+category+")"+": "+start_date+" to "+end_date

    age_chart=alt.Chart(count).mark_bar().encode(
        alt.Y(category,title=category), #y-axis
        alt.X('Percentage'),color='AgeGroup', #x-axis
    
        tooltip = [ alt.Tooltip(category), #hover info
                    alt.Tooltip('AgeGroup:O',title='Age Group'),
                    alt.Tooltip('Percentage:Q',title='Percentage inflow(%)')]
    ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='start',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20,

    ).properties(
        title=age_title,
        width = 1000, #width and height of bars
        height = 500
    )
    g_json=age_chart.to_json()
    return g_json

###################################### appointment ##########################################################################################
def appointment_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    if category=='Department':
        h=500
        dap=pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx",sheet_name='WithAppointmentOP',engine='openpyxl')
        dap['Billing Time'] = pd.to_datetime(dap['BillingTime']).dt.date
        dap["Billing Time2"] = pd.to_datetime(dap["Billing Time"]).dt.strftime("%Y-%m-%d")
        
        after_start_date =dap["Billing Time2"] >= start_date
        before_end_date = dap["Billing Time2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dap = dap.loc[between_two_dates]


        count=dap.groupby(['Speciality']).size().to_frame(name='Percentage').reset_index()
        sum1=sum(count.Percentage)
        for i,row in count.iterrows():
                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1*100  
        count=count.rename(columns={"Speciality": "Department"})
        #print(count)

    elif category=='Area':
        category='District'
        h=500
        
        dfa=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
        df=pd.DataFrame()
        dap=pd.DataFrame()
        df['UHID']=dfa['UHID']
        df['AddedDate']=dfa['visitdate']
        df['pincode']=dfa['pincode']
        
        da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
        dapp = pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx",sheet_name='WithAppointmentOP',engine='openpyxl')
        dap['UHID']=dapp['UHID']
        df2=pd.DataFrame()
        df2['pincode']=da['pincode']
        df2['District']=da['Districtname']
        df2=df2.drop_duplicates(subset=['pincode'])

        df['Date'] = pd.to_datetime(df['AddedDate']).dt.date
        df["Date2"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
        dap['Billing Time'] = pd.to_datetime(dapp['BillingTime']).dt.date
        dap["Billing Time2"] = pd.to_datetime(dap["Billing Time"]).dt.strftime("%Y-%m-%d")

        date_start = dap["Billing Time2"].min()
        date_end = dap["Billing Time2"].max()
        after_start_date =df["Date2"] >= date_start
        before_end_date = df["Date2"] <= date_end
        between_two_dates = after_start_date & before_end_date
        df = df.loc[between_two_dates]

        df=df.dropna()
        dap=dap.dropna()
        after_start_date =df["Date2"] >= start_date
        before_end_date = df["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        df = df.loc[between_two_dates]

        after_start_date =dap["Billing Time2"] >= start_date
        before_end_date = dap["Billing Time2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dap = dap.loc[between_two_dates]


        df = pd.merge(df, df2, how='inner',left_on = 'pincode', right_on = 'pincode')
        dap= pd.merge(dap, df, how='right',left_on = 'UHID', right_on = 'UHID')

        count=dap.groupby(['District']).size().to_frame(name='Percentage').reset_index()
        sum1=sum(count.Percentage)
        for i,row in count.iterrows():
            count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1*100
        
        
    appnt_title="Appointment Analysis ("+category+")"+": "+start_date+" to "+end_date
    appnt_chart=alt.Chart(count).mark_bar().encode(  
        alt.X('Percentage:Q',axis=alt.Axis(title='Percentage inflow(%)')),                                          
        alt.Y(category),
        tooltip = [alt.Tooltip(category), 
                   alt.Tooltip('Percentage:Q',title='Percentage inflow(%)')]

    ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='middle',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20,

    ).properties(
        title=appnt_title, 
        width = 500, #width and height of bars
        height = h
    )
    g_json=appnt_chart.to_json()
    return g_json

############################################## WALKIN #########################################################################################33

def walkin_analysis(category,start_date,end_date): 
    alt.data_transformers.disable_max_rows()
    if category=='Department':
        h=500
        dap=pd.read_excel("mainpage/media/fileupload/OPConsultation.xlsx",sheet_name='WalkInOPConsultation',engine='openpyxl')
        
        dap['Billing Time'] = pd.to_datetime(dap['BillingTime']).dt.date
        dap["Billing Time2"] = pd.to_datetime(dap["Billing Time"]).dt.strftime("%Y-%m-%d")
        
        after_start_date =dap["Billing Time2"] >= start_date
        before_end_date = dap["Billing Time2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dap = dap.loc[between_two_dates]

        count=dap.groupby(['Speciality']).size().to_frame(name='Percentage').reset_index()
        sum1=sum(count.Percentage)
        for i,row in count.iterrows():

                count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1*100  
        count=count.rename(columns={"Speciality": "Department"})
        
    elif category=='Area':
        category='District'
        h=500
        
        dfa=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
        df=pd.DataFrame()
        dap=pd.DataFrame()
        df['UHID']=dfa['UHID']
        df['AddedDate']=dfa['visitdate']
        df['pincode']=dfa['pincode']
        
        da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
        dapp = pd.read_excel('mainpage/media/fileupload/OPConsultation.xlsx', sheet_name='WalkInOPConsultation')
        dap['UHID']=dapp['UHID']
        df2=pd.DataFrame()
        df2['pincode']=da['pincode']
        df2['District']=da['Districtname']
        df2=df2.drop_duplicates(subset=['pincode'])

        df['Date'] = pd.to_datetime(df['AddedDate']).dt.date
        df["Date2"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
        dap['Billing Time'] = pd.to_datetime(dapp['BillingTime']).dt.date
        dap["Billing Time2"] = pd.to_datetime(dap["Billing Time"]).dt.strftime("%Y-%m-%d")

        date_start = dap["Billing Time2"].min()
        date_end = dap["Billing Time2"].max()
        after_start_date =df["Date2"] >= date_start #to match dates in opd with demographics table
        before_end_date = df["Date2"] <= date_end
        between_two_dates = after_start_date & before_end_date
        df = df.loc[between_two_dates]

        df=df.dropna()
        dap=dap.dropna()
        after_start_date =df["Date2"] >= start_date # date filter
        before_end_date = df["Date2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        df = df.loc[between_two_dates]

        after_start_date =dap["Billing Time2"] >= start_date
        before_end_date = dap["Billing Time2"] <= end_date
        between_two_dates = after_start_date & before_end_date
        dap = dap.loc[between_two_dates]

        df = pd.merge(df, df2, how='inner',left_on = 'pincode', right_on = 'pincode')
        dw = pd.merge(dap, df, how='inner',left_on = 'UHID', right_on = 'UHID')
        dw['Date'] = pd.to_datetime(dw['AddedDate']).dt.date
        count=dw.groupby(['District']).size().to_frame(name='Percentage').reset_index()
        sum1=sum(count.Percentage)
        for i,row in count.iterrows():
            count.loc[i,'Percentage']=count.at[i,'Percentage']/sum1*100  
     

            
    walkin_title="Walk-in Analysis ("+category+")"+": "+start_date+" to "+end_date

    walkin_chart=alt.Chart(count).mark_bar().encode(  

        alt.X('Percentage:Q',axis=alt.Axis(title='Percentage inflow(%)')),                                          
        alt.Y(category),
        tooltip = [alt.Tooltip(category), 
                    alt.Tooltip('Percentage:Q',title='Percentage inflow(%)')]

     ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='middle',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20,

    ).properties(
        title=walkin_title,
        width = 500, #width and height of bars
        height = h
    )
    g_json=walkin_chart.to_json()
    return g_json


###########################################################AREA ##############################################################################

def area_analysis(department,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    h=300
    category=department
    df=pd.read_excel("mainpage/media/fileupload/DemographicAnalysis.xlsx",engine='openpyxl')
    df = df.drop_duplicates(subset= ["UHID","Department"])

    da=pd.read_excel("mainpage/media/fileupload/kerala pin codes.xlsx",engine='openpyxl')
    ar=pd.DataFrame()
    df2=pd.DataFrame()
    df2['pincode']=da['pincode']
    df2['District']=da['Districtname']
    df2=df2.drop_duplicates(subset=['pincode'])
    df2=df2.drop_duplicates("pincode")    

    df['visitdate'] = pd.to_datetime(df['visitdate']).dt.date
    df["Date2"] = pd.to_datetime(df["visitdate"]).dt.strftime("%Y-%m-%d")
         
    df=df.dropna()
        
    after_start_date =df["Date2"] >= start_date
    before_end_date = df["Date2"] <= end_date
    between_two_dates = after_start_date & before_end_date
    df = df.loc[between_two_dates]

    if category=='OVERALL':
        for i,row in df.iterrows():
            ar.loc[i,'pincode']=df.at[i,'pincode']
            ar.loc[i,'visitdate']=df.at[i,'visitdate']
            ar.loc[i,'UHID']=df.at[i,'UHID']
    else:
        for i,row in df.iterrows():
            if df.loc[i,'Department']==category:
                ar.loc[i,'pincode']=df.at[i,'pincode']
                ar.loc[i,'visitdate']=df.at[i,'visitdate']
                ar.loc[i,'UHID']=df.at[i,'UHID']

    
    dfa=pd.DataFrame()
    dfa = pd.merge(ar, df2, how='inner',left_on = 'pincode', right_on = 'pincode')


    
    count=dfa.groupby(['District']).size().to_frame(name='Percentage').reset_index()
    totw=sum(count.Percentage)
    for i,row in count.iterrows():
        count.loc[i,'Percentage']=count.at[i,'Percentage']/totw   

    area_title="Area-wise Analysis ("+category+")"
    area_chart=alt.Chart(count).mark_bar().encode( 
        alt.X('Percentage:Q',axis=alt.Axis(title='Percentage inflow(%)')),                                          
        alt.Y('District:O'),
        tooltip = [alt.Tooltip('District:O'),
                   alt.Tooltip('Percentage:Q',title='Percentage inflow(%)')]
    
    ).configure_title(
        fontSize=35,
        font='Arial',
        anchor='middle',#center title
        color='black'
    ).configure_axis(
        domainWidth=2,
        domainColor='black',#domain is axis...axis width and color
        labelFontSize=15,
        titleFontSize=20,

    ).properties(
        title=area_title,
        width = 500, #width and height of bars
        height = h
    )
    g_json=area_chart.to_json()
    return g_json

