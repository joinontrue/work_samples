#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# I am going to analyze some of the data available through <data.seattle.gov>.

# Data currently being considered:
#
#  1.City of Seattle, Department of Information Technology,
#      Seattle Police Department
#    "Seattle Police Department Police Report Incident"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/7ais-f98f/rows.csv?accessType=DOWNLOAD
#  
#  2.City of Seattle, Department of Information Technology, Seattle Police
#    Department
#    "Seattle Police Department 911 Incident Response"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/3k2p-39jp/rows.csv?accessType=DOWNLOAD
#  
#  3.Seattle Police Department (http://www.seattle.gov/police/)
#    "Call Data"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/33kz-ixgy/rows.csv?accessType=DOWNLOAD
#  
#  4.Seattle Police Department (http://www.seattle.gov/police/)
#    "Crime Data"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/4fs7-3vj5/rows.csv?accessType=DOWNLOAD
#  
#  5.City of Seattle, Department of Information Technology
#      (http://seattle.gov/police/crime/default.htm)
#    "Seattle Crime Stats by Police Precinct 2008-Present"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/3xqu-vnum/rows.csv?accessType=DOWNLOAD
#  
#  6.Department of Transportation
#    "Road Weather Information Stations"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/egc4-d24i/rows.csv?accessType=DOWNLOAD

# Libraries importing:
#%%= = = = = = = = = = = = = =[ IMPORT LIBRARIES ]= = = = = = = = = = = = = = =
  import sklearn as skl
  import numpy as np
  import scipy as sp
  import matplotlib as mpl
  import pandas as pd
  import datetime as dt
  from datetime import datetime as dt_dt
#%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%= = = = = = = = = = = = = = =[ PARAMETERS ]= = = = = = = = = = = = = = = = =
subset_size=10000
data_dir='./Desktop/career/0_work_samples/Seattle_stats/data/'
#%%= = = = = = = = = = = =[ READ IN CSV AS PANDAS DATA TABLE ]= = = = = = = = =
#Seattle_Police_Department_Police_Report_Incident=pd.read_csv(data_dir+
#    'Seattle_Police_Department_Police_Report_Incident.csv',
#    dtype={
#        
#  'RMS CDW ID':str,
#  'General Offense Number':str,
#  'Offense Code':str,#np.int32,
#  'Offense Code Extension':np.float64,
#  'Offense Type':str,
#  'Summary Offense Code':str,#np.int32,
#  'Summarized Offense Description':str,
#  'Date Reported':str,#dt.datetime,
#  'Occurred Date or Date Range Start':str,#:dt.datetime,
#  'Occurred Date Range End':str,#datetime,
#  'Hundred Block Location':str,
#  'District/Sector':str,
#  'Zone/Beat':str,
#  'Census Tract 2000':np.float64,
#  'Longitude':np.float64,
#  'Latitude':np.float64,
#  'Location':str,
#  'Month':np.int32,
#  'Year':np.int32      
#        
#        }
#    
##    ,nrows=100
#    ,infer_datetime_format=True
#    
#    
#    )
#
##%%
#
#Crime_Data=pd.read_csv(data_dir+'Crime_Data.csv',
#  dtype={
#      'Occurred Time':str,
#      'Reported Time':str
#          },  
#  infer_datetime_format=True
#  )
#
##%%
#Seattle_Police_Department_Police_Report_Incident['Year'][1:100]
##%%
#Seattle_Police_Department_Police_Report_Incident.dtypes
#
##%%
#Seattle_Police_Department_911_Incident_Response=pd.read_csv(data_dir+
#    'Seattle_Police_Department_911_Incident_Response.csv').astype(dtype={'Event Clearance Date':dt.datetime})
##%%
#Seattle_Police_Department_911_Incident_Response.dtypes  
#
#
#
#
#
##%%
#Incident_Response_sub=Seattle_Police_Department_911_Incident_Response[1:100].astype(dtype={'Event Clearance Date':dt.datetime})
##%%
#Incident_Response_sub.dtypes
##%%
#Incident_Response_sub.loc[:,'Event Clearance Date']
#
##%%
#Incident_Response_sub_2=Incident_Response_sub.assign(m=pd.to_datetime(Incident_Response_sub['Event Clearance Date']))
##%%
#Incident_Response_sub_2.columns
#Incident_Response_sub_2.dtypes
##%%
#
#dt_dt.time(Incident_Response_sub_2.m)
#
#Incident_Response_sub_3=Incident_Response_sub_2.assign(d=day(m))
#
##%%
#Seattle_Police_Department_911_Incident_Response.columns
##%%
#Seattle_Police_Department_911_Incident_Response.astype(dtype={'Event Clearance Date':dt.datetime})
#
#
##%%
#dt_dt.strptime(
#    Seattle_Police_Department_911_Incident_Response.loc[:,'Event Clearance Date'].iloc[1:10]
#    ,'%b %d %Y %I:%M:%S:000%p'
#    )
#
##%%
#dt_dt.strptime(calls2.loc[:,'ta'].iloc[i],'%b %d %Y %I:%M:%S:000%p')
#Seattle_Police_Department_911_Incident_Response.loc[:,'Event Clearance Date'][1:10]
#%%
#Call_Data=pd.read_csv(data_dir+'Call_Data.csv')
#%%
Crime_Data=pd.read_csv(data_dir+'Crime_Data.csv',
 dtype={
     'Report Number':str,
     'Occurred Date':str,
     'Occurred Time':str,
     'Reported Date':str,
     'Reported Time':str,
     'Crime Subcategory':str,
     'Primary Offense Description':str,
     'Precinct':str,
     'Sector':str,
     'Beat':str,
     'Neighborhood':str
     }
 )
