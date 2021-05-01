import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dia_all = pd.read_csv("diabetes.txt") # This loads the full dataset
                 # In the file, attributes are separated by
  
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score


