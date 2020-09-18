#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is running a sinlge loop through a range of n. As the value of n increases, the runtime will increase at that same rate, which is Linear Time, or O(n).


b) There is a loop for every element in the range n, so we have O(n) here. Then we have a nested loop inside of that loop that increments by an amount that is doubling with each loop, and is moving towards n. Since it is doubling with each increment, we know that is O(log(n)).
This means that O(n) * O(log(n)) = O(n log(n)).

The runtime is Log-linear O(n log n) as explained above.


c) This is a recursive problem. The base case will stop the algorithm and return 0 when bunnies == 0. Until then, the state changes each time to move the algorithm towards the base case while bunnies != 0. The function itself is called again and again until it reaches bunnies == 0, thus meeting all 3 rules of recursion. 

The runtime here is O(n) because it takes n number of bunnies, and multiplies the number of bunnies by 2 each time (to get the number of bunny ears for n number of bunnies). Then it decrements the number of bunnies by 1, calls the function to multiply the new number of bunnies by 2, and keeps going until bunnies == 0. As the number of n bunnies increases, the length of time the algorithm takes increases accordingly, which is Linear Time -- O(n).

## Exercise II

For this problem, I would use Binary Search. We have a clear pivot point, between floor e and f, where the egg will break at floor f or above, and will be ok to drop at floors below f. We need to find the target -- Break Floor f.

So, if floor >= f, egg will break. We are trying to figure out the value of f so that we can minimize breaking eggs as we drop them.

The number of floors is like a sorted array of ascending numbers.
Break Floor F is in the array, and we need to find it. (target).
First, check if the egg breaks on the first floor. (index[0]).
    If it does, we are finished, return that first floor.
Otherwise:
  Define a start point. 
  Define an end point. 
  Find the middle of those points -- (start + end) //2.

Set our base case (recursion):
Stop when the start point becomes smaller or equal to our end point, because we can't halve the array anymore.

Otherwsie, we need to get closer and closer to the stopping point:
    Check if the egg breaks on the middle floor:
        If so, move to the left and look for a lower floor.
        Our start point is the same, our end point becomes (middle - 1).
        We can keep calling the function to get the middle - 1 value to keep moving left towards the "break floor f".
    Else, if egg did not break at middle point:
        We need to move right to check through the higher value floors.
        Start point becomes (middle + 1). 
        End point stays the same.
        Check to see if egg breaks here.
        Keep going and overwriting the middle with new middle + 1 each time, until we find the Break Floor F.
    Return Break Floor F.

Else, if none of the floors break the egg, return None.  (or -1)


The runtime of this algorithm would be Logarithmic O(log n) because of the binary search, we are halving the number of amount of work related to finding the target. 