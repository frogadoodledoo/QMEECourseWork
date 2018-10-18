# No preallocation

a <- NA

print(system.time(
for (i in 1:100000) {
    a <- c(a, i)
}))
#print(a)



# Preallocation

a <- rep(NA, 1000000)

print(system.time(
for (i in 1:1000000) {
    a[i] <- i
}))

#print(a)