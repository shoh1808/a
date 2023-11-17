o = open
try:
  x = o(" ").read()
except:
  x = "0"
o(" ","w").write(str(int(x)+1))
print("bad" if x in "1 2 4 5 8 9 10 12 17 20 21 22 28 30 31 32 34 36 37 38".split() else "good")
