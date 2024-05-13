import numpy as np
from scipy.signal import butter, sosfiltfilt
from plotter import Plot

class SignalProcessor():
    @staticmethod
    def limit_frequency_range(signal, fps):
        """
        Limitting frequency range to realistic a BPM (<240BPM)

        :type signal: np.ndarray[float64]
        :type fps: float
        :rtype: tuple[np.ndarray[np.float64], np.ndarray[np.float64], int]
        """

        N = len(signal)
        frequency_index = np.arange(N)

        frequency = (frequency_index * fps) / N
        mask = frequency <= 4  # mask +240bpm
        frequency = frequency[mask]
        signal = signal[mask]

        return frequency, signal, N

    @staticmethod
    def filter(signal, fps, lstLCHC, name, fors): 
        """
        Applies a butterworth bandpass filter

        :type signal: np.ndarray[float]
        :type fps: float
        :type lstLCHC: list[list[float, float]]
        :type name: str
        :type fors: bool
        :rtype: tuple[np.ndarray[np.float64, plt.figure.Figure]
        """

        order = 8
        nyq = 0.5 * fps # calculate Nyquist frequency, half of sampling rate (fps)
        filtered_signal = []

        for lst in lstLCHC:
            lowcut = lst[0]
            highcut = lst[1] 
            low = lowcut / nyq # normalized cutoff frequencies by dividing with nyq
            high = highcut / nyq # "
            sos = butter(order, [low, high], btype='band', analog=False, output='sos')  # design Butterworth bandpass filter
            filtered_signal.append(sosfiltfilt(sos, signal)) # apply filter to the signal

        x_values = np.arange(sum(len(sublist) for sublist in filtered_signal)) / fps

        if not fors:
            filtered_signal = [item for sublist in filtered_signal for item in sublist]
        else:
            filtered_signal = filtered_signal[0]
            x_values = x_values[:len(filtered_signal)]

        fig = Plot.plot(xvals = x_values, signal = filtered_signal, 
                             xlabel = 'Time [s]', ylabel = 'Value',
                             filename = name + "_filtered", save = False)
        
        return np.array(filtered_signal), fig

    @staticmethod
    def fft(signal, windows, fps, name): 
        """
        Applies a fast fourier transform

        :type signal: np.ndarray[np.float64]
        :type windows: int
        :type fps: float
        :type name: str
        :rtype: tuple[np.ndarray[np.ndarray[np.float64]], np.ndarray[plt.figure.Figure], np.ndarray[np.ndarray[np.float64]]]
        """

        fft_result = []
        frequency = []
        fft_resultm = []
        figs = []

        for i in range(windows):
            window_start = int(len(signal) / windows) * i
            window_end = int(len(signal) / windows) * (i + 1)
            window_signal = signal[window_start:window_end]

            fft_result.append(np.fft.fft(window_signal))
            freq, fft_resultm_temp, N = SignalProcessor.limit_frequency_range(np.abs(fft_result[i]), fps) # take abs since np.ftt.ftt returns complex number
            frequency.append(freq)
            fft_resultm.append(fft_resultm_temp)

            figs.append(Plot.plot(xvals = frequency[-1], signal = (np.abs(fft_resultm[-1])),
                                xticks = np.arange(0, 4.0, 0.5),
                                xlabel = "Frequency [Hz]", ylabel = "Magnitude",
                                filename = name + "_ftt" + str(i), save = True))

        return np.array(fft_resultm), np.array(figs), np.array(frequency)

    @staticmethod
    def psd(signal, windows, frequency, fps, name): 
        """
        Performs power spectral density analysis

        :type signal: np.ndarray[np.ndarray[np.float64]]
        :type windows: int
        :type frequency: np.ndarray[np.ndarray[np.float64]]
        :type fps: float
        :type name: str
        :rtype: tuple[np.ndarray[np.float64], np.ndarray[plt.figure.Figure]]
        """

        psd_result = []
        max_index = []
        figs = []
        frequency_max_indexes = []

        for i in range(windows):
            window_start = int(len(signal) / windows) * i
            window_end = int(len(signal) / windows) * (i + 1)
            window_signal = signal[window_start:window_end]

            _, _, N = SignalProcessor.limit_frequency_range(signal[i], fps)
            psd_result.append(np.abs(window_signal) ** 2 / N)
            max_index.append(np.argmax(psd_result[-1])) # argmax returns max index

            figs.append(Plot.plot(xvals = frequency[i], signal = psd_result[-1][-1],
                                    xticks = np.arange(0, 4.0, 0.4),
                                    xlabel = "Frequency [Hz]", ylabel = "Power",
                                    filename = name + "_psd" + str(i), save = True))
            
        for i, index in enumerate(max_index):
            frequency_max_indexes = frequency[i][max_index]

        return frequency_max_indexes, np.array(figs)
        

    @staticmethod
    def bpm(frequency, length_vid, windows):
        """
        Determines the BPM for an array of frequency or just
        a singular frequency. Returns a plot of BPM's for the 
        different frequencies or returns an integer value corresponding
        to the BPM of the single given frequency

        :type frequency: np.ndarray[np.float64]
        :type length_vid: int
        :type windows: int
        :rtype: plt.figure.Figure or int
        """
        
        lst = []
        figs = []
        start = True

        if windows != 1:
            for freq in frequency:
                if start is True:
                    lst.append(round(freq*60))
                    start = False

                lst.append(round(freq*60))

            xvals = np.arange(0, length_vid+length_vid/windows, length_vid/windows)

            fig = Plot.plot(xvals = xvals, signal = lst,
                            xlabel = "Time [s]", ylabel = "BPM",
                            filename = "BPM", save = True)

        else:
            fig = round(frequency[0]*60)

        return fig