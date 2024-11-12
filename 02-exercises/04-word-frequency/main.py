"""
I nedenstående ser du en variabel indeholdende forskelligt genereret tekst, samt en tom
'dict' som skal indeholde frekvensen af hvert ord i teksten.

Din opgave er at skrive noget kode som finder ud af, hvad frekvensen for hvert ord er i teksten.

I din løsning skal du tage højde for, at ord er case-insensitive, altså at "Hello" og "hello"
er det samme ord.

Eksempel på output:

{
    "hello": 4,
    "world": 3,
    "guido": 2,
    "coding": 1
}
"""

text = "Hello world hello Guido Coding World HELLO WORLD hElLO gUiDO"
frequency = {}
