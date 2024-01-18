from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
       with open(fileName,'r')as f:#opening file
           for line in f:#retrieving data from the file
               data=line.strip().split(',')# Remove any whitespace and split by comma delimiter
               if len(data)!=8:
               #checking whether number of fields is valid
                   print("Invalid number of fields in line:",data )
                   continue
               else:
                   try:
                       #converting all the values to the required data types
                       data[2]=float(data[2])
                       data[3]=int(data[3])
                       data[4]=int(data[4])
                       data[5]=int(data[5])
                       data[6]=int(data[6])
                       data[7]=int(data[7])
                       if(isinstance(data[1],str) and isinstance(data[2],float) and isinstance(data[3],int) and isinstance(data[4],int) and isinstance(data[5],int) and isinstance(data[6],int) and isinstance(data[7],int)):
                           #checking all the necessary conditions
                           if(float(data[2])<35.0 or float(data[2])>42.0):#temperature value
                              print("Invalid temperature value (",data[2],") in line:",data )
                              break
                           elif(int(data[3])<30 or int(data[3])>180):#heart rate value
                              print("Invalid heart rate value(",data[3],") in line:",data)
                              break
                           elif(int(data[4])<5 or int(data[4])>40):#respiratory rate value
                              print("Invalid respiratory rate value (",data[4],") in line:",data)
                              break
                           elif(int(data[5])<70 or int(data[5])>200):#systolic blood pressure value
                              print("Invalid systolic blood pressure value (",data[5],") in line:",data)
                              break
                           elif(int(data[6])<40 or int(data[6])>120):#diastolic blood pressure value
                              print("Invalid diastolic blood pressure value (",data[6],") in line:",data)
                              break
                           elif(int(data[7])<70 or int(data[7])>100):#oxygen saturation value 
                              print("Invalid oxygen saturation value (",data[7],") in line:",data)
                              break
                           else:
                              patient_id=int(data[0])
                              visit_data=data[1:]#storing values in a data except patient_id
                              if patient_id not in patients:#check whether the patient_id is present in the dictionary patients
                                  patients[patient_id]=[]
                              patients[patient_id].append(visit_data)#adding values in dictionary as key:pair
                   except:
                        print("Invalid data type in line:",data)
                     
    except FileNotFoundError as e:#if file not found
        print(e)
        print('The file could not be found.')
    except:#all unexpected errors
        print("An unexpected error occurred while reading the file." )
    return patients#return files to the main menu
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """

    #patientId is 0 therefore displaying data for all patients
    if patientId == 0:
        for patientId, visits in patients.items():#accessing data from dictionary patients
            print("Patient ID:", patientId)
            #printing the data of a patient 
            for visit in visits:#printing data from the list visits
                print("  Visit Date:", visit[0])
                print("  Body Temperature:",visit[1],"C")
                print("  Heart Rate:",visit[2],"bpm")
                print("  Respiratory Rate:",visit[3],"bpm")
                print("  Systolic Blood Pressure:",visit[4],"mmHg")
                print("  Diastolic Blood Pressure:",visit[5],"mmHg")
                print("  Oxygen Saturation:",visit[6],"%")
                print()
           
    # If patientId is not 0 then displaying data for the specific patient
    else:
        if patientId in patients:#patientId found in the file
            visits = patients[patientId]
            for visit in visits:
                print("  Visit Date:", visit[0])
                print("  Body Temperature:",visit[1],"C")
                print("  Heart Rate:",visit[2],"bpm")
                print("  Respiratory Rate:",visit[3],"bpm")
                print("  Systolic Blood Pressure:",visit[4],"mmHg")
                print("  Diastolic Blood Pressure:",visit[5],"mmHg")
                print("  Oxygen Saturation:",visit[6],"%")
                print()
        else:#if patientID is not found in the file
            print("Patient with ID",patientId,"not found.")


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    if patientId.isdigit() and (type(patients)is dict):#checking whether the patientID is an integer and patients is a dictionary
        #initializing all variables to 0
        total_temperature=0
        total_heartrate=0
        total_respiratoryrate=0
        total_systolicbloodpressure=0
        total_diastolicbloodpressure=0
        total_oxygensaturation=0
        count=0
        if(int(patientId)==0):#if patientID is 0 calculate for all patients
            
            for patient_Id, visits in patients.items():#accessing data from dictionary patients
                for visit in visits:
                    #calculation of the total values
                    total_temperature+=float(visit[1])
                    total_heartrate+=int(visit[2])
                    total_respiratoryrate+=int(visit[3])
                    total_systolicbloodpressure+=int(visit[4])
                    total_diastolicbloodpressure+=int(visit[5])
                    total_oxygensaturation+=int(visit[6])
                    count+=1
            #average of the total values
            temperature_average=total_temperature/count
            heart_rate_average=total_heartrate/count
            respiratory_rate_average=total_respiratoryrate/count    
            systolic_blood_pressure_average=total_systolicbloodpressure/count
            diastolic_blood_pressure_average=total_diastolicbloodpressure/count
            oxygen_saturation_average=total_oxygensaturation/count
            #displaying the required output
            print("Vital Signs for All Patients:")
            print("  Average temperature:","%.2f" %temperature_average,"C")
            print("  Average heart rate:","%.2f" %heart_rate_average,"bpm")
            print("  Average respiratory rate:","%.2f" %respiratory_rate_average,"bpm")
            print("  Average systolic blood pressure:","%.2f" %systolic_blood_pressure_average,"mmHg")
            print("  Average diastolic blood pressure:","%.2f" %diastolic_blood_pressure_average,"mmHg")
            print("  Average oxygen saturation:","%.2f" %oxygen_saturation_average,"%")
        else:
            if int(patientId) in patients:#checking whether patientID is present in the dictionary and is not 0
                    visits=patients[int(patientId)]
                    for visit in visits:
                        #calculation of the total values
                        total_temperature+=float(visit[1])
                        total_heartrate+=int(visit[2])
                        total_respiratoryrate+=int(visit[3])
                        total_systolicbloodpressure+=int(visit[4])
                        total_diastolicbloodpressure+=int(visit[5])
                        total_oxygensaturation+=int(visit[6])
                        count+=1
                    #average of the total values
                    temperature_average=total_temperature/count
                    heart_rate_average=total_heartrate/count
                    respiratory_rate_average=total_respiratoryrate/count    
                    systolic_blood_pressure_average=total_systolicbloodpressure/count
                    diastolic_blood_pressure_average=total_diastolicbloodpressure/count
                    oxygen_saturation_average=total_oxygensaturation/count
                    #displaying the required output
                    print("Vital Signs for Patient:",patientId)
                    print("  Average temperature:","%.2f" %temperature_average,"C")
                    print("  Average heart rate:","%.2f" %heart_rate_average,"bpm")
                    print("  Average respiratory rate:","%.2f" %respiratory_rate_average,"bpm")
                    print("  Average systolic blood pressure:","%.2f" %systolic_blood_pressure_average,"mmHg")
                    print("  Average diastolic blood pressure:","%.2f" %diastolic_blood_pressure_average,"mmHg")
                    print("  Average oxygen saturation:","%.2f" %oxygen_saturation_average,"%")
           
            else:
                #patientID not found
                print("No data found for patient with ID.",patientId)
                
    else:
        if (patientId.isdigit())==False:#when patientID is not an integer
            print("Error:'patientId' should be an integer.")
        elif(type(patients)is dict)==False:#patients is not a dictionary
            print("Error:'patients' should be a dictionary.")
    
            
    
        
def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    try:
        #taking inputs of the required data
        date_values=date.strip().split('-')#converting string date to list form
        if(len(date_values[0])==4 and len(date_values[1])<=2 and len(date_values[2])<=2):#checking whether the date format is fine
            if(int(date_values[1])>=1 and int(date_values[1])<=12 and int(date_values[2])>=1 and int(date_values[2])<=31):#checking whether date and month is correct
                #checking all the required conditions as mentioned
                if(float(temp)<35.0 or float(temp)>42.0):#temperature value
                    print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")

                elif(int(hr)<30 or int(hr)>180):#heart rate value
                    print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
                    
                elif(int(rr)<5 or int(rr)>40):#respiratory rate value
                    print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
                 
                elif(int(sbp)<70 or int(sbp)>200):#systolic blood pressure value
                    print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
                   
                elif(int(dbp)<40 or int(dbp)>120):#diastolic blood pressure value
                    print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
                  
                elif(int(spo2)<70 or int(spo2)>100):#oxygen saturation value
                    print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%")
                   
                else:
                    #creating a list that will store new entries
                    new_entry=[date,temp,hr,rr,sbp,dbp,spo2]
                    if patientId not in patients:
                        #if patientID is not present in the dictionary
                        patients[patientId]=[]
                        #appending all the values
                    patients[patientId].append(new_entry)
                    #appending newdata in the file
                    with open(fileName, "a") as f:
                        f.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")
                    print("Visit saved for patient #",patientId)
            else:
                #if date is invalid
                print("Invalid date. Please enter a valid date.")
        else:
            #if format of date is invalid
            print("Invalid date format. Please enter date in the format(yyyy-mm-dd).")
    except:
        print("An unexpected error occurred while adding new data.")
    



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filters"""
    visits = []
    #creating an empty list
    for patientId ,patient_visits in patients.items():#accessing data from dictionary patients
        for visit in patient_visits:
            visit_year=visit[0].strip().split('-')#obtaining year value from the file
            if len(visit_year)==3:#checking whether the date is valid
               if int(visit_year[1])>=1 and int(visit_year[1])<=12 and int(visit_year[2])>=1 and int(visit_year[2])<=31:#checking all the required conditions
                   if(year==None and month==None) or(year==None and month!=None and month>=1 and month<=12):#year not given////month may or may not  be given
                       visit.append(patientId)
                       visits.append(visit)
                   elif(year!=None and month==None):#year given month not given
                       if(int(visit_year[0])==year):
                           visit.append(patientId)
                           visits.append(visit)
                   elif(year!=None and month!=None):#both year and month given
                       if(int(visit_year[0])==year and int(visit_year[1])==month):
                           visit.append(patientId)
                           visits.append(visit)                           
    return visits 
    