#%% = = = = = = = = = = = = = = =[ COLUMNS ]= = = = = = = = = = = = = = = = = =
#print(Call_Data.columns);
#  'CAD Event Number'
#  'Event Clearance Description'
#  'Call Type'
#  'Priority'
#  'Initial Call Type'
#  'Final Call Type'
#  'Original Time Queued'
#  'Arrived Time'
#  'Precinct'
#  'Sector'
#  'Beat'

print(Crime_Data.columns);
#  'Report Number'
#  'Occurred Date'
#  'Occurred Time'
#  'Reported Date'
#  'Reported Time'
#  'Crime Subcategory'
#  'Primary Offense Description'
#  'Precinct'
#  'Sector'
#  'Beat'
#  'Neighborhood'
#%% = = = = = = = = = = = = = = =[ ROW COUNTS ]= = = = = = = = = = = = = = = = 
print('len(Call_Data):',len(Call_Data),'\n',
      'len(Crime_Data):',len(Crime_Data),'\n',sep='');
#%% = = = = = = = = = = = = = = =[ SUBSETS ]= = = = = = = = = = = = = = = = = =
#Adding [count] for safe/simple counting.
subset_size=len(Crime_Data);
Call_Data_sub=Call_Data[0:subset_size].assign(count=1);
Crime_Data_sub=Crime_Data[0:subset_size].assign(count=1);
#%% = = = = = = = = = = = = = = =[ TIDYING FORMATS ]= = = = = = = = = = = = = =
Crime_Data_sub_2=Crime_Data[0:subset_size].assign(
    Occurred_Date=pd.to_datetime(Crime_Data_sub['Occurred Date'],format='%m/%d/%Y'),
    Occurred_Time=pd.to_datetime(Crime_Data_sub['Occurred Time'].str.pad(width=4,side='left',fillchar='0'),format='%H%M'),
    Reported_Date=pd.to_datetime(Crime_Data_sub['Reported Date'],format='%m/%d/%Y'),
    Reported_Time=pd.to_datetime(Crime_Data_sub['Reported Time'].str.pad(width=4,side='left',fillchar='0'),format='%H%M')
)
#%% = = = = = = = = = = = = = = =[ MAKE ROOM FOR DATETIMES ]= = = = = = = = = = 
Crime_Data_sub_3=Crime_Data_sub_2.assign(
    Occurred_Datetime='',
    Reported_Datetime='')                
