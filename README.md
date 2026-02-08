## AI Radiology Copilot

In this repo I will be working on a system that takes Chest X-ray as an input and assist (not replace) to diagnose Covid-19 based on localizing infection, and after that it will generate an explainable draft report, and flag uncertainty. 

index.json contains metadata about the dataset.

## Models Trained (Till now)

### Classifier: EfficientNetB0

- classifies Covid vs Normal X-rays
- Outputs prediction class probabilities
- Training AUC: 0.5438
- Validation AUC: 0.7827
- Validation Loss: 0.5557
- Recall: 0.978494623655914

After all analysis, because the dataset contains far more normal cases than COVID-19 cases, I evaluated the model using the Precision–Recall curve rather than accuracy alone. I selected an operating threshold of 0.238, which allows the model to correctly identify approximately 97% of COVID-19 cases, placing emphasis on sensitivity. At this threshold, the model achieves a precision of 39%, meaning that while some non-COVID cases are flagged, the risk of missing true COVID-19 cases is substantially reduced. This trade-off is appropriate for an early screening or triage setting, where false positives can be reviewed further, but false negatives are more critical.