student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6}
for key in student:
    print(key,'=>',student[key])
print()
student["nama"] = "darmawan"
for key in student:
    print(key,'=>', student[key])
