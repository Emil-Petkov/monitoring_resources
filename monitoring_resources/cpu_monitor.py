import psutil
import logging


class CPUMonitor:
    '''
        A class for monitoring CPU statistics.
    '''

    def __init__(self, log_level=logging.ERROR):
        '''
            Initialize the CPUMonitor class with a logger.
        '''

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=log_level)

    def get_cpu_usage(self):
        '''
            Get the current CPU usage percentage.

            Returns:
                float: The CPU usage percentage.
                None: If an error occurs.
        '''

        try:
            return psutil.cpu_percent(interval=1)

        except Exception as e:
            self.logger.error(f"Error getting CPU usage: {e}")
            return None

    def get_cpu_count(self):
        '''
            Get the number of CPU cores.

            Returns:
                int: The numbers of CPU cores.
                None: If an error occurs.
        '''

        try:
            return psutil.cpu_count()

        except Exception as e:
            self.logger.error(f"Error getting CPU count: {e}")
            return None

    def get_cpu_frequency(self):
        '''
            Get the current CPU frequency in megahertz (MHz).

            Returns:
                float: The current CPU frequency in MHz if successful.
                None: If an error occurs.
        '''

        try:
            return psutil.cpu_freq().current

        except Exception as e:
            self.logger.error(f"Error getting CPU frequency: {e}")
            return None
