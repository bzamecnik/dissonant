import numpy as np

__all__ = ['harmonic_tone', 'freq_to_pitch', 'pitch_to_freq']

def harmonic_tone(base_freqs, n_partials=1, profile='exp'):
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
    idx = 1 + np.arange(n_partials)
    freqs = np.outer(np.atleast_2d(base_freqs), idx.reshape(1, -1))
    # eg. amplitudes inversely going down
    if profile == 'exp':
        # exponential fall-off
        amp_profile = 0.88 ** idx
    elif profile == 'inverse':
        amp_profile = 1 / idx
    elif profile == 'constant':
        amp_profile = np.ones(len(idx))
    else:
        raise ValueError("Amplitude profile can be ['exp', 'inverse', 'constant'], was", profile)

    amplitudes = np.tile(amp_profile, (len(base_freqs), 1))
    return freqs, amplitudes

def freq_to_pitch(freq, base_freq=440.0, steps_per_octave=12):
    return np.log2(np.array(freq) / base_freq) * steps_per_octave

def pitch_to_freq(pitch, base_freq=440.0, steps_per_octave=12):
    return (2 ** (np.array(pitch) / steps_per_octave)) * base_freq
