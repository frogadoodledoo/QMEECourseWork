# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"


# Load data
trees <- read.csv("../Data/trees.csv")

# Function to calculate hight

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))

  return (height)
}

# TreeHeight(37, 40) # test function

# Calculate hight for all trees in data

heights <- vector()

for (t in 1:nrow(trees)) {
    degrees <- trees[t,3] # third col of dataframe observation number t
    distance <- trees[t, 2] # second col of dataframe, observation number t
    h <- TreeHeight(degrees, distance)
    heights <- c(heights,h)
}

# Create and save output as csv

output <- cbind(trees, heights) # Bind output to original data

colnames(output)[4] <- "Tree.Height.m"

write.csv(output, "../Results/TreeHts.csv", )