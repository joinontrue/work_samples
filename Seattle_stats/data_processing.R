#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# I am going to analyze some of the data available through <data.seattle.gov>.

# Data used by this script:
#  
#  Seattle Police Department (http://www.seattle.gov/police/)
#    "Crime Data"
#    Downloaded 2018-09-16 from
#    https://data.seattle.gov/api/views/4fs7-3vj5/rows.csv?accessType=DOWNLOAD

# Libraries loaded:
library(dplyr)
library(data.table)
library(ggplot2)
library(stats)
library(stringr)
library(lubridate)
library(tidyr)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# = = = = = = = = = = = = =[ READ IN DATA ]= = = = = = = = = = = = = = = = = =
dir_path=paste0('C:\\Users\\Emily\\Desktop\\career\\0_work_samples\\',
 'Seattle_stats\\')
Crime_Data_o<-read.csv(paste0(dir_path,'data\\Crime_Data.csv'),sep=',')

#= = = = = = = = = = = = = =[ RENAME, TAKE SUBSET ]= = = = = = = = = = = = = =
# n=1000
n=nrow(Crime_Data_o)
crime_data<-data.frame(
  report_number=Crime_Data_o$Report.Number[1:n],
  occurred_date=Crime_Data_o$Occurred.Date[1:n],
  occurred_time=Crime_Data_o$Occurred.Time[1:n],
  reported_date=Crime_Data_o$Reported.Date[1:n],
  reported_time=Crime_Data_o$Reported.Time[1:n],
  crime_subcategory=Crime_Data_o$Crime.Subcategory[1:n],
  primary_offense_description=Crime_Data_o$Primary.Offense.Description[1:n],
  precinct=Crime_Data_o$Precinct[1:n],
  sector=Crime_Data_o$Sector[1:n],
  beat=Crime_Data_o$Beat[1:n],
  neighborhood=Crime_Data_o$Neighborhood[1:n]
)

#= = = = = = = = =[ REFORMAT DATES, TAKE DIFF, AGG CATEGORIES ]= = = = = = = =
df<-crime_data%>%
  mutate(
    occurred_datetime=
      as.POSIXct(strptime(paste0(
        occurred_date,
        substr(paste0(10000+occurred_time),2,5)
      ),format='%m/%d/%Y%H%M')),
    reported_datetime=
      as.POSIXct(strptime(paste0(
        reported_date,
        substr(paste0(10000+reported_time),2,5)
      ),format='%m/%d/%Y%H%M')),
    dt=
      as.numeric(
        difftime(
        reported_datetime,
        occurred_datetime,
        units='d')),
    crime_subcategory_2=
      ifelse(crime_subcategory%like%'AGGRAVATED ASSAULT','agg.assault',
      ifelse(crime_subcategory%like%'ARSON','arson',
      ifelse(crime_subcategory%like%'BURGLARY','burglary',
      ifelse(crime_subcategory%like%'DUI','DUI',
      ifelse(crime_subcategory%like%'HOMICIDE','homicide',
      ifelse(crime_subcategory%like%'NARCOTIC','narcotic',
      ifelse(crime_subcategory%like%'OTHER','(other)',
      ifelse(crime_subcategory%like%'PROSTITUTION','prost.',
      ifelse(crime_subcategory%like%'RAPE','rape',
      ifelse(crime_subcategory%like%'ROBBERY','robbery',
      ifelse(crime_subcategory%like%'THEFT','theft','other'
     ))))))))))))


#=================[ dt DISTRIBUSTIONS BY CRIME TYPE BEGINS ]==================

#- - - - - - - - - - - - -[ X BOUNDS, log_10*(dt) ]- - - - - - - - - - - - - -
#Take log10 of dt. If dt is 0, count as log10(min(dt>0))-bin_width.
#If dt is <0, count as na.
bin_width=0.5
zerosub<-df%>%filter(dt>0)%>%summarize(zerosub=
  floor(log10(min(dt)))-bin_width)%>%as.numeric()
log_min<-df%>%filter(dt>0)%>%summarize(log_min=
  floor(log10(min(dt))))%>%as.numeric()
log_max<-df%>%filter(dt>0)%>%summarize(log_max=
  ceiling(log10(max(dt))))%>%as.numeric()
