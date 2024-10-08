### Apple Silicon ML Environment Setup
#### TODO: properly integrate this and include screenshots when I have time

Note: the Internet shows that even in the last couple years this process has changed. Mileage may vary.

General Steps:

1. Install Homebrew: $ /bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install XCode Tools: $ xcode-select --install

3. Install miniforge: https://github.com/conda-forge/miniforge

4. Install Conda: https://www.anaconda.com/download

5. Install TensorFlow (very important): https://developer.apple.com/metal/tensorflow-plugin/

   From the Apple instructions:

   a. Create and initialize a virtual environment:
   ``` bash
   conda create -n <env_name> python=3.10
   conda activate <env_name>
   ```
   b. Install TensorFlow (follow Apple instructions for GPU access)
   ``` bash
   python -m pip install -U pip
   pip install tensorflow tensorflow-metal
   ```

The following script can be used to test the deployment of TensorFlow and ensure the GPU is being used.

``` python
import tensorflow as tf

# identify TensorFlow version
print(f"TensorFlow version: {tf.__version__}\n")

# identify GPU(s)
gpus = tf.config.list_physical_devices("GPU")
if gpus:
	for gpu in gpus:
		print(f"GPU detected: {gpu}\n")
	print("")

# train a model to ensure everything is working and benchmark
cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()
model = tf.keras.applications.ResNet50(include_top=True,weights=None,input_shape=(32, 32, 3),classes=100,)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64)
```

Note: this script isn't unique to Apple Silicon and should probably be put into a dedicated file and referenced.

References:
* https://medium.com/@iamkamleshrangi/supercharge-your-macbook-pro-with-gpu-setting-up-tensorflow-on-m3-m3-pro-and-m3-max-bbc4a44bcc82
* https://medium.com/@sriram0ku/setting-up-apple-silicon-for-machine-learning-8fd901549d8d
