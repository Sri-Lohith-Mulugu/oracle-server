import os
import json
from fastmcp import FastMCP

# 1. Initialize the Server First (Prevents NameError)
mcp = FastMCP("CodeOracle")

# 2. Helper function for Windows paths
def get_clean_path(path):
    return path.strip('"').strip("'")

# --- TOOL 1: ARCHITECTURE SCAN ---
@mcp.tool()
def audit_project(directory_path: str):
    """Fast architectural scan of the tech stack."""
    path = get_clean_path(directory_path)
    if not os.path.exists(path): return "Error: Path not found."

    tech_stack, key_files = set(), []
    for root, dirs, files in os.walk(path):
        # Surgical skip for speed
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'venv', 'build', 'dist']]
        for file in files:
            if file == "package.json": tech_stack.add("React/Node.js")
            if file == "requirements.txt": tech_stack.add("Python/ML")
            if file.endswith((".py", ".jsx", ".js")) and len(key_files) < 15:
                key_files.append(f"{os.path.basename(root)}/{file}")

    return json.dumps({"Stack": list(tech_stack), "Files": key_files}, indent=2)

# --- TOOL 2: SECURITY SCAN ---
@mcp.tool()
def check_security_leaks(directory_path: str):
    """Surgical security scan for hardcoded secrets."""
    path = get_clean_path(directory_path)
    leaks, patterns = [], ["API_KEY", "PASSWORD", "SECRET", "TOKEN", "MONGO_URI"]
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'venv']]
        for file in files:
            if file in [".env", "config.json"]: leaks.append(f"CRITICAL: {file} exposed.")
            file_path = os.path.join(root, file)
            # Only read small files to prevent hanging
            if file.endswith((".py", ".js")) and os.path.getsize(file_path) < 500000:
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        content = f.read().upper()
                        for p in patterns:
                            if f"{p} =" in content or f"{p}=" in content:
                                leaks.append(f"WARNING: {p} in {file}")
                except: continue
    return json.dumps({"Findings": leaks}, indent=2)

# --- TOOL 3: ML ASSET TRACKER ---
@mcp.tool()
def audit_ml_assets(directory_path: str):
    """ML model asset discovery and size reporting."""
    path = get_clean_path(directory_path)
    models = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git']]
        for file in files:
            if file.lower().endswith((".pth", ".h5", ".onnx", ".pb", ".weights")):
                size_mb = os.path.getsize(os.path.join(root, file)) / (1024 * 1024)
                models.append({"model": file, "size": f"{size_mb:.2f} MB"})
    return json.dumps({"Models Found": models}, indent=2)

# --- TOOL 4: CODE METRICS (LOC) ---
@mcp.tool()
def get_code_stats(directory_path: str):
    """Quantifies the scale of the project (Lines of Code)."""
    path = get_clean_path(directory_path)
    stats = {"ML/Python (.py)": 0, "Frontend/Logic (.js, .jsx)": 0, "Other": 0}
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'venv', 'dist']]
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getsize(file_path) > 500000: continue # Skip huge files
                with open(file_path, 'r', errors='ignore') as f:
                    line_count = sum(1 for line in f)
                if file.endswith(".py"): stats["ML/Python (.py)"] += line_count
                elif file.endswith((".js", ".jsx")): stats["Frontend/Logic (.js, .jsx)"] += line_count
                else: stats["Other"] += line_count
            except: continue
    return json.dumps({"Line Count Breakdown": stats, "Total Custom LOC": sum(stats.values())}, indent=2)

if __name__ == "__main__":
    mcp.run()