import psutil

class CPUMonitor:
    def __init__(self):
        ...
        
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)
    
    def get_cpu_count(self):
        return psutil.cpu_count()
    
    def get_cpu_frequency(self):
        return psutil.cpu_freq().current
    
    