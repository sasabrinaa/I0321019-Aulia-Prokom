link = input("Masukan Link terakhir : ")
if (link[0:3]) == "Tnp":
    hasil = "7"
elif (link[0:3]) == "TVR":
    hasil = "1"
elif (link[0:3]) == "T0R":
    hasil = "8"
elif (link[0:3]) == "T1R":
    hasil = "9"
else:
    hasil = "[ERROR]"

if (link[3]) == "B":
    hasil1 = "0"
elif (link[3]) == "F":
    hasil1 = "1"
elif (link[3]) == "J":
    hasil1 = "2"
elif (link[3]) == "N":
    hasil1 = "3"
elif (link[3]) == "R":
    hasil1 = "4"
elif (link[3]) == "b":
    hasil1 = "5"
elif (link[3]) == "V":
    hasil1 = "5"
elif (link[3]) == "f":
    hasil1 = "6"
elif (link[3]) == "Z":
    hasil1 = "6"
elif (link[3]) == "j":
    hasil1 = "7"
elif (link[3]) == "n":
    hasil1 = "8"
elif (link[3]) == "R":
    hasil1 = "9"
elif (link[3]) == "r":
    hasil1 = "9"
else :
    hasil1 = "[ERROR]"

if (link[4:6]) == "d0":
    hasil2 = "0"
elif (link[4:6]) == "eE":
    hasil2 = "1"
elif (link[4:6]) == "eU":
    hasil2 = "2"
elif (link[4:6]) == "ek":
    hasil2 = "3"
elif (link[4:6]) == "ME":
    hasil2 = "4"
elif (link[4:6]) == "MU":
    hasil2 = "5"
elif (link[4:6]) == "Mk":
    hasil2 = "6"
elif (link[4:6]) == "M0":
    hasil2 = "7"
elif (link[4:6]) == "NE":
    hasil2 = "8"
elif (link[4:6]) == "NU":
    hasil2 = "9"
else:
    hasil2 = "[ERROR]"

if (link[6:8]) == "1E":
    hasil3 = "0"
elif (link[6:8]) == "1U":
    hasil3 = "1"
elif (link[6:8]) == "1q":
    hasil3 = "2"
elif (link[6:8]) == "16":
    hasil3 = "3"
elif (link[6:8]) == "5E":
    hasil3 = "4"
elif (link[6:8]) == "5U":
    hasil3 = "5"
elif (link[6:8]) == "5q":
    hasil3 = "6"
elif (link[6:8]) == "56":
    hasil3 = "7"
elif (link[6:8]) == "9E":
    hasil3 = "8"
elif (link[6:8]) == "9U":
    hasil3 = "9"
else:
    hasil3 = "[ERROR]"

if (link[8]) == "Q":
    hasil4 = "0"
elif (link[8]) == "R":
    hasil4 = "1"
elif (link[8]) == "S":
    hasil4 = "2"
elif (link[8]) == "T":
    hasil4 = "3"
elif (link[8]) == "U":
    hasil4 = "4"
elif (link[8]) == "V":
    hasil4 = "5"
elif (link[8]) == "W":
    hasil4 = "6"
elif (link[8]) == "Y":
    hasil4 = "7"
elif (link[8]) == "Z":
    hasil4 = "8"
elif (link[8]) == "a":
    hasil4 = "9"
else:
    hasil4 = "[ERROR]"

if (link[10]) == "c":
    hasil5 = "0"
elif (link[10]) == "d":
    hasil5 = "0"
elif (link[10]) == "g":
    hasil5 = "1"
elif (link[10]) == "h":
    hasil5 = "1"
elif (link[10]) == "k":
    hasil5 = "2"
elif (link[10]) == "l":
    hasil5 = "2"
elif (link[10]) == "o":
    hasil5 = "3"
elif (link[10]) == "p":
    hasil5 = "3"
elif (link[10]) == "s":
    hasil5 = "4"
elif (link[10]) == "t":
    hasil5 = "4"
elif (link[10]) == "w":
    hasil5 = "5"
elif (link[10]) == "x":
    hasil5 = "5"
elif (link[10]) == "A":
    hasil5 = "4"
elif (link[10]) == "B":
    hasil5 = "4"
elif (link[10]) == "E":
    hasil5 = "5"
elif (link[10]) == "F":
    hasil5 = "5"
elif (link[10]) == "S":
    hasil5 = "5"
elif (link[10]) == "I":
    hasil5 = "6"
elif (link[10]) == "J":
    hasil5 = "6"
elif (link[10]) == "M":
    hasil5 = "7"
elif (link[10]) == "N":
    hasil5 = "7"
elif (link[10]) == "Q":
    hasil5 = "8"
elif (link[10]) == "R":
    hasil5 = "8"
elif (link[10]) == "U":
    hasil5 = "9"
elif (link[10]) == "V":
    hasil5 = "9"
else:
    hasil5 = "[ERROR]"

if (link[0:3]) == "TVR":
    if (link[11:16]) == "NUT09":
            hasil6 = "1"
    elif (link[11:16]) == "NQT09":
            hasil6 = "0"
    elif (link[11:16]) == "NZz09":
            hasil6 = "2"
    elif (link[11:16]) == "Ndz09":
            hasil6 = "3"
    elif (link[11:16]) == "OQT09":
            hasil6 = "4"
    elif (link[11:16]) == "OUT09":
            hasil6 = "5"
    elif (link[11:16]) == "OZz09":
            hasil6 = "6"
    elif (link[11:16]) == "Odz09":
            hasil6 = "7"
    elif (link[11:16]) == "PQT09":
            hasil6 = "8"
    elif (link[11:16]) == "PUT09":
            hasil6 = "9"
    else:
            hasil6 = "[ERROR]"
else:
    hasil6 = " "

link1="https://ocw.uns.ac.id/presensi-online-dosen/view?id="
jawaban = (hasil+hasil1+hasil2+hasil3+hasil4+hasil5+hasil6)
jawaban1 = link1+jawaban

print(jawaban1)
print()
print(jawaban)
print()
print(link[0:3], hasil)
print(link[3], hasil1)
print(link[4:6], hasil2)
print(link[6:8], hasil3)
print(link[8], hasil4)
print(link[10], hasil5)
print(link[11:16], hasil6)