"""
I nedenstående ser du en liste med ord for diverse frugter.

Din opgave er at skabe en 'dict', som grupperer ordene fra listen efter deres første bogstav, 
således at outputtet af din kode derfor bliver følgende:

{
    "a": ["apple", "avocado"],
    "b": ["banana", "blueberry"],
    "c": ["cherry"]
}

* HJÆLP TIL OPGAVEN *
For at løse opgaven skal du bruge en metode der hedder "setdefault", som man kan bruge på en 'dict'.

"setdefault" metoden er en praktisk måde at slå en 'key' op på, og hvis denne 'key' så ikke findes, 
så indsættes der den standardværdi man selv specificerer.

Brug evt. Google eller ChatGPT for at se hvordan man bruger "setdefault" metoden ..
"""

words = ["apple", "banana", "avocado", "blueberry", "cherry"]
