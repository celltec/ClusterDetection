
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

<br/>

---

<br/>

My (perfectly unoptimized) solutions for [Python](https://github.com/celltec/ClusterDetection/tree/master/python_solution) and [Rust](https://github.com/celltec/ClusterDetection/tree/master/rust_solution) are also available. More languages coming soon (maybe).
