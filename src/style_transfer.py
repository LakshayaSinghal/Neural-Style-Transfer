from cost import *
from features import *



def neural_style_transfer(content_path, 
                       style_path,
                       num_iterations=1000,
                       alpha=1e4, 
                       beta=1,
                       learning_rate=5,
                       epsilon=1e-1): 
 

      
  model = get_submodel(full_vgg) 
  for layer in model.layers:
    layer.trainable = False
  

  # get style and content features of both image
  style_features, content_features = get_features(model, content_path, style_path)
  #calculate gram matrix of style image 
  style_features = [gram_matrix(style_feature) for style_feature in style_features]

    
    
    
  #initialize generated image
  gen_image = load_and_process_img(content_path)
  gen_image = tf.Variable(gen_image, dtype=tf.float32)

  #initialize optimizers
  optimizer =  tf.keras.optimizers.Adam(learning_rate=learning_rate, epsilon=epsilon)


  
  # Store our best result
  best_img,best_loss = None,float("inf")
    
  
  # 
  config = {
      'model': model,
      'gen_image': gen_image,
      'style_features': style_features,
      'content_features': content_features,
      'hyperparameters': (beta, alpha)
  }
  

  # required for deprocessing images
  norm_means = np.array([103.939, 116.779, 123.68])
  min_vals = -norm_means
  max_vals = 255 - norm_means   
  

  imgs = []
  for i in range(num_iterations):
    grads, all_loss = compute_grads(config)
    
    loss, style_loss, content_loss = all_loss
    
    optimizer.apply_gradients([(grads, gen_image)])
    
    
    clipped = tf.clip_by_value(gen_image, min_vals, max_vals)
    gen_image.assign(clipped)

    
    if loss < best_loss:
      best_loss = loss
      best_img = deprocess_img(gen_image.numpy())

    if i % 100== 0 or i==num_iterations:
      
      plot_img = gen_image.numpy()
      plot_img = deprocess_img(plot_img)
      imgs.append(plot_img)

      
      im = Image.fromarray(plot_img)
      im.save(f'res/iteration{i}.png')

        
      print(f'Iteration: {i}')        
      print(f'Total loss: {loss} style loss: {style_loss} content loss: {content_loss} ')

      
  return best_img
