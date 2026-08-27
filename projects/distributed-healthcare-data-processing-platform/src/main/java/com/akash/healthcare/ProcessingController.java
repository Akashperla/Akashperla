package com.akash.healthcare;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import org.springframework.http.HttpStatus;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.time.OffsetDateTime;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/records")
public class ProcessingController {

    private final JdbcTemplate jdbcTemplate;

    public ProcessingController(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public record HealthcareRecordRequest(
            @NotBlank String patientReference,
            @NotBlank String recordType,
            @NotBlank String sourceSystem,
            @NotBlank String status
    ) {}

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Map<String, Object> create(@Valid @RequestBody HealthcareRecordRequest request) {
        Long id = jdbcTemplate.queryForObject(
                "INSERT INTO healthcare_record (patient_reference, record_type, source_system, status) VALUES (?, ?, ?, ?) RETURNING id",
                Long.class,
                request.patientReference(),
                request.recordType(),
                request.sourceSystem(),
                request.status()
        );

        return getById(id);
    }

    @GetMapping
    public List<Map<String, Object>> getAll() {
        return jdbcTemplate.queryForList(
                "SELECT id, patient_reference, record_type, source_system, status, created_at FROM healthcare_record ORDER BY id DESC"
        );
    }

    @GetMapping("/{id}")
    public Map<String, Object> getById(@PathVariable Long id) {
        List<Map<String, Object>> rows = jdbcTemplate.queryForList(
                "SELECT id, patient_reference, record_type, source_system, status, created_at FROM healthcare_record WHERE id = ?",
                id
        );

        if (rows.isEmpty()) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Healthcare record not found");
        }
        return rows.get(0);
    }
}
