def priority_non_preemptive(processes):

    processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    current_time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []

    while completed < n:

        # Find available processes
        available_processes = []

        for process in processes:
            if (
                process.arrival_time <= current_time
                and process.remaining_time > 0
            ):
                available_processes.append(process)

        # CPU is idle
        if not available_processes:
            current_time += 1
            continue

        # Select highest priority
        current_process = min(
            available_processes,
            key=lambda process: process.priority
        )

        start_time = current_time

        # Response time
        current_process.response_time = (
            start_time - current_process.arrival_time
        )

        # Execute completely
        current_time += current_process.burst_time
        current_process.remaining_time = 0

        # Completion time
        current_process.completion_time = current_time

        # Turnaround time
        current_process.turnaround_time = (
            current_process.completion_time
            - current_process.arrival_time
        )

        # Waiting time
        current_process.waiting_time = (
            current_process.turnaround_time
            - current_process.burst_time
        )

        # Gantt chart
        gantt_chart.append({
            "process": current_process.process_id,
            "start": start_time,
            "end": current_time
        })

        completed += 1

    return processes, gantt_chart


def priority_preemptive(processes):

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

        # Find available processes
        available_processes = []

        for process in processes:
            if (
                process.arrival_time <= current_time
                and process.remaining_time > 0
            ):
                available_processes.append(process)

        # CPU is idle
        if not available_processes:
            current_time += 1
            continue

        # Select highest priority
        current_process = min(
            available_processes,
            key=lambda process: process.priority
        )

        # Response time only for first execution
        if current_process.response_time is None:
            current_process.response_time = (
                current_time
                - current_process.arrival_time
            )

        # Handle Gantt chart
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

        # Execute for one unit
        current_process.remaining_time -= 1
        current_time += 1

        # Update Gantt chart
        current_gantt["end"] = current_time

        # Check completion
        if current_process.remaining_time == 0:

            completed += 1

            current_process.completion_time = current_time

            current_process.turnaround_time = (
                current_process.completion_time
                - current_process.arrival_time
            )

            current_process.waiting_time = (
                current_process.turnaround_time
                - current_process.burst_time
            )

    return processes, gantt_chart
