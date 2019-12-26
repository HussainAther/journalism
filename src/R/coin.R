library(stats)    # First, import the "stats" library.
par(mfrow=c(3,2)) # Then, create 6 graphs in 3 rows and 2 columns.
x=seq(0,1,by=0.1) # Generate "x", a list from 0 to 1 with steps of size .1.
                  # These are the likelihoods of getting heads. 
                  # An x value of ".5" means the coin is heads 50 percent 
                  # of the time. 
                               # For each of the 6 experiments, 
alpha=c(2, 10, 20, 50, 92, 500) # "alpha" is how many times you flipped a coin, and
beta=c(2, 8, 11, 27, 92, 232)   # "beta" is the how many heads you got.
          
for(i in 1:length(alpha)){ # For each experiment,
    y<-dbeta(x,shape1=alpha[i],shape2=beta[i])
    plot(x,y,type="l",xlab = "Heads probability", ylab = "density")
} 
