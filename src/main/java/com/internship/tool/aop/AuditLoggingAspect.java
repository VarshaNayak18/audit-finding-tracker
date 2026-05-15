package com.internship.tool.aop;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.internship.tool.entity.AuditFinding;
import com.internship.tool.entity.AuditLog;
import com.internship.tool.repository.AuditFindingRepository;
import com.internship.tool.repository.AuditLogRepository;
import lombok.RequiredArgsConstructor;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
@RequiredArgsConstructor
public class AuditLoggingAspect {

    private final AuditFindingRepository auditFindingRepository;
    private final AuditLogRepository auditLogRepository;
    private final ObjectMapper objectMapper;

    @Around("execution(* com.internship.tool.service.impl.AuditFindingServiceImpl.create*(..))")
    public Object logCreate(ProceedingJoinPoint joinPoint) throws Throwable {
        Object result = joinPoint.proceed();

        if (result instanceof AuditFinding created) {
            saveAudit("CREATE", created.getId(), null, toJson(created));
        }

        return result;
    }

    @Around("execution(* com.internship.tool.service.impl.AuditFindingServiceImpl.update*(..))")
    public Object logUpdate(ProceedingJoinPoint joinPoint) throws Throwable {
        Long id = extractId(joinPoint.getArgs());
        String oldJson = null;

        if (id != null) {
            oldJson = auditFindingRepository.findById(id)
                    .map(this::toJson)
                    .orElse(null);
        }

        Object result = joinPoint.proceed();

        if (result instanceof AuditFinding updated) {
            saveAudit("UPDATE", updated.getId(), oldJson, toJson(updated));
        }

        return result;
    }

    @Around("execution(* com.internship.tool.service.impl.AuditFindingServiceImpl.delete*(..))")
    public Object logDelete(ProceedingJoinPoint joinPoint) throws Throwable {
        Long id = extractId(joinPoint.getArgs());
        String oldJson = null;

        if (id != null) {
            oldJson = auditFindingRepository.findById(id)
                    .map(this::toJson)
                    .orElse(null);
        }

        Object result = joinPoint.proceed();

        if (id != null) {
            saveAudit("DELETE", id, oldJson, null);
        }

        return result;
    }

    private Long extractId(Object[] args) {
        if (args == null) {
            return null;
        }

        for (Object arg : args) {
            if (arg instanceof Long value) {
                return value;
            }
        }

        return null;
    }

    private void saveAudit(String action, Long entityId, String oldValue, String newValue) {
        if (entityId == null) {
            return;
        }

        AuditLog auditLog = new AuditLog();
        auditLog.setEntityType("AuditFinding");
        auditLog.setEntityId(entityId);
        auditLog.setAction(action);
        auditLog.setOldValue(oldValue);
        auditLog.setNewValue(newValue);

        auditLogRepository.save(auditLog);
    }

    private String toJson(Object value) {
        try {
            return objectMapper.writeValueAsString(value);
        } catch (JsonProcessingException ex) {
            throw new IllegalStateException("Failed to serialize audit payload", ex);
        }
    }
}
