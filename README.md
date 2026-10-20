\# AI-Powered ScreenshotQA Automation



An AI-assisted screenshot review tool built using Python, Streamlit, Ollama, and Gemma 3 4B.



\## Overview



ScreenshotQA helps QA engineers review application screenshots for potential:



\- UI issues

\- UX issues

\- Accessibility issues

\- Alignment and spacing problems

\- Text visibility problems



The AI provides potential findings with an issue description, category, severity, and recommendation.



\*\*Note:\*\* AI findings are suggestions, not confirmed bugs. QA engineers should validate them before reporting defects.



\## Technologies Used



\- Python — Application logic

\- Streamlit — Web interface

\- Ollama — Runs AI models locally

\- Gemma 3 4B — Vision AI model for screenshot analysis



\## Installation



\### 1. Install Python



Download and install Python 3.11 or newer.



\### 2. Install Ollama



Download and install Ollama.



\### 3. Download the AI Model



Open Command Prompt and run:



```cmd

ollama pull gemma3:4b

```



\### 4. Download the Project



Clone the GitHub repository:



```cmd

git clone https://github.com/tahreemfatimaTF/AI-ScreenshotQA-Automation.git

```



Open the project folder:



```cmd

cd AI-ScreenshotQA-Automation

```



\### 5. Install Streamlit



```cmd

pip install streamlit

```



\## How to Run



Make sure Ollama is running.



Start the application:



```cmd

streamlit run app.py

```



Open your browser at:



http://localhost:8501



\## How to Use



1\. Upload an application screenshot.

2\. Click \*\*Analyze Screenshot\*\*.

3\. Wait for the AI analysis.

4\. Review the potential QA findings.

5\. Validate findings before reporting bugs.



\## Project Files



| File | Description |

|---|---|

| app.py | Streamlit web application |

| screenshot\_reviewer.py | Command-line screenshot reviewer |

| .gitignore | Excludes screenshots and sensitive files |



\## Benefits



\- Assists with initial visual QA reviews.

\- Highlights potential usability and accessibility concerns.

\- Runs locally without paid AI API usage.

\- Supports manual QA rather than replacing it.



\## Limitations



\- Requires Ollama and Gemma 3 4B installed locally.

\- AI findings may be inaccurate or incomplete.

\- Cannot confirm functional defects from screenshots alone.

\- The Streamlit application runs locally and is not publicly hosted.



\## Author



Tahreem Fatima

