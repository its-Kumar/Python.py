math, pysics, chemistry = (float(x) for x in input(
    "Enter marks for math, pysics and chemistry : ").split())
if math < 35:
    print("You have failed in math")
elif pysics < 35:
    print("You have failed in pysics ")
elif chemistry < 35:
    print("You have failed in chemistry")
else:
    avg = (math+pysics+chemistry)/3

    if avg <= 59:
        print("You have passed with grade 'C' .")
    elif avg <= 69:
        print("You have passed with grade 'B' .")
    else:
        print("You have passed with grade 'A' .")
