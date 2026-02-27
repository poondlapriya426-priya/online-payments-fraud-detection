import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 1. Create a tiny dummy model
model = RandomForestClassifier()
# X = [Type, Amount, OldBalance, NewBalance]
X = np.array([[1, 1000, 5000, 4000], [2, 2000, 2000, 0]])
y = np.array([0, 1]) 
model.fit(X, y)

# 2. Save it correctly to 'payments.pkl'
with open('payments.pkl', 'wb') as f:
    pickle.dump(model, f)

print("SUCCESS: A new payments.pkl has been created!")