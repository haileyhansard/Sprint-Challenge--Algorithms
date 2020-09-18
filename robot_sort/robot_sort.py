#NOTES: 
# Robot can:
#  move left
#  move right 
#  pick up item
#  compare item its holding to the item in front of it
#  swap item if it tries to pick up item & is already holding item
#  switch light on or off

#RULES:
# Can use loops, for, while
# Cannot make up new variables
# Cannot store any variables
# Cannot use python libraries or class methods.
# Can define robot helper methods, as long as they follow rules.

# SORT LIST using ONLY these abilites.

# The robot can compare 2 items and swap them, so I could use Selection Sort or Bubble Sort.

# Robot is initialized at position 0, holding NO item, with her light OFF.

# Bubble Sort:
# Starting with current_position which is 0, pick up that value, which is None.
# Move right.
# Compare value of None to the value at position 1.
# If next's value is larger, swap. (because we want largest values at end)

# def bubble_sort(arr):
# keep a flag that tracks whether any swaps occurred 
#   swaps_occurred = True 
#   while swaps_occurred:
#       swaps_occurred = False 
#       for i in range(len(arr)-1):
#           if arr[i] > arr[i+1]:
#               arr[i], arr[i+1] = arr[i+1], arr[i]
#               swaps_occurred = True
# ​
#   return arr

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        #Turn on Robot's light to get this process going.
        self.set_light_on() #this is like a flag that swaps are occurring

        while self.light_is_on(): #while swaps are occurring:
            # Robot is holding NONE. We need her to hold a value, so that she can compare and move through list.
            self.compare_item() #to check the first value, which will be None as initialized
            self.swap_item() #to pick up first item (which is the value at the first position)
            self.move_right() #to make her first move    
            self.set_light_off() #turn light off when swaps have been completed, will end this loop, no more swapping will need to occur, and list will be sorted.

            # While Robot can move right (while position < len(list - 1), move robot right.
            # Need to compare values as robot moves through each position. 
            while self.can_move_right():
                if self.compare_item() <= 0: #will return 0, -1 or none if item robot is holding is smaller than the value in position, so we need to swap and move right with the larger-value item
                    self.swap_item()
                else:
                    self.set_light_on() #need to keep looping and swapping, so light back on
                self.move_right() #move right again, will compare values in the while loop until...
            self.swap_item() #set larger item in the last position, cannot move right any father, swaps were performed so we need to start the while loop over to keep comparing

            while self.can_move_left(): #position decrements until it is no longer greater than 0.
                if self.compare_item() >= 0: #if item is larger than value in position, swape and move left with the smaller-value item
                    self.swap_item()
                else:
                    self.set_light_on() #need to keep looping and swapping, so light back on
                self.move_left() #move left, compare values, until...
            self.swap_item() #set smaller item in the first position, cannot move left any farther




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)