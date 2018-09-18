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
Seattle_Police_Department_Police_Report_Incident=pd.read_csv(data_dir+
    'Seattle_Police_Department_Police_Report_Incident.csv')
Seattle_Police_Department_911_Incident_Response=pd.read_csv(data_dir+
    'Seattle_Police_Department_911_Incident_Response.csv')
Call_Data=pd.read_csv(data_dir+'Call_Data.csv')
Crime_Data=pd.read_csv(data_dir+'Crime_Data.csv')
Seattle_Crime_Stats_by_Police_Precinct_2008_to_Present=pd.read_csv(data_dir+
    'Seattle_Crime_Stats_by_Police_Precinct_2008-Present.csv')
Road_Weather_Information_Stations=pd.read_csv(data_dir+
    'Road_Weather_Information_Stations.csv')

#%% = = = = = = = = = = = = = = =[ COLUMNS ]= = = = = = = = = = = = = = = = = =
print(Seattle_Police_Department_Police_Report_Incident.columns);
#  'RMS CDW ID'
#  'General Offense Number'
#  'Offense Code'
#  'Offense Code Extension'
#  'Offense Type'
#  'Summary Offense Code'
#  'Summarized Offense Description'
#  'Date Reported'
#  'Occurred Date or Date Range Start'
#  'Occurred Date Range End'
#  'Hundred Block Location'
#  'District/Sector'
#  'Zone/Beat'
#  'Census Tract 2000'
#  'Longitude'
#  'Latitude'
#  'Location'
#  'Month'
#  'Year'

print(Seattle_Police_Department_911_Incident_Response.columns);
#  'CAD CDW ID'
#  'CAD Event Number'
#  'General Offense Number'
#  'Event Clearance Code'
#  'Event Clearance Description'
#  'Event Clearance SubGroup'
#  'Event Clearance Group'
#  'Event Clearance Date'
#  'Hundred Block Location'
#  'District/Sector'
#  'Zone/Beat'
#  'Census Tract'
#  'Longitude'
#  'Latitude'
#  'Incident Location'
#  'Initial Type Description'
#  'Initial Type Subgroup'
#  'Initial Type Group'
#  'At Scene Time'

print(Call_Data.columns);
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

print(Seattle_Crime_Stats_by_Police_Precinct_2008_to_Present.columns);
#  'Police Beat'
#  'CRIME_TYPE'
#  'CRIME_DESCRIPTION'
#  'STAT_VALUE'
#  'REPORT_DATE'
#  'Sector'
#  'Precinct'
#  'Row_Value_ID'

print(Road_Weather_Information_Stations.columns);
#  'StationName'
#  'StationLocation'
#  'DateTime'
#  'RecordId'
#  'RoadSurfaceTemperature'
#  'AirTemperature'

#%% = = = = = = = = = = = = = = =[ ROW COUNTS ]= = = = = = = = = = = = = = = = 
print('len(Seattle_Police_Department_Police_Report_Incident):',
        len(Seattle_Police_Department_Police_Report_Incident),'\n',
      'len(Seattle_Police_Department_911_Incident_Response):',
        len(Seattle_Police_Department_911_Incident_Response),'\n',      
      'len(Call_Data):',len(Call_Data),'\n',
      'len(Crime_Data):',len(Crime_Data),'\n',            
      'len(Seattle_Crime_Stats_by_Police_Precinct_2008_to_Present):',
        len(Seattle_Crime_Stats_by_Police_Precinct_2008_to_Present),'\n',      
      'len(Seattle_Real_Time_Fire_911_Calls):',
        len(Seattle_Real_Time_Fire_911_Calls),'\n',            
      'len(Road_Weather_Information_Stations):',
        len(Road_Weather_Information_Stations),'\n',
      'len(Traffic_Flow_Map_Volumes):',len(Traffic_Flow_Map_Volumes),sep='');
#%% = = = = = = = = = = = = = = =[ SUBSETS ]= = = = = = = = = = = = = = = = = =
#Adding [count] for safe/simple counting.
Report_Incident_sub= \
  Seattle_Police_Department_Police_Report_Incident[0:subset_size].assign(
  count=1);
Incident_Response_sub= \
  Seattle_Police_Department_911_Incident_Response[0:subset_size].assign(
  count=1);
Call_Data_sub=Call_Data[0:subset_size].assign(count=1);
Crime_Data_sub=Crime_Data[0:subset_size].assign(count=1);
Crime_Stats_by_Precinct_sub= \
  Seattle_Crime_Stats_by_Police_Precinct_2008_to_Present[0:subset_size].assign(
  count=1);
Road_Weather_Information_Stations_sub= \
  Road_Weather_Information_Stations[0:subset_size].assign(count=1);

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
#%%  
print(Report_Incident_sub.head(),
  Incident_Response_sub.head(),
  Call_Data_sub.head(),
  Crime_Data.head(),
  Crime_Stats_by_Precinct_sub.head(),
  Road_Weather_Information_Stations_sub.head()
  )
#%%= = = = = = = = = = =[ RENAME, TAKE SUBSET FOR DEV ]= = = = = = = = = = = =
calls=Call_Data.rename(index=str, columns={
    'CAD Event Number':'CAD_event_number',        
    #- - - - - - - - -[ WHERE ]- - - - - - - - - - - - - - - - - - - - - - - -
    'Precinct':'precinct',
    'Sector':'sector',
    'Beat':'beat',        
    #- - - - - - - - -[ WHEN ]- - - - - - - - - - - - - - - - - - - - - - - - -
    'Original Time Queued':'tq',
    'Arrived Time':'ta',                
    #- - - - - - - - -[ HOW ]- - - - - - - - - - - - - - - - - - - - - - - - -
    'Call Type':'channel',        
    'Priority':'priority',        
    #- - - - - - - - -[ WHAT ]- - - - - - - - - - - - - - - - - - - - - - - - -
    'Initial Call Type':'description_i',
    'Final Call Type':'description_f',
    'Event Clearance Description':'resolution'
  })[0:subset_size]
#print(calls.columns)
#print(len(calls))
#%%= = = = = = = = = = = = =[ REFORMAT TIME FIELDS ]= = = = = = = = = = = = = =
calls2=calls.assign(
    tq2=dt.datetime(1700,1,1),
    ta2=dt.datetime(1700,1,1)
  );
for i in range(0,len(calls2)):
  if np.mod(i+1,1000)==0:
    print(i+1)
  calls2.loc[:,'ta2'].iloc[i]= \
    dt_dt.strptime(calls2.loc[:,'ta'].iloc[i],'%b %d %Y %I:%M:%S:000%p')
  calls2.loc[:,'tq2'].iloc[i]= \
    dt_dt.strptime(calls2.loc[:,'tq'].iloc[i],'%m/%d/%Y %I:%M:%S %p')
#print(calls2.loc[:,['ta2','tq2']].iloc[1:1000])    
#%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%