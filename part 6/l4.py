from abc import ABCMeta, abstractmethod

class BluetoothUtils(metaclass=ABCMeta):
    @abstractmethod
    def connect_device(self, device_id):
        pass

class WirelessUtils(metaclass=ABCMeta):
    @abstractmethod
    def send_wireless_data(self, data):
        pass

class MultiUtils(BluetoothUtils, WirelessUtils):
    @abstractmethod
    def connect_device(self, device_id):
        pass
    @abstractmethod
    def send_wireless_data(self, data):
        pass


class AirPods(BluetoothUtils):
    def connect_device(self, device_id):
        print(f"[AirPods] - {device_id} - Connecting to device")


class SamsungHeadphones(MultiUtils):
    def connect_device(self, device_id):
        print(f"[SamsungHeadphones] - {device_id} - Connecting to device")

    def send_wireless_data(self, data):
        print(f"[SamsungHeadphones] - {data} - Sending wireless data")


class DefaultHeadphones(WirelessUtils):
    def send_wireless_data(self, data):
        print(f"[DefaultHeadphones] - {data} - Sending wireless data")


air = AirPods()
samsung  = SamsungHeadphones()
default   = DefaultHeadphones()

air.connect_device('iphone')
samsung.connect_device('android device')
samsung.send_wireless_data("0x11")
default.send_wireless_data(222)