#%% = = = = = = = = = = = = = = =[ ADD DATES AND TIMES ]= = = = = = = = = = = = 
for i in range(0,len(Crime_Data_sub_2)):
  if np.mod(i,1000)==0:
    print(i)
  Crime_Data_sub_3.loc[:,'Occurred_Datetime'].iat[i]=dt_dt.combine(Crime_Data_sub_2.loc[:,'Occurred_Date'].iat[i].date(),
                  Crime_Data_sub_2.loc[:,'Occurred_Time'].iat[i].time())    
  Crime_Data_sub_3.loc[:,'Reported_Datetime'].iat[i]=dt_dt.combine(Crime_Data_sub_2.loc[:,'Reported_Date'].iat[i].date(),
                  Crime_Data_sub_2.loc[:,'Reported_Time'].iat[i].time())    
#%%

##%%    
#Crime_Data_sub_2.columns
#Crime_Data_sub_2.dtypes
#Crime_Data_sub.dtypes
#%%
#a=pd.DataFrame(Report_Incident_sub.groupby(['RMS CDW ID'])['count'].sum())
#a[a['count']>1]
#Report_Incident_sub[pd.isna(Report_Incident_sub['RMS CDW ID'])]
#df1=pd.merge(
#    Call_Data_sub,
#    Incident_Response_sub,
#    how='left',
#    on=['CAD Event Number','CAD Event Number'],
#    suffixes=('__cd','__911'),
#    validate='many_to_one')
#%%= = = = = = = = = = =[ RENAME, TAKE SUBSET FOR DEV ]= = = = = = = = = = = =
#call_data_sub=Call_Data[1:100].rename(index=str, columns={
#    'CAD Event Number':'CAD_event_number',        
#    #- - - - - - - - -[ WHERE ]- - - - - - - - - - - - - - - - - - - - - - - -
#    'Precinct':'precinct',
#    'Sector':'sector',
#    'Beat':'beat',        
#    #- - - - - - - - -[ WHEN ]- - - - - - - - - - - - - - - - - - - - - - - - -
#    'Original Time Queued':'tq',
#    'Arrived Time':'ta',                
#    #- - - - - - - - -[ HOW ]- - - - - - - - - - - - - - - - - - - - - - - - -
#    'Call Type':'channel',        
#    'Priority':'priority',        
#    #- - - - - - - - -[ WHAT ]- - - - - - - - - - - - - - - - - - - - - - - - -
#    'Initial Call Type':'description_i',
#    'Final Call Type':'description_f',
#    'Event Clearance Description':'resolution'
#  })[0:subset_size].assign(count=1);
#print(calls.columns)
#print(len(calls))
#%%= = = = = = = = = = = = =[ REFORMAT TIME FIELDS ]= = = = = = = = = = = = = =
#calls2=calls.assign(
#    tq2=dt.datetime(1700,1,1),
#    ta2=dt.datetime(1700,1,1)
#  );
#for i in range(0,len(calls2)):
#  if np.mod(i+1,1000)==0:
#    print(i+1)
#  calls2.loc[:,'ta2'].iloc[i]= \
#    dt_dt.strptime(calls2.loc[:,'ta'].iloc[i],'%b %d %Y %I:%M:%S:000%p')
#  calls2.loc[:,'tq2'].iloc[i]= \
#    dt_dt.strptime(calls2.loc[:,'tq'].iloc[i],'%m/%d/%Y %I:%M:%S %p')
#print(calls2.loc[:,['ta2','tq2']].iloc[1:1000])    
#%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%