"""medical record model
SQLAlchemy model reprenting the medical record of the patient data"""

from ...app import db


class MedicalRecord(db.Model):
    """Model for medical records."""
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer,
                           db.ForeignKey('patient.id'),
                           nullable=False)
    diagnosis = db.Column(db.String(200), nullable=False)
    treatment = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
