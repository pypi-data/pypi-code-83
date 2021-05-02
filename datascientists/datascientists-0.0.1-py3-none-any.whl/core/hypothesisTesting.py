# Hide all other packages
__all__ = ["hypothesisTesting"]

import numpy as np
from IPython.display import display, Latex
from datascientists.core.preprocessing import *
from datascientists._config import *

class hypothesisTesting:
    def __init__(self, df, label, type="mean", CI=95):
        """
        Accept a Pandas DataFrame object with one label.

        df: DataFrame object
            df is the sample or population dataset.
        label: str
            A column name of df
        type: str
            Default: "mean"
            One of "mean" or "median"
        CI: float
            Default: 95
            Confidence Interval: between 0 to 100.
        """
        # Validate type
        if type not in ["mean", "median"]:
            raise Exception(f'type must be in one of ["mean", "median"]')

        self.df = df
        self.label = label
        self.type = type
        self.CI = CI

    # Define function bootstraping for Bootstraping.
    def bootstraping(self, repetition=10000):
        """
        Resampling from the sample.
        Returns an DataFrame of bootstrapped sample medians/means from df.

        repetition: int
            Default: 10000
            The times of the experiment repetition.
        """

        self.repetition = repetition

        # Extract the bootstrapping data from self.df
        data = self.df[self.label]
        # Bootstrapping sample size is the length of self.df
        sample_size = len(self.df)
        # Define to arrays to store medians and means
        medians = np.array([])
        means = np.array([])
        # Start "repetition" times of experiment
        for i in np.arange(self.repetition):
            # One trail
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
            bootstrap_sample = data.sample(n=sample_size, replace=True).reset_index(drop=True)
            # Calculate median and store median
            resampled_median = np.percentile(bootstrap_sample, q=50, interpolation="higher")
            medians = np.append(medians, resampled_median)
            # Calculate mean and store mean
            resampled_mean = np.mean(bootstrap_sample)
            means = np.append(means, resampled_mean)

        if self.type == "median":
            sample = pd.DataFrame({f"Sample Median of {self.label}": medians})   
        elif self.type == "mean":
            sample = pd.DataFrame({f"Sample Mean of {self.label}": means})

        return sample

    # Define function hist_bootstraping returning histogram of Bootstraping.
    def hist_bootstraping(self):
        sample = self.bootstraping()
        sample_label = sample.columns[0]
        CI = self.CI
        alpha = 100 - CI
        
        # Calculate left and right
        left_tail = 1/2 * alpha
        left = np.percentile(sample, q=left_tail, interpolation='higher')

        right_tail = 1/2 * alpha + CI
        right = np.percentile(sample, q=right_tail, interpolation='higher')

        # Histogram
        fig = go.Figure()
        fig.add_trace(
            go.Histogram(
                x=sample[sample_label],
                name=sample_label,
                marker_color="rgba(55, 73 ,99, .8)" # rgb + opacity
            )
        )
        # Mark confidence interval
        fig.add_shape(
            type="line", 
            x0=left, y0=0, 
            x1=right, y1=0, 
            line_color="gold"
        )
        # Mark observed value
        if self.type == "median":
            observed_value = np.median(self.df[self.label])
        elif self.type == "mean":
            observed_value = np.mean(self.df[self.label])
        fig.add_trace(
            go.Scatter(
                mode="markers",
                x=[observed_value],
                y=[0],
                name="Observed Value",
                marker=dict(
                    color="red",
                    size=9
                )
            )
        )
        # Set layout
        title = f"{sample_label} Distribution"
        title += f"<br>Confidence Interval: {CI}%"
        title += f"<br>Experiment Times: {self.repetition}"
        fig.update_layout(
            title=title,
            xaxis_title=sample_label,
            yaxis_title="Percent",
            width=1200,
            height=600
        )

        return fig

    def histogram(self, test=""):
        """
        Return one Hypothesis Testing histogram.

        test: str
            One of ["bootstraping"]
        """

        # Define available Hypothesis testing
        hists = ["bootstraping"]
        if test not in hists:
            raise Exception(f"test must be in one of {hists}")

        for hist in hists:
            if hist == test:
                return self.hist_bootstraping()