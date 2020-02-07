#use pacman to load all the pakages you'll use for the project
pacman::p_load(pacman, bibliometrix, dplyr, GGally, ggplot2, ggthemes, ggvis,
               httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr,
               grid, gridExtra, gapminder, tidyverse, frequency)

## ----Data loading--------------------------------------------------------

#load the files that contains the data
X<-read.csv(file.choose(), header = TRUE, sep = ",")

#specify the file length using options to get all the data load 
options(max.print = 1000000)

#check if the data is correct by loading the dataset
X
#create variable of total citations and pubication year
Tcitation<-X$Total.Citations
Pyear<-X$Publication.Year
Apyear<-X$Average.per.Year

#---------------------------------------WORKING WITH PUBLICATION YEAR------------------------------------------

#create vel to stire the table of publication
vel<-table(X$Publication.Year)

#create the axis range of x
x<-seq(1970,2020, len = 5)

#-----------PLOT THE GRAPHS---------------------------------

#plot vel number of pulbication in web of science on mikoko
barplot(vel, col = "#FFFF09",main="NUMBER OF PUBLICATION IN WEB OF SCIENCE ON MIKOKO", ylab = "PUBLICATIONS", xlab = "YEAR")

#plot graph of frequency of mikoko mangrove journals per year
barplot(jymT, main = "FREQUENCY OF MIKOKO JOURNALS PER YEAR",xlab = "YEAR",ylab = "FREQUINCY",col = "#FFFF09")
#plot a histogram 
hist(vel, main = "HISTOGRAM OF PUBLICATION PER YEAR", col = "#FFFF09", xlab = "VOLUME", ylab = "FREQUENCY")

plot(Tcitation~Pyear, data = X, pch=16, col = "#ffff09",xlab="TOTAL CITATION",ylab = "PUBLICATION YEAR",main="TOTAL CITATION OF MANGROVE ARTICLE PER YEAR")
plot(Apyear~Pyear, data = X, pch=16, col = "#ffff09",xlab="AVERAGE PER YEAR",ylab = "PUBLICATION YEAR",main="AVERAGE PUBLICATION BETWEEN THE YEAR 1980 TO 2020")
#-----------------------------------WORKING WITH TOTAL CITATION-------------------------------------------------

#table total citation
bk<-table(X$Total.Citations)

#plot a graph of tatal citation
barplot(bk, xlab = "Total Citation", ylab = "frequency", main = "TOTAL CITATION", col = "#ffff99")

#----------------------------------WORKING WITH VOLUMES---------------------------------------------------------------
Vtable<-table(X$Volume)

#plot
barplot(Vtable, col = "#ffff99", main = "FREQUENCY OF AVAILABLE VOLUMES", xlab = "VOLUME", ylab = "FREQUENCY")

#plot a histogram
hist(Vtable, main = "HISTOGRAM OF VOLUME", col = "#FFFF09", xlab = "FREQUENCY", ylab = "VOLUME")

#to unload all the packages after finishing
p_unload(all