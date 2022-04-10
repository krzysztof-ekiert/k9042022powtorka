from tabulate import tabulate

pw = 350/100
mw = 325/100
sw = 350/100


d = [ ["Pomidor", ",", "kalorie: " + str(round(pw*19, 2)) +",", "b: " + str(round(pw*1, 2)) + ",", "t: "+ str(round(pw*0, 2)) + ",", "w: " + str(round(pw*4, 2))+ ",", "waga: " + str(pw*100) + "g, ", "koszt: " + str(round(pw*5.7/10, 2)) + "PLN"],
     ["Mozarella", ",", "kalorie: " + str(round(mw*248, 2)) +",", "b: " + str(round(mw*18, 2)) + ",", "t: "+ str(round(mw*19, 2)) + ",", "w: " + str(round(mw*2, 2))+ ",", "waga: " + str(mw*100) + "g, ", "koszt: " + str(round(mw*38.32/10, 2)) + "PLN"],
     ["Sałata", ",", "kalorie: " + str(round(sw*13, 2)) +",", "b: " + str(round(sw*1, 2)) + ",", "t: "+ str(round(sw*0, 2)) + ",", "w: " + str(round(sw*2, 2))+ ",", "waga: " + str(sw*100) + "g, ", "koszt: " + str(round(sw*3.15/10, 2)) + "PLN"],
      ["========"],
    ["SUMA", ",", "kalorie: " + str(round(pw*19+mw*248+sw*13, 2)) +",", "b: " + str(round(pw*1+mw*18+sw*1, 2)) + ",", "t: "+ str(round(pw*0+mw*19+sw*0, 2)) + ",", "w: " + str(round(pw*4+mw*2+sw*2, 2))+ ",", "waga: " + str(pw*100+mw*100+sw*100) + "g, ", "koszt: " + str(round(pw*5.7/10+mw*38.32/10+sw*3.15/10, 2)) + "PLN"]]



print(tabulate(d))
