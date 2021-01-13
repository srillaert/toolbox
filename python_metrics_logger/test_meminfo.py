from metricslogger import MemInfo

def test_MemInfo_integrated():
	meminfo = MemInfo.read()
	assert meminfo.memory_available >= 0

def test_MemInfo_unit():
	meminforead = """MemTotal:        8028308 kB
MemFree:         1782368 kB
MemAvailable:    4577480 kB
Buffers:          524892 kB
Cached:          2861064 kB
SwapCached:         2564 kB
Active:          3095164 kB
Inactive:        2446836 kB
Active(anon):    1514968 kB
Inactive(anon):  1175888 kB
Active(file):    1580196 kB
Inactive(file):  1270948 kB
Unevictable:      124568 kB
Mlocked:              16 kB
SwapTotal:       8388604 kB
SwapFree:        8345788 kB
Dirty:              1468 kB
Writeback:             0 kB
AnonPages:       2275012 kB
Mapped:           838176 kB
Shmem:            535420 kB
KReclaimable:     248604 kB
Slab:             435000 kB
SReclaimable:     248604 kB
SUnreclaim:       186396 kB
KernelStack:       15104 kB
PageTables:        45060 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    12402756 kB
Committed_AS:    9875108 kB
VmallocTotal:   34359738367 kB
VmallocUsed:       47892 kB
VmallocChunk:          0 kB
Percpu:             9984 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:      493256 kB
DirectMap2M:     7772160 kB
DirectMap1G:           0 kB
"""
	meminfo = MemInfo(meminforead)
	assert meminfo.memory_available == 4577480
