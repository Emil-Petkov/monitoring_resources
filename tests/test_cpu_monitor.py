import unittest
from unittest.mock import patch, MagicMock
from monitoring_resources.cpu_monitor import CPUMonitor


class TestCPUMonitor(unittest.TestCase):
    '''
         Unit tests for the CPUMonitor class.
    '''

    def setUp(self):
        '''
             Initialize the CPUMonitor instance before each test.
        '''

        self.cpu_monitor = CPUMonitor()

    @patch('psutil.cpu_percent')
    def test_get_cpu_usage_success(self, mock_cpu_percent):
        '''
             Test get_cpu_usage when psutil.cpu_percent works correctly.
        '''

        mock_cpu_percent.return_value = 35.5  # Simulate CPU usage 35.5%
        result = self.cpu_monitor.get_cpu_usage()
        self.assertEqual(result, 35.5, 'CPU usage should be 35.5%')

    @patch('psutil.cpu_percent')
    def test_get_cpu_usage_failure(self, mock_cpu_percent):
        '''
            Test get_spu_usage when psutil.cpu_percent raises an exception.
        '''

        mock_cpu_percent.side_effect = Exception('Simulate Error')
        result = self.cpu_monitor.get_cpu_usage()
        self.assertIsNone(result, 'CPU usage should be None when an error occurs')
        
        
    @patch('psutil.cpu_count')
    def test_get_cpucount_success(self, mock_cpu_count):
        '''
            Test get_CPU count when psutil.cpu_count work correctly.
        '''

        mock_cpu_count.return_value = 8 # Simulate 8 CPU cores
        result = self.cpu_monitor.get_cpu_count()
        self.assertEqual(result, 8, 'CPU count should be 8')
        
        
    @patch('psutil.cpu_count')
    def test_get_cpu_count_failure(self, mock_cpu_count):
        '''
            Test get_cpu_count when psutil.cpu_count raises an exception.
        '''
        
        mock_cpu_count.side_effect = Exception('Simulate error')
        result = self.cpu_monitor.get_cpu_count()
        self.assertIsNone(result, 'CPU count should be None when an error occurs')
        
        
    @patch('psutil.cpu_freq')
    def test_get_cpu_frequency_success(self, mock_cpu_freq):
        '''
            Test get_cpu_frequency when psutil.cpu_freq work correctly.
        '''
        
        mock_cpu_freq.return_value = MagicMock(current=3200.0) # Simulate 3200 MHz
        result = self.cpu_monitor.get_cpu_frequency()
        self.assertEqual(result, 3200.0, 'CPU frequency should be 3200.0 MHz')
        
    
    @patch('psutil.cpu_freq')
    def test_get_cpu_frequency_failure(self, mock_cpu_freq):
        '''
            Test get_cpu_frequency when psutil.cpu_freq raises an exception.
        '''
        
        mock_cpu_freq.side_effect= Exception('Simulated error')
        result = self.cpu_monitor.get_cpu_frequency()
        self.assertIsNone(result, 'CPU frequency should be None when an error occurs')
        
        
if __name__ == '__main__':
    unittest.main()
