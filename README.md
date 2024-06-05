# Signal and System Course Project
# Sound Recording and Analysis
## Project rules
### 1- Each group should have three students
### 2- The project should be implemented using python
### 3- Grades are based on the submitted code as well as a project evaluation
### 4- All the values in the project should be variable and could be changed during the evaluation
### 5- You may use existing python Fourier transform functions (but you have to adjust the parameters
### correctly)
## In this project you will use python to do the following
### 1- Each member of the group has to record the following sentence
### “The signals course is useful and interesting”
### You have to know exactly the sampling rate used.
### 2- The time signals 𝑥(𝑡) of all the group recording should be plotted
### 3- Implement a function to scale and time the recoded time signal
#### 𝑦(𝑡) = 𝑥(𝑎𝑡 − 𝑡0)
### and play the time scaled and shifted version
### 4- Add the time scaled and shifted signal to the original signal and play the resulting signal
#### 𝑦(𝑡) = 𝑥(𝑡) + 𝑥(𝑎𝑡 − 𝑡0)
### 5- Convert the find the Fourier transform of the each voice signal
### 6- Shift the Fourier transform function by a frequency equal to 𝜔𝑠 and perform an inverse Fourier
### transform and play the time version
### 7- Run the Fourier transform through a low pass filter with cutoff frequency 𝜔𝑐 and perform an
### inverse Fourier transform to the time domain and play the signal
### 8- Run the Fourier transform through a High pass filter with cutoff frequency 𝜔𝑐 and perform an
### inverse Fourier transform to the time domain and play the signal
### 9- Multiply the frequency transform by the following function
