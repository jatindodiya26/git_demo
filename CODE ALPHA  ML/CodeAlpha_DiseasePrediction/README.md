# CodeAlpha - Disease Prediction from Medical Data

## Objective
Build a machine learning classification model to predict disease outcome using medical features.

This project is completed as part of the **CodeAlpha Machine Learning Internship (Task 4: Disease Prediction)**.

## Dataset
- **Breast Cancer Wisconsin dataset** (built into scikit-learn)
- Loaded using:
  - `sklearn.datasets.load_breast_cancer()`
- Target:
  - `malignant` / `benign`

## Approach
1. Load dataset from scikit-learn
2. Split into train/test sets (stratified)
3. Preprocess:
   - Standardize features using `StandardScaler`
4. Model:
   - Logistic Regression
5. Evaluation:
   - Classification report (precision, recall, f1-score)
   - Confusion matrix heatmap
   - ROC-AUC score
6. Save model pipeline:
   - `disease_prediction_model.joblib`

## Project Structure
```text
CodeAlpha_DiseasePrediction/
  disease_prediction.py
  requirements.txt
  README.md