import pandas as pd

class Process:
    def __init__(self, pid: str, arrival_time: int, burst_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, quantum=12):
    queue = [process for process in processes]
    current_time = 0
    while queue:
        process = queue.pop(0)
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        if process.burst_time > quantum:
            process.burst_time -= quantum
            current_time += quantum
            queue.append(process)
        else:
            current_time += process.burst_time
            process.completion_time = current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            process.burst_time = 0

def read_processes_from_excel(file_path):
    file_path = 'processes.xlsx'
    df = pd.read_excel(file_path)
    print("Column names in the Excel file:", df.columns)
    processes = []
    for _, row in df.iterrows():
        processes.append(Process(row['PID'], row['arrival_time'], row['Burst_time']))

    return processes

def save_processes_to_excel(processes, output_file_path):
    data = {
        'PID': [p.pid for p in processes],
        'Arrival Time': [p.arrival_time for p in processes],
        'Burst Time': [p.burst_time for p in processes],
        'Start Time': [p.start_time for p in processes],
        'Completion Time': [p.completion_time for p in processes],
        'Waiting Time': [p.waiting_time for p in processes],
        'Turnaround Time': [p.turnaround_time for p in processes]
    }
    df = pd.DataFrame(data)
    df.to_excel(output_file_path, index=False)

def main():
    file_path = 'processes.xlsx'
    output_file_path_rr = 'round_robin_output.xlsx'
    
    # Read processes
    processes = read_processes_from_excel(file_path)
 
    # Round Robin
    round_robin(processes, quantum=12)
    save_processes_to_excel(processes, output_file_path_rr)
    
    print("Scheduling simulations completed.")

if __name__ == "__main__":
    main()