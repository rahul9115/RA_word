import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
class LogisticRegression:
    def __init__(self,iterations,learning_rate):
        self.w=[]
        self.b=0
        self.epochs=iterations
        self.n=learning_rate
    
    def update_weights(self,x,y,y_pred):
        dw=(x.T).dot(y_pred-y))/x.shape[0]
        db=-(2*np.sum(y_pred-y))/x.shape[0]
        self.w=self.w-self.n*dw
        self.b=self.b-self.n*db

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def fit(self,x,y):
        self.w=np.zeros(x.shape[1])
        for i in range(self.epochs):
            y_pred=self.predict(x)
            self.update_weights(x,y,y_pred)

    def predict(self,x):
        dot_weights=np.dot(x,self.w)+self.b
        probabilities=self.sigmoid(dot_weights)
        return [1 if p>0.5 else 0 for p in probabilities] 

def main() : 
    df = pd.read_csv( "salary_data.csv" ) 
    X = df.iloc[:,:-1].values 
    Y = df.iloc[:,1].values 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0) 
    model = LogisticRegression( iterations = 1000,learning_rate = 0.01) 
    model.fit( X_train, Y_train ) 
    Y_pred = model.predict( X_test )  
    print( "Predicted values ", np.round( Y_pred[:3], 2 ) )     
    print( "Real values      ", Y_test[:3] )    
    print( "Trained W        ", round( model.w[0], 2 ) )  
    print( "Trained b        ", round( model.b, 2 ) ) 
if __name__ == "__main__" :  
    main()