from ligotools.utils import whiten, write_wavfile, reqshift, plot1, plot2, plot3
import pytest
import os
import numpy as np
from ligotools import readligo as rl
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab


CWD = os.getcwd()
filepath = os.path.join(CWD, 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5')

def test_whiten():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(filepath, 'H1')
	time = time_H1
	dt = time[1] - time[0]
	fs = 4096
	NFFT = 4*fs
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
	psd_H1 = interp1d(freqs, Pxx_H1)
	strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
	assert(len(strain_H1_whiten)==131072)

def test_write_wavfile():
	write_wavfile('audio/test.wav',10, np.array([ 4.93134680e-01,  3.95507149e-01,  2.42073125e-01,  5.77207881e-02,
       -1.32135495e-01, -3.06880439e-01, -4.53899402e-01, -5.69172786e-01,
       -6.55444671e-01, -7.18794889e-01, -7.64772510e-01, -7.95153723e-01,
       -8.06100315e-01, -7.88282883e-01, -7.29345141e-01, -6.18562031e-01]))
	assert(os.path.exists('audio/test.wav'))

def test_reqshift():
	res = reqshift(np.array([ 4.93134680e-01,  3.95507149e-01,  2.42073125e-01,  5.77207881e-02,
       -1.32135495e-01, -3.06880439e-01, -4.53899402e-01, -5.69172786e-01,
       -6.55444671e-01, -7.18794889e-01, -7.64772510e-01, -7.95153723e-01,
       -8.06100315e-01, -7.88282883e-01, -7.29345141e-01, -6.18562031e-01]),fshift=400.,sample_rate=4096)
	assert(len(res)==16)

def test_plot1():
	time = np.array([1.12625945e+09, 1.12625945e+09, 1.12625945e+09, 1.12625948e+09,
 1.12625948e+09, 1.12625948e+09])
	SNR = np.array([0.1772689, 0.16502585, 0.15148758, 0.20383076, 0.19690024, 0.18797517])
	indmax = np.argmax(SNR)
	timemax = time[indmax]
	plot1(time, timemax, SNR, 'r', 'H1', 'GW150914', 'png')
	assert(os.path.exists('figures/GW150914_H1_SNR.png'))

