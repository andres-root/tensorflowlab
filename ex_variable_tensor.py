import tensorflow as tf

x = 10
y = 2
z = x/y - 1

x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.div(x, y), 1)

with tf.Session() as sess:
    output = sess.run(z)
    print(output)
