import math

f = open('cos_table_signed_13.mif', 'w')

f.write("DEPTH = 8192;\nWIDTH = 13;\nADDRESS_RADIX = DEC;\nDATA_RADIX = DEC;\n\n")
f.write("CONTENT\nBEGIN\n")

for A in range(0,8192):
    val = 8191*math.cos((float(A)/8192)*2*math.pi)
    f.write("%s  : %d;\n" % (A,round(val)))

f.write("END;") 

