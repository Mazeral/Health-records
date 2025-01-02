"""Utils file for the doctor model
Contains the CRUD methods
"""

from ... import db
from ..models.doctor import Doctor


def get_all_doctors():
    return Doctor.queury.all()


def get_doctor_by_id(doctor_id):
    return Doctor.queury.get(doctor_id)


def create_doctor(first_name,
                  last_name,
                  date_of_birth,
                  specialization,
                  contact_number,
                  email,
                  patients):
    try:
        doctor = Doctor(first_name=first_name,
                        last_name=last_name,
                        date_of_birth=date_of_birth,
                        specialization=specialization,
                        contact_number=contact_number,
                        email=email,
                        patients=patients)
        db.session.add(doctor)
        db.session.commit()
        return doctor
    except Exception as e:
        raise e


def update_doctor(doctor_id, **kwargs):
    doctor = get_doctor_by_id(doctor_id)
    if doctor:
        for key, value in kwargs.items():
            setattr(doctor, key, value)
        db.session.commit()
    return doctor


def delete_doctor(doctor_id):
    doctor = get_doctor_by_id(doctor_id)
    if doctor:
        db.session.delete(doctor)
    db.session.commit()
    return doctor
