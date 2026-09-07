class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority=0):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        # Used during execution
        self.remaining_time = burst_time

        # Calculated after scheduling
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.response_time = None

    def reset(self):
        self.remaining_time = self.burst_time
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.response_time = None