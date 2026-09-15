"""Telegram-бот: /esf, /fresh — работает ли система сейчас. Данные: BuhGPT Статус — buhgpt.kz/status

    pip install requests
    TELEGRAM_BOT_TOKEN=... python telegram_bot.py
"""
import os
import time

import requests

API = "https://buhgpt.kz/status/api/pulse/v1"
TG = f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}"
COMMANDS = {"/esf": "esf", "/snt": "esf_vs", "/ecp": "nuc", "/knp": "knp", "/fresh": "fresh_ea", "/kaspi": "kaspi"}


def answer(service_id, lang):
    s = requests.get(f"{API}/context", params={"service": service_id, "lang": lang}, timeout=10).json()
    return f"{s['service_name']}: {s['status_label']}\n{s['advice']}\n\n{s['attribution']}\n{s['source_url']}"


def main():
    offset = 0
    while True:
        updates = requests.get(f"{TG}/getUpdates", params={"offset": offset, "timeout": 50}, timeout=60).json()
        for u in updates.get("result", []):
            offset = u["update_id"] + 1
            msg = u.get("message") or {}
            cmd = (msg.get("text") or "").split("@")[0].strip().lower()
            if cmd in COMMANDS:
                lang = "ru" if (msg.get("from", {}).get("language_code") or "").startswith("ru") else "kk"
                requests.post(f"{TG}/sendMessage", data={"chat_id": msg["chat"]["id"], "text": answer(COMMANDS[cmd], lang),
                                                          "disable_web_page_preview": "true"}, timeout=10)
        time.sleep(1)


if __name__ == "__main__":
    main()
