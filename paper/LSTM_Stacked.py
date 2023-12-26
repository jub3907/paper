#%%
import numpy as np
import pandas as pd
from pandas import DataFrame
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import tensorflow as tf
from sklearn.metrics import precision_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from keras import backend as K
import csv
import time
from numpy import array
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


class CustomHistory(keras.callbacks.Callback):
    def init(self):
        self.train_loss = []
        self.val_loss = []
        
    def on_epoch_end(self, batch, logs={}):
        self.train_loss.append(logs.get('loss'))
        self.val_loss.append(logs.get('val_loss'))


def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the dataset
		if end_ix > len(sequences)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, -1]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

def Drop_column(df):
    df = df.drop('time', axis=1)
    df = df.drop('moving_avg', axis=1)
    df = df.drop('RUL', axis=1)
    df = df.drop('flow_rate', axis = 1)
    df = df.drop('upstream_pressure', axis = 1)
    df = df.drop('downstream_pressure', axis = 1)
    df = df.drop('pressure_drop', axis = 1)
    df = df[6:]
    return df

def Healthy_Drop(df):
    for i in range(n_steps, len(df)):
        k = 0
        for j in range(n_steps):
            if (float(df.iloc[i-j, 2]) < training_threshold):
                k += 1
        if (k == n_steps):
            train_split_num = i
            break
    return df[train_split_num:]
