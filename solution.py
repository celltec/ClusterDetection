import os
import random
from collections import Counter
from timeit import default_timer as timer

def clear_console():
    """Macro to clear the console."""
    os.system("cls" if os.name == "nt" else "clear")

def red(text):
    """Macro to change the text color to red."""
    return "\033[31m" + text + "\033[0m"

def green(text):
    """Macro to change the text color to green."""
    return "\033[32m" + text + "\033[0m"

def cross(number):
    """Macro for more readable concatination."""
    return str(number) + "x" + str(number)

def seconds(time):
    """Macro to format the time."""
    return "[{:.0f}ms]".format(time*1000) if time < 1 else "[{:.2f}s]".format(time)

def execute_timed(function, *args, message=None):
    """Macro for timed function calls with an optional message. 
    Returns the time or the return value of the function if available."""
    if message:
        print("  " + message + "...", end=" ", flush=True)
    else:
        print("  Starting timed function '" + str(function.__name__) + "'...")
    start = timer()
    value = function(*args)
    end = timer()
    time = end - start
    if message:
        print("Done! " + seconds(time))
    else:
        print("  Timed function '" + str(function.__name__) + "' done! " + seconds(time))
    return time if value is None else value

class Cluster:
    def __init__(self, position, size=1):
        self.x = position['x']  # x coordinate of top left corner
        self.y = position['y']  # y coordinate of top left corner
        self.size = size        # lenth of one side
        self.area = set()       # a collection of all coordinates
        for y in range(self.y, self.y + self.size):
            for x in range(self.x, self.x + self.size):
                self.area.add((x, y))

def filter_overlap(clusters):
    """Returns a list of clusters that do not intersect. Bigger clusters are dominant."""
    filtered_clusters = set()
    sorted_clusters = sorted(clusters, key=lambda x: x.size, reverse=True)
    for cluster in sorted_clusters:
        if cluster in filtered_clusters:
            continue
        for compare in sorted_clusters:
            if compare in filtered_clusters or compare is cluster:
                continue
            if cluster.area.intersection(compare.area):
                if cluster.size < compare.size:
                    filtered_clusters.add(cluster)
                    break
                else:
                    filtered_clusters.add(compare)
    return [cluster for cluster in clusters if cluster not in filtered_clusters]

def check_cluster_size(matrix, position, size):
    """Calculates and returns the size of a cluster."""
    if size > 0:
        for y in range(position['y'] + 1, position['y'] + size):
            for x in range(position['x'], position['x'] + size):
                if matrix[y][x] is "O":
                    new_size = x - position['x']
                    if new_size is 0:
                        new_size = y - position['y']
                        return new_size
                    return check_cluster_size(matrix, position, new_size)
        return size

def get_clusters(matrix, min_required_size):
    """Returns a list of all square clusters."""
    # count the consecutive occurrences of 'X' in one line until an 'O' or the edge is reached
    # check the cluster size based on that amount as it is the potential side length of a cluster
    if not matrix:
        return []
    if min_required_size < 1:
        min_required_size = 1
    clusters = []
    matrix_size = len(matrix)
    for y in range(matrix_size):
        x = 0
        position = None
        assumed_size = 0
        edge_reached = False
        while x < matrix_size:
            if matrix[y][x] is "X":
                if not position:
                    position = {'x': x, 'y': y}
                assumed_size += 1
                if assumed_size is matrix_size - position['x'] or assumed_size is matrix_size - position['y']:
                    edge_reached = True
            if (matrix[y][x] is "O" and assumed_size) or edge_reached:
                if assumed_size >= min_required_size:
                    actual_size = check_cluster_size(matrix, position, assumed_size)
                    if actual_size >= min_required_size:
                        cluster = Cluster(position, actual_size)
                        clusters.append(cluster)
                x = position['x']
                position = None
                assumed_size = 0
                edge_reached = False
            x += 1
    return clusters

def make_matrix(size, x_frequency=1):
    """Returns a 2D list containing randomly distributed 'X' and 'O'."""
    matrix = []
    for row in range(size):
        matrix.append([])
        for _ in range(size):
            value = random.choices("XO", [x_frequency, 1]).pop()
            matrix[row].append(value)
    return matrix

