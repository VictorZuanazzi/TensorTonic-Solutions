import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    series = np.array(series)
    mean_ = series.mean()
    series_ = series - mean_
    var_ = (series_ ** 2).sum()
    
    if var_ == 0:
        return [1] + [0] * (len(series) - max_lag)
    
    def _compute_correlation(s1, s2):
        return (s1 * s2).sum() / var_ 
    
    
    auto_correlations = [_compute_correlation(series_, series_)]
    for k in range(1, max_lag + 1):
        
        auto_correlations.append(_compute_correlation(
            series_[:-k], series_[k:]
        ))

    return auto_correlations