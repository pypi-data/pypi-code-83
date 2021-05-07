# Hide all other packages
__all__ = ["simulation"]

import numpy as np
from IPython.display import display, Latex
from datascientists.core.preprocessing import *
from datascientists._config import *

class simulation:
    def __init__(self, df, label, type=None, CI=95, repetition=10000):
        """
        Accept a Pandas DataFrame object with one label.

        df: DataFrame object
            df is the sample or population dataset.
        label: str
            A column name of df
        type: str
            Default: None
            One of "mean", "median", or None. If none, the program will return a pure histogram.
        CI: float
            Default: 95
            Confidence Interval: between 0 to 100.
        repetition: int
            Default: 10000
            The times of the experiment repetition.

        >>> import pandas as pd
        >>> import datascientists as ds
        >>> df = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')

        >>> df_hypo = ds.simulation(df, 'sepal_length', type='mean', CI=99, repetition=5000)
        """
        # Validate type
        if type not in [None, "mean", "median"]:
            raise Exception(f'type must be in one of [None, "mean", "median"]')

        self.df = df
        self.label = label
        self.type = type
        self.CI = CI
        self.repetition = repetition

    # Define function bootstraping for Bootstraping.
    def bootstraping(self):
        """
        Resampling from the sample.
        Returns an DataFrame of bootstrapped sample medians/means from df.

        >>> import pandas as pd
        >>> import datascientists as ds
        >>> df = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')

        >>> df_hypo = ds.simulation(df, 'sepal_length', type='mean', CI=99, repetition=5000)

        >>> df_hypo.bootstraping().head()
        """

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


            # Calculate median and store median
            resampled_median = np.percentile(bootstrap_sample, q=50, interpolation="higher")
            medians = np.append(medians, resampled_median)
            # Calculate mean and store mean
            resampled_mean = np.mean(bootstrap_sample)
            means = np.append(means, resampled_mean)

        if self.type == None:
            sample = self.df.copy()
        elif self.type == "median":
            sample = pd.DataFrame({f"Sample Median of {self.label}": medians})   
        elif self.type == "mean":
            sample = pd.DataFrame({f"Sample Mean of {self.label}": means})

        return sample

    # Define function hist_bootstraping returning histogram of Bootstraping.
    def _hist_bootstraping(self, filename="fig", format="svg"):
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
        # Control displaying CI on plot
        if self.show_CI is True:
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
        if self.show_CI is True:
            title += f"<br>Confidence Interval: {CI}%"
        title += f"<br>Experiment Times: {self.repetition}"
        fig.update_layout(
            title=title,
            xaxis_title=sample_label,
            yaxis_title="Percent",
            width=1200,
            height=600
        )

        # Save plot to the root directory of the current Python kernel.
        fig.write_image(f"{filename}.{format}")
        return fig

    def histogram(self, test="", show_CI=True, filename="fig", format="svg"):
        """
        Return one Hypothesis Testing histogram.

        test: str
            One of ["bootstraping"]
        show_CI:
            Default: True
            Display the CI and observed value on the plot.
        filename: str
            Default: "fig"
            Set the filename of the plot.
        format: One of "png", "svg", "jpeg", "webp"
            Default: "svg"
            Set the plot format.

        >>> import pandas as pd
        >>> import datascientists as ds
        >>> df = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')

        >>> df_hypo = ds.simulation(df, 'sepal_length', type='mean', CI=99, repetition=5000)
        >>> df_hypo.histogram("bootstrapping")
        >>> df_hypo.histogram("bootstrapping", show_CI=False)
        """

        self.show_CI = show_CI

        # Define available Hypothesis testing
        hists = ["bootstrapping"]
        if test not in hists:
            raise Exception(f"test must be in one of {hists}")

        for hist in hists:
            if hist == test:
                return self._hist_bootstraping()