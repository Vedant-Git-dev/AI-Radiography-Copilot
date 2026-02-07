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