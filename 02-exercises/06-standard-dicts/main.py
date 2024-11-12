"""
I nedenstående ser du først en liste med navne på nyansatte programmører i en virksomhed, 
og dernæst en 'dict' bestående af de standardværdier (titel og løn), som virksomheden har for nyansatte.

Din opgave er at skabe en 'dict', som grupperer ansatte efter deres navne og standardværdierne.

Din kode skal give følgende output:

{
    "Kelly": {"designation": "Developer", "salary": 8000},
    "Emma": {"designation": "Developer", "salary": 8000},
    "Mikkel": {"designation": "Developer", "salary": 8000}
}

* HJÆLP *
For at løse opgaven skal du gøre brug af metoden "fromkeys" på en 'dict'.

Helt konkret kan man kalde "dict.fromkeys()" og give funktionskaldet de to 
argumenter der skal bruges for at løse opgaven.

Er du i tvivl om, hvordan "fromkeys" på en 'dict' fungerer, så slå det gerne
op på enten via Google eller fx ChatGPT.
"""

new_employees = ["Mads", "Emma", "Mikkel"]
defaults = {"title": "Developer", "salary": 8000}
