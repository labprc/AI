import time

print("========== HOSPITAL EXPERT SYSTEM ==========")

name=input("Enter Patient Name : ")
age=input("Enter Age : ")

print("\nAnswer in yes/no\n")

fever=input("Fever : ").lower()
cough=input("Cough : ").lower()
cold=input("Cold : ").lower()
headache=input("Headache : ").lower()
stomach=input("Stomach Pain : ").lower()
vomit=input("Vomiting : ").lower()

print("\n========== MEDICAL REPORT ==========")

disease=""
medicine=""
advice=""

# Rules
if fever=="yes" and cough=="yes" and cold=="yes":

    disease="Flu"

    medicine="Paracetamol"

    advice="Drink warm water and take rest"

elif fever=="yes" and headache=="yes":

    disease="Viral Fever"

    medicine="Crocin"

    advice="Take proper sleep and medicines"

elif stomach=="yes" and vomit=="yes":

    disease="Food Poisoning"

    medicine="ORS and Antibiotics"

    advice="Drink clean water"

elif cough=="yes" and cold=="yes":

    disease="Common Cold"

    medicine="Cough Syrup"

    advice="Avoid cold drinks"

else:

    disease="Unknown"

    medicine="Doctor Consultation"

    advice="Visit hospital for proper diagnosis"

# Display report
print("Patient Name :",name)
print("Age :",age)
print("Disease :",disease)
print("Medicine :",medicine)
print("Advice :",advice)

print("Report Time :",time.strftime("%H:%M:%S"))
print("Report Date :",time.strftime("%d/%m/%Y"))

# Save report
file=open("hospital_report.txt","a")

file.write("\n===== PATIENT REPORT =====\n")
file.write("Name : "+name+"\n")
file.write("Age : "+age+"\n")
file.write("Disease : "+disease+"\n")
file.write("Medicine : "+medicine+"\n")
file.write("Advice : "+advice+"\n")
file.write("Time : "+time.strftime("%H:%M:%S")+"\n")
file.write("Date : "+time.strftime("%d/%m/%Y")+"\n")

file.close()

print("\nReport Saved Successfully")