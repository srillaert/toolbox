from metricslogger import Battery
import pytest

def test_Battery_integrated():
	battery = Battery()
	capacity = battery.read_capacity()
	assert capacity >= 0
	assert capacity <= 100