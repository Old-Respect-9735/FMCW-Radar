import numpy as np
import matplotlib.pyplot as plt

# sample rate and duration
fs = 1000
duration = 1

# time 
t = np.linspace(0, duration, duration * fs, endpoint=False)
t2 = np.linspace(0, 2 * duration, 2 * duration * fs, endpoint=False)

# ref frequency
fc = 10

# modulation frequency and index
fm = 10
beta = 5

# Linear modulation signal 
modulation = np.linspace(-beta, beta, len(t))
# modulation2 = np.linspace(beta, -beta, len(t))
modulation2 = np.linspace(beta, beta, len(t))
modulation3 = np.concatenate((modulation, modulation2))

print(t2)
print(np.size(t2))
# print(np.size(modulation3))

# fm signal
# fm_signal = np.sin(2 * np.pi * (fc + modulation) * t)

# plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 1)
# plt.plot(t, modulation, label='Modulation signal')
# plt.plot(t, modulation2, label = "Modulation 2 signal")
# plt.xlabel('Time (s)')
# plt.ylabel('Frequency Deviation')
# plt.legend()

# plt.subplot(2, 1, 2)
# plt.plot(t, fm_signal, label='FM signal')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()

# mod 3

modulation4 = modulation3[0:] + fc
print(modulation4 * t2)

fm_signal2 = np.sin(2 * np.pi * (modulation4) * t2)


plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t2, modulation3, label = "Modulation 3 signal")
plt.xlabel('Time (s)')
plt.ylabel('Frequency Deviation')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t2, fm_signal2, label='FM signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()


plt.subplot(3, 1, 3)
plt.plot(t2, modulation4, label = "frequency deviation")
plt.xlabel('Time (s)')
plt.ylabel('Frequency Deviation')
plt.legend()

plt.tight_layout()
plt.show()


