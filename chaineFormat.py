# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
# chaînes de formatage
# les formats de chaines de caractères sont ceux du langage C
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====

# entier
int1 = 10
print(f"[int1={int1}]")
print(f"[int1={int1:4d}]")
print(f"[int1={int1:04d}]")

# float
float1 = 8.2
print(f"[float1={float1}]")
print(f"[float1={float1:8.2f}]")
print(f"[float1={float1:.3e}]")

# string
str1 = "abcd"
print(f"[str1={str1}]")
print(f"[str1={str1:8s}]")
str2 = "jean de florette"
print(f"[{str2:20.10s}]")

# les chaînes formatées peuvent être affectées à des variables
str3 = f"[{str2:20.10s}]"
print(str3)

# [int1= 10]
# [int1=  10]
# [int1 = 0010]
# [float1 = 8.2]
# [float1 =    8.20]
# [float1= 8.200e+00]
# [str1= abcd]
# [str1 = abcd]
# [jean de fl]
# [jean de fl]
