# PINN for Burgers' equation
# coded by St.Watermelon

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np

class Burgers(Model):

    def __init__(self):
        super(Burgers, self).__init__()

        self.h1 = Dense(20, activation='tanh')
        self.h2 = Dense(20, activation='tanh')
        self.h3 = Dense(20, activation='tanh')
        self.h4 = Dense(20, activation='tanh')
        self.h5 = Dense(20, activation='tanh')
        self.h6 = Dense(20, activation='tanh')
        self.u = Dense(1, activation='linear')


    def call(self, state):
        x = self.h1(state)
        x = self.h2(x)
        x = self.h3(x)
        x = self.h4(x)
        x = self.h5(x)
        x = self.h6(x)
        out = self.u(x)
        return out


class Pinn(object):

    def __init__(self):

        self.lr = 0.001
        self.opt = Adam(self.lr)

        self.burgers = Burgers()
        self.burgers.build(input_shape=(None, 2))

    def physics_net(self, xt):
        x = xt[:, 0:1]
        t = xt[:, 1:2]

        with tf.GradientTape(persistent=True) as tape:
            tape.watch(t)
            tape.watch(x)
            xt_t = tf.concat([x,t], axis=1)
            u = self.burgers(xt_t)
            u_x = tape.gradient(u, x)
        u_xx = tape.gradient(u_x, x)
        u_t = tape.gradient(u, t)
        del tape

        return u_t + u*u_x - (0.01/np.pi)*u_xx


    def save_weights(self, path):
        self.burgers.save_weights(path + 'burgers.h5')


    def load_weights(self, path):
        self.burgers.load_weights(path + 'burgers.h5')


    def learn(self, xt_col, xt_bnd, tu_bnd):
        with tf.GradientTape() as tape:
            f = self.physics_net(xt_col)
            loss_col = tf.reduce_mean(tf.square(f))

            tu_bnd_hat = self.burgers(xt_bnd)
            loss_bnd = tf.reduce_mean(tf.square(tu_bnd_hat-tu_bnd))

            loss = loss_col + loss_bnd

        grads = tape.gradient(loss, self.burgers.trainable_variables)
        self.opt.apply_gradients(zip(grads, self.burgers.trainable_variables))

        return loss


    def predict(self, xt):
        tu = self.burgers(xt)
        return tu


    def train(self, max_num):

        # initial and boundary condition
        x_data = np.linspace(-1.0, 1.0, 500)
        t_data = np.linspace(0.0, 1.0, 500)
        xt_bnd_data = []
        tu_bnd_data = []

        for x in x_data:
            xt_bnd_data.append([x, 0])
            tu_bnd_data.append([-np.sin(np.pi * x)])

        for t in t_data:
            xt_bnd_data.append([1, t])
            tu_bnd_data.append([0])
            xt_bnd_data.append([-1, t])
            tu_bnd_data.append([0])

        xt_bnd_data = np.array(xt_bnd_data)
        tu_bnd_data = np.array(tu_bnd_data)

        # collocation point
        t_col_data = np.random.uniform(0, 1, [20000, 1])
        x_col_data = np.random.uniform(-1, 1, [20000, 1])
        xt_col_data = np.concatenate([x_col_data, t_col_data], axis=1)
        xt_col_data = np.concatenate((xt_col_data, xt_bnd_data), axis=0)

        train_loss_history = []

        for iter in range(int(max_num)):

            loss = self.learn(tf.convert_to_tensor(xt_col_data, dtype=tf.float32),
                       tf.convert_to_tensor(xt_bnd_data, dtype=tf.float32),
                       tf.convert_to_tensor(tu_bnd_data, dtype=tf.float32))

            train_loss_history.append([iter, loss.numpy()])

            print('iter=', iter, ', loss=', loss.numpy())

        self.save_weights("./save_weights/")

        np.savetxt('./save_weights/loss.txt', train_loss_history)
        train_loss_history = np.array(train_loss_history)

        plt.plot(train_loss_history[:, 0], train_loss_history[:, 1])
        plt.yscale("log")
        plt.show()


def main():

    max_num = 3000
    agent = Pinn()

    agent.train(max_num)


if __name__=="__main__":
    main()
