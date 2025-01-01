"""Patient model
SQLAlchemy model reprenting the patient data"""

from ...app import db


class Patient(db.Model):
    """Model for patients."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    medical_records = db.relationship(
                                        'MedicalRecord',
                                        backref='patient',
                                        lazy=True
                                      )

    def __repr__(self):
        return f'<Patient {self.first_name} {self.last_name}>'
