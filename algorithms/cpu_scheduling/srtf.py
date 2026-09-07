def srtf(processes):
    # Sort processes according to arrival time
    processes = sorted(processes, key=lambda process: process.arrival_time)

    current_time = 0
    gantt_chart = []