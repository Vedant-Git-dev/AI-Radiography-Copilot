from mcp.tools.classifier import run_classifier
from mcp.tools.grad_cam import compute_grad_cam

THRESHOLD = 0.24099901

def mcp_infer(img_path):
    prob = run_classifier(img_path)

    result = {
        "probability": prob,
        "decision": None,
        "tools_used": [],
        "overlay": None
    }

    if prob < 0.15:
        result["decision"] = "Likely Normal"

    elif prob < THRESHOLD:
        result["decision"] = "Borderline – Needs Review"
        overlay = compute_grad_cam(img_path)
        result["tools_used"].append("Grad-CAM")
        result["overlay"] = overlay

    else:
        result["decision"] = "COVID Suspected"
        overlay = compute_grad_cam(img_path)
        result["tools_used"].append("Grad-CAM")
        result["overlay"] = overlay

    return result
