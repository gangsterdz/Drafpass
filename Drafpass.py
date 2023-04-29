#!/usr/bin/python3

profile = {}

# ادخال الاسم الأول
name = input("> First Name: ").lower()
while len(name) == 0 or name == " ":
    print("\r\n[-] You must enter a name!")
    name = input("> First Name: ").lower()
profile["name"] = name

# ادخال اللقب
surname = input("> Family name: ").lower()
while len(surname) == 0 or surname == " ":
    print("\r\n[-] You must enter a surname!")
    surname = input("> Family name: ").lower()
profile["surname"] = surname

# ادخال الاسم الثاني
second_name = input("> Second name: ")
profile["second_name"] = second_name

# ادخال اللقب
nickname = input("> Nickname: ")
profile["nickname"] = nickname

# ادخال رقم الهاتف
mobile = input("> Mobile: ")
profile["mobile"] = mobile

# ادخال اسم الشريك
partner = input("> Partner's name: ")
profile["partner"] = partner

# ادخال اسم الطفل
child = input("> child name: ")
profile["child"] = child

# ادخال تاريخ الميلاد
date_of_birth = input("> Date of birth: ")
profile["date_of_birth"] = date_of_birth

# قائمة سنوات الميلاد
years = [year for year in range(1990, 2025)]

# قائمة رموز وإضافات
chars = ['@', '#', '_', '-', ' ', '/', '+']

# قائمة أرقام
nums = [num for num in range(0, 123)]

# قائمة أرقام عشوائية
ran_nums = [1234, 4321, 0123, 321]

# قائمة الكلمات الممنوعة
forbidden_words = ['']

