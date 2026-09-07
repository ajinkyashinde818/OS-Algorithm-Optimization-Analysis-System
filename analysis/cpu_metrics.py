def calculate_cpu_metrics(processes):

    n = len(processes)

    # Avoid division by zero
    if n == 0:
        return {}

    total_waiting_time = sum(
        process.waiting_time for process in processes
    )

    total_turnaround_time = sum(
        process.turnaround_time for process in processes
    )

    total_response_time = sum(
        process.response_time for process in processes
    )

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    average_response_time = total_response_time / n

    # Total time from first arrival to last completion
    first_arrival = min(
        process.arrival_time for process in processes
    )

    last_completion = max(
        process.completion_time for process in processes
    )

    total_time = last_completion - first_arrival

    throughput = n / total_time if total_time > 0 else 0

    return {
        "average_waiting_time": average_waiting_time,
        "average_turnaround_time": average_turnaround_time,
        "average_response_time": average_response_time,
        "throughput": throughput
    }
