# Python Funktionen
# _________________________________________________________________________________________

# 1 def   => bedeutet: "Wir definieren eine Funktion"
# 2 Name  => der Name der Funktion
# 3 ()    => hier können wir der Funktion Informationen geben (Parameter)
# 4 type  => hier können wir einen Parameter-Typ bestimmen
# 4 :     => danach kommt der Funktions-Inhalt eingerückt.
# Eine Funktion sollte immer etwas zurückgeben (returnen)
# _________________________________________________________________________________________

# 1       2        3    4      3       4  5
def new_password(name: str, birthday: str):
  newPassword = name.replace(" ", "") + birthday.replace(".", "")
  return newPassword


name = input("Name eingeben:\n")
birthday = input("Geburtsdatum eingeben:\n")

password = new_password(name, birthday) # Ausgabe "VornameNachname01012000"
print(password)
