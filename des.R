getwd()

library(readxl)

w_a <- read_excel("~/R/git_exercise-master/ahmedabad-weather.xlsx")
w_b <- read_excel("~/R/git_exercise-master/bangalore-weather.xlsx")
df2 <-  read.csv("~/R/git_exercise-master/bangalore-cas-alerts.csv",stringsAsFactors=FALSE)
df2$deviceCode_deviceCode <- as.character(df2$deviceCode_deviceCode)

names(df2) <- c("deviceCode",             
                "location_latitude",      
                "location_longitude",     
                "location_wardName",      
                "pyld_alarmType",         
                "pyld_speed",             
                "time_recordedTime_.date")
str(df2)

df2$time_date <- as.Date(df2$time_recordedTime_.date)
df2$time_recordedTime_.date <- strptime(df2$time_recordedTime_.date,format="%Y-%m-%dT%H:%M:%S.000Z")
df2$time_time <- format(df2$time_recordedTime_.date,format="%H:%M:%S")

rapply(df2[,c(1,4,5,6,8)],function(x)length(unique(x)))
tt<- ftable(xtabs(~deviceCode+pyld_alarmType, df2))
tt<-as.matrix(tt)
tt<-data.frame(tt)
des<-describe(tt,IQR=TRUE,quant=c(.05,.25,.50,.75,.95))

xtabs(~time_time+pyld_alarmType,sub)

w_b$temperature <- as.numeric(w_b$temperature)
w_b$visibility <- as.numeric(w_b$visibility)
w_b$test <- paste(w_b$weatherDate[1:5036], w_b$time[1:5036])
w_b$weatherDate <- as.Date(w_b$test,format="%Y%m%d %H:%M")
w_b$time <- format(strptime(w_b$test,format="%Y%m%d %H:%M"), format="%H:%M:%S")
describe(w_b)
str(w_b)
