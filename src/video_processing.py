import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from plotter import Plot
from preprocessing import PreProcesser

class VideoProcessor():
    def __init__(self, filepath):
        """
        Initialisation function of VideoProcessor class, used to 
        set the video's filepath (for capture) and fps as object attributes

        :type filepath: str
        """

        self.filepath = filepath
        self.cap = cv.VideoCapture(self.filepath)
        self.fps = self.cap.get(cv.CAP_PROP_FPS)

    def get_data(self):
        """
        Extracts the data corresponding to the red channel from the video and returns
        an numpy array containing floats ranging from 0 to 255 with 255 being the reddest.
        These floats are the mean of all the red pixels of a singular frame of the video, 
        the numpy array is the whole video (after preprocessing).

        :rtype: np.ndarray[np.float64]
        """

        peaks = []
        
        while True:
            isTrue, frame = self.cap.read() # returns boolean that says if frame is successfully read, and the frame
            
            if not isTrue:
                break

            b, g, r = cv.split(frame) # split three channels, opencv uses BGR format
            onlyred = cv.merge([b*0, g*0, r]) 
            peaks.append(np.mean(onlyred))

        self.cap.release() # stop capturing frames

        peaks = np.array(peaks) # convert to numpy array for faster iterations

        x_values = np.arange(len(peaks)) / self.fps 
        fig = Plot.plot(xvals = x_values, signal = peaks, 
                             xlabel = "Time [s]", ylabel = "Mean Pixel Intensity",
                             filename = "onlyRed", save = True)

        return peaks