#exercice du perroquet
#by alex
#beweb




quitter = False
oui = "o"
non = "n"
reponse = ""
flag = False

while quitter == False:
	print("Bienvenue chez le perroquet du capitaine")
	perroquet = raw_input("entrez une phrase ou un mot: ")
	print(str(perroquet))
	flag = True

	while flag == True:
		reponse = raw_input("Voulez vous quitter o/n ?")

		if reponse.lower() == oui:
			quitter = True
			flag = False
		elif reponse.lower() == non:
			print("non")
			flag = False
		else:
			print("Moi y a na pas comprendre ce que toi vouloir me dire")
