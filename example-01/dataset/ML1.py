from scipy.io import loadmat
import matplotlib.pyplot as plt
load_raw = loadmat("mnist-original.mat")

mnist = {
    "data": load_raw["data"].T,
    "target": load_raw["label"][0]
}
x, y = mnist["data"], mnist["target"]
number = x[35000]
number_image = number.reshape(28, 28)

print(y[35000])
plt.imshow(number_image,
           cmap=plt.cm.binary,
           interpolation="nearest"
           )
plt.show()

print(x.shape)
