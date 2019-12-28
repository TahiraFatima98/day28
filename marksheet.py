import math
print('Marksheet')
print('Student 1')
CH=3
students=['std1','std2','std3','std4']
for std in students:
    print(std)
    x1=int(input("chemistry marks:"))
    x2=int(input("Maths marks:"))
    x3=int(input("Geography marks:"))
    chemGPA=((x1/20)-1)
    mathGPA=((x2/20)-1)
    geoGPA=((x3/20)-1)
    avgGPA=(chemGPA+mathGPA+geoGPA)/3
    GPA=print("Your GPA is","%.2f"%avgGPA)
    if(avgGPA<2.5):
        print("you're not eligible for next semester")
    else:
        print("Congrats! Admitted to next semester")
