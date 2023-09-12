# Nomor 1a
str_val = "balonku ada lima"

str_val = str_val.replace("o","a")
str_val = str_val.replace("u","a")
str_val = str_val.replace("i","a")
str_val = str_val.replace("e","a")

print(str_val)
print("Fitur baruu")

# Nomor 1b
word = input("Masukkan kata (lowercase): ")
word = word.replace("o", "a")
word = word.replace("i", "a")
word = word.replace("u", "a")
word = word.replace("e", "a")
print("Berubah menjadi: " + word)

# Nomor 2
Class_held = 20
Students = ["Asnawi", "Haaland", "Hazard", "Maudy Ayunan", "Marselino", "Dembele"]
Class_attended = [18, 19, 10, 20, 17, 13]

def check_attendance(Class_held, Students, Class_attended):

    for i in range(len(Students)):
        attendance_percentage = (Class_attended[i] / Class_held) * 100

        if attendance_percentage >= 75:
            hasil = "lebih dari 75%, dapat mengikuti ujian cunin"
        else:
            hasil = "kurang dari 75%, tidak dapat mengikuti ujian cunin"

        print(f"Kehadiran {Students[i]} {hasil}")

check_attendance(Class_held, Students, Class_attended)