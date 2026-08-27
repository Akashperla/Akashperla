CREATE TABLE IF NOT EXISTS healthcare_record (
    id BIGSERIAL PRIMARY KEY,
    patient_reference VARCHAR(100) NOT NULL,
    record_type VARCHAR(80) NOT NULL,
    source_system VARCHAR(120) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_healthcare_record_patient
    ON healthcare_record (patient_reference);

CREATE INDEX IF NOT EXISTS idx_healthcare_record_type
    ON healthcare_record (record_type);
