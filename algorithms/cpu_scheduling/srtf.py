def srtf(processes):

    # Sort processes according to arrival time
    processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    current_time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []
    current_gantt = None

    while completed < n:

        # Find all available processes
        available_processes = []

        for process in processes:

            if (
                process.arrival_time <= current_time
                and process.remaining_time > 0
            ):
                available_processes.append(process)

        # If no process is available, CPU is idle
        if not available_processes:
            current_time += 1
            continue

        # Select process with shortest remaining time
        current_process = min(
            available_processes,
            key=lambda process: process.remaining_time
        )

        # Record response time only when the process runs first time
        if current_process.response_time is None:
            current_process.response_time = (
                current_time - current_process.arrival_time
            )

        # Gantt chart handling
        if (
            current_gantt is None
            or current_gantt["process"] != current_process.process_id
        ):

            current_gantt = {
                "process": current_process.process_id,
                "start": current_time,
                "end": current_time
            }

            gantt_chart.append(current_gantt)

        # Execute for 1 time unit
        current_process.remaining_time -= 1
        current_time += 1

        # Update Gantt chart end time
        current_gantt["end"] = current_time

        # Check if process is completed
        if current_process.remaining_time == 0:

            completed += 1

            # Completion Time
            current_process.completion_time = current_time

            # Turnaround Time
            current_process.turnaround_time = (
                current_process.completion_time
                - current_process.arrival_time
            )

            # Waiting Time
            current_process.waiting_time = (
                current_process.turnaround_time
                - current_process.burst_time
            )

    return processes, gantt_chart