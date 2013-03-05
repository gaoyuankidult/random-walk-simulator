class ConfInfo():
    def __init__(self):
        self.repeat_time = None
        self.initial_state = None
        self.random_walk_number = None
        self.upper_range = None
        self.lower_range =None
    def check_valid(self):
        #TOUNDERSTAND 
        # if I have () then I do not need \ to break a line
        if (self.repeat_time is not None and
            self.initial_state is not None and 
            self.random_walk_number is not None and 
            self.upper_range is not None and 
            self.lower_range is not None):
            return True
        else:
            return False
    def set_info(self, list):
        if len(list) != 5:
            return False
        self.set_init_state(list[0])
        self.set_random_walk_number(list[1])
        self.set_upper_range(list[2])
        self.set_lower_range(list[3])
        self.set_period(list[4])

    def set_period(self, float):
        self.repeat_time = float
    def set_init_state(self, float):
        self.initial_state = float
    def set_lower_range(self, float):
        self.lower_range = float
    def set_upper_range(self, float):
        self.upper_range = float
    def set_random_walk_number(self, float):
        self.random_walk_number = float

                         
