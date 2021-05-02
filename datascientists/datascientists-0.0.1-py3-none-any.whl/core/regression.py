# Hide all other packages
__all__ = ["regression"]

import numpy as np
from IPython.display import display, Latex
from datascientists.core.preprocessing import *
from datascientists._config import *

class regression:
    def __init__(self, df, label_x, label_y):
        """
        Accept a Pandas DataFrame object with two labels.

        df: DataFrame object
        label_x: str
            A column name of df
        label_y: str
            A column name of df
        """

        self.df = df
        self.label_x = label_x
        self.label_y = label_y
        self.x = df[label_x]
        self.y = df[label_y]
        self.standard_x = preprocessing(self.x).standardize()
        self.standard_y = preprocessing(self.y).standardize()

    # Define function correlation returning correlation coefficient r
    def correlation(self, formula=False):
        """
        Return correlation coefficient r. 

        formula: boolean
            Return formula.
        """

        # assert isinstance(df, pd.core.frame.DataFrame), "df is not DataFrame!"
        # Display formula
        if formula is True:
            # r for sample
            display(Latex(r"$r_{xy} = \frac{S_{xy}}{S_{x}S_{y}}$"))
            # r for population
            display(Latex(r"$\rho_{xy} = \frac{\sigma_{xy}}{\sigma_{x}\sigma_{y}}$"))
        
        # Calculate correlation coefficient r
        r = np.mean(self.standard_x * self.standard_y)
        return r

    # Define function slope returning slope
    def slope(self,  formula=False):
        """
        Return regresion slope b. 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$b = r \times \frac{SD_y}{SD_x}$"))

        # Calculate slope m
        r = self.correlation()
        slope = r * np.std(self.y) / np.std(self.x)
        return slope

    # Define function intercept returning regression intercept
    def intercept(self, formula=False):
        """
        Return regression intercept a. 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$a = r \times \frac{\Delta_{y}}{\Delta_{x}}$"))

        # Calculate intercept
        slope = self.slope()
        intercept = np.mean(self.y) - slope * np.mean(self.x)
        return intercept

    # Define function fit returning a array of fitted values
    def fit(self, formula=False):
        """
        Return the fitted y. 

        formula: boolean
            Return formula.
        """
        
        # Display formula
        if formula is True:
            display(Latex(r"$\overline{Y} = a +  b \overline{X}$"))

        # Calculate fitted y
        b = self.slope()
        a = self.intercept()
        fitted = a + b * self.x
        return fitted

    # Define function error returning residuals
    def error(self, formula=False):
        pass
        """
        Return the errors. 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$e = y - \hat{y}$"))

        # Calculate residuals
        fitted = self.fit()
        residual = self.y - fitted
        return residual

    # Define function residual returning residuals
    def residual(self, formula=False):
        """
        Return the residuals e. 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$e = y - \hat{y}$"))

        # Calculate residuals
        fitted = self.fit()
        residual = self.y - fitted
        return residual

    # Define function mse returning mean-square error(MSE)
    def mse(self, formula=False):
        """
        Return the mse (mean-square error). 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$MSE = \frac{1}{n} \sum^{n}_{i = 1}({y_i - \hat{y}_i})^2 = \overline{e^2}$"))

        # Calculate mse
        # return np.mean((df[label_y] - regression.fit(df, label_x, label_y)) **2)
        residual = self.residual()
        mse = np.mean(residual**2)
        return mse

    # Define function rmse returning root mean-square error(MSE)
    def rmse(self, formula=False):
        """
        Return the rmse (root mean-square error). 

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$RMSE = \sqrt{\frac{1}{n}\sum^{n}_{i = 1}({y_i - \hat{y}_i})^2} = \sqrt{MSE}$"))

        # Calculate rmse
        mse = self.mse()
        rmse = np.sqrt(mse)
        return rmse

    # Define function linearRegression returning Scatter and Linear Regression with errors
    def linearRegression(self, fixed_ratio=False, show_errors=False, num_errors=5, filename="fig", format="svg"):
        """
        Return Scatter and Linear Regression with errors. 

        fixed_ratio: boolean
            Default: False
            Fixed Ratio Axes.
        show_errors: boolean
            Default: False
            Randomly select several number of errors and display in the plot.
        num_errors: int
            Default: 5
            Modify the number of errors.
        filename: str
            Default: "fig"
            Set the filename of the plot.
        format: One of "png", "svg", "jpeg", "webp"
            Default: "svg"
        """

        b = self.slope()
        a = self.intercept()
        fitted = self.fit()
        rmse = self.rmse()

        # Linear Regression Prediction
        fig = go.Figure()

        # Add trace self.x & self.y
        fig.add_trace(go.Scatter(
            mode="markers",
            x=self.x,
            y=self.y,
            name=self.label_y,
            marker_color="rgba(55, 73 ,99, .8)" # rgb + opacity
            )
        )

        # Add trace self.x & Linear Prediction
        fig.add_trace(go.Scatter(
            mode="lines",
            x=self.x,
            y=fitted,
            name="Linear Prediction",
            marker_color="rgba(248, 202, 84, .8)" # rgb + opacity
            )
        )

        # Set layout
        title = f"Linear Regression of {self.label_y} vs. {self.label_x}"
        title += f"<br>Regression Slope b: {np.round(b, 2)}" # Add slope to title. <br> next line in HTML
        title += f"<br>Regression Intercept a: {np.round(a, 2)}" # Add error to title. <br> next line in HTML
        title += f"<br>Root mean squared error rmse: {np.round(rmse, 2)}" # Add rmse to title. <br> next line in HTML
        fig.update_layout(
            title=title,
            xaxis_title=self.label_x,
            yaxis_title=self.label_y,
            width=1200,
            height=600
        )
        # https://plotly.com/python/axes/#fixed-ratio-axes
        if fixed_ratio is True:
            fig.update_yaxes(scaleanchor="x", scaleratio=1)

        # Add errors of samples to fig
        if show_errors is True:
            # Randomly select samples points from self.df
            samples = self.df.sample(n=num_errors, replace=False)
            # Iterate all samples as error points.
            for i in samples.index:
                x0, y0 = samples.loc[i, self.label_x], samples.loc[i, self.label_y]
                # Calculate errors between sample points and predicted y as y1
                x1, y1 = x0, a + b * x0
                fig.add_shape(
                    type="line",
                    x0=x0, y0=y0,
                    x1=x0, y1=y1,
                    line_color="red"
                )

        # Save plot to the root directory of the current Python kernel.
        fig.write_image(f"{filename}.{format}")
        # For advanced usage. Also display the figure, more than fig.show()
        return fig

    # Define function residualPlot returning Residual Plot from linearRegression.
    def residualPlot(self, fixed_ratio=False, filename="fig", format="svg"):
        """
        Return Scatter of residuals e. 

        fixed_ratio: boolean
            Default: False
            Fixed Ratio Axes.
        filename: str
            Default: "fig"
            Set the filename of the plot.
        format: One of "png", "svg", "jpeg", "webp". 
            Default: "svg".
        """
        # Calculate residuals
        residual = self.residual()
        # self.df["Residual"] = residual

        # Construct residual plot
        fig = go.Figure()

        # Add trace x & Residuals
        fig.add_trace(go.Scatter(
            mode="markers",
            x=self.x,
            #y=self.df["Residual"],
            y=residual,
            name="Residuals",
            marker_color="rgba(246, 46, 56, .8)" # rgb + opacity
            )
        )

        # Add horizontal axis
        fig.add_shape(
            type="line",
            x0=min(self.x), y0=0,
            x1=max(self.x), y1=0,
            line_color="rgba(0, 0, 120, .8)"
        )

        # Set layout
        title = f"Residual Plot of Residuals vs. {self.label_x}"
        fig.update_layout(
            title=title,
            xaxis_title=self.label_x,
            yaxis_title="Residuals",
            width=1200,
            height=600
        )
        # https://plotly.com/python/axes/#fixed-ratio-axes
        if fixed_ratio is True:
            fig.update_yaxes(scaleanchor="x", scaleratio=1)

        # Save plot to the root directory of the current Python kernel.
        fig.write_image(f"{filename}.{format}")
        # For advanced usage. Also display the figure, more than fig.show()
        return fig