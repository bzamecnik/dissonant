import numpy as np

__all__ = [
    'Sethares1993', 'Vassilakis2001', 'Cook2002', 'Cook2006', 'Cook2009',
    'model_by_name'
]

class Sethares1993:
    a = 3.5
    b = 5.75
    d_max = 0.24
    s_1 = 0.0207
    s_2 = 18.96

    def dissonance_pair(self, f_1, f_2, a_1, a_2):
        s = self.d_max / (self.s_1 * f_1 + self.s_2)
        x = s * (f_2 - f_1)
        spl = a_1 * a_2
        d = np.exp(-self.a * x) - np.exp(-self.b * x)
        return spl * d

class Vassilakis2001:
    """
    Fixes compared to the paper:
    - the 0.5 term removed compared to the original formula
      since we counts pairs of partials only once, not twice
    """
    a = 3.5
    b = 5.75
    d_max = 0.24
    s_1 = 0.0207
    s_2 = 18.96
    spl_exponent = 0.1
    afd_exponent = 3.11

    def dissonance_pair(self, f_1, f_2, a_1, a_2):
        spl = a_1 * a_2
        af_degree = (2 * a_2) / (a_1 + a_2)
        s = self.d_max / (self.s_1 * f_1 + self.s_2)
        x = s * (f_2 - f_1)
        d = np.exp(-self.a * x) - np.exp(-self.b * x)
        return (spl ** self.spl_exponent) * (af_degree ** self.afd_exponent) * d

class Cook2002:
    """
    Dissonance at semitone 1.0 normalized to 1.0.

    Fixes compared to the paper:
    - `c` is defined exactly, not with limited precision
    - logarithm should be of base 2
    - log2(f_2 / f_1) needs to be multiplied by 12 to get the 12-TET semitone
      interval
    """
    a = 1.2
    b = 4.0
    # c ~= 3.5350857058976985 (3.53 in the paper which is not precise)
    c = 1 / (np.exp(-a) - np.exp(-b))

    def dissonance_pair(self, f_1, f_2, a_1, a_2):
        # difference of tones in 12-TET semitone intervals
        x = 12 * np.log2(f_2 / f_1)
        return self.c * (np.exp(-self.a * x) - np.exp(-self.b * x))

class Cook2006:
    """
    Maximum dissonance normalized to 1.0.

    Fixes compared to the paper:
    - there's one more minus sign when applying beta_1, beta_2
    - logarithm should be of base 2
    - log2(f_2 / f_1) needs to be multiplied by 12 to get the 12-TET semitone
      interval
    - there should be bracket, not floor around the difference of exponentials
      (probably a printing error)
    """
    beta_1 = -0.8
    beta_2 = -1.6
    beta_3 = 4.0
    gamma = 1.25

    def dissonance_pair(self, f_1, f_2, a_1, a_2):
        spl = a_1 * a_2
        # frequency ratio -> 12-TET semitone interval
        x = 12 * np.log2(f_2 / f_1)
        x_to_gamma = x ** self.gamma
        d = np.exp(self.beta_1 * x_to_gamma) - np.exp(self.beta_2 * x_to_gamma)
        return spl * self.beta_3 * d

class Cook2009:
    """
    Maximum dissonance normalized to 1.0.

    Fixes compared to the paper:
    - there's one more minus sign when applying beta_1, beta_2
    - logarithm should be of base 2
    - log2(f_2 / f_1) needs to be multiplied by 12 to get the 12-TET semitone
      interval
    """
    beta_1 = -0.8
    beta_2 = -1.6
    beta_3 = 4.0

    def dissonance_pair(self, f_1, f_2, a_1, a_2):
        spl = a_1 * a_2
        # frequency ratio -> 12-TET semitone interval
        x = 12 * np.log2(f_2 / f_1)
        d = np.exp(self.beta_1 * x) - np.exp(self.beta_2 * x)
        return spl * self.beta_3 * d

models = {
    'sethares1993': Sethares1993(),
    'vassilakis2001': Vassilakis2001(),
    'cook2002': Cook2002(),
    'cook2006': Cook2006(),
    'cook2009': Cook2009(),
}

def model_by_name(name):
    return models[name]
