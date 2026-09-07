from collections import deque


def round_robin(processes, time_quantum):

    # Sort processes according to arrival time
    processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    current_time = 0
    completed = 0
    n = len(processes)

    ready_queue = deque()
    gantt_chart = []

    index = 0

    # Continue until all processes are completed
    while completed < n:

        # Add processes that have arrived
        while (
            index < n
            and processes[index].arrival_time <= current_time
        ):
            ready_queue.append(processes[index])
            index += 1

        # CPU is idle
        if not ready_queue:

            if index < n:
                current_time = processes[index].arrival_time
                continue

        # Get first process from queue
        current_process = ready_queue.popleft()

        # Response time (only first time)
        if current_process.response_time is None:
            current_process.response_time = (
                current_time - current_process.arrival_time
            )

        start_time = current_time

        # Decide how much time process will execute
        execution_time = min(
            time_quantum,
            current_process.remaining_time
        )

        # Execute process
        current_process.remaining_time -= execution_time
        current_time += execution_time

        # Add Gantt Chart entry
        gantt_chart.append({
            "process": current_process.process_id,
            "start": start_time,
            "end": current_time
        })

        # Add newly arrived processes during execution
        while (
            index < n
            and processes[index].arrival_time <= current_time
        ):
            ready_queue.append(processes[index])
            index += 1

        # Check if process is completed
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

        else:
            # Process is not finished, put it back in queue
            ready_queue.append(current_process)

    return processes, gantt_chart