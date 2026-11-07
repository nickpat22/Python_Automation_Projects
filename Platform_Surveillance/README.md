# Platform Surveillance System

A Python-based system monitoring and automation tool that collects information about CPU utilization, RAM usage, network statistics, and running processes.

The project periodically generates timestamp-based log files containing system information and process details using Python automation libraries.

## Features

- Retrieves information about running processes.
- Collects Process ID (PID), process name, username, and process status.
- Monitors CPU utilization and the number of CPU cores.
- Monitors RAM utilization and total RAM.
- Collects network data transfer statistics.
- Records sent and received network data in MB.
- Generates timestamp-based log files.
- Supports automated periodic monitoring.
- Allows users to specify the monitoring interval.
- Supports command-line help and usage instructions.

## Technologies Used

- **Programming Language:** Python
- **System Monitoring:** psutil
- **Operating System Operations:** os
- **Command-Line Arguments:** sys
- **Time Management:** time
- **Task Scheduling:** schedule
- **Logging:** Python File Handling

## Project Structure

```text
Platform_Surveillance/
│
├── platform_surveillance.py
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.x
- pip (Python Package Installer)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/nickpat22/Python_Automation_Projects.git
```

**2. Navigate to the project directory**

```bash
cd Python_Automation_Projects/Platform_Surveillance
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

## How to Run

**Display help information**

```bash
python platform_surveillance.py --h
```

**Display usage instructions**

```bash
python platform_surveillance.py --u
```

**Execute the monitoring system**

```bash
python platform_surveillance.py 1 Logs
```

Here:

- `1` – Monitoring interval in minutes.
- `Logs` – Directory where generated log files are stored.

The program continues monitoring periodically until manually stopped using `Ctrl + C`.

## Working Process

1. Accepts the monitoring interval and log directory through command-line arguments.
2. Checks whether the specified log directory exists.
3. Creates the directory if it does not exist.
4. Schedules the monitoring function using the Schedule library.
5. Collects CPU utilization and CPU core information.
6. Retrieves RAM utilization and total memory.
7. Collects network data transfer statistics.
8. Scans currently running processes using the psutil library.
9. Records process details, CPU usage, and memory utilization.
10. Generates a timestamp-based log file containing the collected information.

## Log File Information

Each generated log file contains:

- Log creation timestamp.
- Number of CPU cores.
- CPU utilization percentage.
- RAM utilization percentage.
- Total RAM.
- Network data sent and received.
- Running process IDs.
- Process names and usernames.
- Process status.
- Individual process CPU and memory utilization.

## Learning Outcomes

Through this project, I explored:

- System monitoring using Python.
- Process management using the psutil library.
- CPU and memory utilization monitoring.
- Network statistics collection.
- Iterating through running processes.
- Dictionary handling and process information extraction.
- File handling and automated report generation.
- Command-line argument handling.
- Periodic task scheduling using the Schedule library.

## Author

**Nikunj Patidar**

GitHub: [@nickpat22](https://github.com/nickpat22)

---

*This project is part of my Python Automation learning journey, focused on system monitoring, process management, and automated reporting.*
