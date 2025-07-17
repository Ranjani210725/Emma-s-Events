# 🗓️ Emma's Events – AI-Powered Event Management System

A full-stack Flask web application for managing events with AI-based event category prediction, RSVP management, and user authentication.

---

 🚀 Features

 ✅ User Authentication (Login & Logout)
 ✅ Add/Edit/Delete Events
 ✅ RSVP to Events with Guest Count
 ✅ AI-Based Event Type Prediction (using Cohere)
 ✅ Search Events by Name, Location, Description, or Type
 ✅ Fully Responsive UI with Bootstrap
 ✅ SQLite Database with SQLAlchemy ORM

---

🛠️ Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Cohere AI API
- SQLite
- HTML, CSS (Bootstrap)

---

📦 Project Structure


project-folder/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth/
│   │   └── routes.py
│   ├── classifier/
│   │   └── predict\_event.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add\_event.html
│   │   ├── edit\_event.html
│   │   └── rsvp.html
│   └── static/
│       └── style.css
│
├── run.py
├── requirements.txt
├── README.md
└── events.db (created at runtime)


---

# 🧠 AI Integration (Event Category Prediction)

The system uses the [Cohere AI](https://cohere.com) API to predict the category/type of each event based on the event name, location, and description.

Example categories:
- Seminar
- Conference
- Party
- Workshop
- Celebration

> You must add your own Cohere API key in `predict_event.py`.

---

 ⚙️ How to Run Locally

1. Clone the Repository

```bash
git clone https://github.com/yourusername/emmas-events.git
cd emmas-events
````

2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Add Cohere API Key

Open `app/classifier/predict_event.py` and replace:

```python
co = cohere.Client("your-api-key")  # 🔁 Replace with your Cohere API key
```

5. Run the App

```bash
python run.py
```

Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

📸 Screenshots

🏠 Home Page
![Home](screenshots/home.png)

➕ Add Event
![Add Event](screenshots/add_event.png)

📋 RSVP Page
![RSVP](screenshots/rsvp.png)

---

📄 License

This project is part of an internship assignment and is for educational purposes only.
