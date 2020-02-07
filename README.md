# R_Data_Statistics
bibliometrics
creating a bibliometrix analysis of the mikoko project 

we strat the project analysis by installing pacman
the code used to install pacman is
install.package("pacman")
pacman is the initials of package manager
this package is used to help you manage and install other package as you progess with your project
#How it is used
pacman::p_load(the packages to be loaded)
eg, pacman::p_load(pacman, bibliometrix, dplyr, GGally, ggplot2, ggthemes, ggvis,
               httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr,
               grid, gridExtra, gapminder, tidyverse, frequency)
    to remove all the packages loaded use pacman::p_unload(all) to unload all the packges loadd
    to remove one or two packages use pacman::p_unload(the name of the package to be unloaded)
    eg pacman::p_uload(bibliometrix) or pacman::p_unload(frequency, shiny, anyother package to unload)
 #How to install packages in R
 To install a package in R studio use this code
 install.package("the name of package to be installed")
 eg. install.package("bibliometrix")
 
    
