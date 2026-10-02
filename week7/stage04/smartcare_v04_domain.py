class Patient:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be blank")
        self.name = name
        self.appointments = []

    def get_appointments(self):
        return self.appointments


class Practitioner:
    def __init__(self, identifier: str, name: str, specialty: str):
        if not identifier:
            raise ValueError("Identifier cannot be blank")
        if not name:
            raise ValueError("Name cannot be blank")
        if not specialty:
            raise ValueError("Specialty cannot be blank")
        self.identifier = identifier
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def get_schedule(self):
        return self.appointments


from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"


class Appointment:
    def __init__(self, patient: "Patient", practitioner: "Practitioner", time: str):
        if not patient:
            raise ValueError("Appointment requires a patient")
        if not practitioner:
            raise ValueError("Appointment requires a practitioner")
        if not time or not time.strip():
            raise ValueError("Appointment time cannot be blank")
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = AppointmentStatus.BOOKED
        self.created_at = datetime.now()

    def validate(self) -> bool:
        return bool(self.patient and self.practitioner and self.time.strip())

    def is_duplicate(self, other: "Appointment") -> bool:
        return (
            self.patient == other.patient
            and self.practitioner == other.practitioner
            and self.time == other.time
        )

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")
        self.status = AppointmentStatus.CANCELLED