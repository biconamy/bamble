# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MiniCRM
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    dates = set(r['date'] for r in records)
    week_start = min(dates).isocalendar()[1]  # ISO year-week number is insufficient; use actual date range
    weeks = []
    current_week_start = None
    for d in sorted(dates):
        if current_week_start is None:
            w_start = d - timedelta(days=d.weekday())
            w_end = w_start + timedelta(weeks=1) - timedelta(days=1)
            current_week_start = w_start
        elif not (current_week_start <= d <= current_week_start + timedelta(weeks=1)):
            weeks.append((current_week_start, len([r for r in records if current_week_start <= date(r['date'].year, r['date'].month, r['date'].day) <= current_week_start + timedelta(weeks=1)])))
            w_start = d - timedelta(days=d.weekday())
            w_end = w_start + timedelta(weeks=1) - timedelta(days=1)
            current_week_start = w_start
    if current_week_start: weeks.append((current_week_start, len([r for r in records if current_week_start <= date(r['date'].year, r['date'].month, r['date'].day) <= current_week_start + timedelta(weeks=1)])))
    return {str(w[0]): w[1] for w in weeks}
