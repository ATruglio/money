print ("Money: \n Determina il numero minimo di banconote (da 20$, 10$, 5$ o 1$) per pagare un importo inserito in input.  "\
       "\n  \n  ")
imp = input ("Importo: ")
imp = int (imp)
if imp < 0:
	print(" \n ERRORE! L'importo non puo' essere negativo!")
else:
	venti = imp // 20
	imp = imp % 20
	dieci = imp // 10
	imp = imp % 10
	cinque = imp // 5
	imp = imp % 5
	uno = imp
	print(" \n Banconote da 20$=", venti, "; \n Banconote da 10$=", dieci, "; \n Banconote da  5$=", cinque, "; \n "\
	      "Banconote da  1$:", uno,".")
