import numpy as np

from dissonant.tuning import harmonic_tone, freq_to_pitch, pitch_to_freq


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

def test_freq_to_pitch_and_back():
    def test_both(pitches, freqs, **kwrgs):
        assert np.allclose(pitch_to_freq(pitches, **kwrgs), freqs)
        assert np.allclose(freq_to_pitch(freqs, **kwrgs), pitches)

    # scalar
    test_both(0, 440)
    # verctorized
    test_both([0, 4, 7, 12], [440., 554.36526195, 659.25511383, 880.])
    # different base freq
    test_both([0, 4, 7, 12], [430., 541.76605145, 644.27204306, 860.],
        base_freq=430)
    # different steps per octave
    test_both([0, 4, 7, 11, 12], [440., 566.13255512, 683.93876398, 880., 937.23615871],
        steps_per_octave=11)
