# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MiniCRM
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="MiniCRM CLI")
    sub = parser.add_subparsers(dest="command")

    # -- contacts --
    p = sub.add_parser("contacts", help="contacts management")
    p.add_argument("subcmd", choices=["add", "list", "show", "delete"])
    p.add_argument("--name", "-n", help="Contact name")
    p.add_argument("--phone", "-p", help="Phone number")
    p.add_argument("--email", "-e", help="Email")
    p.add_argument("--id", "-i", type=int, help="Contact ID (for show/delete)")

    # -- deals --
    p = sub.add_parser("deals", help="deals management")
    p.add_argument("subcmd", choices=["add", "list", "show", "delete", "update"])
    p.add_argument("--title", "-t", help="Deal title")
    p.add_argument("--amount", "-a", type=float, help="Deal amount")
    p.add_argument("--status", "-s", help="Deal status (new/negotiation/deal)")
    p.add_argument("--id", "-i", type=int, help="Deal ID")
    p.add_argument("--value", "-v", help="New value for update")

    # -- reminders --
    p = sub.add_parser("reminders", help="reminders management")
    p.add_argument("subcmd", choices=["add", "list", "delete"])
    p.add_argument("--text", "-t", help="Reminder text")
    p.add_argument("--date", "-d", help="Reminder date (YYYY-MM-DD)")
    p.add_argument("--id", "-i", type=int, help="Reminder ID")

    # -- messages --
    p = sub.add_parser("messages", help="messages management")
    p.add_argument("subcmd", choices=["add", "list"])
    p.add_argument("--text", "-t", help="Message text")
    p.add_argument("--contact_id", "-c", type=int, help="Contact ID")
    p.add_argument("--date", "-d", help="Message date (YYYY-MM-DD)")

    args = parser.parse_args()
    return args
