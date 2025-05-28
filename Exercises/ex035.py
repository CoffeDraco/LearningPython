#Receive three different line lengths and calculate if it can
#be used to form a triangle

line_1 = float(input("Enter the first line length: "))
line_2 = float(input("Enter the second line length: "))
line_3 = float(input("Enter the third line length: "))

rule_1 = True if line_1 + line_2 > line_3 else False
rule_2 = True if line_1 + line_3 > line_2 else False
rule_3 = True if line_2 + line_3 > line_1 else False

if rule_1 == rule_2 == rule_3 == True:
    print("With these lines we can form a triangle.")
else:
    print("No deal, we can't form a triangle.")