package com.internship.tool.controller;
///Temp code only 
import com.internship.tool.service.AuditService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/audit")
@RequiredArgsConstructor
public class AuditController {

    private final AuditService auditService;

    //  UPDATE AUDIT FINDING
    @PutMapping("/{id}")
    public ResponseEntity<?> updateAudit(
            @PathVariable Long id,
            @RequestBody Object request) {

        Object response = auditService.updateAudit(id, request);
        return ResponseEntity.ok(response);
    }

    //  SOFT DELETE (NOT HARD DELETE)
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteAudit(@PathVariable Long id) {

        auditService.softDeleteAudit(id);
        return ResponseEntity.noContent().build();
    }

    // SEARCH API
    @GetMapping("/search")
    public ResponseEntity<Page<Object>> searchAudit(
            @RequestParam String q,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(defaultValue = "id") String sortBy,
            @RequestParam(defaultValue = "asc") String sortDir) {

        Page<Object> results = auditService.searchAudit(q, page, size, sortBy, sortDir);
        return ResponseEntity.ok(results);
    }

    //  DASHBOARD STATS API
    @GetMapping("/stats")
    public ResponseEntity<Map<String, Object>> getStats() {

        Map<String, Object> stats = auditService.getStats();
        return ResponseEntity.ok(stats);
    }
}