# إنشاء ملف نصي للحفظ
with open("passwords.txt", mode="w") as f:

    # الحالة الأولى: اسم الشخص
    f.write(name + "\n")

    # الحالة الثانية: اسم الشخص + تاريخ الميلاد
    for year in years:
        f.write(name + str(year) + "\n")
        f.write(name + str(year)[2:] + "\n")

    # الحالة الثالثة: اسم الشخص + رموز وإضافات
    for char in chars:
        f.write(name + char + "\n")
        f.write(name + char + surname + "\n")
        f.write(name + char + date_of_birth + "\n")

    # الحالة الرابعة: اسم الشخص + أرقام
    for num in nums:
        f.write(name + str(num) + "\n")

    # الحالة الخامسة: اسم الشخص + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(name + str(ran_num) + "\n")

    # الحالة السادسة: اسم الشخص + اسم الشريك
    f.write(name + partner + "\n")
    f.write(name + partner + date_of_birth + "\n")

    # الحالة السابعة: اسم الشخص + اسم الطفل
    f.write(name + child + "\n")

    # الحالة الثامنة: اسم الشخص + اللقب
    f.write(name + surname + "\n")

    # الحالة التاسعة: اسم الشخص + كلمات ممنوعة
    for word in forbidden_words:
        f.write(name + word + "\n")

   # الحالة الأولى: لقب الشخص
    f.write(surname + "\n")

    # الحالة الثانية: لقب الشخص + تاريخ الميلاد
    for year in years:
        f.write(surname + str(year) + "\n")
        f.write(surname + str(year)[2:] + "\n")

    # الحالة الثالثة: لقب الشخص + رموز وإضافات
    for char in chars:
        f.write(surname + char + "\n")
        f.write(surname + char + date_of_birth + "\n")

    # الحالة الرابعة: لقب الشخص + أرقام
    for num in nums:
        f.write(surname + str(num) + "\n")

    # الحالة الخامسة: لقب الشخص + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(surname + str(ran_num) + "\n")

    # الحالة السادسة: لقب الشخص + اسم الشريك
    f.write(surname + partner + "\n")
    f.write(surname + partner + date_of_birth + "\n")

    # الحالة السابعة: لقب الشخص + اسم الطفل
    f.write(surname + child + "\n")

    # الحالة الثامنة: لقب الشخص + الاسم
    f.write(surname + name + "\n")

    # الحالة التاسعة: لقب الشخص + كلمات ممنوعة
    for word in forbidden_words:
        f.write(surname + word + "\n")
        
   # الحالة الأولى: الاسم الثاني للشخص
    f.write(nickname + "\n")

    # الحالة الثانية: الاسم الثاني للشخص + تاريخ الميلاد
    for year in years:
        f.write(nickname + str(year) + "\n")
        f.write(nickname + str(year)[2:] + "\n")

    # الحالة الثالثة: الاسم الثاني للشخص + رموز وإضافات
    for char in chars:
        f.write(nickname + char + "\n")
        f.write(nickname + char + surname + "\n")
        f.write(nickname + char + date_of_birth + "\n")

    # الحالة الرابعة: الاسم الثاني للشخص + أرقام
    for num in nums:
        f.write(nickname + str(num) + "\n")

    # الحالة الخامسة: الاسم الثاني للشخص + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(nickname + str(ran_num) + "\n")

    # الحالة السادسة: الاسم الثاني للشخص + اسم الشريك
    f.write(nickname + partner + "\n")
    f.write(nickname + partner + date_of_birth + "\n")

    # الحالة السابعة: الاسم ثاني للشخص + اسم الطفل
    f.write(nickname + child + "\n")

    # الحالة الثامنة: الاسم الثاني للشخص + اللقب
    f.write(nickname + surname + "\n")

    # الحالة التاسعة: الاسم الثاني للشخص + كلمات ممنوعة
    for word in forbidden_words:
        f.write(nickname + word + "\n")
        
   # الحالة الأولى: اسم الشريك
    f.write(partner + "\n")

    # الحالة الثانية: اسم الشريك + تاريخ الميلاد
    for year in years:
        f.write(partner + str(year) + "\n")
        f.write(partner + str(year)[2:] + "\n")

    # الحالة الثالثة: اسم الشريك + رموز وإضافات
    for char in chars:
        f.write(partner + char + "\n")
        f.write(partner + char + surname + "\n")
        f.write(partner + char + date_of_birth + "\n")

    # الحالة الرابعة: اسم الشريك + أرقام
    for num in nums:
        f.write(partner + str(num) + "\n")

    # الحالة الخامسة: اسم الشريك + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(partner + str(ran_num) + "\n")

    # الحالة السادسة: اسم الشريك + اسم الشريك
    f.write(partner + date_of_birth + "\n")

    # الحالة السابعة: اسم الشريك + اسم الطفل
    f.write(partner + child + "\n")

    # الحالة الثامنة: اسم الشريك + اللقب
    f.write(partner + surname + "\n")

    # الحالة التاسعة: اسم الشريك + كلمات ممنوعة
    for word in forbidden_words:
        f.write(partner + word + "\n")
        
   # الحالة الأولى: اسم الشخص
    f.write(name + "\n")

    # الحالة الثانية: اسم الابن + تاريخ الميلاد
    for year in years:
        f.write(child + str(year) + "\n")
        f.write(child + str(year)[2:] + "\n")

    # الحالة الثالثة: اسم الابن + رموز وإضافات
    for char in chars:
        f.write(child + char + "\n")
        f.write(child + char + surname + "\n")
        f.write(child + char + date_of_birth + "\n")

    # الحالة الرابعة: اسم الابن + أرقام
    for num in nums:
        f.write(child + str(num) + "\n")

    # الحالة الخامسة: اسم الابن + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(child + str(ran_num) + "\n")

    # الحالة السادسة: اسم الابن + اسم الشريك
    f.write(child + partner + "\n")
    f.write(child + date_of_birth + "\n")

    # الحالة الثامنة: اسم الابن + اللقب
    f.write(child + surname + "\n")

    # الحالة التاسعة: اسم الابن + كلمات ممنوعة
    for word in forbidden_words:
        f.write(child + word + "\n")
        
   # الحالة الأولى: كلمة أخرى
    f.write(name + "\n")

    # الحالة الثانية: كلمة أخرى + تاريخ الميلاد
    for year in years:
        f.write(name + str(year) + "\n")
        f.write(name + str(year)[2:] + "\n")

    # الحالة الثالثة: كلمة أخرى + رموز وإضافات
    for char in chars:
        f.write(name + char + "\n")
        f.write(name + char + surname + "\n")
        f.write(name + char + date_of_birth + "\n")

    # الحالة الرابعة: كلمة أخرى + أرقام
    for num in nums:
        f.write(name + str(num) + "\n")

    # الحالة الخامسة: كلمة أخرى + أرقام عشوائية
    for ran_num in ran_nums:
        f.write(name + str(ran_num) + "\n")

    # الحالة السادسة: كلمة أخرى + اسم الشريك
    f.write(name + partner + "\n")
    f.write(name + partner + date_of_birth + "\n")

    # الحالة السابعة: كلمة أخرى + اسم الطفل
    f.write(name + child + "\n")

    # الحالة الثامنة: كلمة أخرى + اللقب
    f.write(name + surname + "\n")

    # الحالة التاسعة: كلمة أخرى + كلمات ممنوعة
    for word in forbidden_words:
        f.write(name + word + "\n")