def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patientslist = []#creating an empty list
    try:
        for patientId,visits in patients.items():#accessing data from dictionary patients
           for visit in visits:
               if(int(visit[2])<60 or int(visit[2])>100 or int(visit[4])>140 or int(visit[5])>90 or int(visit[6])<90):#checking all the required conditions
                   followup_patientslist.append(patientId)#appending patientId in the created list
                   break          
                
    except Exception as e:
        print("An error has occured.")
        
                
    return followup_patientslist


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    patientId_lst=[]#creating an empty list
    if patientId not in patients:#when patientId is not in the patients dictionary
        print("No data found for patient with ID",patientId)
    else:#patientId is present in patients dictionary
        file=open(filename,'w')
        patients.pop(int(patientId))#deleting data related to that patientId
        for i in patients:
            for j in patients.get(i):
                #converting all data into string
                Id=str(i)
                date=str(j[0])
                temp=str(j[1])
                hr=str(j[2])
                rr=str(j[3])
                sbp=str(j[4])
                dbp=str(j[5])
                spo2=str(j[6])
                st=""
                st=(Id+","+date+","+temp+","+hr+","+rr+","+sbp+","+dbp+","+spo2+"\n")#concatenating in string form
                file.write(st)#rewriting the data in the file
        print("Data for patient",patientId,"has been deleted.")

        
    
  




###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile("patients.txt")
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
            
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                   
                    print("Patient ID:", visit[7])
                    print(" Visit Date:", visit[0])
                    print("  Temperature:", "%.2f" % visit[1], "C")
                    print("  Heart Rate:", visit[2], "bpm")
                    print("  Respiratory Rate:", visit[3], "bpm")
                    print("  Systolic Blood Pressure:", visit[4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[5], "mmHg")
                    print("  Oxygen Saturation:", visit[6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
