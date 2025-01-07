import unittest
from monitoring_resources.cpu_monitor import CPUMonitor


class TestCPUMonitor(unittest.TestCase):
    def setUp(self):
        self.cpu_monitor = CPUMonitor()

    def test_cpu_usage(self):
        usage = self.cpu_monitor.get_cpu_usage()
        self.assertIsInstance(usage, float)
        self.assertGreaterEqual(usage, 0)

    def test_cpu_count(self):
        count = self.cpu_monitor.get_cpu_count()
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_cpu_frequency(self):
        freq = self.cpu_monitor.get_cpu_frequency()
        self.assertIsInstance(freq, float)
        self.assertGreater(freq, 0)
        
if __name__ == '__main__':
    unittest.main()
