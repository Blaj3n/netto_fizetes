# TOVÁBBFEJLESZTÉSI LEHETŐSÉGEK:
# 25 év alatti szja kedvezmény

brutto_fizetes = int(input("Kérem adja meg bruttóban jelenlegi fizetését: "))

szja = round(brutto_fizetes * 0.15)
tb = round(brutto_fizetes * 0.185)

osszes_levonas = szja + tb

print(f"Személyi Jövedelemadó(15%): \t\t\t{szja:,.0f}".replace(",", "."))
print(f"Társadalombiztosítási Járulék(18,5%): \t{tb:,.0f}".replace(",", "."))
print(f"Levonások összesen: \t\t\t\t\t{osszes_levonas:,.0f}".replace(",", "."))

netto_fizetes = brutto_fizetes - osszes_levonas
print(f"Nettó fizetése: \t\t\t\t\t\t{netto_fizetes:,.0f}".replace(",", "."))