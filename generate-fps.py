import tensorflow as tf

from model import DCGAN, visualize

with tf.Session() as sess:
    dcgan = DCGAN(
        sess,
        dataset_name='grayscale',
        input_fname_pattern='*.png',
        checkpoint_dir='checkpoint',
    )

    dcgan.load('checkpoint')
    visualize(sess, dcgan, dict(generate_test_images= 500, batch_size= 4, z_dim=1))
