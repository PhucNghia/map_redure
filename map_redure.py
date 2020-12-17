test = [[1, 0.1], [2, 0.5], [6, 0.2], [2, 0.7], [3, 0.8], [5, 0.1], [4, 0.3], [1, 0.2], [2, 0.4], [3, 0.3], [7, 0.7]]


class Device:
    def __init__(self, deviceId, x):
        self.deviceId = deviceId
        self.x = x


class MapRedure:
    def __init__(self):
        self

    @classmethod
    def run(cls):
        devices = []
        for i in range(len(test)):
            devices.append(Device(test[i][0], test[i][1]))

        # process map
        device_map = {}
        for device in devices:
            if device.deviceId in device_map:
                device_map[device.deviceId] = device_map.get(device.deviceId) + 1
            else:
                device_map[device.deviceId] = 1

        for device in device_map:
            print(device, device_map[device])

        # implement with multi thread

        # for i in range(len(test)):
        #     devices.append(Device(test[i][0], test[i][1]))
        #
        # # process map
        # device_map_list = []
        # batch_size = 3
        #
        # for i in range(0, len(devices), batch_size):
        #     # create multi thread here
        #     cls.process_map(devices, i, batch_size, device_map_list)
        #
        # for i in device_map_list:
        #     print(i)

    def process_map(devices, i, batch_size, device_map_list):
        print("thread i: ", i)
        for device in devices[i:i + batch_size]:
            device_map = {device.deviceId: 1}
            device_map_list.append(device_map)


if __name__ == "__main__":
    MapRedure.run()
