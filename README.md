# Vityarthi-Fundamentals-of-AI-ML-Project
 #  Fundamentals of AI & ML Project – CSA2001

##  Student Details
- **Name:** Love Chaudhari  
- **Course:** B.Tech (CSE AI & ML)  
- **University:** VIT Bhopal University  
- **Course Code:** CSA2001  
- **Project Type:** Smart Attendance Risk Predictor  

---

## Smart Attendance Risk Predictor

A simple Python-based machine learning project that helps predict whether a student is safe or at risk based on attendance.
The project uses the number of classes held and classes attended to calculate attendance percentage, then checks it against the 75% minimum attendance rule.

### What the project does
- Takes input from the user:
  - total classes held
  - classes attended
- Calculates attendance percentage
- Checks whether the student is safe or at risk
- Displays the result clearly
- Uses a basic Logistic Regression model from scikit-learn

### Why this project matters

In many colleges, attendance is very important. Students often do not realize they are falling below the safe limit until it becomes a problem. This project gives a quick and easy way to check attendance status early.

### Features
- User input-based prediction
- Attendance percentage shown in output
- Based on the 75% attendance rule
- Easy to run and understand

### Requirements

Make sure you have:

scikit-learn

Install the required package using:

pip install scikit-learn

### How to run the project

```
1.Download or clone the repository.
2.Open the Python file in your editor.
3.Run the script.
4.Enter:
- total classes held
- classes attended
5.The program will show:
- attendance percentage
- whether the student is safe or at risk
```

### Example

```
Enter total number of classes held: 40
Enter number of classes attended: 30
Your attendance percentage is: 75.0 %
You are safe in terms of attendance.
```

### How it works

The project uses a small sample dataset for training.
From that dataset, it calculates:

- attendance percentage
- missed classes

Then it trains a simple classification model to understand the pattern of safe and risky attendance cases.

After training, the model takes new user input and gives a prediction.
