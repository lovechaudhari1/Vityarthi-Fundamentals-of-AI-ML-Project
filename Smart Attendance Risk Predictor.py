from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# starting with some basic sample data (total classes and attended classes)
data = [
    [40, 30],
    [50, 20],
    [45, 35],
    [60, 40],
    [55, 25],
    [48, 30],
    [52, 45],
    [47, 20]
]

# converting the raw data into something the model can understand better
# adding percentage and missed classes
X = []
for item in data:
    held = item[0]
    attended = item[1]
    percent = (attended / held) * 100
    missed = held - attended
    X.append([held, attended, percent, missed])

# deciding whether each case is safe or risky based on 75% rule
y = []
for row in X:
    if row[2] >= 75:
        y.append(0)   # safe
    else:
        y.append(1)   # at risk

# splitting the data so we can train and test properly
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

# using a simple model for prediction
model = LogisticRegression()
model.fit(Xtrain, ytrain)

# checking how well the model is performing
pred = model.predict(Xtest)
print("Model accuracy:", accuracy_score(ytest, pred))

# taking input from the user
held = int(input("Enter total number of classes held: "))
attended = int(input("Enter number of classes attended: "))

# calculating percentage and missed classes for the user
percent = (attended / held) * 100
missed = held - attended

print("Your attendance percentage is:", round(percent, 2), "%")

# preparing input for prediction
new_data = [[held, attended, percent, missed]]
result = model.predict(new_data)

# final output
if percent >= 75:
    print("You are safe in terms of attendance.")
else:
    print("You are at risk due to low attendance.")
