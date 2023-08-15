liste = ["Zafer","Cengiz","Duygu","Suleyman","Aytekin","Semih","Hanifi",
"Emin","Mehmet","Ayşe","Demet","Seda"]

import os 

for item in liste:
    fileName = f"01_pandas_{item}.ipynb"
    if not os.path.exists(os.path.join("Exercises",item)):
        os.mkdir(os.path.join("Exercises",item))
    open(os.path.join("Exercises",item,fileName),"w")
