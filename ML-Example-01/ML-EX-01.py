from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = ["ECO CAR / B-SEGMENT", "ECO CAR / B-SEGMENT", "VAN", "VAN"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
x = input("Horepower :")
y = input("Seats :")
print(clf.predict([[x, y]]))
