class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hh = (360 / 12) * hour + ((360 / 12) / 60) * minutes
        mh = (360 / 60) * minutes
        angle = abs(hh - mh)
        if angle > 180:
            angle = 360 - angle

        return angle