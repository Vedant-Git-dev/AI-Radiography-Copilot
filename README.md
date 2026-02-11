# RadiantAI - AI Clinical Assistant for Radiology

## Overview

This project presents an AI assisted clinical screening system for chest X ray interpretation, designed with a Model Context Protocol (MCP) driven architecture. Instead of producing a single static prediction, the system dynamically adapts its behavior based on model confidence, invoking explainability tools and human review pathways when uncertainty is detected.

The primary use case demonstrated is COVID 19 screening from chest X ray images, with an emphasis on high sensitivity, transparency, and safe clinical decision support rather than automated diagnosis.

## Live Demo

**Try it now:** [RadiantAI](https://radiantai-jnle2pz7dedksseytcnncg.streamlit.app/)


## Key Idea

- Traditional deep learning classifiers output probabilities or labels without context. In clinical settings, this can lead to unsafe overconfidence or silent failure.

- This system introduces an MCP layer that acts as a decision orchestrator. The MCP layer interprets model outputs, applies clinically motivated thresholds, selects appropriate tools such as Grad CAM for explainability, and produces human readable clinical guidance.

- The result is a system that knows when it is confident, when it is uncertain, and when a human expert should be involved.

## System Architecture

1. Chest X ray image upload

2. Image preprocessing and normalization

3. Deep learning classifier inference using EfficientNet

4. MCP decision logic based on confidence thresholds

5. Conditional invocation of explainability tools

6. Structured clinical output and recommendation

## Model Details

- The classifier is based on **EfficientNetB0** and trained for binary classification between COVID positive and normal chest X rays.

- Due to class imbalance in medical imaging datasets, evaluation prioritized recall and precision recall analysis rather than accuracy alone.

## Evaluation Summary

On an unseen test subset from the same source dataset, the model achieved:

- AUC approximately 0.78

- High recall(97.98) with lower precision, consistent with screening oriented behavior

- The operating threshold was selected to achieve approximately 97 percent recall, prioritizing sensitivity over specificity to reduce missed positive cases.

## Model Context Protocol Logic

The MCP layer translates raw model probabilities into clinically meaningful system behavior.

Decision logic is defined as follows:

- Low probability cases are treated as likely normal with no additional tools invoked.

- Intermediate probability cases are classified as indeterminate and routed for human review with Grad CAM visualization enabled.

- High probability cases are flagged as COVID suspected and escalated for further clinical evaluation with explainability output.

This design ensures that uncertainty is explicitly surfaced rather than hidden.

## Explainability with Grad CAM

- For cases requiring review or escalation, Grad CAM is used to highlight image regions that contributed most strongly to the model’s prediction.

- These visual explanations help clinicians understand model attention patterns and assess whether predictions align with clinically relevant lung regions.

- Grad CAM is not shown for confidently normal cases to reduce cognitive overload.

## Limitations

- The model is trained on publicly available datasets and may not generalize across all populations, imaging devices, or clinical settings.

- Grad CAM provides qualitative explanations and should not be interpreted as precise lesion localization.

## Conclusion

This project demonstrates how Model Context Protocols can be applied to medical imaging systems to move beyond static predictions toward adaptive, transparent, and clinically aligned AI behavior.

By combining deep learning, explainability, and decision orchestration, the system provides a realistic example of how AI can assist rather than replace clinical expertise.