# Python Built-In Methods


text = "Hallo Welt"
# _________________________________________________________________________________________

# .replace()
# Ersetzt Teile eines Strings

text.replace("Welt", "Python") # "Hallo Python"
# _________________________________________________________________________________________

# .lower(), .upper()
# Macht alle Buchstaben klein oder groß

text.lower() # "hallo welt"
text.upper() # "HALLO WELT"
# _________________________________________________________________________________________

# .strip()
# Entfernt Zeichen am Anfang und Ende

text.strip("Ha") # "llo Welt"
text.strip("lt") # "Hallo We"
# _________________________________________________________________________________________

# .split()
# Teilt einen String in eine Liste (Standard Trennzeichen ist das Leerzeichen)

text.split() # ["Hallo", "Welt"]
# _________________________________________________________________________________________
