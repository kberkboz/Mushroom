import mushroom

while True:
	print("  __  __           _                               ")
	print(" |  \/  |         | |                              ")
	print(" | \  / |_   _ ___| |__  _ __ ___   ___  _ __ ___  ")
	print(" | |\/| | | | / __| '_ \| '__/ _ \ / _ \| '_ ` _ \ ")
	print(" | |  | | |_| \__ \ | | | | | (_) | (_) | | | | | |")
	print(" |_|  |_|\__,_|___/_| |_|_|  \___/ \___/|_| |_| |_|")
	print("")
	print("")
	print("Spread the spores!")
	print("Base code by davidcallanan")
	print("Foremost features added by kberkboz")

	while True:

		text = input('mushroom > ')
		if text.strip() == "": continue
		result, error = mushroom.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				print(repr(result.elements[0]))
			else:
				print(repr(result))