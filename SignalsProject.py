import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
from scipy.io import wavfile

#####################################################################
'''These are the inputs that you could change'''

audio_files = ('AhmedAudio.wav', 'safawt.wav', 'nesegemaa.wav')
members = ('Ahmed', 'Safwat', 'Nour')
a = 1.5
t0 = 0.5
ws = 20000

#####################################################################

# A simple function that just plots and label the inputs, just to prevent repeated code.
def quick_plot(time, wave, title, x_axis):
    plt.figure()
    plt.plot(time, wave)
    plt.xlabel(x_axis)
    plt.ylabel('Amplitude')
    plt.title(title)
    
# Reading and plotting the signals for each group member
sample_rates = []
waves = []
for i in range(len(audio_files)):
    sample_rate, wave = wavfile.read(audio_files[i])
    sample_rates.append(sample_rate)
    
    if len(wave.shape) > 1:
        wave = wave[:, 0]
    
    waves.append(wave)
    t = np.arange(len(waves[i])) / sample_rates[i]
    
    quick_plot(t, waves[i], f"{members[i]}'s Audio", 'Time [s]')

# Shifting, Scaling, and Outputting the modified voices for each member
modified_waves = []
for i in range(len(waves)):
    t = np.arange(len(waves[i])) / sample_rates[i]
    a = 1.5
    t0 = 0.5
    t_modified = (t + t0)/a
    
    modified_wave = np.zeros(len((t_modified*sample_rates[i]).astype(int)))
    modified_wave[:] = waves[i][(t_modified*sample_rates[i]).astype(int)]
    modified_waves.append(modified_wave)

    quick_plot(t_modified, modified_waves[i], f"{members[i]}'s Modified Audio", 'Time[s]')

    wavfile.write(f'test{i+1}.wav', sample_rates[i], modified_wave.astype(np.int16))

# Adding the original signal to the modified signal and outputting
combined_waves = []
for i in range(len(waves)):
    combined_waves.append(waves[i] + modified_waves[i])
    t= np.arange(len(waves[i])) / sample_rates[i]
    
    quick_plot(t, combined_waves[i], f"{members[i]}'s Combined Audio", 'Time [s]')

    wavfile.write(f'test{i+4}.wav', sample_rates[i], combined_waves[i].astype(np.int16))

# Finding the Fourier Transform of each signal
fft_waves = []
for i in range(len(waves)):
    N = len(waves[i])
    T = 1.0/sample_rates[i]
    
    frequency = fftfreq(N, T)
    fft_wave = fft(waves[i])
    fft_waves.append(fft_wave)
    
    #frequency_test = np.linspace(0.0, N/4, int(N/2))
    #y = 2/N * np.abs(fft_waves[i][1][:int(N/2)])
    quick_plot(frequency, fft_waves[i], f"{members[i]}'s FFT Audio", 'Frequency [Hz]')
    
    shift = np.exp(2j * np.pi * ws * np.arange(N) / sample_rates[i])
    shifted_fft_wave =  fft_wave * shift
    
    shifted_wave = ifft(shifted_fft_wave)
    shifted_wave = np.real(shifted_wave)
    
    t = len(shifted_wave)/sample_rates[i]
    
    wavfile.write(f'test{i+7}.wav', sample_rates[i], shifted_wave.astype(np.int16))
    

# Shifting the Fourier Transformed signals
shifted_fft_waves = []
shifted_waves = []
for i in range(len(waves)):
    shift = np.exp(2j * np.pi * ws * np.arange(len(waves[i])) / sample_rates[i])
    shifted_fft_wave = fft_waves[i] * shift
    shifted_fft_waves.append(shifted_fft_wave)
    
    shifted_wave = ifft(shifted_fft_wave)
    shfited_wave = np.real(shifted_wave)
    shifted_waves.append(shifted_wave)
    
    quick_plot(len(shifted_wave)/sample_rates[i]*shift, shifted_wave, f"{members[i]}'s Shifted Wave", 'Time [s]')
    
    
    
    
    
    
    
    
    