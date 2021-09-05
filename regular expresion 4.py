import re
#pattern = r"colo..r"# ei dot dara bujacche ei dot er jagay ja dawa hbe tai match hbe
#pattern = r"^colo.r$"# ei ^ eta dara bujacche ei symbol er por dot er ag porjnto ja ja ase sob milte hbe
#and $ eita dara bujacche j $ ei symbol er age ja thakbe seta match hote hbe

#pattern = r"a*"# a* eta dara bujacche 0 number a thakte parbe or 0 thake beshi a thakte parbe

#pattern = r"a+"# a+ etar mane holo minimum ekbar a thakte hbe or ek er beshi thakte parbe

#pattern = r"ice-?cream"# ? er mane holo hyfen na thakleo kaj korbe abr sudu matro 1 bar thakle kaj korbe
#kintu ek er beshi thakle kaj korbe na

pattern = r"a{1,3}$"
if re.match(pattern,"aa"):
    print("matched")