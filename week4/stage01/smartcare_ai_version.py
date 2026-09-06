# A very simple appointment booking system for beginners.
# No database, no GUI — just basic Python lists and dictionaries.

appointments = []  # This will store all booked appointments

def book_appointment(patient_name, practitioner_name, appointment_time):
    """Adds a new appointment to the appointments list."""
    
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    
    appointments.append(appointment)
    print("Appointment booked successfully!")

def display_appointments():
    """Shows all booked appointments."""
    
    if not appointments:
        print("No appointments booked yet.")
        return
    
    print("\n--- All Appointments ---")
    for appt in appointments:
        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")
    print("------------------------\n")


# Example usage:
book_appointment("Alice Smith", "Dr. John Doe", "2026-09-11 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2026-09-11 11:30 AM")

display_appointments()
#book_appointment('', 'Dr. Nobody', '2026-09-11 09:00 AM')   # test 1: blank patient name
#book_appointment('Alice Smith', 'Dr. John Doe', '2026-09-11 10:00 AM')  # test 2: exact duplicate
book_appointment(None, None, None)                            # test 3: None values