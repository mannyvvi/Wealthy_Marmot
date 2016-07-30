import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style
style.use("ggplot")

x =[1,5,6,8,2,3,9]
y = [2,4,1,7.5,3,3,0]

plt.scatter(x,y)
plt.show

X = np.array([[1,2],[5,4],[6,1],[8,7.5],[3,3],[9,3]])

y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear',C=1.0)
clf.fit(X,y)

print(clf.predict([0.5,1]))
