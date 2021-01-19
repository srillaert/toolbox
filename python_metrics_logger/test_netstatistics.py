from metricslogger import NetStatistics
import pytest

def test_LoadAvg_integrated():
	net_statistics = NetStatistics("wlp4s0")
	assert net_statistics.read_rx_bytes() >= 0
	assert net_statistics.read_tx_bytes() >= 0

def test_LoadAvg_notexisting():
	with pytest.raises(ValueError) as e_info:
		net_statistics = NetStatistics("notexisting")	
	assert str(e_info.value) == "No such interface: 'notexisting'"
