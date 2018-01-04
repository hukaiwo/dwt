import tensorflow as tf
Hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))