from metricslogger import LoadAvg

def test_LoadAvg_integrated():
	loadavg = LoadAvg.read()
	assert loadavg.last_minute >= 0

def test_LoadAvg_unit():
	loadavgread = """0.21 0.16 0.26 3/803 45443
"""
	loadavg = LoadAvg(loadavgread)
	assert loadavg.last_minute == 0.21
