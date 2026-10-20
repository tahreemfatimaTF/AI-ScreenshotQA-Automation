import streamlit as st
import base64
import json
import urllib.request

st.set_page_config(page_title="ScreenshotQA", page_icon="🔍")

st.title("🔍 ScreenshotQA")
st.subheader("AI Screenshot QA Reviewer")

st.write(
    "Upload an application screenshot and AI will identify potential "
    "UI, UX, accessibility, alignment, spacing, and text visibility issues."
)

uploaded_file = st.file_uploader(
    "Choose a screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Screenshot")

    if st.button("Analyze Screenshot"):

        with st.spinner("AI is reviewing the screenshot..."):

            image_bytes = uploaded_file.getvalue()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            prompt = """
You are an experienced Software QA Engineer.

Review this application screenshot and identify potential:
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

Only report issues that can reasonably be identified from the screenshot.
Do not claim functional bugs that cannot be verified from an image.
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

            try:
                with urllib.request.urlopen(request) as response:
                    result = json.loads(
                        response.read().decode("utf-8")
                    )

                st.success("Screenshot analysis completed!")
                st.subheader("AI QA Review")
                st.markdown(result["response"])

                st.info(
                    "AI findings are potential issues. "
                    "A QA engineer should validate them before logging bugs."
                )

            except Exception as error:
                st.error(f"Unable to analyze screenshot: {error}")