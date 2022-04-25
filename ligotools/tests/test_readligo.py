from ligotools import readligo as rl
import numpy as np
import pytest

import warnings
warnings.filterwarnings("ignore")

def test_getsegs():
	seglist = rl.getsegs(842657792, 842658792, 'H1', flag='DATA', filelist=None)
	isinstance(seglist, list)
	assert(seglist, rl.SegmentList( [] ))

def test_dq_channel_to_seglist():
	arr = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	segment_list = rl.dq_channel_to_seglist(arr)
	assert(len(segment_list) == 1)

def test_loaddata():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
	isinstance(strain_H1, list)
	assert(len(strain_H1) == 131072)

def test_read_hdf5():
	strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)
	assert(gpsStart == 1126259446)
	assert(ts == 0.000244140625)

