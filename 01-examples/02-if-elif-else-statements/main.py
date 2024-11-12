"""
Eksempler på brugen af if, elif og else statements
"""

# Example 1.1 - simpel brug af 'if' statement, der evaluerer til True
x = 20
y = 10

if x > y:
    print(f"Eksempel 1.1: OMG!! {x} er større end {y} .. \n")


# Eksempel 1.2 - if statement som ikke bliver eksekveret, da det evalueres til False
if x <= y:
    print("Eksempel 1.2: Oopsii .. Dette kodeblok vil ikke blive eksekveret ..")


# Eksempel 2 - Flere sekventielle if checks
z = 15

if x > y:
    print(f"Eksempel 2.1: Whoa .. {x} er virkelig større end {y}")

if x > z:
    print(f"Eksempel 2.2: Whoa .. og {x} er sør'me også større end {z} \n")


# Eksempel 3 - simpelt if og elif check
if "Jonas" == "God":
    print("Damn!")
elif "Guido is God":
    print("Eksempel 3: Selvfølgelig er det 'Guido' som er 'gud' ..\n")


# Eksempel 4 - if og multiple elif checks
if 10 == 15:
    print("Øøhmmm .. m'kay ..")
elif 10 == 12:
    print("Arghh .. det check er da heller ikke rigtigt .. !")
elif 10 == 10:
    print(
        "Eksempel 4: Sådan! Tænkte det nok .. 10 er lig med 10 - happiness restored!\n"
    )


# Eksempel 5 - if og else check
if "Jonas" == "God":
    print("Arghhh .. ")
else:
    print("Eksempel 5: Nemlig! Guido er GUD!\n")


# Eksempel 6 - brugen af alle if/elif/else kontrolstrukturer på én gang
if 10 == 12:
    print("Dét er sgu ikke sandt!")
elif 10 == 11:
    print("Yo .. 10 er IKKE lig med 11!")
elif 10 == 200:
    print("Og 10 er sgu da heller ikke lig med 200 altså ..")
else:
    print("Ja, 10 er lig med 10 .. ligesom True er lig med True .. mind blown!")


# Illustration af hvad der egentlig sker, når vi bruger if/elif/else
if 10 == 12:
    1
else:
    if 10 == 11:
        2
    else:
        if 10 == 20:
            3
        else:
            4
