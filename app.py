from keras.datasets import mnist
from matplotlib import pyplot

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

print("X_train: " + str(train_X.shape))
print("Y_train: " + str(train_Y.shape))
print("X_test: " + str(test_X.shape))
print("Y_test: " + str(test_Y.shape))

for i in range(9):
    pyplot.subplot(330 + 1 + i)
    pyplot.imshow(train_X[i], cmap=pyplot.get_cmap('gray'))
pyplot.show()
