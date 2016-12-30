#nbre de lettre
#by alex
#beWeb



$word = "tacossauceBlanche"
$char = "s"
$result = 0
#initialisation du nombre de "s" a zero
$i = 0
#initialisation de l'index donc index 0

	while $i < $word.length
#tant que index inferieur a la longueur du mot cela exectute le code ci-dessous
		if $word[$i] == $char
#si a l'index ou je me trouve c'est bien un "n" j'incremente de 1
			$result += 1
		end
#fin de ma condition
	$i += 1
#et je passe a l'index suivant
	end
#fin de ma condition

print "le caractereRechercher est : #{$result}\r\n"
	
# \r =retour chariot et \n = passage a la ligne
