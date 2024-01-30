import numpy as np


def calculate_covariance_matrix(data: np.ndarray) -> np.ndarray:
    """
    Calculates the covariance matrix for the given data.

    Args:
    data (np.ndarray): A 2D array of data.

    Returns:
    np.ndarray: The covariance matrix.
    """
    mean_values = np.mean(data, axis=0)
    n = len(data)
    cov_matrix = np.zeros((data.shape[1], data.shape[1]))
    for i in range(data.shape[1]):
        for j in range(data.shape[1]):
            cov_matrix[i, j] = np.sum(
                (data[:, i] - mean_values[i]) * (data[:, j] - mean_values[j])
            ) / (n - 1)
    return cov_matrix
