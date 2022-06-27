import numpy as np
import tensorflow as tf

import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO
#import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Define a flask app
#app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='pepper_bell_Leaf_cnn.h5'

# Load your trained model
model = load_model(MODEL_PATH)




#def model_predict(img_path, model):
#    print(img_path)
##    img = load_img(img_path,target_size=(256,256))
#    x = img_to_array(img)
#    img = np.expand_dims(x,axis=0)
#    pred = model.predict(img)
#    preds = np.argmax(pred,axis=1)
#    if(preds==0):
#        preds = "bacterial"
#    else:
#        preds = "healthy"
#        
#    return preds


#@app.route('/predict', methods=['GET','POST'])
#def upload():
#   if request.method == 'POST':
#        f = request.files['file']
#       # print(f)
#       basepath = os.path.dirname(__file__)
#        #print(basepath)
#        file_path = os.path.join(basepath,secure_filename(f.filename))
#        #print(file_path)
#        #f.save(file_path)
#        
 #       preds = model_predict(file_path, model)
 #       result=preds
 #           
 #       return result
 #   return "hello"

def main():
    st.title("Pepper bell")
    file = st.file_uploader("Choose a file")
    if file is not None:
        byte = file.read()
        image = Image.open(BytesIO(byte))
        image = image.convert("RGB")
        image = image.resize((256,256))
        st.image(image)
        image = img_to_array(image)
        image = np.expand_dims(image,axis=0)
        pred = model.predict(image)
        preds = np.argmax(pred,axis=1)
        result=""
        if(preds==0):
            result = "bacterial"
        else:
            result = "healthy"
        
    #basepath = os.path.dirname(__file__)
    #file_path = os.path.join(basepath,secure_filename(image.name))
        
        if st.button("Predict"):
            st.success('{}'.format(result))
            if(preds==0):
                st.title('Cause:')
                st.markdown('The bacterium Xanthomonas campestris pv. vesicatoria causes bacterial leaf spot. It thrives in areas with hot summers and frequent rainfall. The bacterium is spread by plant debris in the soil and through infected seeds.')
                st.title('Symptom:')
                st.markdown('Bacterial leaf spot causes lesions on the leaves that look as though they are soaked with water. These lesions normally begin on the lower leaves. As the disease progresses, it leaves a dark, purple-brown spot with a light brown center. Bacterial leaf spot on peppers causes spotting and raised cracks in the fruit. The cracks provide an opening for other disease pathogens')            
                st.title('Treatment:')
                st.markdown('Of course, once the symptoms of bacterial leaf spot begin to appear on your pepper plants, it’s too late to save them. However, if you take precautions before planting next season, you’ll have a better chance of preventing peppery leaf spot problems in the future. Crop rotation can help prevent bacterial leaf spot. Do not plant peppers or tomatoes in a location where either of these crops has been grown in the past four or five years. At the end of the season, remove all crop debris from the garden and destroy it')
            else:
                st.tille("Congratulation")
                st.markdown("Your plant is healthy")
    

if __name__ == '__main__':
    main()
