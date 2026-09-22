class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        diff = [0] * n

        for l, r, seats in bookings:
            diff[l - 1] += seats
            if r < n - 1:
                diff[r] -= seats

        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff