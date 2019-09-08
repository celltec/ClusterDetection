
# ClusterDetection

### Find the largest square cluster in a matrix.

![example matrix](https://user-images.githubusercontent.com/20523988/64360441-ce3f0e00-d00a-11e9-936b-ee8453e61881.png)

## Exercise

**1. Create the matrix**
* The matrix should be a 2D array consisting of two randomly distributed values or characters, e.g. 'X' and 'O'. 
* Being able to change the ratio of the values could be advantageous. 

**2. Find the clusters**
* Find the positions and sizes of all square submatrices of a certain minimum size that only contain one of the characters. 
* Ideally, clusters should not intersect. 

**3. Print the result**
* Print the matrix and highlight the largest cluster by changing the text color. 
* If more than one cluster of that size is present, highlight all of them. 
* Optionally printing a summary would make sense.

**4. Performance test** [optional]
* Measure the runtime of each function. 
* Test the functions with different parameters and see how well they scale.



# My solution
Starting the program you will be greeted with a small menu. 

![menu](https://user-images.githubusercontent.com/20523988/64320530-0b7dae80-cfbf-11e9-81a8-515c96490860.png)

## Menu options
**Run once:** Creates one random matrix, finds square clusters and prints the results.

**Performance test:** Executes a set of test cases, calculates the average runtimes and prints out the timings.

**Help:** Prints a description of the options.

**Quit:** Ends the program.



## Parameters
**Run once:**
* Size of the matrix
* Enable highlighting all clusters
* Enable overlapping
* Minimum cluster size to be recognized
* Factor to increase the probability for 'X' to appear

**Performance test:**
* Amount of test cases
* Runs per case
* Size of the matrix at the start
* Size increment for every new case

#### Parameters can be set via the function calls in main
```python
if choice is "1":
    run(matrix_size=15, show_all_clusters=False, no_overlap=True)
elif choice is "2":
    performance_test(cases=15, runs=3, start_size=10, increment=10)
```

## Examples

### Multiple large clusters

![example two large clusters](https://user-images.githubusercontent.com/20523988/64451554-c3f14280-d0e4-11e9-9d25-7423b6af08bb.png)

### Show all clusters

![example show all clusters](https://user-images.githubusercontent.com/20523988/64360535-f595db00-d00a-11e9-99ce-531400010e70.png)

### Overlap enabled

![example overlap](https://user-images.githubusercontent.com/20523988/64451645-ec793c80-d0e4-11e9-8d41-c9de10739e18.png)

### Performance test

![example performance test](https://user-images.githubusercontent.com/20523988/64360763-6a691500-d00b-11e9-9344-d4028498f96f.png)
