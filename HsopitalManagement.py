class InvalidPatientError(Exception):
  pass
class Patient:
  def __init__(self,Pid,Pname,age,gender,illness):
  
      if not Pname.strip():
        raise InvalidPatientError("patient name cannot be empty")
      if int(age)<=0:
        raise InvalidPatientError("age should be positive number")
      self.Pid=Pid
      self.Pname=Pname
      self.age=int(age)
      self.gender=gender
      self.illness=illness
  def PatientRecords(self):
    return{
        "patientId":self.Pid,
        "patientName":self.name,
        "patientAge":self.age,
        "patientGender":self.gender,
        "patientIllness":self.illness
    }
class Doctor:
 def __init__(self,docId,docName,specialization):
    self.docId=docId
    self.docNname=docName
    self.specialization=specialization
    self.appointments=[]
def add_appointment(self,appointment):
  self.appointments.append("PatientId:", Pid, "Time:", time_slot)
class HospitalManagementSystem:
  def __init__(self):
    self.patient_records={}
    self.patient_ids=[]
    self.doctors={}
  def add_doctor(self,docId, docName,specialization):
    new_doctor = Doctor(docId, docName, specialization)
    self.doctors[docId] = new_doctor
    print("Added Dr.",docName,"specializaiton",specialization)
  def register_patients(self,Pid,Pname,age,gender,illness):
    try:
      patient=Patient(Pid,Pname,age,gender,illness)
      self.patient_records[Pid]=patient.PatientRecords()
      self.patient_ids.append(Pid)
      print("registered patient:",Pname)
    except InvalidPatientError as e:
      print("Invalid patient information:",str(e))
  def schedule_appointment(self,Pid,doctor_id,time_slot):
    if Pid in self.patient_ids:
      if doctor_id in self.doctors:
        doctor=self.doctors[doctor_id]
        doctor.add_appointment(Pid,time_slot)
      else:
        print("doctor id does not exsit")
    else:
      print("patient id does not exsit")
  def save_records(self, filename="hospital.txt"):
    with open(filename,"w") as file:
      for Pid,patient_record in self.patient_records.items():
        line=f"{Pid},{patient_record['patientName']},{patient_record['patientAge']},{patient_record['patientGender']},{patient_record['patientIllness']}\n"
        file.write(line)
    print("records saved successfully")
class main():
  hms=HospitalManagementSystem()
  while True:
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("1. Add Doctor")
    print("2. Register Patient")
    print("3. Schedule Appointment")
    print("4. Save Patient Records to File")
    print("5. Exit")
        
    choice = input("Select an option (1-5): ").strip()
    print("-" * 35)

    if choice == "1":
      docId = input("Enter Doctor ID: ").strip()
      docName = input("Enter Doctor Name: ").strip()
      specialization = input("Enter Specialization: ").strip()
      hms.add_doctor(docId, docName, specialization)

    elif choice == "2":
      Pid = input("Enter Patient ID: ").strip()
      Pname = input("Enter Patient Name: ").strip()
      age = input("Enter Patient Age: ").strip()
      gender = input("Enter Patient Gender: ").strip()    
      illness = input("Enter Illness/Ailment: ").strip()
      hms.register_patient(Pid, Pname, age, gender, illness)

    elif choice == "3":
      Pid = input("Enter Patient ID: ").strip()
      docId = input("Enter Doctor ID: ").strip()
      time_slot = input("Enter Appointment Time Slot (e.g., 10:30 AM): ").strip()
      hms.schedule_appointment(Pid, docId, time_slot)

    elif choice == "4":
      hms.save_records()

    elif choice == "5":
      print("Exiting system. Goodbye!")
      break
    else:
      print(" Invalid selection. Please choose a number between 1 and 5.")

main()
#Hello! This is hospital management system
  
