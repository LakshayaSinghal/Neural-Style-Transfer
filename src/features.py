from load import *


#load pretrained vgg19
full_vgg = tf.keras.applications.vgg19.VGG19(include_top = False,
                                             weights = 'imagenet')

#we're not training vgg
full_vgg.trainable = False


#define the submodel through which we'll pass our images
def get_submodel(vgg):
    
    outputs = [vgg.get_layer(layer).output for layer in layer_names]

    
    model = tf.keras.Model(vgg.input, outputs)
    return model



#get the output of content and style images after they're passed through the submodel
def get_features(model, content_path, style_path):
  
  # Load our images in 
  content_image = load_and_process_img(content_path)
  style_image = load_and_process_img(style_path)
  
  # batch compute content and style features
  style_outputs = model(style_image)
  content_outputs = model(content_image)
  
  
  # Get the style and content feature representations from our model  

  style_features = [style_layer[0] for style_layer in style_outputs[:num_style_layers]]
  content_features = [content_layer[0] for content_layer in content_outputs[num_style_layers:]]


  return style_features, content_features
