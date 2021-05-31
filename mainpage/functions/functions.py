
import altair as alt
from altair.vegalite.v4.schema.core import JsonDataFormat
import pandas as pd
from altair import datum
from django.shortcuts import render

def handle_file(f,filename):
    with open('mainpage/static/fileupload/'+filename,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


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

        df = pd.read_excel("mainpage/static/fileupload/OPConsultation.xlsx", sheet_name='Walkins June 2020', engine='openpyxl')
        df['date']=pd.to_datetime(df['Consult IN']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]

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
        df2

        bars=alt.Chart(df2,title="Average Waiting time for Each Department(Walkins)").mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
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

            ).interactive()

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
            
        df = pd.read_excel("mainpage/static/fileupload/OPConsultation.xlsx", sheet_name='Walkins June 2020', engine='openpyxl')
        df['date']=pd.to_datetime(df['Consult IN']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]

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
        df2

        bars=alt.Chart(df2,title="Average Waiting time for Each Department(Walkins)").mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis(title='Department Name')),
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

            ).interactive()
        
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
            
        df = pd.read_excel("mainpage/static/fileupload/OPConsultation.xlsx", sheet_name='Appts June 2020', engine='openpyxl')
        df['date']=pd.to_datetime(df['Consultation start Date/Time']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]



        docList= df['Doctor Name'].values.tolist()
        billList= df['Billing Time'].values.tolist()
        inList= df['Consultation start Date/Time'].values.tolist()

        #time difference list
        df['diff_seconds'] =df['Consultation start Date/Time']-df['Billing Time']
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


        bars=alt.Chart(df2,title="Average Waiting time for Each Department(Appointments)").mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
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

            ).interactive()
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
        df = pd.read_excel("mainpage/static/fileupload/OPConsultation.xlsx", sheet_name='Appts June 2020', engine='openpyxl')
        df['date']=pd.to_datetime(df['Consultation start Date/Time']).dt.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        df = df.loc[mask]


        deptList= df['Dept Name'].values.tolist()
        billList= df['Billing Time'].values.tolist()
        inList= df['Consultation start Date/Time'].values.tolist()

        #time difference list
        df['diff_seconds'] =df['Consultation start Date/Time']-df['Billing Time']
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
    

        bars=alt.Chart(df2,title="Average Waiting time for Each Department(Appointments)").mark_bar().encode(
            x=alt.X('AVG', axis=alt.Axis( title='Average Time in Hours')),
            y=alt.Y('DName', axis=alt.Axis( title='Department Name')),
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

            ).interactive()
   
        g_json=bars.to_json()
        return g_json

        
