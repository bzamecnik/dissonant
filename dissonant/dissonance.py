import numpy as np

from . import models

__all__ = ['dissonance', 'dissonance_pair']

def dissonance(freqs, amps, model='sethares1993', aggregation=lambda d: d.sum()):
    """
    Computes dissonance score for chord composed of muliple frequences,
    each possible with different amplitudes using a given dissonance model.
    """
    # Get rid of practically zero terms:
    nonzero_amps = amps >= 1e-6
    freqs, amps = freqs[nonzero_amps], amps[nonzero_amps]

    # The frequencies are sorted in order to generate pairs where f_1 <= f_2.
    # Otherwise bad things happen.
    freqs = freqs.flatten()
    freq_idx = freqs.argsort()
    freqs = freqs[freq_idx]
    amps = amps.flatten()[freq_idx]
    n = len(freqs)
    idx_pairs = np.array([(i, j) for i in range(n) for j in range(n) if i < j])
    idx_1 = idx_pairs[:, 0]
    idx_2 = idx_pairs[:, 1]
    dissonances = dissonance_pair(
        freqs[idx_1], freqs[idx_2],
        amps[idx_1], amps[idx_2],
        model)
    return aggregation(dissonances)

def dissonance_pair(f_1, f_2, a_1, a_2, model):
    """
    Computes the dissonance metric for a pair(s) of sinusoidal tones with given
    frequency and amplitude using the specified model.

    The parameters can be either a single value or a numpy array. In the latter
    case the computation is vectorized for the whole array.

    Parameters:
    f_1 - lower frequencies
    f_2 - upper frequencies
    a_1 - amplitudes for f_1
    a_2 - amplitudes for f_2
    model - known model name (see list_models())

    Returns:
    dissonance - a single value or array
    """
    assert_nonnegative((f_1, f_2, a_1, a_2))
    if type(model) == str:
        model = models.models[model]
    return model.dissonance_pair(f_1, f_2, a_1, a_2)

def assert_nonnegative(values):
    for v in values:
        assert np.all(v >= 0)
