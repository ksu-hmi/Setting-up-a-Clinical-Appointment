CLASS_NAME = 'NAME'
CLASS_APPOINTMENT_INFO = 'APPOINTMENT_INFO'


class Patient(object):

    CLASS_ID = 'ID'
    CLASS_PREV_APPOINTMENTS = 'PREVIOUS_APPOINTMENTS'

    def __init__(self, f_name, l_name, ssn):
        self.f_name = f_name
        self.l_name = l_name
        self.ssn = ssn
        self.patient_name = self.f_name + " " + self.l_name
        self.patient_id = self.f_name[:1] + self.l_name + ssn
        self.patient_calendar = {
            CLASS_NAME: self.patient_name,
            self.CLASS_ID: self.patient_id,
            #self.CLASS_PREV_APPOINTMENTS: {},
            CLASS_APPOINTMENT_INFO: {}
        }
    def get_patient_record(self):
        patient_record =  {
            CLASS_NAME : self.patient_name,
            self.CLASS_ID : self.patient_id,
        }
        return patient_record

    def print_patient_calendar(self):
         print (self.patient_calendar)


class Doctor(object):

    CLASS_SPECIALITY = 'SPECIALITY'

    def __init__(self, f_name, l_name, speciality):
        self.f_name = f_name
        self.l_name = l_name
        self.doctor_name = self.f_name + " " + self.l_name
        self.speciality = speciality
        self.doctor_calendar = {
            CLASS_NAME: self.doctor_name,
            self.CLASS_SPECIALITY: self.speciality,
            CLASS_APPOINTMENT_INFO: {},
        }

    def get_doctor_record(self):
        doctor_record =  {
            CLASS_NAME : self.doctor_name,
            self.CLASS_SPECIALITY: self.speciality
        }
        return doctor_record

    def print_doctor_calendar(self):
        print (self.doctor_calendar)


class Scheduler(object):

    def schedule(self,doctor,patient,time):
        
        self.time = time
        self.doctor = doctor
        self.patient = patient
        
        if self.isdoctoravailable(doctor,time) and self.ispatientavailable(patient,time):
            self.update_patient_calendar(patient,doctor,time)
            self.update_doctor_calendar(patient,doctor,time)
            
            print ("Appointment Scheduled with Dr. " + doctor.doctor_name +  " for patient " + patient.patient_calendar[CLASS_NAME] + " at " + SLOT + "\n")
        
            return True

    def isdoctoravailable(self,doctor,time):
        if time in doctor.doctor_calendar[CLASS_APPOINTMENT_INFO]:
            print ("No Appointment Available with Dr. " + doctor.doctor_name + "\n")
            return False
        else:
            return True

    def ispatientavailable(self,patient,time):
        if time in patient.patient_calendar[CLASS_APPOINTMENT_INFO]:
            print ("The patient " + patient.patient_name +  " already has an appointment with Dr. " + patient.patient_calendar[CLASS_APPOINTMENT_INFO][time][CLASS_NAME] + "\n")
            return False
        else:
            return True

    def update_patient_calendar(self,patient,doctor,time):
        patient.patient_calendar[CLASS_APPOINTMENT_INFO][time] = doctor.get_doctor_record()

    def update_doctor_calendar(self,patient,doctor,time):
        doctor.doctor_calendar[CLASS_APPOINTMENT_INFO][time] = patient.get_patient_record()

        
while True:
        
    P01 = input("Enter Patient's first name: ")
    P02 = input("Enter Patient's last name: ")
    P03 = input("Enter Patient's ID: ")

    D01 = input("Enter Doctor's first name: ")
    D02 = input("Enter Doctor's last name: ")
    D03 = input("Enter Doctor's Speciality: ")
    
    SLOT = input("Enter Time: ")

    D1 = Doctor(D01, D02, D03)
    P1 = Patient(P01, P02, P03)

    S1 = Scheduler()
    S1.schedule(D1,P1,SLOT)

    P1.print_patient_calendar()

    D1.print_doctor_calendar()
