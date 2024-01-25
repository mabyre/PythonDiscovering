""" Digit Signal Processing functions

    Moving Average Calculation in Digital Signal Processing

    Noise Filtering: Rolling averaging can be used to filter out noise or random fluctuations in a signal. By smoothing the signal over a period of time, it can help highlight long-term trends while reducing short-term noise.

    Trend Analysis: By calculating the rolling average over larger windows, one can obtain a better representation of the long-term trends of a signal. This can be useful for identifying general patterns or behaviors in time series.

    Reducing rapid variations: If a signal exhibits rapid variations that are not of interest, rolling averaging can smooth them out, allowing clearer visualization of important features.

    Outlier Elimination: Rolling averaging can help eliminate outliers or sudden spikes that could be the result of measurement errors or corrupted data.

    Tracking temporal evolution: By smoothing a signal, rolling averaging can make it easier to track large temporal changes while minimizing unnecessary fluctuations.

    Improved visualization: When graphing temporal data, using the rolling average can make the visualization more readable by reducing noise and highlighting trends.
"""
import numpy

def moving_average(signal, window, mode='valid'):
    """ Use convolve to calculate moving average
        Args:
        - window: is calculate as integral calculation of the function equal to 1
          sigma(weights) = 1
    """
    weights = numpy.repeat(1.0, window)/window
    nparray_values = numpy.asarray(signal, dtype=float)
    smas = numpy.convolve(nparray_values, weights, mode)
    return smas
