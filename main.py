import feladatok

szamkiiras=feladatok.elso()
print(szamkiiras)
feladatok.otos()
gyok=feladatok.negyzetgyok()
print(gyok)
feladatok.szamokosszead()



randomsz=feladatok.fel6()
print(randomsz)

pozitiv, negativ=feladatok.fel6_2(randomsz)
print("Pozitív számok:", pozitiv)
print("Negatív számok:",negativ)

ossz=feladatok.fel6_3(randomsz)
print("A páros számok összege:", ossz)

paratlan, paros=feladatok.fel6_4(randomsz)
print("Páros számok összege:",paros)
print("Páratlan számok összege:", paratlan)

atlag=feladatok.fel6_5(randomsz)
print("Átlag:", atlag)

max=feladatok.fel6_6(randomsz)
print("A legnagyobb szám: ", max)




