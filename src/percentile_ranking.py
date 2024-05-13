import pandas as pd

class PercentileRanker():
    @staticmethod
    def detPercentileRanking(activeBPM, restBPM):
        """
        Determines the percentile ranking of given active and rest BPM
        corresponding to the dataset.

        :type activeBPM: int
        :type restBPM: int
        """

        dataset_url = "https://pmagunia.com/assets/data/csv/dataset-72971.csv"
        pulse_data = pd.read_csv(dataset_url)

        pulse_RestValues = pulse_data['Rest'] # rest column in dataset
        pulse_ActValues = pulse_data['Active'] # active column in dataset

        resting_percentile = (pulse_RestValues < restBPM).mean() * 100
        post_exercise_percentile = (pulse_ActValues < activeBPM).mean() * 100

        print("Your resting heart rate percentile ranking:", resting_percentile)
        print("Your post-exercise heart rate percentile ranking:", post_exercise_percentile)