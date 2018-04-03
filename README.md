# Chord dissonance models

This package implements various models of perceptual chord dissonance. Given a musical chord composed of individual tones, each composed of partials, a dissonance model provides a score that estimate how dissonant (harsh) does it sound to human listener.

It contains implementation of several models of dissoance with corrections of errors found in the formulas in the papers. See below.

## Installation

```
pip install dissonant
```

Why `dissonant`? PyPI package `dissonance` was already taken.

## Usage

Dissonance of a C major chord with harmonic tones using the Sethares1993 model:

```
from dissonant import harmonic_tone, dissonance, pitch_to_freq
h_freqs, h_amps = harmonic_tone(pitch_to_freq([0, 4, 7, 12]), n_partials=10)
d = dissonance(h_freqs, h_amps, model='sethares1993')
```

Dissonance curve of a sliding interval of two harmonic tones: see [notebooks/dissonance_curve.ipynb](notebooks/dissonance_curve.ipynb).

## Papers

- [1965, Plomp, Levelt - Tonal Consonance and Critical Bandwidth](http://www.mpi.nl/world/materials/publications/levelt/Plomp_Levelt_Tonal_1965.pdf)
- 1979, Hutchinson, Knopoff - The significance of the acoustic component of consonance in Western triad
- [1993, Sethares - Local Consonance and the Relationship Between Timbre and Scale](http://sethares.engr.wisc.edu/paperspdf/consonance.pdf)
    - http://sethares.engr.wisc.edu/papers/consance.html
- [2000, Vassilakis - Auditory roughness estimation of complex spectra](http://www.escom.org/proceedings/ICMPC2000/Wed/Vassilak.htm)
    - PDF is not public, only HTML
- [2001, Vassilakis - Perceptual and Physical Properties of Amplitude Fluctuation and their Musical Significance](http://www.acousticslab.org/papers/VassilakisP2001Dissertation.pdf) - PhD thesis
- [2002, Cook - Tone of Voice and Mind](http://www.res.kutc.kansai-u.ac.jp/~cook/PDFs/Tone_of_Voice_and_Mind.pdf) - book
- [2004, Sethares - Tuning Timbre Spectrum Scale](http://eceserv0.ece.wisc.edu/~sethares/ttss.html) - book
- [2005, Vassilakis - Auditory Roughness as Means of Musical Expression](http://www.acousticslab.org/papers/Vassilakis2005SRE.pdf)
- [2006, Benson - David Benson Music: A Mathematical Offering](http://homepages.abdn.ac.uk/mth192/pages/html/music.pdf) ([book page](http://homepages.abdn.ac.uk/mth192/pages/html/maths-music.html))
- [2006, Cook, Fujisawa - The Psychophysics of Harmony Perception: Harmony is a Three-Tone Phenomenon](http://www.res.kutc.kansai-u.ac.jp/~cook/PDFs/EMR2006.pdf)
- [2009, Cook - Harmony Perception: Harmoniousness Is More Than the Sum of Interval Consonance](http://www.res.kutc.kansai-u.ac.jp/~cook/PDFs/MusPerc2009.pdf)
- [2010, Vassilakis, Kendall - Psychoacoustic and congitive aspects of auditory roughness - definitions, models and applications](http://acousticslab.org/papers/VassilakisKendall2010.pdf)
- [2013, Dillon - Calculating the Dissonance of a Chord according to Helmholtz theory](https://arxiv.org/pdf/1306.1344v5)

### Extra

- [2001, McKinney et al. - Neural correlates of musical dissonance in the inferior colliculus](http://research.meei.harvard.edu/NeuralCoding/Papers/mckinneyISH.pdf)
- [2007, Vassilakis - SRA: A Web-based Research Tool for Spectral and Roughness Analysis of Sound Signals](http://musicalgorithms.ewu.edu/learnmoresra/files/vassilakis2007smc.pdf)
    - http://musicalgorithms.ewu.edu/algorithms/Roughness.html
    - http://musicalgorithms.ewu.edu/learnmoresra/moremodel.html
- Kameoka, A. & Kuriyagawa, M. (1969a). Consonance theory, part I: Consonance of dyads. Journal of the Acoustical Society of America, Vol. 45, No. 6, pp. 1451-1459.
- Kameoka, A. & Kuriyagawa, M. (1969b). Consonance theory, part II: Consonance of complex tones and its computation method. Journal of the Acoustical Society of America, Vol. 45, No. 6, pp. 1460-1469.
- Mashinter, Keith. (1995). Discrepancies in Theories of Sensory Dissonance arising from the Models of Kameoka & Kuriyagawa, and Hutchinson & Knopoff. Undergraduate thesis submitted for the double honours degrees in Applied Mathematics and Music, University of Waterloo.
- Phil Keenan ([@ingthrumath](https://twitter.com/ingthrumath))
  - http://meandering-through-mathematics.blogspot.com/2015/03/consonance-and-dissonance-in-music.html
  - http://meandering-through-mathematics.blogspot.com/2016/06/experimenting-with-sounds-consonance.html

## Other resources

- https://en.wikipedia.org/wiki/Consonance_and_dissonance
- http://www.res.kutc.kansai-u.ac.jp/~cook/
  - http://www.res.kutc.kansai-u.ac.jp/~cook/05%20harmony.html
  - http://www.res.kutc.kansai-u.ac.jp/~cook/Harmony.c
    - N. D. Cook, T. Fujisawa and K. Takami. This program is an improved version of the algorithm reported in Tone of Voice and Mind (Benjamins, Amsterdam, 2002). It calculates the dissonance, tension, instability and modality of chords containing 2-5 tones and assuming the presence of 1-5 upper partials.
    - video: [CogMIR 2013 - Norman D Cook - Visual Display of the Acoustical Properties of Harmony](https://www.youtube.com/watch?v=CrmnaiyS5EE)
- http://sethares.engr.wisc.edu/consemi.html#anchor149613
- http://sethares.engr.wisc.edu/forrestjava/html/TuningAndTimbre.html
- http://sethares.engr.wisc.edu/comprog.html - MATLAB, C++, Lisp
- https://gist.github.com/endolith/3066664
- http://www.davideverotta.com/A_folders/Theory/m_dissonance.html
- http://www.music-cog.ohio-state.edu/Music829B/diss.html

## Models

There are several acoustic models of dissonance. They may work on different data and provide several various metrics. All of them are based on some perceptual experiments.

Input signals:

- two plain sinusoidal tones
- two harmonic tones - integer multiples of the base frequency
- chord (two or more) of harmonic tones
- signals with continuous spectrum

### PlompLevelt1965

They measured the perceived dissonance of pairs of sinusoidal tones and of complex tones with 6 harmonics. They provide only experimental data, not a parametric model.

### Sethares1993

First, he explicitly parameterizes the data of PlompLevelt1965 (for a pair of sinusoids and for any number of complex tones) with constants found by fitting the curve to the data.

Dissonance `d(x)` for the difference `x` between a pair of frequencies. This ignores the absolute frequencies.

```
d(x) = exp(-a * x) - exp(-b * x)
Constants:
a = 3.5
b = 5.75
```

Dissonance for a pair of frequencies `(f_1, f_2)` (for f_1 < f_2) and their amplitudes `(a_1, a_2)`. This  takes into account the absolute frequencies. `d_max` is just the maximum of d(x).

```
d_pair(f_1, f_2, a_1, a_2) =
  s = d_max / (s_1 * f_1 + s_2)
  x = s * (f_2 - f_1)
  a_1 * a_2 * (exp(-a * x) - exp(-b * x))

Constants:
a = 3.5
b = 5.75
d_max = 0.24
s_1 = 0.0207 # 0.021 in the paper
s_2 = 18.96 # 19 in the paper
```

Expressed in terms of `d(x)`:

```
d_pair(f_1, f_2, a_1, a_2) = a_1 * a_2 * d((f_2 - f_1) * d_max / (s_1 * f_1 + s_2))
```

Model of dissonance of a single complex tone (containing various partials) is just the sum of dissonances for all pairs of partials. In case the partials are integer multiples of a base frequency we can call tone "harmonic", otherwise just a general "timbre".

```
freqs = (f_1, f_2, ... f_n)
amps = (a_1, a_2, ... a_n)
d_complex(freqs, amps) = 0.5 * sum([d(f_i, f_j, a_i, a_j) for i in range(n) for j in range(n)])

or equally:

d_complex(freqs, amps) = sum([
  d(freqs[i], freqs[j], amps[i], amps[j])
  for i in range(n)
  for j in range(n)
  if i < j])
```

Then we can model dissonance of a pair of complex tones (timbres). Basically it's still a sum of dissonances of all pairs of partials. We can however express `freqs_2 = alpha * freqs_1` and plot `d_complex()` for fixed `freqs_1` and varying `alpha` to get a "dissonance curve".

Note that this model can be used to model dissonance of intervals of complex tones, as well as chords (any number of tones).

Note the constants `s_1`, `s_2` are defined in the paper with low precision. Better precision is provided in the code by Mr. Sethares: http://sethares.engr.wisc.edu/comprog.html.

#### Questions?

Why we just sum the dissonance and not compute mean? Which aggregation operation makes more sense?

### Vassilakis2001

There's a modification to the `d_pair()` function which should make it depend more reliably on "SPL" and "AF-degree", in particular put more accent on the relative amplitudes of interfering sinusoids rather than on thir absolute amplitudes.

Defined in Eq.(6.23) on page 197 (219 in the PDF).

```
a_2 should be >= a_1
d_pair(f_1, f_2, a_1, a_2) =
  (a_1 * a_2) ^ 0.1 * 0.5 *
  ((2 * a_2) / (a_1 + a_2)) ^ 3.11 *
  (exp(-a * s * (f_2 - f_1)) - exp(-b * s * (f_2 - f_1)))

Where:
spl = a_1 * a_2
af_degree = (2 * a_2) / (a_1 + a_2)
a = 3.5
b = 5.75
d_max = 0.24
s_1 = 0.0207
s_2 = 18.96

It can be expressed in terms of d(x):

d_pair(f_1, f_2, a_1, a_2) =
  spl = a_1 * a_2
  af_degree = (2 * a_2) / (a_1 + a_2)
  s = d_max / (s_1 * f_1 + s_2)
  x = s * (f_2 - f_1)
  spl ^ 0.1 * 0.5 * af_degree ^ 3.11 * d(x)
```

In comparison in the Sethares1993 model it is:

```
d_pair(f_1, f_2, a_1, a_2) =
  spl = a_1 * a_2
  s = d_max / (s_1 * f_1 + s_2)
  x = (f_2 - f_1) * x
  spl * d(x)
```

Note that in order to handle the case if a_1 < a_2 we could define:

```
af_degree(a_1, a_2) = (2 * min(a_1, a_2)) / (a_1 + a_2)
```

Looking at Vassilakis2010 this is exactly what they do, extending Vassilakis2001, otherwise the model is the same.

Extending this to a set of complex tones is the same as in Sethares1993 - just aggregate `d_pair()` for all pairs via a sum.

Note there's an additional `0.5` factor in the Vassilakis2001 model compared to Sethares1993. IMHO the meaning is to compensate for pairs of partials being summed twice. In order to make the models comparable we should remove this term and take only pairs of partials only once in all models.

### Cook2002

Dissonance model (Cook2002, Appendix 2, page 276 and on, eg. A2-1):

```
Original - wrong:
d_pair(x, a_1, a_2) =
  mu_a = (a_1 + a_2) / 2
  mu_a * (exp(-a * x) - exp(-b * x))

Fixed:
  d_pair(x, a_1, a_2) =
    mu_a = (a_1 + a_2) / 2
    mu_a * c * (exp(-a * x) - exp(-b * x))

Where:
mu_a ... mean amplitude, within [0.0; 1.0]
x ... interval between the frequencies (in semitones)
a = 1.2
b = 4.0
c = 3.5351 = 1 / (np.exp(-1.2) - np.exp(-4))
```

Parameters were "chosen to give a maximal dissonance value at roughly one quartertone, a dissonance of 1.00 at an interval of one semitone, and smaller values for larger intervals".

The constants `a` and `b` are quite different than in the Sethares1993 model. Also the amplitudes are aggregated by mean, instead of product or minimum. The constant `c` is missing in the paper but needs to be on the place as in the formula above.

### Cook2006

Other metrics: dissonance, tension, modality, tonal instability. Based on three tones, not just an interval of two.

Dissonance model (Cook2006, eq. 3).

Note that in the article it's actually defined in a wrong way:
- there's one more minus sign when applying `beta_1`, `beta_2`
- logarithm should be of base 2
- `log2(f_2 / f_1)` needs to be multiplied by 12 to get the 12-TET semitone interval
- there should be bracket, not floor around the difference of exponentials (probably a printing error)

Note: for the sake of readability we replace here original greek `nu` with `v`.

```
Original - wrong:
d_pair(f_1, f_2, a_1, a_2) =
  x = log(f_2 / f_1)
  v = a_1 * a_2
  v * beta_3 *
  floor(
    exp(-beta_1 * x ^ gamma) -
    exp(-beta_2 * x ^ gamma))

Fixed:
d_pair(f_1, f_2, a_1, a_2) =
  x = 12 * log2(f_2 / f_1)
  v = a_1 * a_2
  v * beta_3 *
  (exp(beta_1 * x ^ gamma) -
   exp(beta_2 * x ^ gamma))

Constants:
beta_1 = -0.8 # "interval of maximal dissonance"
beta_2 = -1.6 # "steepness of the fall from maximal dissonance"
beta_3 = 4.0
gamma = 1.25
```

Total dissonance of a chords is the sum of dissonances of all pairs of partials.

### Cook2009

Simplified version of Cook2006. Still the definition is wrong (see above).

There's no gamma exponent.

```
Original - wrong:
d_pair(f_1, f_2, a_1, a_2) =
  x = log(f_2 / f_1)
  v = a_1 * a_2
  v * beta_3 *
  (exp(-beta_1 * x) -
   exp(-beta_2 * x))

Fixed:
d_pair(f_1, f_2, a_1, a_2) =
  x = 12 * log2(f_2 / f_1)
  v = a_1 * a_2
  v * beta_3 *
  (exp(beta_1 * x) -
   exp(beta_2 * x))

Constants:
beta_1 = -0.8 # "interval of maximal dissonance"
beta_2 = -1.6 # "steepness of the fall from maximal dissonance"
beta_3 = 4.0
```

Tension of a triad (not implemented yet):

```
tension(f_1, f_2, f_3) =
  x = log(f_2 / f_1)
  y = log(f_3 / f_2)
  v = a_1 * a_2 * a_3
  v * exp(-((y - x) / alpha)^2)

alpha = ~0.6
```
