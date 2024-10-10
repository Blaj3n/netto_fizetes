# Ez az egyik legkényelmesebb módja, hogy számokat ezres csoportosításban jeleníts meg.

'''
A :,.0f formázási szintaxis a Python format() függvényében vagy f-stringben speciális szabályokat határoz meg
a szám formázására. Nézzük meg részletesen, mit jelent:
    - :: A kettőspont jelzi, hogy formázási szabály következik.
    - ,: Ezres elválasztóként szolgál. Ez azt jelenti, hogy a számot 3-as csoportokba osztja és vesszővel választja el
         az ezreket (pl. 1,000,000).
    - .0f: Itt az f a lebegőpontos számot jelenti (float), és a .0 azt jelenti, hogy nincs tizedesjegy,
         azaz egész számra lesz kerekítve.
'''

print("1. Számok ezres csoportosításban megjelenítése F-Stringgel: ")

print("\t1.1. Pontokkal (európai formátum): ")
brutto_fizetes = 100000
print(f"\t\t{brutto_fizetes:,.0f}".replace(",", "."))

print("\t1.1. Szóközökkel: ")
brutto_fizetes = 100000
print(f"\t\t{brutto_fizetes:,}".replace(",", " "))

print()


print("2. Számok ezres csoportosításban megjelenítése format() függvénnyel: ")

print("\t2.1. Pontokkal (európai formátum): ")
brutto_fizetes = 100000
print("\t\t{:,.0f}".format(brutto_fizetes).replace(",", "."))

print("\t2.2. Szóközökkel: ")
brutto_fizetes = 100000
print("\t\t{:,}".format(brutto_fizetes).replace(",", " "))



