<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=009688&center=true&vCenter=true&width=600&height=70&lines=⚡+FastAPI+Projects;REST+APIs+Built+with+Python;Routing+%7C+Middleware+%7C+Background+Tasks" alt="Typing SVG" />

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)

</div>

---

## 📌 About This Repository

This repository is a **collection of FastAPI projects and practice files** built while learning production-grade REST API development with Python. It covers core FastAPI concepts including routing, Pydantic validation, dependency injection, background tasks, file uploads, cookies, middleware, and HTML form handling.

---

## 📁 Project Breakdown

### 🛒 1. Inventory Management API — `inventory_api.py`

A full **CRUD REST API** for managing a product inventory with an HTML customer suggestion form.

**Features:**
- `GET /` — Serves an HTML form where customers can suggest new products
- `POST /submit` — Accepts form data and saves suggestions to a file via **Background Task**
- `GET /get_all_products` — Admin-only route using **Dependency Injection** (`Depends`)
- `GET /single/{id}` — Fetch a single product by ID using **Path Parameters**
- `POST /create_pp` — Add a new product with **Pydantic validation** (`Field`, `gt`)
- `POST /create_order` — Create a product order
- `GET /check_stock/{id}` — Check if a product needs restocking
- `GET /check_price/{id}` — Categorize product pricing (costly / reasonable / budget)
- `PUT /update_price/{id}` — Update product price
- `DELETE /del/{id}` — Remove out-of-stock products

**Concepts demonstrated:** `Path`, `Query`, `Form`, `Depends`, `BackgroundTasks`, `HTTPException`, `HTMLResponse`, `BaseModel`, `Field`, `Enum`

---

### ✅ 2. Task Management API — `task_management.py`

A **task uploader API** with file upload support, cookie management, and admin authentication via headers.

**Features:**
- `GET /` — HTML form to submit tasks with name, description, category, status, email, and file upload
- `POST /upload/` — Accepts form + file, stores task in memory, and saves data + file via **two Background Tasks**
- `GET /all_tasks` — Admin-only route protected by **Header-based authentication**
- `GET /tasks?name=...` — Search tasks by name using **Query Parameters** with min-length validation
- `GET /taskss?Category=...` — Search tasks by category
- `GET /set_cookie` — Sets an HTTP-only session cookie with expiry
- `GET /whoima` — Reads the cookie and identifies the user

**Concepts demonstrated:** `Header`, `Cookie`, `Response`, `File`, `UploadFile`, `BackgroundTasks`, `Depends`, `HTMLResponse`, `os.makedirs`

---

### 📧 3. Email Simulation — `Email_Stimulation.py`

Simulates an email notification system using **Background Tasks** — sends email processing to the background so the API response returns immediately without waiting.

---

### 📚 4. Online Library API — `Online_library.py`

A REST API for managing an online library catalog with book listings, search, and borrowing logic.

---

### 📝 5. Feedback Collector — `feedbackcollector.py`

An API that collects user feedback through a form and stores responses, demonstrating **Form handling** and **file persistence**.

---

## 🧠 FastAPI Concepts Covered

| Concept | Used In |
|---|---|
| Path Parameters | Inventory API, Task API |
| Query Parameters | Task API |
| Pydantic Models & Validation | Inventory API |
| Form Data Handling | Inventory API, Task API, Feedback Collector |
| File Upload (`UploadFile`) | Task API |
| Background Tasks | Inventory API, Task API, Email Simulation |
| Dependency Injection (`Depends`) | Inventory API, Task API |
| Header Authentication | Task API |
| Cookie Set & Read | Task API |
| HTTPException | Inventory API, Task API |
| HTML Response | Inventory API, Task API |
| Enum | Inventory API |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/AimCodes-beep/Fastapi_Code.git
cd Fastapi_Code
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn python-multipart
```

**3. Run any project**
```bash
# Run Inventory API
uvicorn inventory_api:app --reload

# Run Task Management API
uvicorn task_management:app --reload
```

**4. Open in browser**
```
http://127.0.0.1:8000        → HTML Form
http://127.0.0.1:8000/docs   → Interactive Swagger UI (auto-generated)
http://127.0.0.1:8000/redoc  → ReDoc Documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **FastAPI** | Web framework for building REST APIs |
| **Uvicorn** | ASGI server to run the app |
| **Pydantic** | Data validation and serialization |
| **Python-Multipart** | Form data and file upload parsing |

---

## 📂 File Structure

```
Fastapi_Code/
│
├── inventory_api.py       # Full CRUD Inventory API with HTML form
├── task_management.py     # Task uploader with file upload & cookies
├── Email_Stimulation.py   # Background email simulation
├── Online_library.py      # Online library catalog API
├── feedbackcollector.py   # Feedback collection API
├── main.py                # Practice / entry point
├── practise8.py           # FastAPI practice exercises
├── Task_details.txt       # Auto-generated by task_management.py
└── README.md
```

---

## 👩‍💻 Author

**Aiman Nisar** — Aspiring Data Scientist & Backend Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aiman-nisar-a20790354)
[![GitHub](https://img.shields.io/badge/GitHub-AimCodes--beep-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AimCodes-beep)

---

<div align="center">
<i>Built with ⚡ FastAPI — Modern, fast, production-ready APIs with Python</i>
</div>
