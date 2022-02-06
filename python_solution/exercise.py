import os

def clear_console():
    """Macro to clear the console"""
    os.system("cls" if os.name == "nt" else "clear")

clear_console()  # clearing once can fix ANSI escape codes on windows

def green(text):
    """Macro to change the text color to green using ANSI escape codes"""
    return "\033[32m" + text + "\033[0m"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                       #
#  Cluster detection: Find the largest square cluster in a matrix.                      #
#                                                                                       #
#  1) Create the matrix                                                                 #
#      - The matrix should be a 2D array consisting of two                              #
#        randomly distributed values or characters, e.g. 'X' and 'O'.                   #
#      - Being able to change the ratio of the values could be advantageous.            #
#                                                                                       #
#  2) Find the clusters                                                                 #
#      - Find the positions and sizes of all square submatrices of a certain            #
#        minimum size that only contain one of the characters.                          #
#      - Ideally, clusters should not intersect.                                        #
#                                                                                       #
#  3) Print the result                                                                  #
#      - Print the matrix and highlight the largest cluster by changing the text color. #
#      - If more than one cluster of that size is present, highlight all of them.       #
#      - Optionally printing a summary would make sense.                                #
#                                                                                       #
#  4) Performance test                                                                  #
#      - Measure the runtime of each function.                                          #
#      - Test the functions with different parameters and see how well they scale.      #
#                                                                                       #
#  You may change this template in any way, it's just a starting point.                 #
#  More info at https://github.com/celltec/ClusterDetection/blob/master/README.md       #
#                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Cluster:
    pass

def make_matrix():
    pass

def get_clusters(matrix):
    pass

def print_result(matrix, clusters):
    pass

def run():
    print('Clusters are ' + green('fun'))
    matrix = make_matrix()
    clusters = get_clusters(matrix)
    print_result(matrix, clusters)

run()
