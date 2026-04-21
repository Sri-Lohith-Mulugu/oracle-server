\# Code-Oracle 🔍 

\### \*MCP-Based Repository Diagnostic \& Security Engine\*



Code-Oracle is a high-performance \*\*Model Context Protocol (MCP)\*\* server built to bridge the gap between AI agents and local codebases. It provides automated architectural mapping, security vulnerability detection, ML asset tracking and quantitative code metrics — all accessible directly from AI assistants like Claude Desktop and Cursor IDE.



\---



\## 🚀 Key Features



\* \*\*Architectural Auditing:\*\* Instantly identifies tech stacks (React, Node.js, Flask, Python/ML) and maps core file structures

\* \*\*Security SAST:\*\* Static Analysis Security Testing that flags hardcoded passwords, JWT tokens, API keys and exposed `.env` files

\* \*\*ML Asset Discovery:\*\* Specialized tracking for machine learning model weights (`.pth`, `.h5`, `.onnx`) with size reporting

\* \*\*Quantitative Metrics:\*\* Calculates total Lines of Code (LOC) broken down by file type while intelligently filtering auto-generated files



\---



\## 🛠️ The "Turbo" Engine — Performance Optimization



To solve the common \*\*"Request Timeout"\*\* issue in the MCP ecosystem, Code-Oracle implements \*\*Surgical Directory Pruning\*\*.



Instead of scanning every file, Code-Oracle uses a \*\*Skip-First logic\*\* that completely bypasses "black-hole" directories like `node\_modules`, `.git` and `venv` at the OS level \*\*before\*\* recursing into them:



```python

dirs\[:] = \[d for d in dirs if d not in \['node\_modules', '.git', 'venv', 'build', 'dist']]

```



This reduces scan times from \~15 seconds to \*\*under 200ms\*\*, even on massive full stack projects.



\---



\## 📊 Demo Output



!\[Code-Oracle MCP Inspector Output](output-demo.png)



| Metric | Value |

| :--- | :--- |

| \*\*Total Lines of Code\*\* | 22,552 |

| \*\*Frontend Logic (JS/JSX)\*\* | 818 LOC |

| \*\*ML Backend (Python)\*\* | 218 LOC |

| \*\*Security Findings\*\* | 4 Critical Leaks Detected |



\---



\## 🔧 4 Built-in Tools



\### 1. 🏗️ `audit\_project` — Architecture Scan

Scans a repository and identifies the tech stack and key source files.



\*\*Example Output:\*\*

```json

{

&#x20; "Stack": \["Python/ML", "React/Node.js"],

&#x20; "Files": \["flask\_server/app.py", "client/src/App.jsx"]

}

```



\### 2. 🔒 `check\_security\_leaks` — Security Scanner

Scans Python and JavaScript files for hardcoded secrets and exposed sensitive files.



\*\*Detects:\*\* API keys, passwords, tokens, secrets, MongoDB URIs, exposed `.env` files



\*\*Example Output:\*\*

```json

{

&#x20; "Findings": \[

&#x20;   "CRITICAL: .env exposed.",

&#x20;   "WARNING: API\_KEY in config.js"

&#x20; ]

}

```



\### 3. 🧠 `audit\_ml\_assets` — ML Asset Tracker

Discovers all trained ML model files in a repository with their sizes.



\*\*Detects:\*\* `.pth`, `.h5`, `.onnx`, `.pb`, `.weights` files



\*\*Example Output:\*\*

```json

{

&#x20; "Models Found": \[

&#x20;   {"model": "model.pth", "size": "9.49 MB"},

&#x20;   {"model": "model2.pth", "size": "0.05 MB"}

&#x20; ]

}

```



\### 4. 📊 `get\_code\_stats` — Lines of Code Counter

Quantifies the scale of a project by counting lines of code broken down by file type.



\*\*Example Output:\*\*

```json

{

&#x20; "Line Count Breakdown": {

&#x20;   "ML/Python (.py)": 218,

&#x20;   "Frontend/Logic (.js, .jsx)": 818,

&#x20;   "Other": 21516

&#x20; },

&#x20; "Total Custom LOC": 22552

}

```



\---



\## ⚙️ Installation, Setup \& Launch



```bash

\# Clone the repository

git clone https://github.com/Sri-Lohith-Mulugu/oracle-server.git



\# Navigate into the project

cd oracle-server



\# Install dependencies

pip install -r requirements.txt



\# Set timeout for stable MCP connection (Windows PowerShell)

$env:MCP\_SERVER\_REQUEST\_TIMEOUT=300000



\# Run the MCP server using Inspector

npx @modelcontextprotocol/inspector python server.py

```



\---



\## 🔌 Connecting to Claude Desktop



Add this to your Claude Desktop config file (`claude\_desktop\_config.json`):



```json

{

&#x20; "mcpServers": {

&#x20;   "CodeOracle": {

&#x20;     "command": "python",

&#x20;     "args": \["path/to/oracle-server/server.py"]

&#x20;   }

&#x20; }

}

```



Once connected, you can ask Claude:

\- \*"Scan my project at C:/Users/me/MyProject"\*

\- \*"Check for security leaks in my repository"\*

\- \*"How many lines of code does my project have?"\*

\- \*"Find all ML models in my project folder"\*



\---



\## 📁 Project Structure



```

oracle-server/

│

├── server.py          # Main MCP server with all 4 tools

├── requirements.txt   # Dependencies (fastmcp)

├── output-demo.png    # Sample MCP Inspector output

└── .gitignore

```



\---



\## 🌍 Real-World Applications



\- 🔍 \*\*Code Review Assistant\*\* — let AI scan your repo before code review

\- 🔒 \*\*Security Auditing\*\* — catch hardcoded secrets before pushing to GitHub

\- 📊 \*\*Project Metrics\*\* — quickly understand the scale of any codebase

\- 🧠 \*\*ML Project Management\*\* — track large model files across repositories

\- 🏗️ \*\*Tech Stack Discovery\*\* — instantly understand unfamiliar codebases



\---



\## 🧠 What I Learned



\- Building MCP (Model Context Protocol) servers using FastMCP

\- Connecting custom Python tools directly into AI assistants like Claude Desktop

\- Solving timeout issues in recursive file system operations using Surgical Directory Pruning

\- Designing structured JSON responses for AI tool consumption

\- Security scanning patterns (SAST) for detecting hardcoded secrets in source code



\---



\## ⚠️ Note



This tool scans \*\*local repositories only\*\* — it does not make any network requests or access remote repositories. All scanning is done on your local file system.



\---



\## 📄 License



This project is for educational and personal use.



