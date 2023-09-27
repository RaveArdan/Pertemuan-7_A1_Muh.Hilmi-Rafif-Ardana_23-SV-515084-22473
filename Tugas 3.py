student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6
 }
student.update({"hobi" : "coding"})
for key in student:
    print(key,'=>', student.get(key))
