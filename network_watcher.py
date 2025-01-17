import psutil
import time
import csv
from collections import defaultdict

class NetworkWatcher:
    def __init__(self, log_file='network_usage_log.csv', interval=5):
        self.log_file = log_file
        self.interval = interval
        self.previous_data = defaultdict(lambda: (0, 0))

    def log_network_usage(self):
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Application', 'Bytes Sent', 'Bytes Received'])

            while True:
                current_data = self.get_network_usage_by_process()
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                for proc_name, (sent, recv) in current_data.items():
                    prev_sent, prev_recv = self.previous_data[proc_name]
                    writer.writerow([
                        timestamp,
                        proc_name,
                        sent - prev_sent,
                        recv - prev_recv
                    ])

                self.previous_data = current_data
                time.sleep(self.interval)

    def get_network_usage_by_process(self):
        process_data = defaultdict(lambda: (0, 0))

        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_ESTABLISHED and conn.pid is not None:
                try:
                    process = psutil.Process(conn.pid)
                    sent, recv = process.io_counters().other
                    process_data[process.name()] = (
                        process_data[process.name()][0] + sent,
                        process_data[process.name()][1] + recv
                    )
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

        return process_data

if __name__ == '__main__':
    watcher = NetworkWatcher()
    print("Starting NetworkWatcher...")
    watcher.log_network_usage()