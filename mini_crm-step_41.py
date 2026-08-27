# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MiniCRM
import datetime
import random
import string
import sys

# ============================================
# MiniCRM — Этап 41: Dry-run режим
# ============================================

class DryRunMode:
    """
    Dry-run режим для всех операций изменения данных.
    Записи не сохраняются в БД, но логируются в лог.
    """

    def __init__(self):
        self.enabled = False
        self.log = []
        self._dry_run_log = []

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def log(self, entity, action, record):
        if self.enabled:
            self._dry_run_log.append({
                'entity': entity,
                'action': action,
                'record': record,
                'timestamp': datetime.datetime.now().isoformat(),
            })
            print(f"[DRY-RUN] {entity}: {action} → {record}")

    def get_dry_run_log(self):
        return self._dry_run_log

    def clear_dry_run_log(self):
        self._dry_run_log = []
