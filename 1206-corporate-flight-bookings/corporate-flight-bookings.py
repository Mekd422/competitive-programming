class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        corop. flight booking
        """
        diffe = [0] * n
        for first, last, seats in bookings:
            diffe[first - 1] += seats

            if last < len(diffe):
                diffe[last] -= seats

        for i in range(1, n):
            diffe[i] += diffe[i - 1]
        return diffe            
        