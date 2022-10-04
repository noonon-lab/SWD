
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

number = input('What is your number?: ').strip()
roman_number = ['I','V','X','L','C','D','M']

if 0 < int(number) < 1000:
    num_place = len(number)
    roman = ''
    
    for i in range(num_place):

        if int(number[i]) == 0:
            pass

        elif 1 <= int(number[i]) <= 3:
            roman += roman_number[2*(num_place-i-1)]*int(number[i])

        elif int(number[i]) == 4:
            roman += roman_number[2*(num_place-i-1)]+\
                     roman_number[2*(num_place-i-1)+1]

        elif int(number[i]) == 5:
            roman += roman_number[2*(num_place-i)-1]

        elif int(number[i]) == 6:
            roman += roman_number[2*(num_place-i-1)+1]+\
                     roman_number[2*(num_place-i-1)]

        elif 7 <= int(number[i]) <= 8:
            roman += roman_number[2*(num_place-i)-1]+\
                     roman_number[2*(num_place-i-1)]*(int(number[i])-5)           

        else:
            roman += roman_number[2*(num_place-i-1)]+\
                     roman_number[2*(num_place-i)]

    print(roman)

else:
    print('Your number is out of range.')
