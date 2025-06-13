
![best-removebg-preview](https://github.com/user-attachments/assets/a929b0a7-e590-4c99-a94d-ec8b95b2e26c)

# 🕵️‍♂️ SkitDetector

**SkitDetector** is an advanced AI-powered CLI tool that scans Python code for potential skid behavior (copied, low-effort, or AI-generated code) using **Google Gemini AI**.

Made for devs who got trust issues 🥀

---

## 🚀 Features

- 🔍 **AI-Powered Analysis** — Uses Gemini to analyze and detect sus code patterns
- 🎨 **Rich CLI UI** — Clean, colorful terminal output with `rich`
- 📊 **Detailed Reports** — Insightful breakdown of scan results
- 🔐 **Secure API Handling** — Load Gemini API key from `.env`
- ⚡ **Fast asf** — Async file scanning for speed demons

---

## ⚙️ Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Run SkitDetector:**
   ```bash
   python skitdetector.py scan <file_or_directory>
   ```

---

## 🛠️ Usage

### 🔹 Scan a single file
```bash
python skitdetector.py scan path/to/file.py
```

### 🔹 Scan a whole directory
```bash
python skitdetector.py scan path/to/directory
```

### 🔹 Help menu
```bash
python skitdetector.py --help
```

---

## 📋 Requirements

- Python 3.8+
- Valid Google Gemini API key
- Internet connection (obviously lol)

---

## 📄 License

MIT License — do whatever tf u want, just don’t skid my skit detector 😭🙏

---

## 💭 Extra Ideas?

- Add Discord webhook support for auto-reporting skids 💀  
- Export JSON/PDF reports  
- VS Code extension integration? maybe...

---

> made by skit for skits 💀  
> now go catch some frauds
