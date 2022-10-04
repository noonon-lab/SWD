
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

number = int(input('What is your number?: ').strip())
thai_text_single_number = ['ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า','สิบ']
thai_text_place_value = ['สิบ','ร้อย','พัน','หมื่น','แสน','ล้าน']

if 0 <= number < 1e7:
    num_place = len(str(number))

    if num_place == 1:
        print(thai_text_single_number[number])

    elif num_place == 2:
        output = []
        for i in range(num_place):
            if str(number)[i] == '1':
                if i == 0:
                    output.append(thai_text_place_value[i])
                else:
                    output.append('เอ็ด')
            elif str(number)[i] == '2':
                if i == 0:
                    output.append('ยี่สิบ')
                else:
                    output.append(thai_text_single_number[i+1])
            elif str(number)[i] == '0':
                pass
            else:
                output.append(thai_text_single_number[int(str(number)[i])])
                if i < num_place-1:
                    output.append(thai_text_place_value[i])
        text = ''
        for j in range(len(output)):
            text += output[j]
        print(text)

    else:
        output = []
        for i in range(num_place):
            if str(number)[i] == '0':
                pass
            elif str(number)[i] == '2' and i == num_place-2:
                output.append('ยี่สิบ')
            elif str(number)[i] == '1' and i == num_place-2:
                output.append('สิบ')
            elif str(number)[i] == '1' and i == num_place-1:
                output.append('เอ็ด')
            else:
                output.append(thai_text_single_number[int(str(number)[i])])
                if i < num_place-1:
                    output.append(thai_text_place_value[num_place-i-2])
        text = ''
        for j in range(len(output)):
            text += output[j]
        print(text)
        
else:
    print('Your number is out of range.')
