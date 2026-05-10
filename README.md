# 🚀 CodeLens – AI Code Reviewer

CodeLens is an AI-powered code review platform that helps developers analyze, review, debug, and improve their code instantly.

Built with a clean frontend and a FastAPI backend, CodeLens can:

- Detect programming languages automatically
- Review code quality
- Find logical issues and bugs
- Suggest improvements
- Generate fixed versions of code
- Execute code snippets
- Provide smart AI-generated insights

---

# 🌐 Live Demo

🔗 Frontend (Vercel):  
https://codelens-repo.vercel.app/

🔗 Backend API (Railway):  
https://codelens-ai.up.railway.app/

---

# ✨ Features

## 🤖 AI Code Review

- Reviews submitted code using AI
- Detects bad practices and potential bugs
- Gives improvement suggestions

## 🧠 Automatic Language Detection

Supports multiple languages including:

- C
- C++
- Python
- Java
- JavaScript
- TypeScript
- Go
- Rust
- PHP
- Ruby
- Swift

## 🛠 Code Fix Suggestions

- Generates improved/fixed code
- Helps optimize logic and structure

## ▶️ Code Execution

- Run code directly from the platform
- Instant output generation

## 🎨 Clean UI

- Modern and responsive design
- Easy-to-use interface
- Fast interaction experience

## ⚡ FastAPI Backend

- Built with FastAPI
- REST API architecture
- Lightweight and efficient

---

# 🏗 Tech Stack

## Frontend

- HTML
- CSS
- JavaScript
- Vercel Deployment

## Backend

- Python
- FastAPI
- Uvicorn
- AI API Integration
- Railway Deployment

---

# 📂 Project Structure

```bash
CodeLens/
│
├── frontend/
│   ├── index.html
│
├── backend/
│   ├── main.py
│   ├── reviewer.py
│   ├── request.py
│   ├── fixer.py
│   ├── executor.py
│   ├── parser.py
│   ├── prompt.py
│   └── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nasibyun/ai-code-reviewer.git
cd ai-code-reviewer
```

---

## 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=your_api_key_here
```

Run the backend:

```bash
uvicorn main:app --reload
```

Backend will run on:

```bash
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

Simply open:

```bash
index.html
```

Or use Live Server in VS Code.

---

# 🚀 Deployment

## Frontend Deployment

- Hosted on Vercel

## Backend Deployment

- Hosted on Railway
- API URL:
  https://codelens-ai.up.railway.app/

---

# 🔥 Future Improvements

- User authentication
- Save review history
- Dark/Light theme toggle
- Multiple AI models
- Better code execution sandbox
- GitHub integration
- Real-time collaboration

---

# 💡 Why CodeLens?

CodeLens helps developers:

- Debug faster
- Improve code quality
- Learn best practices
- Save development time
- Get AI-powered assistance instantly

---

# 👨‍💻 Author

Built and designed by Nasib.

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
🛠 Contribute improvements

---

# 📜 License

This project is open-source and available under the MIT License.
