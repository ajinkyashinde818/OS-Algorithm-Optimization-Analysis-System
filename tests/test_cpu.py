from models.process import Process
from algorithms.cpu_scheduling.fcfs import fcfs
from algorithms.cpu_scheduling.sjf import sjf

# First come first Serve
# Create sample processes
processes = [
    Process("P1", 0, 5, 2),
    Process("P2", 1, 3, 1),
    Process("P3", 2, 2, 3)
]


# Run FCFS algorithm
result_processes, gantt_chart = fcfs(processes)


# Print process results
print("\nFCFS Results:\n")

for process in result_processes:
    print(
        process.process_id,
        "| Completion:", process.completion_time,
        "| Waiting:", process.waiting_time,
        "| Turnaround:", process.turnaround_time,
        "| Response:", process.response_time
    )


# Print Gantt Chart data
print("\nGantt Chart:\n")

for item in gantt_chart:
    print(item)



# Shortest Job First

processes = [
    Process("P1", 0, 6),
    Process("P2", 1, 2),
    Process("P3", 2, 4)
]

result_processes, gantt_chart = sjf(processes)

print("\nSJF Results:\n")

for process in result_processes:
    print(
        process.process_id,
        "| Completion:", process.completion_time,
        "| Waiting:", process.waiting_time,
        "| Turnaround:", process.turnaround_time,
        "| Response:", process.response_time
    )

print("\nGantt Chart:\n")

for item in gantt_chart:
    print(item)
