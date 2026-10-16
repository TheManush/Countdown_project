# ⏳ Donnarumma Contract Countdown

A simple, live countdown website tracking the time remaining until Gianluigi Donnarumma's contract with Manchester City expires.

## 🌐 Live Website

🌐 **Live Website:** [Open the Countdown](https://donna-contract-cntdown.onrender.com)
## 📸 About the Project

Countdown Studio is a personal web project built to display the remaining time until the target contract expiration date. It features a countdown timer that updates every second, a player photograph, and the Manchester City club logo.

### ✨ Features

- Live countdown displaying days, hours, minutes, and seconds.
- Automatic updates every second without refreshing the page.
- Donnarumma's photograph and Manchester City logo.
- Dark blue gradient background with a modern, minimalist design.
- Responsive layout for desktop and mobile devices.
- Free online deployment using Render.

## 🛠️ Technologies Used

- **Python** — countdown calculations and backend logic.
- **Flask** — web application framework.
- **HTML** — webpage structure.
- **CSS** — styling and responsive design.
- **JavaScript** — automatic countdown updates.
- **Git & GitHub** — version control and source code hosting.
- **Render** — web hosting and deployment.

## 📁 Project Structure

```text
Countdown_project/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── DONNA.jpg
    └── city_logo.png
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/TheManush/Countdown_project.git
cd Countdown_project
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open the website

Visit **http://127.0.0.1:5000** in your browser.

## ☁️ Deployment

This project is deployed on Render using a free web service connected to GitHub.

**Build command:**

```bash
pip install -r requirements.txt
```

**Start command:**

```bash
gunicorn app:app
```

The website may take a little longer to load after a period of inactivity because Render's free web services can spin down when idle.

## 👨‍💻 Author

**TheManush**

GitHub: [@TheManush](https://github.com/TheManush)

---

*Built as a personal web development project.*
