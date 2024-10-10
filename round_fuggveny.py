'''
A round() függvény a Pythonban egy számot kerekít a megadott tizedesjegy pontosságra.
Alapértelmezésben egész számra kerekít, de megadhatod, hogy hány tizedesjegyre szeretnéd a kerekítést.
Íme a működése:

round(szám, tizedesjegyek_száma): kerekíti a megadott számot a megadott tizedesjegy pontosságra.
Ha nincs megadva a tizedesjegyek száma, akkor egész számra kerekít.
Példák:
'''
# Kerekítés egész számra
print("Kerekítés egész számra:")
print(round(4.56))   # Eredmény: 5
print(round(4.34))   # Eredmény: 4

# Kerekítés két tizedesjegyre
print("Kerekítés két tizedesjegyre:")
print(round(4.56789, 2))  # Eredmény: 4.57
print(round(4.12345, 3))  # Eredmény: 4.123
