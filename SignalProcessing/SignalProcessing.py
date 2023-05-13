import numpy
import numpy as np
import scipy
from scipy import signal
from scipy import fft
import matplotlib.pyplot as plt
import pandas as pd

n = 500
Fs = 1000
F_max = 21
F_filter = 28

generation = numpy.random.normal(0, 10, n)

time_check = numpy.arange(n) / Fs

w = F_max / (Fs / 2)
parametr = scipy.signal.butter(3, w, 'low', output='sos')
filtered_signal = scipy.signal.sosfiltfilt(parametr, generation)

fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(time_check, filtered_signal, linewidth=1)
ax.set_xlabel('«текст»', fontsize=14)
ax.set_ylabel('«текст»', fontsize=14)
plt.title('«текст»', fontsize=14)

# fig.savefig("./SignalProcessing/title.png", dpi=600)

spectrum = scipy.fft.fft(filtered_signal)

mod = numpy.abs(scipy.fft.fftshift(spectrum))
print("Mодульне значення:" + str(mod))

checks = scipy.fft.fftfreq(n, 1 / n)

fftshift = scipy.fft.fftshift(checks)

ax.plot(checks, spectrum, linewidth=1)
ax.set_xlabel('«текст»', fontsize=14)
ax.set_ylabel('«текст»', fontsize=14)
plt.title('«текст»', fontsize=14)

# fig.savefig("/SignalProcessing/title2.png", dpi=600)

discrete_signals = []
discrete_spectrum = []
discrete_signal_after_filers = []
discretes_signal_after_filers = []
diff = []
diff2 = []
signs_noise = []

for Dt in [2, 4, 8, 16]:
    discrete_signal = numpy.zeros(n)
    for i in range(0, round(n / Dt)):
        discrete_signal[i * Dt] = int(filtered_signal[i * Dt])
    discrete_signals += [list(discrete_signal)]
    discrete_spectrum += [list(np.fft.fft(discrete_signal))]

    w = F_filter / (Fs / 2)
    parameters_filter = scipy.signal.butter(3, w, 'low', output='sos')
    discrete_signal_after_filers = scipy.signal.sosfiltfilt(parameters_filter, discrete_signal)
    discretes_signal_after_filers += [list(discrete_signal_after_filers)]

    E1 = discrete_signal_after_filers - filtered_signal
    diff += [E1]

    dyspers = numpy.var(filtered_signal)
    dyspers_diff = numpy.var(E1)
    diff2 += [dyspers_diff]
    sign_noise = numpy.var(filtered_signal) / numpy.var(E1)
    signs_noise += [sign_noise]

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_check, discrete_signals[s], linewidth=1)

    s += 1

fig.supxlabel("Час", fontsize=14)
fig.supylabel("Амплитудща", fontsize=14)
fig.savefig("figures\prac3_pictures1.png", dpi=600)

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))
s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_check, discrete_spectrum[s], linewidth=1)

    s += 1
fig.supxlabel("Час", fontsize=14)
fig.supylabel("Spectrum", fontsize=14)
fig.savefig("figures\prac3_pictures2.png", dpi=600)

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_check, discretes_signal_after_filers[s], linewidth=1)

    s += 1
fig.supxlabel("Час", fontsize=14)
fig.supylabel("Видновлення", fontsize=14)
fig.savefig("figures\prac3_pictures3.png", dpi=600)

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_check, diff[s], linewidth=1)

    s += 1
fig.supxlabel("Час", fontsize=14)
fig.supylabel("Видновлення", fontsize=14)
fig.savefig("figures\prac3_pictures4.png", dpi=600)

fig, ax = plt.subplots(1, 1, figsize=(21 / 2.54, 14 / 2.54))

x = [2, 4, 8, 16]
y = diff2
print("diff2 \n" + str(diff2))

ax.plot(x, y, linewidth=1)

fig.supxlabel("Крок дискредитац", fontsize=14)
fig.supylabel("Дисперсия", fontsize=14)
fig.savefig("figures\prac3_picture5.png", dpi=600)

fig, ax = plt.subplots(1, 1, figsize=(21 / 2.54, 14 / 2.54))

y = pd.DataFrame(signs_noise)

ax.plot(x, y, linewidth=1)

fig.supxlabel("Крок дискредитац", fontsize=14)
fig.supylabel("Отношение сигнал шум", fontsize=14)
fig.savefig("figures\prac3_picture6.png", dpi=600)
