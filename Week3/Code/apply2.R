SomeOperation <- function(v){ 
  if (sum(v) > 0){# If the sum of the elements of the matrix is positive
    return (v * 100) # multiplies each element of the matrix by 100
  }
  return  # else returns the unmodified matrix
}
M <- matrix(rnorm(100), 10, 10)
print (apply(M, 1, SomeOperation)) # Applies the function to each row of the matrix