def mlc_analysis(category):
    import pandas as pd
    import altair as alt
    alt.data_transformers.disable_max_rows()
    df = pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    w=pd.Series(df['Is MLC'].value_counts())
    if category=="MLCSpecialty":
        
        input_dropdown = alt.binding_select(options=df['Primary doctor Specialty'].unique(), name="Specialty Name")  # creates drop-down menu of unique department names
        selection = alt.selection_single(fields=['Primary doctor Specialty'], bind=input_dropdown, name='Select')
        area_chart=alt.Chart(df, title="Number of MLC's").mark_bar().transform_filter(selection
                    ).encode(
                    alt.X('Is MLC:N'),
                    alt.Y('count(Is MLC):Q'),
                    tooltip = [alt.Tooltip('Is MLC:N'),
                            alt.Tooltip('count(Is MLC):Q'),
                            alt.Tooltip('Primary doctor Specialty')
                            ]
                            
                        
                #).interactive(# zoom
                ).add_selection(selection
                    ).interactive(
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
        area_chart=alt.Chart(df, title="Number of MLC's").mark_bar().transform_filter(selection
                    ).encode(
                    alt.X('Is MLC:N'),
                    alt.Y('count(Is MLC):Q'),
                    tooltip = [alt.Tooltip('Is MLC:N'),
                            alt.Tooltip('count(Is MLC):Q'),
                            alt.Tooltip('Ward Name')
                            ]
                        
                #).interactive(# zoom
                ).add_selection(selection
                    ).interactive(
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
        df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        data = [df['Discharge Date & Time '], df['Ward Name']]

        headers = ['Discharge','Wardname']

        df2 = pd.concat(data, axis=1, keys=headers)
        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]
        gk=df2.groupby(by=['Wardname']).count().reset_index()

        gk=gk.rename(columns={'Discharge':'Count'})

        area_chart=alt.Chart(gk).mark_bar().encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Wardname:N',axis=alt.Axis(title=None)),
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

            ).interactive()


        g_json=area_chart.to_json()
        return g_json
    elif category=='EachWardBed':
        df1=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        #alt.data_transformers.disable_max_rows()
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]     #selecting data frame rows in the desired date range

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
            ).interactive()

        g_json=area_chart.to_json()
        return g_json
    elif category=='AllWardBed':
        df1=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]     #selecting data frame rows in the desired date range

        bars=alt.Chart(df1, title='Number of discharges from all wards: Bed-wise').mark_bar(size=15).encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

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

            ).interactive()

       
        g_json=bars.to_json()
        return g_json
    elif category=='EachSpec':
        df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        data = [df['Discharge Date & Time '], df['Primary doctor Specialty']]

        headers = ['Discharge','Specialty']

        df2 = pd.concat(data, axis=1, keys=headers)

        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format


        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]

        gk=df2.groupby(by=['Specialty']).count().reset_index()

        gk=gk.rename(columns={'Discharge':'Count'})

        area_chart=alt.Chart(gk).mark_bar().encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Specialty:N',axis=alt.Axis(title=None)),
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
        ).interactive()
        g_json=area_chart.to_json()
        return g_json
    elif category=='EachDoc':
        
        df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows()
        data = [df['Discharge Date & Time '], df['Primary doctor']]

        headers = ['Discharge','Doctor']

        df2 = pd.concat(data, axis=1, keys=headers)

        df2['date']=pd.to_datetime(df2['Discharge']).dt.strftime("%Y-%m-%d") #string to date format


        df2=df2.loc[(df2["date"]>=start_date) & (df2["date"]<=end_date)]

        gk=df2.groupby(by=['Doctor']).count().reset_index()

        gk=gk.rename(columns={'Discharge':'Count'})

        area_chart=alt.Chart(gk).mark_bar(size=15).encode(alt.X('Count:Q',title='Number of Discharges'),

            alt.Y('Doctor:N',axis=alt.Axis(title=None)),
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

            ).interactive()

        

        g_json=area_chart.to_json()
        return g_json

    elif category=='BedEachWard':
        df1=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows() #to allow more than 5000 rows in display
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        
        df1=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]

        area_chart=alt.Chart(df1).mark_bar().encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

            alt.Y('Billable Bed Type:N',axis=alt.Axis(title=None)),

            alt.Color('Billable Bed Type', legend=alt.Legend(title="Billable Bed Type")),

            tooltip = [

                    alt.Tooltip('count(Billable Bed Type)'),

                    alt.Tooltip('Billable Bed Type')

                    ]

        ).facet(row=alt.Row('Ward Name:N', header=alt.Header(title='Ward Name',labelOrient='top',labelAngle=0)) #categorize orders based on ordering station

            ).properties(title='Number of discharges from each ward: Bed-wise'

            ).interactive(
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
        df1=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
        alt.data_transformers.disable_max_rows() #to allow more than 5000 rows in display
        df1["date2"] = pd.to_datetime(df1['Discharge Date & Time ']).dt.strftime("%Y-%m-%d") #string to date format
        df=df1.loc[(df1["date2"]>=start_date) & (df1["date2"]<=end_date)]

        bars=alt.Chart(df1, title='Number of discharges from all wards: Bed-wise').mark_bar().encode(alt.X('count(Billable Bed Type):Q',title='Number of Discharges'),

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
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name']]
    headers = ['Discharge','Wardname']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Wardname']==category)]
    df3['date']=pd.to_datetime(df3['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    
    
    t1=pd.Series(df3['date'].value_counts())
    pdf1=t1.to_frame()
    pdf1=pdf1.reset_index()
    pdf1=pdf1.rename(columns={"index":"date", "date":"count"})
    print(sum(pdf1['count']))
    area_chart=alt.Chart(pdf1, title="Number of patients discharged from ("+category+")").mark_bar().encode(
        alt.X('count'),
        alt.Y('date'),
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
        ).properties(width=300,height=300

            ).interactive()
    
    g_json=area_chart.to_json()
    return g_json

def spec_doc_and_spec(doctor,specialty,start_date,end_date):
    category1=specialty
    category2=doctor
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Billable Bed Type'], df['Primary doctor Specialty'], df['Primary doctor']]

    headers = ['Discharge', 'BedType', 'Speciality', 'Doctor']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category1) & (df2["Doctor"]==category2)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range
    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),

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
        ).properties(title="("+category1+") speciality: Doctor ("+category2+")",width=300,height=300

            ).interactive()

    g_json=area_chart.to_json()
    return g_json

def specific_spec_bed(specialty,start_date,end_date):
    category=specialty
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty']]

    headers = ['Discharge','Wardname', 'BedType', 'Speciality']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range


    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),

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

            ).interactive()
    
    g_json=area_chart.to_json()
    return g_json

