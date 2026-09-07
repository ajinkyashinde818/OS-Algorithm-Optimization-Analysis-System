from models.process import Process

from algorithms.cpu_scheduling.fcfs import fcfs
from algorithms.cpu_scheduling.sjf import sjf
from algorithms.cpu_scheduling.srtf import srtf

from algorithms.cpu_scheduling.priority import (
    priority_non_preemptive,
    priority_preemptive
)

from algorithms.cpu_scheduling.round_robin import round_robin

from analysis.cpu_metrics import calculate_cpu_metrics


# Create fresh copies of processes
def create_process_copy(processes):

    new_processes = []

    for process in processes:

        new_process = Process(
            process.process_id,
            process.arrival_time,
            process.burst_time,
            process.priority
        )

        new_processes.append(new_process)

    return new_processes


# Run and compare all CPU scheduling algorithms
def compare_cpu_algorithms(processes, time_quantum=2):

    results = {}

    # ---------------- FCFS ----------------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = fcfs(
        fresh_processes
    )

    results["FCFS"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    # ---------------- SJF ----------------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = sjf(
        fresh_processes
    )

    results["SJF"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    # ---------------- SRTF ----------------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = srtf(
        fresh_processes
    )

    results["SRTF"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    # -------- Priority Non-Preemptive --------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = (
        priority_non_preemptive(fresh_processes)
    )

    results["Priority Non-Preemptive"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    # -------- Priority Preemptive --------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = (
        priority_preemptive(fresh_processes)
    )

    results["Priority Preemptive"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    # ---------------- Round Robin ----------------

    fresh_processes = create_process_copy(processes)

    completed_processes, gantt_chart = round_robin(
        fresh_processes,
        time_quantum
    )

    results["Round Robin"] = {
        "metrics": calculate_cpu_metrics(completed_processes),
        "gantt_chart": gantt_chart
    }


    return results


# Normalize metric where LOWER value is better
def normalize_lower_is_better(value, min_value, max_value):

    # If all algorithms have the same value
    if max_value == min_value:
        return 1

    return (
        (max_value - value)
        / (max_value - min_value)
    )


# Normalize metric where HIGHER value is better
def normalize_higher_is_better(value, min_value, max_value):

    # If all algorithms have the same value
    if max_value == min_value:
        return 1

    return (
        (value - min_value)
        / (max_value - min_value)
    )


# Calculate weighted optimization scores
def calculate_optimization_scores(results):

    # Collect all metric values

    waiting_times = [
        data["metrics"]["average_waiting_time"]
        for data in results.values()
    ]

    turnaround_times = [
        data["metrics"]["average_turnaround_time"]
        for data in results.values()
    ]

    response_times = [
        data["metrics"]["average_response_time"]
        for data in results.values()
    ]

    throughputs = [
        data["metrics"]["throughput"]
        for data in results.values()
    ]


    scores = {}


    # Calculate score for every algorithm
    for algorithm, data in results.items():

        metrics = data["metrics"]


        # Waiting Time
        # Lower is better
        waiting_score = normalize_lower_is_better(
            metrics["average_waiting_time"],
            min(waiting_times),
            max(waiting_times)
        )


        # Turnaround Time
        # Lower is better
        turnaround_score = normalize_lower_is_better(
            metrics["average_turnaround_time"],
            min(turnaround_times),
            max(turnaround_times)
        )


        # Response Time
        # Lower is better
        response_score = normalize_lower_is_better(
            metrics["average_response_time"],
            min(response_times),
            max(response_times)
        )


        # Throughput
        # Higher is better
        throughput_score = normalize_higher_is_better(
            metrics["throughput"],
            min(throughputs),
            max(throughputs)
        )


        # Weighted final score

        final_score = (
            waiting_score * 0.40
            + turnaround_score * 0.30
            + response_score * 0.20
            + throughput_score * 0.10
        )


        scores[algorithm] = {

            "waiting_score": waiting_score,

            "turnaround_score": turnaround_score,

            "response_score": response_score,

            "throughput_score": throughput_score,

            "final_score": final_score
        }


    return scores


# Find the algorithm with the highest optimization score
def find_best_algorithm(results):

    scores = calculate_optimization_scores(results)

    best_algorithm = max(
        scores,
        key=lambda algorithm: scores[algorithm]["final_score"]
    )

    return best_algorithm, scores