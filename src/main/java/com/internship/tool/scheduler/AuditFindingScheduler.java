package com.internship.tool.scheduler;

import com.internship.tool.entity.AuditFinding;
import com.internship.tool.repository.AuditFindingRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.List;
import java.util.stream.Collectors;

@Slf4j
@Component
@RequiredArgsConstructor
public class AuditFindingScheduler {

    private static final String CLOSED_STATUS = "CLOSED";
    private final AuditFindingRepository auditFindingRepository;

    @Scheduled(cron = "${scheduler.audit.overdue.cron:0 0 9 * * *}", zone = "${app.timezone:Asia/Kolkata}")
    public void sendDailyOverdueReminder() {
        LocalDate today = LocalDate.now();
        List<AuditFinding> overdueFindings = auditFindingRepository
                .findByDueDateBeforeAndStatusIgnoreCaseNot(today, CLOSED_STATUS);

        if (overdueFindings.isEmpty()) {
            return;
        }

        log.info("[Daily Overdue Reminder] {} overdue findings: {}",
                overdueFindings.size(), formatFindings(overdueFindings));
    }

    @Scheduled(cron = "${scheduler.audit.advance-alert.cron:0 0 10 * * *}", zone = "${app.timezone:Asia/Kolkata}")
    public void sendSevenDayAdvanceDeadlineAlert() {
        LocalDate today = LocalDate.now();
        LocalDate sevenDaysFromNow = today.plusDays(7);

        List<AuditFinding> upcomingFindings = auditFindingRepository
                .findByDueDateBetweenAndStatusIgnoreCaseNot(today.plusDays(1), sevenDaysFromNow, CLOSED_STATUS);

        if (upcomingFindings.isEmpty()) {
            return;
        }

        log.info("[7-Day Deadline Alert] {} findings due in next 7 days: {}",
                upcomingFindings.size(), formatFindings(upcomingFindings));
    }

    @Scheduled(cron = "${scheduler.audit.weekly-summary.cron:0 0 11 * * MON}", zone = "${app.timezone:Asia/Kolkata}")
    public void sendWeeklySummary() {
        long total = auditFindingRepository.count();
        long closed = auditFindingRepository.countByStatusIgnoreCase(CLOSED_STATUS);
        long open = total - closed;
        long overdue = auditFindingRepository
                .countByDueDateBeforeAndStatusIgnoreCaseNot(LocalDate.now(), CLOSED_STATUS);

        log.info("[Weekly Summary] total={}, open={}, closed={}, overdue={}", total, open, closed, overdue);
    }

    private String formatFindings(List<AuditFinding> findings) {
        return findings.stream()
                .map(f -> String.format("[id=%d,title=%s,dueDate=%s,status=%s]",
                        f.getId(), f.getTitle(), f.getDueDate(), f.getStatus()))
                .collect(Collectors.joining(", "));
    }
}
