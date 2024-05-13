from gui import App
from video_processing import VideoProcessor
from signal_processing import SignalProcessor
from preprocessing import PreProcesser
from percentile_ranking import PercentileRanker

init_lstLCHC = [[0.08, 7.0]]
name = "first_analysis"
secName = "second_analysis"

def check_entry(data, fps, length_vid):
    """
    Checks for an entry in the entry boxes (lowcut/highcut) of the GUI.
    If no entry has been confirmed, waits for a second and rechecks.

    :type data: np.ndarray[float]
    :type fps: float
    :type length_vid: int
    """
    
    if (app.confirmed == True):
        secFilter, fig_2filt = SignalProcessor.filter(data, fps, app.lstLCHC, secName, True)
        secFtt, figs_2ftt, freq = SignalProcessor.fft(secFilter, app.windows, fps, secName)
        secPsd, figs_2psd = SignalProcessor.psd(secFtt, app.windows, freq, fps, secName)

        fig = SignalProcessor.bpm(secPsd, length_vid, app.windows)

        app.launch(fig_2filt, figs_2ftt, figs_2psd, True, fig, app.windows)
    else:
        app.after(1000, check_entry, data, fps, length_vid)

def main():
    vid = VideoProcessor(app.path)
    data = vid.get_data()
    processed_data, length_vid = PreProcesser.crop(data, vid.fps)

    filter, fig_1filt = SignalProcessor.filter(processed_data, vid.fps, init_lstLCHC, name, False)
    ftt, figs_1ftt, freq = SignalProcessor.fft(filter, app.windows, vid.fps, name)
    psd, figs_1psd = SignalProcessor.psd(ftt, app.windows, freq, vid.fps, name)

    app.launch(fig_1filt, figs_1ftt, figs_1psd, False, 0, app.windows)

    check_entry(processed_data, vid.fps, length_vid)

if __name__ == "__main__":
    app = App(callback=main)
    app.mainloop()