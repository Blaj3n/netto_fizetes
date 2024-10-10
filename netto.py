brutto_fizetes = int(input("Kérem adja meg bruttóban jelenlegi fizetését: "))

szja = round(brutto_fizetes * 0.15)
tb = round(brutto_fizetes * 0.185)

osszes_levonas = szja + tb

print(f"Személyi Jövedelemadó(15%): {szja}")
print(f"Társadalombiztosítási Járulék(18,5%): {tb}")
print(f"Levonások összesen: {osszes_levonas}")

netto_fizetes = brutto_fizetes - osszes_levonas
print(f"Nettó fizetése: {netto_fizetes}")