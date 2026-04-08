import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    num_classes = max(y_true) + 1 if num_classes is None else num_classes
    cm = np.zeros((num_classes, num_classes))
    for i in range(num_classes):
        for j in range(num_classes):
            cm[i, j] = ((y_true == i) & (y_pred == j)).sum()

    if normalize == "true":
        cm /= cm.sum(axis=1, keepdims=True)
    elif normalize == "pred":
        cm /= cm.sum(axis=0, keepdims=True)
    elif normalize == "all":
        cm /= cm.sum()
        
    return cm