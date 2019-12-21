### Morgan Wade and the Dark Gene Brigade, December 20, 2019, DTP Bioinformatics Hackathon Project: Exploring GC content across the metazoa


##Code to generate the chromosome-mapping histograms used in our GC content presentation

install.packages(stringr)
library(stringr)


install.packages("tidyverse")
library(tidyverse)

hist_data <- read.csv("~/GC_project_copy/Rodent/Rattus_norvegicus_chromosome_position_new.csv", header=FALSE)


#tidy up the data
hist_data$V1 <- NULL
hist_data <- t(hist_data)
    
hist_vector <- as.vector(hist_data)
hist_vector <- str_sort(hist_vector, numeric = TRUE)

table_hist <- table(hist_vector)
table_hist <- table_hist[str_sort(hist_vector, numeric = TRUE)]
View(table_hist)

?unique

df_hist <- as.data.frame(table_hist)
View(df_hist)
View(table_hist)


table_hist_unique <- unique(df_hist)

plot(df_hist)


ggplot(table_hist_unique, aes(x = table_hist_unique$hist_vector, y = table_hist_unique$Freq)) + 
  geom_bar(stat = "identity") + xlab("Chromosome") + ylab("Frequency") + theme_bw(base_size = 22)



###############################################

chromosome_lengths1 <- read.csv("~/GC_project_copy/Rodent/Rattus_norvegicus_chromosome_lengths1.csv", header=FALSE)
chromosome_lengths2 <- read.csv("~/GC_project_copy/Rodent/Rattus_norvegicus_chromosome_lengths2.csv", header=FALSE)




chromosome_lengths1$V1 <- NULL
chromosome_lengths2$V1 <- NULL
chromosome_lengths2$V31716 <- NULL

chromosome_lengths1 <- t(chromosome_lengths1)
chromosome_lengths2 <- t(chromosome_lengths2)

str(chromosome_lengths1)
str(chromosome_lengths2)

data <- cbind(chromosome_lengths1, chromosome_lengths2)

View(data)

install.packages("data.table")
library(data.table)


data2 <- data.table(data)
View(data2)


install.packages("dplyr")
library(dplyr)

data2$V2 <- as.numeric(data2$V2)

data3 <- group_by(data2, V1) %>% summarise_all(sum)

data3 <- data3[-c(21:137),]
data3 <- data3[-c(5, 21, 23),]
colnames(data3) <- c("hist_vector", "Length")

####

data4 <- merge(table_hist_unique, data3, by = "hist_vector")

data4 <- mutate(data4, hitRatio = Freq/Length)
data4$Length <- NULL
data4$Freq <- NULL


data4$hist_vector <- factor(data4$hist_vector, levels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                                                          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
                                                          "X"))


levels(data4$hist_vector)

  ggplot(data4, aes(x = data4$hist_vector, y = data4$hitRatio)) + 
  geom_bar(stat = "identity") + xlab("Chromosome") + ylab("Frequency per nucleotide base") + theme_bw(base_size = 22)




