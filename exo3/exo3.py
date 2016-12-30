#retrouver un caractere
#by alex
#beWeb




word = "tacos sauce blanche"
char = "b"
result = 0
i = 0
#initialisation du nombre de "a" a zero

while i < len(word) :
#tant que index inferieur a la longueur du mot cela exectute le code ci-dessous
	if word[i] == char :
#si a l'index ou je me trouve c'est bien un "a" j'incremente de 1

		result += 1
	i += 1
#et je passe a l'index suivant

print ("le nombre de caractereRechercher est: "+ str(result))
