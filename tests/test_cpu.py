from models.process import Process
from algorithms.cpu_scheduling.fcfs import fcfs
from algorithms.cpu_scheduling.sjf import sjf
from algorithms.cpu_scheduling.srtf import srtf
from algorithms.cpu_scheduling.priority import priority_non_preemptive
from algorithms.cpu_scheduling.priority import priority_preemptive
from algorithms.cpu_scheduling.round_robin import round_robin
from analysis.cpu_metrics import calculate_cpu_metrics



from analysis.optimizer import (
    compare_cpu_algorithms,
    find_best_algorithm
)


# Create processes

processes = [

    Process("P1", 0, 8, 3),

    Process("P2", 1, 4, 1),

    Process("P3", 2, 2, 2)

]


# Compare algorithms

results = compare_cpu_algorithms(
    processes,
    time_quantum=2
)


# Print algorithm metrics

print("\nCPU Algorithm Comparison\n")

for algorithm, data in results.items():

    print(f"\n{algorithm}")

    for metric, value in data["metrics"].items():

        print(
            f"{metric}: {round(value, 2)}"
        )


# Find best algorithm

best_algorithm, scores = find_best_algorithm(
    results
)


# Print optimization scores

print("\n📊 Optimization Scores:\n")

for algorithm, score_data in scores.items():

    print(
        algorithm,
        "→",
        round(score_data["final_score"], 3)
    )


# Print recommended algorithm

print(
    "\n🏆 Recommended Algorithm:",
    best_algorithm
)