def specific_discharge_analysis(wardname,start_date,end_date):
    category=wardname
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type']]

    headers = ['Discharge','Wardname', 'BedType']

    df2 = pd.concat(data, axis=1, keys=headers)
   
    df3= df2[(df2['Wardname']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range

    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),
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

        ).interactive()

    
    g_json=area_chart.to_json()
    return g_json

def spec_doc_bed(doctor, start_date, end_date):
    category=doctor
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Primary doctor'], df['Billable Bed Type']]
    headers = ['Discharge','Primary doctor', 'BedType']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Primary doctor']==category)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range

    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),

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

            ).interactive()

    g_json=area_chart.to_json()
    return g_json




def spec_ward_and_spec_and_doc(wardname, specialty, doctor,start_date,end_date):
    category1=wardname
    category2=specialty
    category3=doctor
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty'], df['Primary doctor']]
    headers = ['Discharge','Wardname', 'BedType', 'Speciality', 'Doctor']
    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category2) & (df2['Wardname']==category1) & (df2["Doctor"]==category3)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range


    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),

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

            ).interactive()


    g_json=area_chart.to_json()
    return g_json


def spec_ward_and_spec(wardname, specialty,start_date,end_date):
    category1=wardname
    category2=specialty
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')
    alt.data_transformers.disable_max_rows()
    data = [df['Discharge Date & Time '], df['Ward Name'], df['Billable Bed Type'], df['Primary doctor Specialty']]

    headers = ['Discharge','Wardname', 'BedType', 'Speciality']

    df2 = pd.concat(data, axis=1, keys=headers)
    df3= df2[(df2['Speciality']==category2) & (df2['Wardname']==category1)]
    gk=df3.groupby(by=['BedType', 'Discharge']).count().reset_index()
    gk['date']=pd.to_datetime(gk['Discharge']).dt.strftime("%Y-%m-%d") #string to date format
    gk=gk.loc[(gk["date"]>=start_date) & (gk["date"]<=end_date)]     #selecting data frame rows in the desired date range

    area_chart=alt.Chart(gk).mark_bar(size=20).encode(alt.X('count(BedType):Q',title='Number of Discharges'),

        alt.Y('BedType:N',axis=alt.Axis(title=None)),

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

            ).interactive()
            
    g_json=area_chart.to_json()
    return g_json



def payments_analysis():
    import matplotlib.pyplot as plt
    df=pd.read_excel("mainpage/static/fileupload/DischargeAnalysis.xlsx",engine='openpyxl')

    a=df['PaymentType'].str.count("Cash").sum()
    b=df['PaymentType'].str.count("Credit").sum()
    labels = ['Cash','Credit']
    explodeTuple = (0.1,0.1)
    sizes=[a,b]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True,explode=explodeTuple)
    ax1.axis('equal')
    ax1.set_title("payment type")
    plt.show()
    print ("Total number of patients paying by cash or credit.")
    print (a)
    print(b)

################################## amala's team  ##################################################################################################

