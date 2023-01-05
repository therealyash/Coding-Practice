"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. T
he balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not
know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points
along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
       # Sort the balloons by their xstart coordinate
        points.sort(key=lambda x: x[0])

        # Keep track of the rightmost xend coordinate we have seen so far
        rightmost_xend = float('-inf')
        arrow_count = 0

        for xstart, xend in points:
            # If the xstart of the current balloon is greater than the rightmost xend,
            # we need to shoot an additional arrow to burst this balloon and any subsequent balloons
            if xstart > rightmost_xend:
                arrow_count += 1
                rightmost_xend = xend
            # Otherwise, if the xstart of the current balloon is less than or equal to the rightmost xend,
            # we can burst this balloon and all preceding balloons with a single arrow shot at the rightmost xend
            else:
                rightmost_xend = min(rightmost_xend, xend)

        return arrow_count
