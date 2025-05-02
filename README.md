
# 🧠 Cloud Architecture Review Agent

This project automates the **initial review of cloud architecture diagrams**, identifying best practices, potential issues, cost inefficiencies, and more — all through LLM agents. It uses **CrewAI** to coordinate multiple intelligent agents, each focused on a different aspect of review.

---

## 🚀 Features

- 🔍 **Extracts architecture details** from AWS diagrams (via GPT or multimodal models)
- 🧠 **Agent reviews**: security, cost, topology, best practices
- 📊 **Summarized output** with recommendations
- 🧱 Modular structure with `CrewAI` agents and tasks
- 📁 Outputs markdown reports, and structured metadata

---

## 🧭 Architecture Overview

```
📤 Image or JSON input
   │
   ├─▶ (Optional) Multimodal Extraction (Ollama or GPT-4 Vision)
   │       ↓
   └──▶ 📄 service_extraction.json
             │
             ▼
     🤖 CrewAI Agents
         ├─ Topology Analyst
         ├─ Security Reviewer
         ├─ Cost Evaluator
         ├─ Best Practice Checker
         ├─ Interrogator (asks questions)
         └─ Summary Generator
```
---

## 🔧 Setup

1. **Install dependencies**
   ```bash
   pip install crewai crewai-tools
   ```

2. **Set OpenAI API key** (if using GPT-4):
   ```bash
   export OPENAI_API_KEY=sk-...
   ```

3. *(Optional)* For multimodal extraction via Ollama:
   ```bash
   ollama run llava
   ```

---

## ▶️ Running the App

1. **Step 1: Extract Services from Diagram**
   - Use your own script or model to create `output/service_extraction.json`.

2. **Step 2: Run Crew**
   ```bash
   python main.py
   ```

---

## 📄 Sample Output (from Agents)

```json
{
  "services": [
    { "provider": "AWS", "service": "Lambda", "type": "Compute", "metadata": {...} },
    ...
  ],
  "connections": [
    { "source": "API Gateway", "target": "Lambda", "relationship": "invokes" },
    ...
  ]
}
```

Markdown summary report will be saved in:  
📄 `output/final_summary.md`

---

## 🛠 Customization

- Define agents in `config/agents.yaml`
- Define tasks in `config/tasks.yaml`
- Modify review process in `crew.py`

---

## 🧪 Testing Locally with Ollama

If you're using a local model for extraction:
```bash
ollama run llava
```

Then, pipe the output of image → JSON into `output/service_extraction.json`.

---

## 📬 Future Improvements

- Integrate diagram upload UI
- Add model confidence scoring
- Add Azure & GCP support
- Auto-generate architecture maps from JSON

---

## 🤝 Contributors

Built with ❤️ using CrewAI.
