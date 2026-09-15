#!/usr/bin/env bash
# BuhGPT Статус — открытое API. Данные: BuhGPT Статус — buhgpt.kz/status
BASE="https://buhgpt.kz/status/api/pulse/v1"

# Работает ли ЭСФ прямо сейчас (готовый совет пользователю в поле advice)
curl -s "$BASE/context?service=esf&lang=ru"

# Все системы с проблемами (нужен jq)
curl -s "$BASE/summary?lang=ru" | jq -r '.groups[].services[] | select(.status != "OPERATIONAL" and .status != "UNKNOWN") | "\(.name): \(.status_label)"'

# Последний сбой 1С:Fresh Бухгалтерии и сколько он длился
curl -s "$BASE/summary?lang=ru" | jq '.groups[].services[] | select(.id == "fresh_ea") | .last_incident'
