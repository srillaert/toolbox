from metricslogger import NetStatistics

def test_LoadAvg_integrated():
	net_statistics = NetStatistics("wlp4s0")
	assert net_statistics.read_rx_bytes() >= 0
	assert net_statistics.read_tx_bytes() >= 0
