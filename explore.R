# investigate holidays

library(data.table)
dt <- fread('holidays_gfkproject.csv')
dt[, date:=as.Date(date)]

dt[, month:=as.Date(paste0(substr(as.character(date), 1, 7), '-01'))]
setcolorder(dt, c('country','date','month','public','name'))

monthly <- dt[, list(Npublic=length(which(public==T)), Nnonpublic = length(which(public==F))),by=c('country','month')]

tmp = dcast(monthly, month~country, value.var=c('Npublic'), fill = 0)

library(lattice)

xyplot(Npublic~month|country, data = monthly, type='l', main = 'Number of public holidays, by country')

xyplot(Npublic+Nnonpublic~month|country, data = monthly, type='l', main = 'Number of public and non-public holidays, by country', auto.key=T)

library(xlsx)
write.xlsx(tmp, 'holidays_gfkproject.xlsx', append = FALSE, sheetName = 'npublic_holidays', row.names=F)
write.xlsx(dt, 'holidays_gfkproject.xlsx', append = TRUE, sheetName = 'rawdata', row.names=F)

