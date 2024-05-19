class PreProcesser():
    @staticmethod
    def crop(lst, fps):
        """
        Crops the video length to 10-second interval to make sure that all windows
        are of the same length. (e.g. 34s vid -> 30s vid, last 4s are deleted)

        :type lst: np.ndarray[np.float64]
        :type fps: float
        :rtype: tuple[np.ndarray[np.float64], int]
        """
        
        length_video = round(len(lst) / fps)
        shortend_video = length_video - (length_video%10)

        new_lst = lst[:(shortend_video*round(fps))]

        return new_lst, int(len(new_lst)/fps)
