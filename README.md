# Monitoring Resources

`monitoring_resources` is a Python library for monitoring system resources such as CPU, memory, disk, network, and more. This library provides a unified interface for accessing system state information using existing tools like `psutil`.

## Features

Currently, the `monitoring_resources` library includes the following features:

- ✅ **CPU Monitoring**: Retrieve real-time information about CPU usage, core count, and frequency.
- ❌ **Memory Monitoring**: Monitor the usage of system memory (to be implemented).
- ✅ **Device Monitoring**: Retrieve information about connected devices and monitor disk usage statistics.
- ❌ **Network Monitoring**: Check the bandwidth and activity of the network (to be implemented).
- ❌ **Process Monitoring**: Analyze running processes (to be implemented).
- ❌ **Disk Monitor**: Track detailed disk usage and activity (to be implemented).
- ❌ **Temperature Monitoring**: Retrieve hardware temperature data (to be implemented).
- ❌ **Power Monitoring**: Monitor power consumption and battery status (to be implemented).

## Dependencies

The library relies on the `psutil` library to collect information about system resources. This dependency is listed in the `requirements.txt` file.

Example content of `requirements.txt`:
```
psutil==6.1.1
```

## Example Usage

Here is an example of how to use the library to monitor CPU resources:

```python
from monitoring_resources.cpu_monitor import CPUMonitor

# Create a CPU monitor object
cpu_monitor = CPUMonitor()

# Display CPU information
print(f"CPU Usage: {cpu_monitor.get_cpu_usage()}%")
print(f"CPU Count: {cpu_monitor.get_cpu_count()} cores")
print(f"CPU Frequency: {cpu_monitor.get_cpu_frequency()} MHz")
```

## Progress

This project is under development. New features and optimizations will be added over time.

