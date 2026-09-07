def fcfs(processes):
    # Sort processes according to arrival time
    processes = sorted(processes, key=lambda process: process.arrival_time)

    current_time = 0
    gantt_chart = []

    for process in processes:

        # If CPU is idle, move time to process arrival time
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        # Process starts executing
        start_time = current_time

        # Response time
        process.response_time = start_time - process.arrival_time

        # Execute the complete process
        current_time += process.burst_time

        # Completion time
        process.completion_time = current_time

        # Turnaround time
        process.turnaround_time = (
            process.completion_time - process.arrival_time
        )

        # Waiting time
        process.waiting_time = (
            process.turnaround_time - process.burst_time
        )

        # Add execution details for Gantt chart
        gantt_chart.append({
            "process": process.process_id,
            "start": start_time,
            "end": current_time
        })

    return processes, gantt_chart
