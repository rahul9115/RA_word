import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
class LinearRegression:
    def __init__(self,iterations,learning_rate):
        self.w=[]
        self.b=0
        self.epochs=iterations
        self.n=learning_rate
    
    def update_weights(self,x,y,y_pred):
        print((x.T).dot(y-y_pred).shape)
        dw=-(2*(x.T).dot(y-y_pred))/x.shape[0]
        db=-(2*np.sum(y-y_pred))/x.shape[0]
        print(dw)
        self.w=self.w-self.n*dw
        self.b=self.b-self.n*db

    def fit(self,x,y):
        self.w=np.zeros(x.shape[1])
        for i in range(self.epochs):
            y_pred=self.predict(x)
            self.update_weights(x,y,y_pred)

    def predict(self,x):
        return np.dot(x,self.w)+self.b

def main() : 
    df = pd.read_csv( "salary_data.csv" ) 
    X = df.iloc[:,:-1].values 
    Y = df.iloc[:,1].values 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0) 
    model = LinearRegression( iterations = 1000,learning_rate = 0.01) 
    model.fit( X_train, Y_train ) 
    Y_pred = model.predict( X_test )  
    print( "Predicted values ", np.round( Y_pred[:3], 2 ) )     
    print( "Real values      ", Y_test[:3] )    
    print( "Trained W        ", round( model.w[0], 2 ) )  
    print( "Trained b        ", round( model.b, 2 ) ) 
if __name__ == "__main__" :  
    main()