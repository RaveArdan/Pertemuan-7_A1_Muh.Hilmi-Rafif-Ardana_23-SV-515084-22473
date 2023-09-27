student = {
"nama" : "Ardan",
 "umur" : 17,
 "tinggi" : 167.8}
#Sebelum ditambah data
for key in student:
    print(key, '=>', student[key])
print()
#Setelah ditambah data 
student["hobi"] = "coding"
for key in student :
    print(key, '=>',student[key] )

