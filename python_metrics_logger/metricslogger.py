import datetime
import re
import time

class LoadAvg:
	def __init__(self, loadavgread):
		# From `man proc` : The first three fields in this file are load average figures giving the number of jobs in the run queue (state R) or waiting  for  disk  I/O (state  D)  averaged  over  1, 5, and 15 minutes.
		split =  loadavgread.split() 
		self.last_minute = float(split[0])

	@classmethod
	def read(cls):
		with open('/proc/loadavg', 'r') as input_file:
			meminforead = input_file.read()
		return cls(meminforead)

line_re = re.compile('^(?P<name>[^:]+):[ ]+(?P<value>\d+)');

class MemInfo:
	def __init__(self, meminforead):
		name_to_value = dict()
		for line in meminforead.splitlines():
			m = line_re.search(line)
			name = m.group('name')
			valuestring = m.group('value')
			value = int(valuestring)
			name_to_value[name] = value
		self.memory_available = name_to_value['MemAvailable'] # MemAvailable: An estimate of how much memory is available for starting new applications, without swapping.

	@classmethod
	def read(cls):
		with open('/proc/meminfo', 'r') as input_file:
			meminforead = input_file.read()
		return cls(meminforead)

# https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-statistics
class NetStatistics:
	def __init__(self, iface):
		self.iface = iface

	def __read_file_content(self, filename):
		filepath = '/sys/class/net/' + self.iface + '/statistics/' + filename
		with open(filepath, 'r') as input_file:
			file_read = input_file.read()
		return int(file_read)

	def read_rx_bytes(self):
		return int(self.__read_file_content('rx_bytes'))

	def read_tx_bytes(self):
		return int(self.__read_file_content('tx_bytes'))

if __name__ == '__main__':
	print('timestamp memory_available load_avg rx_bytes tx_bytes')
	utcnow = datetime.datetime.utcnow()
	wireless_statistics = NetStatistics('wlp4s0')
	while True:
		sleepseconds = 1.0 - (utcnow.microsecond / 1000000.0)
		time.sleep(sleepseconds)
		loadavg = LoadAvg.read()
		meminfo = MemInfo.read()
		rx_bytes = wireless_statistics.read_rx_bytes()
		tx_bytes = wireless_statistics.read_tx_bytes()
		utcnow = datetime.datetime.utcnow()
		print(utcnow.isoformat() + ' ' + str(meminfo.memory_available) + ' ' + str(loadavg.last_minute) + ' ' + str(rx_bytes) + ' ' + str(tx_bytes))
