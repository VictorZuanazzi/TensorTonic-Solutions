import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    bins_start = np.linspace(0, 1, n_bins, endpoint=False)
    step = bins_start[1] - bins_start[0]
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    ece = 0
    for start in bins_start:
        end = start + step
        if np.isclose(end, 1.0):
            mask = (start <= y_pred) & (y_pred <= end)
        else:
            mask = (start <= y_pred) & (y_pred < end)
        norm = mask.sum()
        
        if norm == 0:
            continue
            
        acc = y_true[mask].sum()
        conf = y_pred[mask].sum()

        ece += np.abs(acc - conf)

    ece /= len(y_pred)
    
    return ece
    