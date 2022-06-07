# Embedding layer (NOT REQUIRED)

class F2V(tf.keras.layers.Layer):
    
    def __init__(self, output_dim, dim):
        self.output_dim = output_dim
        super(F2V, self).__init__()
        
    def build(self, input_shape):

        #periodicity
        self.W = self.add_weight(name='W',
                      shape=(input_shape[-1], self.output_dim),
                      initializer='random_normal',
                      trainable=True)
        self.P = self.add_weight(name='P',
                      shape=(input_shape[1], self.output_dim),
                      initializer='random_normal',
                      trainable=True)
        #trend
        self.w = self.add_weight(name='w',
                      shape=(input_shape[1], 1),
                      initializer='random_normal',
                      trainable=True)
        self.p = self.add_weight(name='p',
                      shape=(input_shape[1], 1),
                      initializer='random_normal',
                      trainable=True)
        super(F2V, self).build(input_shape)   

    #def gaussian(self, x):
      #return K.exp(-K.pow(x, 2)) 
        
    def call(self, x):
        
        bias = int(self.w) * int(x) + int(self.p)
        dotpro = K.dot(int(x), int(self.W)) + int(self.P)
        em_wts = K.exp(-K.pow(float(dotpro), 2))                 # frequency domain plots maintain a Gaussian function
        em_wts = int(em_wts)
        return K.concatenate([em_wts, bias], -1)
        #ret = K.reshape(ret, (-1, x.shape[1]*(self.ks + 1)))
        #return ret



# Attention Layer (Bahdanau et al., 2014)

class attention1(tf.keras.layers.Layer):
    def __init__(self):
        super(attention1, self).__init__(trainable=True)
    
    def build(self, input_shape):
        #self.num_dim = input_shape[-1]
        #self.sample = input_shape[-2]
        num_units = 1

        self.w = self.add_weight(shape=(input_shape[-1],1), initializer="random_normal", trainable=True)
        self.b = self.add_weight(shape=(input_shape[1],1), initializer="zeros", trainable=True)
        super(attention1, self).build(input_shape)
    
    def call(self, x):

        # Alignment scores       
        e = K.tanh(K.dot(x, self.w) + self.b)
        #e = K.squeeze(e, axis=-1)        
        # Compute softmaxed weights
        attn_weights = K.softmax(e, axis=1)
        # Compute context vector
        context = x * attn_weights
        return e, attn_weights, K.sum(context, axis=1)