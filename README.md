# Real Time Process Monitoring System 
This project is a real-time system monitoring dashboard that displays key system metrics, including CPU usage, memory usage, network activity (sent/received), disk usage, and the total number of running processes.

The backend is built using Python's psutil library, which fetches live system data every second. It collects accurate and detailed information such as CPU load, memory usage, bytes sent/received over the network, disk I/O stats, and the current process count.

The frontend uses Matplotlib to visualize this data in real-time. Graphs are updated every second, providing dynamic visual feedback through line charts and bar graphs for each metric. Each metric is shown in a separate subplot for clarity.

This project helps in understanding system performance at a glance and serves as a basic foundation for creating more advanced monitoring tools.