def pharmacyorders_from_nursing_stations_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    dip=pd.read_excel("mainpage/static/fileupload/Pharmacy.xlsx",usecols=['OrderId','OrderDateTime','UHId','OrderingStation','PriorityName'],engine='openpyxl')    #create dataframe
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
            ).properties(title='Pharmacy Orders From Each Nursing Station: Priority-wise'
            ).interactive()
            g_json=pharmacy1_chart.to_json()
            return g_json

        elif category=='OrderingStation':
            #Pharmacy Orders From Each Nursing Stations- ORDERING STATION              
            data = pd.read_excel('mainpage/static/fileupload/Pharmacy.xlsx',usecols=['OrderDateTime','OrderId','OrderingStation','PriorityName'])
            data["OrderDate"] = pd.to_datetime(data["OrderDateTime"]).dt.strftime("%Y-%m-%d") #convert to desired date format
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
            ).add_selection(select_station).interactive()    #so that we can select a station


            priority_chart = alt.Chart(df1).mark_bar(size=30).encode(
                    alt.Y('Counts',title='Number of Orders'),
                    alt.X("PriorityName",title='Priority'),
                    color=alt.Color('PriorityName',title='Priority', scale=alt.Scale(scheme='tableau10')),
                    tooltip = [
                        alt.Tooltip('PriorityName',title='Priority Name'),
                        alt.Tooltip('Counts',title='Number of Orders'),
                        ]
                ).transform_filter(select_station).properties(width=100).interactive()   #apply filter



            pharmacy2_chart = alt.hconcat(station_chart, priority_chart).configure_title(fontSize=20, font='Calibri',dy=-25, anchor='middle', color='black'
                    ).configure_axis(domainWidth=2,
                    domainColor='black',#domain is axis...axis width and color
                    labelFontSize=15, titleFontSize=20,
                    ).configure_legend(titleFontSize=15,labelFontSize=15
                    ).properties(
                title="Pharmacy Orders From Each Nursing Station and Priority-wise"
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
            ).properties(title='Pharmacy Orders From Each Nursing Station: All Priorities'
            ).interactive()
            g_json=pharmacy3_chart.to_json()
            return g_json

def pharmacyorders_per_patient_analysis(start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/static/fileupload/Pharmacy.xlsx",usecols=['OrderDateTime','UHId'],engine='openpyxl')    #create dataframe
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
        ).properties(title='Pharmacy Orders - Number of Orders per Patient per Day',width=300,height=300).interactive()
        g_json=orderperpatient_chart.to_json()
        return g_json

def topmedicines_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/static/fileupload/Top100Medicines.xlsx",usecols=['ItemName', 'Quantity','Unit', 'ItemCatagory','Station','BillDateTime'],engine='openpyxl')    #create dataframe
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
                    ).interactive()

            topmedicines_chart1 = alt.vconcat()

            for station in stations:
                topmedicines_chart1 &= base.transform_filter(datum.Station == station).properties(title=station)
            topmedicines_chart1.properties(title='Top Movable Medicines in Each Station',width=2000,height=500)
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
            ).properties(title='Top 100 Movable Medicines in Hospital',width=800,height=2000).interactive()
            g_json=topmedicines_chart2.to_json()
            return g_json
            

def drugstock_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/static/fileupload/Top100Medicines.xlsx",usecols=['ItemName', 'Quantity','Unit', 'ItemCatagory','Station','BillDateTime'],engine='openpyxl')    #create dataframe
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
                    ).interactive()

            drug_chart1 = alt.vconcat()

            for category in categories:
                drug_chart1 &= base.transform_filter(datum.ItemCatagory == category).properties(title=category)
            drug_chart1.properties(title='Drug Stock Analysis')
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
            ).properties(title='Drug Stock Analysis',width=600).interactive()
            g_json=drug_chart2.to_json()
            return g_json


def radiology_analysis(test,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df=pd.read_excel("mainpage/static/fileupload/Radiology.xlsx",usecols=['RegistrationNo','sex', 'Age','Item Name',"Bill Datetime"],engine='openpyxl')
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

        title='Radiology  (Test wise Analysis) : '+test
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
                ).properties(title=title,height=300).interactive()

        g_json=radio_chart.to_json()
        return g_json



def surgery_analysis(category,start_date,end_date):
    alt.data_transformers.disable_max_rows()
    df1 = pd.read_excel("mainpage/static/fileupload/SurgeryAnalysis.xlsx",usecols=["UHID","SurgeryName","Surgery Department","Date Of Surgery"],engine='openpyxl')
    df2 = pd.read_excel("mainpage/static/fileupload/DemographicAnalysis.xlsx",usecols=["UHID","AgeYears","Sex"],engine='openpyxl')
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
                ).properties(title='Surgery - Surgery Name wise analysis',height=300,width=200
            ).interactive() # to zoom 
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
            ).properties(title='Surgery - Department wise analysis',height=300,width=200
            ).interactive() # to zoom 
            g_json=surgery_chart2.to_json()
            return g_json


################################## varsha's team  ##################################################################################################