def print_matrix(matrix, clusters=None):
    """Prints out a matrix with the option to color certain areas red."""
    output = ""
    for y, line in enumerate(matrix):
        output += "\n  "
        for x, element in enumerate(line):
            if not clusters:
                output += element + " "
            else:
                for cluster in clusters:
                    if (x, y) in cluster.area:
                        output += red(element + " ")
                        break
                else:
                    output += element + " "
    print(output + "\n")

def print_result(matrix, clusters, show_all_clusters=False):
    """Prints out a summary of the results as well as the matrix itself while highlighting possible clusters."""
    print("")
    if not clusters:
        print(red("  No clusters found!"))
        print_matrix(matrix)
    else:
        cluster_counts = Counter(cluster.size for cluster in clusters)
        for size, amount in sorted(cluster_counts.items()):
            print(green("  Found " + str(amount) + " " + cross(size) + " cluster" + ("s" if amount > 1 else "") + "!"))
        if show_all_clusters:
            print_matrix(matrix, clusters)
        else:
            max_size = max(cluster_counts)
            print_matrix(matrix, [cluster for cluster in clusters if cluster.size is max_size])

def run(matrix_size=13, show_all_clusters=False, no_overlap=True, cluster_min_size=3, x_frequency=5):
    """Creates one random matrix, finds square clusters and prints the results."""
    print("")
    matrix = execute_timed(make_matrix, matrix_size, x_frequency, 
                           message="Generating random " + cross(matrix_size) + " matrix containing 'X' and 'O'")
    clusters = execute_timed(get_clusters, matrix, cluster_min_size, 
                             message="Searching for square shaped clusters that are at least " + cross(cluster_min_size))
    if no_overlap:
        clusters = execute_timed(filter_overlap, clusters, message="Filtering overlapping clusters")
    print_result(matrix, clusters, show_all_clusters)

def performance_test(cases=15, runs=3, start_size=10, increment=10):
    """Executes a set of test cases, calculates the average runtimes and prints out the timings."""
    print("\n  Running performance test...\n")
    results = {}
    for case in range(cases):
        size = start_size + case * increment
        results[size] = []
        for _ in range(runs):
            results[size].append(execute_timed(run, size))
            print("\n " + "="*(size*2+1 if size > 34 else 69) + "\n")
    clear_console()
    print(green("\n  Performance test results:\n"))
    print("  There are {} test cases and every case ran {} times.".format(cases, runs))
    print("  The size was incremented by {} for every new case.\n".format(increment))
    print("  Average times:\n")
    for case, times in results.items():
        average = sum(times) / len(times)
        format_distance = str(len(str(cases * increment if cases > 1 else start_size)) * 2 + 1)
        print(("  {:>" + format_distance + "} -> ").format(cross(case)) + seconds(average)[1:-1])
    print("")

def print_menu():
    print("\n  \u2554" + "\u2550"*22 + "\u2557\n"
          + "  \u2551         MENU         \u2551\n"
          + "  \u255F" + "\u2500"*22 + "\u2562\n"
          + "  \u2551 [1] Run once         \u2551\n"
          + "  \u2551 [2] Performance test \u2551\n"
          + "  \u2551 [3] Help             \u2551\n"
          + "  \u2551 [4] Quit             \u2551\n"
          + "  \u2551                      \u2551\n"
          + "  \u2551 Choice:              \u2551\n"
          + "  \u255A" + "\u2550"*22 + "\u255D", end=" ", flush=True)
    
def print_help():
    print("\n   1 -> " + run.__doc__ + "\n"
          + "   2 -> " + performance_test.__doc__ + "\n"
          + "   3 -> Prints a description of the options.\n"
          + "   4 -> Ends the program.")

if __name__ == "__main__":
    clear_console() # clearing once can fix ANSI escape codes on windows
    while True:
        print_menu()
        choice = input("\u001b[1A\u001b[15D") # move cursor
        clear_console()
        if choice is "1":
            run() # change parameters here
        elif choice is "2":
            performance_test() # change parameters here
        elif choice is "3":
            print_help()
        elif choice is "4":
            break # end program
