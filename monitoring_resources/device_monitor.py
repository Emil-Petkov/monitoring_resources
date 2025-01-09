import psutil
import logging


class DeviceMonitor:
    '''
        A class for monitoring connected devices.
    '''

    def __init__(self, log_level=logging.ERROR):
        '''
            Inicialize the DeviceMonitor class with logger.
        '''

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=log_level)

    def list_devices(self):
        '''
            Get a list of all connected devices.

            Returns:
                list: A list of disk partitions information (e.g., disk partitions).
                None: If an error occurs.
        '''

        try:
            devices = psutil.disk_partitions()
            self.logger.info('Successfully listed devices.')
            return devices

        except Exception as e:
            self.logger.error(f'Error listing devices: {e}')
            return []

    def device_usage(self, device):
        '''
            Get a usage statistics for a specific device.

            Args:
                device (str): The device path (e.g., 'C:\\').

            Returns:
                dict: Usage information with keys 'total', 'used' and 'free'.
                None: If an error occurs.
        '''

        if not self.is_device_accessible(device):
            self.logger.warning(f'Device {device} is not accessible.')
            return None

        try:
            usage = psutil.disk_usage(device)
            return {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent,
            }

        except Exception as e:
            self.logger.error(f'Error getting usage for device {device}: {e}')
            return None

    def is_device_accessible(self, device):
        '''
            Check if a device is accessible.

            Args:
                device (str): The device path (e.g., 'C\\').

            Returns:
                bool: True if the device is assessible, False otherwise.
        '''

        try:
            psutil.disk_usage(device)
            self.logger.info(f'Device {device} is accessible.')
            return True

        except Exception as e:
            self.logger.warning(f'Device {device} is not accessible: {e}.')
            return False
