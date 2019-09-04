# ClusterDetection

## Find the largest square cluster in a matrix.

![example](https://user-images.githubusercontent.com/20523988/64257015-e2a8db00-cf24-11e9-86bc-2466a645d28c.png)

<br/>

### Exercise

#### 1. Create the matrix
The matrix should be a 2D array that consists of two randomly distributed values or characters, e.g. 'X' and 'O'. 
It could be advantageous to have an option to change the probability of one value to get better results. 

#### 2. Find the clusters
Find the positions and sizes of all square submatrices of a certain minimum size that only contain one of the characters. 
Ideally clusters do not intersect. 

#### 3. Print the result
Print out the matrix and highlight the largest cluster by changing the text color in that area. 
If there is more than one cluster with that size present, draw all of them. 
Optionally printing a summary would make sense.

#### 4. Performance test [optional]
Measure the time every step took to calculate. Test the functions with different parameters and see how well they scale. 
