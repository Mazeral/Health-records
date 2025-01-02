"""medical record model
SQLAlchemy model reprenting the medical record of the patient data"""

from .. import db


class Doctor(db.Model):
    """Model for doctors."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # We are saying here that we will create a new row in the refrenced model
    # (Patient) named (doctor)
    # To make it one-to-one: add the option uselist and set it to False
    patients = db.relationship('Patient', back_populates="doctor")
