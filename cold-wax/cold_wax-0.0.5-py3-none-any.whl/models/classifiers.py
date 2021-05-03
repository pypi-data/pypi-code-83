import tensorflow as tf

class PatchClassifier(tf.keras.Model):
    def __init__(self, n_classes, batch_size, input_shape, max_pool=False):
        super().__init__()
        input_tensor = tf.keras.layers.Input(shape=input_shape, batch_size=batch_size)
        self.backbone = tf.keras.applications.ResNet50(include_top=False,
                                                       weights='imagenet',
                                                       input_tensor=input_tensor,
                                                       pooling=None)
        if max_pool:
            self.max_pool = tf.keras.layers.MaxPooling2D(pool_size=(1, 1), strides=None)
        else:
            max_pool = None
        self.flatten = tf.keras.layers.Flatten()
        self.dropout = tf.keras.layers.Dropout(0.5)
        self.dense = tf.keras.layers.Dense(units=n_classes, activation='softmax')

    def call(self, inputs, training=False):
        x = self.backbone(inputs)
        if self.max_pool:
            x = self.max_pool(x)
        x = self.flatten(x)
        if training:
            x = self.dropout(x)
        return self.dense(x)

