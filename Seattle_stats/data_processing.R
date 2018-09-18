#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# I am going to analyze some of the data the Seattle Police Department 
# publishes.

# Data used:
#   Seattle Police Department (http://www.seattle.gov/police/) Call Data,
#   downloaded (2018-09-04) from
#   https://data.seattle.gov/api/views/33kz-ixgy/rows.csv?accessType=DOWNLOAD
# Libraries loaded:
    library(dplyr)
    library(data.table)
    library(ggplot2)
    library(stats)
    library(stringr)
    library(lubridate)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
# = = = = = = = = = = = = =[ READ IN DATA ]= = = = = = = = = = = = = = = = = =
Call_Data<-read.csv(
  file='C:\\Users\\Emily\\Desktop\\github\\Call_Data.csv',sep=',')

#= = = = = = = = = =[ TAKE SUBSET FOR EASIER CODE DEVELOPMENT ]= = = = = = = =
n=1000
df<-data.frame(
        t_i=Call_Data$Original.Time.Queued[1:n],
        t_f=Call_Data$Original.Time.Queued[1:n],
        
        precinct=Call_Data$Precinct[1:n],
        beat=Call_Data$Beat[1:n],
        sector=Call_Data$Sector[1:n],
        
        call_type_i=Call_Data$Initial.Call.Type[1:n],
        call_type_f=Call_Data$Final.Call.Type[1:n],
        call_type=Call_Data$Call.Type[1:n],
        priority=Call_Data$Priority[1:n]
      ) #%>%

View(df)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%