import numpy as np

from dissonance.tuning import harmonic_tone


def test_harmonic_tone():
    assert np.allclose(harmonic_tone(440, 1)[0], np.array([[440]]))
    assert np.allclose(harmonic_tone(440, 1)[1], np.array([[1.]]))

    assert np.allclose(harmonic_tone(440, 5)[0], np.array([[440, 880, 1320, 1760, 2200]]))
    assert np.allclose(harmonic_tone(440, 5)[1], np.array([[1, 0.5, 0.33333333, 0.25, 0.2]]))

    assert np.allclose(harmonic_tone([440, 441], 1)[0], np.array([[440], [441]]))
    assert np.allclose(harmonic_tone([440, 441], 1)[1], np.array([[1], [1]]))

    assert np.allclose(harmonic_tone([440, 441], 5)[0],
        np.array([[440, 880, 1320, 1760, 2200], [441,  882, 1323, 1764, 2205]]))
    assert np.allclose(harmonic_tone([440, 441], 5)[1],
         np.array([[1, 0.5, 0.33333333, 0.25, 0.2], [1, 0.5, 0.33333333, 0.25, 0.2]]))

# TODO: freq_to_pitch, pitch_to_freq
