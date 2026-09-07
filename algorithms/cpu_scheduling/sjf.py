def sjf(processes):
    # Sort by arrival time
    processes = sorted(processes, key=lambda process: process.arrival_time)

    current_time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []
    ready_queue = []

    while completed < n:

        # Add all processes that have arrived
        for process in processes:
            if (
                process.arrival_time <= current_time
                and process.completion_time is None
                and process not in ready_queue
            ):
                ready_queue.append(process)

        # If no process is available, CPU is idle
        if not ready_queue:
            current_time += 1
            continue

        # Select process with shortest burst time
        current_process = min(
            ready_queue,
            key=lambda process: process.burst_time
        )

        ready_queue.remove(current_process)

        # Start execution
        start_time = current_time

        # Response Time
        current_process.response_time = (
            start_time - current_process.arrival_time
        )

        # Execute completely (Non-Preemptive)
        current_time += current_process.burst_time

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

        # Add to Gantt Chart
        gantt_chart.append({
            "process": current_process.process_id,
            "start": start_time,
            "end": current_time
        })

        completed += 1

    return processes, gantt_chart