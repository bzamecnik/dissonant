import numpy as np

__all__ = ['harmonic_tone', 'freq_to_pitch', 'pitch_to_freq']

def harmonic_tone(base_freqs, n_partials=1):
    """
    Creates a harmonic tone out of one or more base frequencies.

    Input:
    base_freqs - single value, or an numpy array of base frequencies
    n_partials - number of partial in the harmonic tone

    Output:
    Tuple of (freqs, amplitudes).

    Freqs are a 2D array of the frequencies of partials
    of shape (len(freqs), n_partials)

    Amplitudes are of the same shape.

    The amplitude values for a single harmonic tone are going down
    inversely in this case.
    """
    base_freqs = np.atleast_2d(base_freqs)
    idx = 1 + np.arange(n_partials).reshape(1, -1)
    freqs = np.outer(base_freqs, idx)
    # eg. amplitudes inversely going down
    amplitudes = 1 / np.tile(idx[0], (base_freqs.shape[1], 1))
    # amplitudes = np.ones(freqs.shape)
    return freqs, amplitudes

def freq_to_pitch(freq, base_freq=440.0, steps_per_octave=12):
    return np.log2(np.array(freq) / base_freq) * steps_per_octave

def pitch_to_freq(pitch, base_freq=440.0, steps_per_octave=12):
    return (2 ** (np.array(pitch) / steps_per_octave)) * base_freq
