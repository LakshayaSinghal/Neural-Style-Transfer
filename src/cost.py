from dependencies import *

#content loss
def get_content_cost(gen_content, target_content):
  return tf.reduce_mean(tf.square(gen_content - target_content))


#gram matrix for style loss
def gram_matrix(input_tensor):
  
  channels = int(input_tensor.shape[-1])
  a = tf.reshape(input_tensor, [-1, channels])
    
  n = tf.shape(a)[0]
  gram = tf.matmul(a,a,transpose_a=True)
    
  return gram / tf.cast(n, tf.float32)



#style cost
def get_style_cost(gen_style, target_style):

  
  height, width, channels = gen_style.get_shape().as_list()

  gen_style = gram_matrix(gen_style)
  
  return tf.reduce_mean(tf.square(gen_style - target_style)) / (4.) #* (channels ** 2) * (width * height) ** 2)


#compute total cost for backprop
def compute_cost(model, gen_image, style_features, content_features,hyperparameters,):

  beta, alpha = hyperparameters
    
    
  GI_features = model(gen_image)
  
  #extract style features of generated image
  style_features_GI = GI_features[:num_style_layers]
  #extract content features of generated image
  content_features_GI = GI_features[num_style_layers:]
  


  style_cost = 0
  content_cost = 0

  weight_per_style_layer = 1.0 / float(num_style_layers)
  
  #calculate style cost  
  for target_style, generated_style in zip(style_features, style_features_GI):
    style_cost += weight_per_style_layer * get_style_cost(generated_style[0], target_style)
    
    
  weight_per_content_layer = 1.0 / float(num_content_layers)
  #calculate content cost  
  for target_content, generated_content in zip(content_features, content_features_GI):
    content_cost += weight_per_content_layer* get_content_cost(generated_content[0], target_content)
  
  content_cost *= alpha
  style_cost *= beta


  cost = style_cost + content_cost
  return cost, style_cost, content_cost



#backprop
def compute_grads(config):
  with tf.GradientTape() as tape: 
    all_cost = compute_cost(**config)
  
  total_cost = all_cost[0]
  return tape.gradient(total_cost, config['gen_image']), all_cost
