#  AI Event Vendor Recommendation System

An AI-powered event planning assistant built with Flask that helps users select vendors based on event type, budget, and location. Users can also submit bargain offers for listed vendors!

---

##  Features

-  Vendor recommendation based on location and budget
-  Planning steps generated based on event type
-  Bargain option to submit custom offers
-  Built with Python, Flask, and Jinja templating
-  Clean and responsive UI with HTML + CSS

---

##  Tech Stack

- **Backend:** Python + Flask
- **Frontend:** HTML, CSS, Jinja2
- **Mock Data:** Python Dictionary (easily extendable to CSV/JSON/API)
- **IDE Used:** VS Code

---

##  How It Works

1. User selects:
   - Event Type (Wedding, Birthday, etc.)
   - Budget range
   - Location

2. System filters vendors by:
   - Matching location
   - Price ≤ Budget

3. Sorted vendors are shown (highest rating first)
4. Planning steps are displayed based on event type
5. Users can **request a bargain** by submitting a custom offer

---

## 🖼️ Screenshots

### 🧾 Form Page:
![Form Page](/screenshots/form.png)

### 📊 Result Page:
![Result Page](/screenshots/result.png)




## 📂 Folder Structure

event-planner-ai/
├── app.py
├── README.md
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── result.html
│   └── bargain_response.html
├── screenshots/
│   ├── form.png
│   └── result.png


