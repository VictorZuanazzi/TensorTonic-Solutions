import numpy as np
def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    sequence_length = len(values)
    median_sequence_length = sequence_length - window_size + 1
    medians = []
    for start in range(median_sequence_length):
        end = start + window_size
        medians.append(np.median(values[start:end]))

    return medians
        