liste = ["Zafer","Cengiz","Duygu","Suleyman","Aytekin","Semih","Hanifi",
"Emin","Mehmet","Ayşe","Demet","Seda"]

import os 
fileName = "ilk.ipynb"
for item in liste:
    if not os.path.exists(os.path.join("Exercises",item)):
        os.mkdir(os.path.join("Exercises",item))
    open(os.path.join("Exercises",item,fileName),"w")
