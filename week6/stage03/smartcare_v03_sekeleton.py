# ---- Stage 3: Domain Model Skeleton (Part G) ----

class Patient:
    def __init__(self, name):
        self.name = name

    def get_appointments(self):
        """Return this patient's appointment history. Not yet implemented."""
        pass


class Practitioner:
    def __init__(self, name):
        self.name = name

    def get_schedule(self):
        """Return this practitioner's scheduled appointments. Not yet implemented."""
        pass


class Appointment:
    def __init__(self, patient, practitioner, time):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = "booked"
        self.created_at = None  # will hold a timestamp once implemented

    def validate(self):
        """Check required fields aren't blank. Not yet implemented."""
        pass

    def is_duplicate(self, other):
        """Check if this appointment duplicates another. Not yet implemented."""
        pass

    def cancel(self):
        """Mark this appointment as cancelled, retaining its record. Not yet implemented."""
        pass


# ---- Part H: Consistency Check ----
# Compared against the UML Class Diagram and CRC cards in the Domain Model
# Workbook: all three classes match the same attributes (patient.name,
# practitioner.name, appointment.patient/practitioner/time/status/created_at)
# and the same three Appointment methods (validate, is_duplicate, cancel).
# No behaviour is implemented yet, consistent with the handout's instruction

# Quick manual test
p = Patient("Red John")
pr = Practitioner("Dr. Patrick Jane")
a = Appointment(p, pr, "2026-09-11 10:00 AM")

print(a.patient.name)
print(a.practitioner.name)
print(a.time)
print(a.status)