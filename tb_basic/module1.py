import tensorflow as tf

a = tf.constant(3.0)
b = tf.constant(5.0)
c = a * b
# tensorboard 에 point 라는 이름으로 표시됨

sum = tf.summary.scalar('point',c)
merged = tf.summary.merge_all()

# with tf.Session() as sess:
#    writer = tf.summary.FileWriter('')
