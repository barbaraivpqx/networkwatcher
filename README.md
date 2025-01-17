# NetworkWatcher

NetworkWatcher is a Python program designed to monitor network traffic and log data usage by applications on a Windows system. It utilizes the `psutil` library to gather network usage statistics and logs them into a CSV file.

## Features

- Monitors network traffic on a Windows system.
- Logs data usage per application.
- Outputs data to a CSV file for easy analysis.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/networkwatcher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd networkwatcher
    ```

3. Install the required Python packages:

    ```bash
    pip install psutil
    ```

## Usage

To start monitoring network traffic, run the `network_watcher.py` script:

```bash
python network_watcher.py
```

The program will log network traffic data to a file named `network_usage_log.csv` in the same directory. The logging interval is set to 5 seconds by default, but it can be adjusted by modifying the `interval` parameter in the `NetworkWatcher` class.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.