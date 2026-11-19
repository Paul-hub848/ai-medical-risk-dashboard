import re

def run_scan(code_content):
    vulnerabilities = []
    lines = code_content.split('\n')
    
    for i, line in enumerate(lines, 1):
        if re.search(r'(api_key|secret|password|token)\s*=\s*[\'"][^\'"]+[\'"]', line, re.IGNORECASE):
            vulnerabilities.append({
                "line": i,
                "severity": "High",
                "type": "Hardcoded Secret / API Key",
                "description": f"Potential hardcoded credential or key detected: {line.strip()}"
            })
        
        if 'http://' in line:
            vulnerabilities.append({
                "line": i,
                "severity": "Medium",
                "type": "Insecure Network Protocol",
                "description": f"Unencrypted HTTP endpoint used instead of HTTPS: {line.strip()}"
            })
        
        if 'pickle.load' in line or 'pickle.loads' in line:
            vulnerabilities.append({
                "line": i,
                "severity": "Critical",
                "type": "Unsafe Deserialization (Pickle)",
                "description": f"Using pickle.load can expose medical AI models to arbitrary code execution: {line.strip()}"
            })
            
    return vulnerabilities