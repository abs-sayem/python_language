import ramdom

class LotterySystem:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.remaining_numbers = list(range(lower_limit, upper_limit+1))