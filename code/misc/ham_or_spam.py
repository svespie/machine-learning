# this is incomplete

import numpy as np

def ham_or_spam(words):
    hamness = np.array([np.log(v) for k,v in hamminess(words).items()]).sum()
    spamness = np.array([np.log(v) for k,v in spamminess(words).items()]).sum()
    ham_or_spam = True if hamness > spamness else False
    return (ham_or_spam, hamness, spamness)