import base64
import json
import urllib.request

image_path = "screenshot.png"

with open(image_path, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

prompt = """
You are an experienced Software QA Engineer.

Review this application screenshot and identify possible:
- UI issues
- UX issues
- Accessibility issues
- Alignment or spacing problems
- Text visibility problems

For each issue provide:
1. Issue
2. Category
3. Severity
4. Recommendation

Do not invent bugs that are not visible in the screenshot.
"""

data = {
    "model": "gemma3:4b",
    "prompt": prompt,
    "images": [image_base64],
    "stream": False
}

request = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

print("\n===== AI SCREENSHOT QA REVIEW =====\n")
print(result["response"])