MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F,  stringsAsFactors = F))
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T,  sep=";", stringsAsFactors = F)

install.packages("reshape2")
# ‘/tmp/Rtmpib1l8g/downloaded_packages’
require(reshape2)