#%%
for i_count in range(100):
    #i_count = 0
    count = 9

    if (0<= i_count <= 50):
        Test_count = str(100*count + i_count)
        epoch = 70
        learning_rate = 0.001
    else:
        Test_count = str(100 * count + i_count)
        epoch = 75
        learning_rate = 0.001
    #%%
    training_threshold = threshold = 0.84722125

    Drop_out = 0
    Hidden_node = 16
    #이 위만 건들면 됨
    #####################################################################################
    train_num = "41"
    train_num2 = "42"
    train_num3 = "43"
    pred_num = "44"
    pred_split_num = 0
    n_steps = 30
    activation = 'elu'
    epoch2 = epoch
    epoch3 = epoch  

    #####################################################################################

    #%%

    Data = DataFrame(pd.read_csv('.\\sample_data\\training\\Processed_Sample'+ train_num +'.csv'))
    Data = Drop_column(Data)
    Data = Healthy_Drop(Data)
    Data = Data.values

    Data2 = DataFrame(pd.read_csv('.\\sample_data\\training\\Processed_Sample'+ train_num2 +'.csv'))
    Data2 = Drop_column(Data2)
    Data2 = Healthy_Drop(Data2)
    Data2 = Data2.values

    Data3 = DataFrame(pd.read_csv('.\\sample_data\\training\\Processed_Sample'+ train_num3 +'.csv'))
    Data3 = Drop_column(Data3)
    Data3 = Healthy_Drop(Data3)
    Data3 = Data3.values
    #%%
    pred_data = DataFrame(pd.read_csv('.\\sample_data\\training\\Processed_Sample'+pred_num+'.csv'))
    pred_data = Drop_column(pred_data)

    for h in range(n_steps, len(pred_data)):
        k = 0
        for j in range(n_steps):
            if (float(pred_data.iloc[h-j, 2]) < training_threshold):
                k += 1
        if (k == n_steps):
            pred_split_num = h
            break
    pred_data = pred_data[pred_split_num:]
    pred_data = pred_data.values
    #%%
    f = open(".\\Stack\\Output\\"+pred_num+"_RUL_Predtopred_Stack_"+Test_count+".csv", 'w',  newline='')
    writer = csv.writer(f)
    row_num = pred_split_num
    writer.writerow(["index", "Real" , "Pred"] )
    #%%
    X, y = split_sequences(Data, n_steps)
    X2, y2 = split_sequences(Data2, n_steps)
    X3, y3 = split_sequences(Data3, n_steps)

    pred_X, pred_y = split_sequences(pred_data, n_steps)
    # reshape from [samples, timesteps] into [samples, timesteps, features]

    n_features = X.shape[2]
    X = X.reshape((X.shape[0], n_steps, n_features))
    X2 = X2.reshape((X2.shape[0], n_steps, n_features))
    X3 = X3.reshape((X3.shape[0], n_steps, n_features))

    pred_X = pred_X.reshape((pred_X.shape[0], n_steps, n_features))



    #y = y.reshape(y.shape[0], 1)
    #val_y = val_y.reshape(val_y.shape[0], 1)

    # define model
    model = Sequential()
    model.add(LSTM(Hidden_node, activation=activation, return_sequences=True, input_shape=(n_steps, n_features)))
    model.add(Dropout(Drop_out))
    model.add(LSTM(Hidden_node, activation=activation, return_sequences=True, input_shape=(n_steps, n_features)))
    model.add(Dropout(Drop_out))
    model.add(LSTM(Hidden_node, activation=activation))
    #Simple -> return sequence가 필요하고, input_shape는 맨위층만
    model.add(Dense(1))
    adam = keras.optimizers.Adam(lr=learning_rate)
    model.compile(optimizer=adam , loss='mse')


    custom_hist = CustomHistory()
    custom_hist.init()
    # fit model
    model.fit(X, y, epochs=epoch, verbose=0, callbacks=[custom_hist])
    model.fit(X2, y2, epochs = epoch2, verbose=0, callbacks=[custom_hist])
    model.fit(X3, y3, epochs = epoch3, verbose=0, callbacks=[custom_hist])

    model.save(".\\Stack\\Model\\Stack_" + Test_count + ".h5")
    #%%
    plt.clf()
    plt.plot(custom_hist.train_loss)
    plt.plot(custom_hist.val_loss)
    #####################################################################################
    plt.ylim(0, 0.01)
    #####################################################################################
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.savefig(".\\Stack\\Loss\\RUL_Predtopred_Stack_Loss_" + Test_count + ".png")
    #plt.show()
    plt.close('all')

    #%%
    i = 0
    pred_row = pred_X[0]
    row = 0
    while (True):

        pred_row = pred_row.reshape(1, n_steps, n_features)
        pred_x_1 = model.predict(pred_row)
        arr = np.array([pred_row[0][0][0], pred_row[0][0][1], pred_x_1[0][0]])
        new_pred_row = pred_row[0][1:]
        pred_row = np.vstack([new_pred_row, arr])
        if (i < pred_y.shape[0]):
            if (pred_x_1[0][0] < 0):
                writer.writerow([pred_split_num+i, pred_y[i], 0])
            else:
                writer.writerow([pred_split_num+i, pred_y[i], pred_x_1[0][0]])
        else:
            if i == pred_y.shape[0]:
                break

        row += 1
        i = i + 1
    #%%

    # multistep에서는 reshape하고서 받아와서 예측
    f.close()
    #%%
    f = open(".\\Stack\\Output\\" + pred_num + "_RUL_Predtopred_Stack_variables.csv", 'a')
    HC = pd.read_csv(".\\Stack\\Output\\"+pred_num+"_RUL_Predtopred_Stack_"+Test_count+".csv")
    HC_Data = DataFrame(HC)
    real_list = np.array(HC['Real'])
    pred_list = np.array(HC['Pred'])
    plt.clf()
    plt.plot(real_list)
    plt.plot(pred_list)
    #####################################################################################
    plt.ylim(0, 1)
    #####################################################################################
    plt.ylabel('HI')
    plt.xlabel('time')
    plt.legend(['Real', 'Pred'], loc = 'upper right')
    plt.savefig(".\\Stack\\Graph\\RUL_Predtopred_Stack_Graph_" + Test_count + ".png")
    #plt.show()
    plt.close('all')

    RMSE = np.sqrt(((pred_list - real_list) ** 2).mean())
    nRMSE = RMSE / (real_list.mean())
    f.write(str(RMSE) + ',' + str(nRMSE) + ','  + str(train_num)  + ',' + str(pred_num) + ',' + str(n_steps) + ',' + str(Hidden_node) + ',' + str(learning_rate) + ',' + str(epoch) + ',' + str(Drop_out) + ',' + str(Test_count) + '\n')

    f.close()


    # %%
