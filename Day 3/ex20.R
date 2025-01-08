rolls = sample(c(1,2,3,4,5,6), 100, replace = TRUE)
rolls
freq = table(rolls)
freq
barplot(freq)