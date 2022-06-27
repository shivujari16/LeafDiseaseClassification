import numpy as np
import tensorflow as tf
# Keras
import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO
#import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Define a flask app
#app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='cotton_Leaf_cnn.h5'

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
    st.title("Cotton")
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
            result = "Bacterial"
        else:
            result = "Healthy"
        
    #basepath = os.path.dirname(__file__)
    #file_path = os.path.join(basepath,secure_filename(image.name))
        
        if st.button("Predict"):
            st.success('{}'.format(result))
            if(preds==0):
                st.title('Cause:')
                st.markdown('Bacterial Blight, also called Angular Leaf Spot, is a disease caused by the bacterium, Xanthomonas citri pv. malvacearum')
                st.title('Symptom:')
                st.markdown('Bacterial Blight starts as small, water-soaked lesions (spots) on leaves and can be observed on seedlings as well as mature plants. Lesions progress into characteristic angular shapes when the leaf veins restrict the bacterial movement ')            
                st.title('Treatment:')
                st.markdown('Buy clean seed from a reputable source. If saving seed, do not collect seed from infected plants. Rotate vegetables so two or more years go by before planting any member of the squash family in the same location. Use drip irrigation instead of overhead sprinklers if possible. If watering by hand, water at the base of the plant where the vine meets the soil. Do not work in plants when leaves are wet. Remove and destroy infected fruit and vines at the end of the season in small gardens.')
            else:
                st.tille("Congratulation")
                st.markdown("Your plant is healthy")
    

if __name__ == '__main__':
    main()
