"""
I denne opgave skal du selv kode et "sten, saks, papir" spil fra bunden af, som skal spilles mod din computer.

Eneste du er givet på forhånd er nedenstående kode, som for computeren blot automatiskvælger én af 
de 3 muligheder (dvs. 'sten', 'saks' eller 'papir').

Din opgave er at kode resten af spillet med det du har lært indtil videre.

* P.S. *
Du er til denne opgave IKKE givet en løsning! Har du svært at løse opgaven, så bed om hjælp :-)
"""

import random

choices = ["sten", "saks", "papir"]

comp_choice = random.choice(choices)
