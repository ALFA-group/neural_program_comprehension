def read_cache():
 # Perform some read operations
 # Return lst = [zipname, direc]
 return lst

def write_cache(a, b):
 # Perform some write operations
 # Nothing to return

def ui():
 g = input("Use cache? (y/n):")

 if g == "y":
   i = read_cache()
   return i

 elif g == "n":
   zipname = input("Zip fname:")
   direc = input("Zip directory:")
   write_cache(zipname, direc)
   i = [zipname, direc]
   return i
   
 else:
   print("Respond with y/n \n")
   ui()
# End of ui()

x = ui()
zipname = x[0]
direc = x[1]