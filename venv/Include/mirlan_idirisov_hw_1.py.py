temperature_kyrguzstan = 4.5
print(type(temperature_kyrguzstan))

chuy = float(input("chuy temperature"))
yssyk_kol = float(input("yssyk_kol temperature"))
naryn = float(input("naryn temperature"))
osh = float(input("osh temperature"))
djalal_abat = float(input("djalal_abat temperature"))
batken = float(input("batken temperature"))
talas = float(input("talas temperature"))

averge = float(chuy+yssyk_kol+naryn+osh+djalal_abat+batken+talas) / 7
m = round(averge, 1)
print(f'Срединий показатель температуры по КР на сегодя',{m},'C')