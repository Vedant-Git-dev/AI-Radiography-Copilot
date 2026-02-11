import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
import cv2
import tempfile
from mcp.orchestrator import mcp_infer

st.set_page_config(page_title="AI Clinical Assistant (MCP)", layout="wide")

st.title("🩻 AI Clinical Assistant for Radiology")
st.subheader("MCP-Orchestrated COVID Screening")

uploaded_file = st.file_uploader(
    "Upload Chest X-ray (PNG/JPG)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(uploaded_file.read())
        img_path = tmp.name

    st.image(img_path, caption="Uploaded X-ray", width=300)

    with st.spinner("Running MCP pipeline..."):
        result = mcp_infer(img_path)

    st.markdown("### Model Output")
    st.write(f"**COVID Probability:** {result['probability']:.3f}")
    st.write(f"**MCP Decision:** {result['decision']}")
    st.write(f"**Tools Used:** {', '.join(result['tools_used']) or 'Classifier only'}")

    if result["overlay"] is not None:
        st.markdown("### Grad-CAM Explanation")
        overlay_rgb = cv2.cvtColor(result["overlay"], cv2.COLOR_BGR2RGB)
        st.image(overlay_rgb, caption="Grad-CAM Overlay", width=400)

    st.markdown("### Clinical Note")
    if result["decision"] == "Likely Normal":
        st.info("Low likelihood of COVID-19. Routine monitoring recommended.")
    elif "Borderline" in result["decision"]:
        st.warning("Uncertain findings. Radiologist review recommended.")
    else:
        st.error("High sensitivity screening flagged possible COVID-19. Further evaluation advised.")
