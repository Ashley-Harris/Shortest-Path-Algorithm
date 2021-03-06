# Shortest Path Algorithm 

Conceived by Edsger Dijkstra in 1956, this algorithm finds the shortest path for nodes in a graph. Graph theory is a mathematical concept that can used to model real-life networks - such as roadways and airport flying routes - and Dijkstra's algorithm can be a useful tool to more effectively navigate these complex systems. 

Suppose you are flying a plane from an origin airport to a destination airport. Assume that the plane can fly a maximum of 200km before needing to land and refuel at an intermediate airport. I utilised Dijkstra’s algorithm to find the shortest distance from origin to destination, taking into account the plane’s need to refuel. 

* Each line of the input file, input.txt, contains a unique set of origin, destination, and intermediate points. 
* The (x, y) coordinates of the origin are given by the first two comma-separated values, and by the last values for the destination.
* There is an even number of values in-between that represent airport coordinates that can be used for refuelling.

My programme returns the shortest distance from origin to destination, or -1 if the destination cannot be reached from the origin. 
