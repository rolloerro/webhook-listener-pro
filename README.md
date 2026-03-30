# 📡 Webhook Listener Pro

🔥 Лёгкий, быстрый и готовый к продакшену сервис для приёма, логирования и проверки входящих вебхуков.

---

## 🚀 Возможности

* 🔥 Приём любых `POST /webhook` событий
* 🧾 Автоматическое логирование входящих данных
* 🛡️ Проверка подписи (HMAC-SHA256, опционально)
* 📤 JSON-ответ клиенту
* 🧩 Интеграция с:

  * GitHub
  * Telegram
  * Stripe
  * Notion
  * и любыми другими сервисами

---

## ⚡ Быстрый старт

```bash
git clone https://github.com/rolloerro/webhook-listener-pro.git
cd webhook-listener-pro
pip install -r requirements.txt
```

---

## ▶️ Запуск

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

📡 Endpoint будет доступен:

```
http://localhost:8080/webhook
```

---

## 📬 Пример запроса

```bash
curl -X POST http://localhost:8080/webhook \
-H "Content-Type: application/json" \
-d '{"event": "hello", "value": 123}'
```

### Ответ:

```json
{
  "status": "received"
}
```

---

## 🧪 Быстрый тест

```bash
python3 - << 'EOF'
import requests

r = requests.post("http://localhost:8080/webhook", json={"ping": True})
print(r.status_code, r.json())
EOF
```

---

## ⚙️ Переменные окружения

| Переменная     | Описание                                |
| -------------- | --------------------------------------- |
| WEBHOOK_SECRET | Включает проверку подписи (HMAC-SHA256) |

---

## 📁 Структура проекта

```
webhook-listener-pro/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Логи

Все входящие вебхуки логируются:

```
[2026-01-01 12:00:00] Incoming webhook: { "event": "order.created" }
```

---

## 🧩 Использование в продакшене (systemd)

```ini
[Unit]
Description=Webhook Listener Pro
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/opt/webhook-listener-pro
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 💡 Кейсы использования

* Приём webhook от GitHub (CI/CD)
* Telegram bot callbacks
* Stripe платежи
* Notion интеграции
* Автоматизация процессов

---

## 🧑‍💻 Автор

**rolloerro** — быстрые API и практичные решения ⚡

---

## ⭐ Поддержка проекта

Если проект оказался полезным:

👉 Поставь звезду
👉 Сделай fork
👉 Открой PR

---
