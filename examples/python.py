"""BuhGPT Статус — открытое API. Данные: BuhGPT Статус — buhgpt.kz/status

    pip install requests
    python python.py
"""
import requests

BASE = "https://buhgpt.kz/status/api/pulse/v1"


def context(service_id, lang="ru"):
    r = requests.get(f"{BASE}/context", params={"service": service_id, "lang": lang}, timeout=10)
    r.raise_for_status()
    return r.json()


def problems(lang="ru"):
    s = requests.get(f"{BASE}/summary", params={"lang": lang}, timeout=10).json()
    return [x for g in s["groups"] for x in g["services"] if x["status"] not in ("OPERATIONAL", "UNKNOWN")]


if __name__ == "__main__":
    esf = context("esf")
    print(f"{esf['service_name']}: {esf['status_label']}. {esf['advice']}")
    for p in problems():
        last = p.get("last_incident") or {}
        print(f"— {p['name']}: {p['status_label']}" + (f", длится {last['duration_s'] // 60} мин" if last.get("ongoing") else ""))
    print(esf["attribution"])
