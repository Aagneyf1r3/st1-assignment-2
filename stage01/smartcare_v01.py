# ---- Part A: Understanding the Problem (AI OFF) ----

# What data must be stored?
# - patient name
# - practitioner name
# - appointment time

# What functions might be useful?
# - book_appointment(patient, practitioner, time): creates and stores one appointment
# - display_appointments(): prints all recorded appointments
# - (optional, later) validate_input(): checks for empty names or invalid times

# What could go wrong?
# - patient name might be blank
# - practitioner name might be blank
# - appointment time might be missing or incorrectly formatted
# - duplicate appointments could be added accidentally
# - None values might be passed into the function
# - the list might stay empty if nothing is booked

# What requirements are unclear?
# - whether duplicate bookings should be blocked
# - whether empty names should be rejected
# - what time format is expected
# - whether appointments can be edited or cancelled
# - whether practitioner availability should be checked
# - whether the system should validate input or just store whatever is given

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Red John'
practitioner1_name = 'Dr. Patrick Jane'
appointment1_time = '2026-09-11 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Thea Merlyn'
practitioner2_name = 'Dr. Moira Queen'
appointment2_time = '2026-09-11 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

book_appointment('Red John', 'Dr. Patrick Jane', '2026-09-11 10:00 AM')
book_appointment('Thea Merlyn', 'Dr. Moira Queen', '2026-09-11 11:30 AM')

display_appointments()

# book_appointment('', 'Dr. Nobody', '2026-09-11 09:00 AM')      # blank patient name
# book_appointment('Red John', 'Dr. Patrick Jane', '2026-09-11 10:00 AM')  # exact duplicate test
# book_appointment(None, None, None)                              # None values
# display_appointments()

# ---- Part B: Testing & Limitations Found (evidence-based) ----

# Test 1: book_appointment('', 'Dr. Nobody', '2026-09-11 09:00 AM')
# Result: crashed with ValueError("Patient name cannot be empty")
# Limitation: blank patient name crashes the whole program instead of
# failing gracefully with a user-friendly message.

# Test 2: book_appointment('Red John', 'Dr. Patrick Jane', '2026-09-11 10:00 AM')  -- duplicate
# Result: ran successfully, duplicate appointment silently added
# Limitation: no check for duplicate bookings (same patient/practitioner/time
# can be booked twice with no warning).

# Test 3: book_appointment(None, None, None)
# Result: crashed with the same ValueError as Test 1
# Limitation: None values crash the same way as blank strings. Also,
# practitioner_name and appointment_time have NO validation at all --
# only patient_name is ever checked.

# Additional limitations (found by inspection, not testing):
# - No time format validation (any string is accepted as a "time")
# - No function to cancel or edit an existing appointment
# - Appointments only exist in memory -- they disappear when the program closes

# ---- Part G: Improvement (AI OFF) ----
# Based on the limitations found in Part B, chose ONE controlled improvement:
# consistent required-field validation. The handout's example only validates
# patient_name, but validating just one of three required fields while leaving
# practitioner_name and appointment_time unchecked would be inconsistent --
# a system meant to prevent bad bookings shouldn't only protect one field.
# Treating this as ONE improvement: "consistent required-field validation"
# applied uniformly across all three required fields. (The actual code change
# is in the book_appointment function defined above, which now checks all
# three fields instead of just patient_name.)
book_appointment('Red John', '', '2026-09-11 10:00 AM')   # blank practitioner — should now raise ValueError