df<-df%>%mutate(log_dt=ifelse(dt>0,log10(dt),ifelse(is.na(dt),NA,zerosub)))


#----------------------------[ FACET GRIDS BEGINS ]---------------------------
#- - - - - - - - -[ HOMICIDE/AGGRAVATED ASSAULT/RAPE/ROBBERY ]- - - - - - - -
dists_1<-ggplot(df%>%filter(is.element(crime_subcategory_2,c(
  'homicide',
  'agg. assault',
  'rape',
  'robbery'
  ))))+
stat_bin(aes(x=log_dt,y=stat(density)),
  color="black",
  fill="light green",
  breaks=c(zerosub,seq(log_min,log_max,bin_width))
  )+
scale_x_continuous(
  breaks=c(zerosub+(bin_width/2),
           as.integer(seq(log_min,log_max,bin_width))+(bin_width/2)),
  labels=c('-Inf',as.integer(seq(log_min,log_max,bin_width)))
  )+
scale_y_discrete()+
labs(title="time from crime to reporting",
  x=expression('log'[10]*'(days)'))+
facet_grid(crime_subcategory_2~.)

jpeg(paste0(dir_path,'output\\dists_1.jpg'))
print(dists_1)
dev.off()
print(dists_1)

#- - - - - - - - - - - - -[ THEFT/ARSON/BURGLARY ]- - - - - - - - - - - - - -
dists_2<-ggplot(df%>%filter(is.element(crime_subcategory_2,c(
  'theft',
  'arson',
  'burglary'
))))+
  stat_bin(aes(x=log_dt,y=stat(density)),
           color="black",
           fill="light green",
           breaks=c(zerosub,seq(log_min,log_max,bin_width))
  )+
  scale_x_continuous(
    breaks=c(zerosub+(bin_width/2),
             as.integer(seq(log_min,log_max,bin_width))+(bin_width/2)),
    labels=c('-Inf',as.integer(seq(log_min,log_max,bin_width)))
  )+
  scale_y_discrete()+
  labs(title="time from crime to reporting",
    x=expression('log'[10]*'(days)'))+
  facet_grid(crime_subcategory_2~.)

jpeg(paste0(dir_path,'output\\dists_2.jpg'))
print(dists_2)
dev.off()
print(dists_2)

#- - - - - - - - - -[ DUI/NARCOTIC/PROSTITUTION/OTHER ]- - - - - - - - - - - -
dists_3<-ggplot(df%>%filter(is.element(crime_subcategory_2,c(
  'DUI',
  'narcotic',
  'prost.',
  '(other)'
))))+
  stat_bin(aes(x=log_dt,y=stat(density)),
           color="black",
           fill="light green",
           breaks=c(zerosub,seq(log_min,log_max,bin_width))
  )+
  scale_x_continuous(
    breaks=c(zerosub+(bin_width/2),
             as.integer(seq(log_min,log_max,bin_width))+(bin_width/2)),
    labels=c('-Inf',as.integer(seq(log_min,log_max,bin_width)))
  )+
  scale_y_discrete()+
  labs(title="time from crime to reporting",
    x=expression('log'[10]*'(days)'))+
  facet_grid(crime_subcategory_2~.)

jpeg(paste0(dir_path,'output\\dists_3.jpg'))
print(dists_3)
dev.off()
print(dists_3)

#==================[ dt DISTRIBUSTIONS BY CRIME TYPE ENDS ]===================


# = = = = = = = =[ AVERAGE DAYS BETWEEN OCCURANCE AND REPORTING ]= = = = = = =
df_sum<-df%>%
  group_by(crime_subcategory)%>%
  summarize(
    count=n(),
    dt_mean=mean(dt,na.rm=TRUE),
    dt_median=median(dt,na.rm=TRUE)
  )
View(df_sum)

df_sum<-df%>%
  group_by(crime_subcategory,year=year(reported_datetime))%>%
  summarize(
    count=n(),
    dt_mean=mean(dt,na.rm=TRUE),
    dt_median=median(dt,na.rm=TRUE)
    )%>%arrange(year,.by_group=TRUE)
View(df_sum)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%