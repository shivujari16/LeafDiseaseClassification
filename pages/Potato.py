import numpy as np
import tensorflow as tf
# Keras
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
#from gevent.pywsgi import WSGIServer
from PIL import Image, ImageOps
from io import BytesIO
#import cv2


# Define a flask app
#app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='potato_Leaf_cnn.h5'

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
    
    st.title("Potato")
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
            result = "Early Blight"
        elif(preds==1):
            result = "Late Blight"
        else:
            result = "Healthy"
        
    #basepath = os.path.dirname(__file__)
    #file_path = os.path.join(basepath,secure_filename(image.name))
        if st.button("Predict"):
            st.success('{}'.format(result))
            if(preds==0):
                st.title("Cause:")
                st.markdown("The disease is caused by the the fungus Alternaria saloni. Potatoes become infected with early blight when foliage has become excessively wet due to rain, fog, dew, or irrigation.")
                st.title("Symptom:")
                st.markdown("Early blight rarely affects young plants. Symptoms first occur on the lower or oldest leaves of the plant. Dark, brown spots appear on this older foliage and, as the disease progresses, enlarge, taking on an angular shape")
                st.title("Treatment:")
                st.markdown("Keep the potato plants healthy and stress free by providing adequate nutrition and sufficient irrigation, especially later in the growing season after flowering when plants are most susceptible to the disease.Burn or bag infected plant parts. Do NOT compost")
            elif(preds==1):
                st.title("Cause:")
                st.markdown("Late blight is caused by the fungal-like oomycete pathogen Phytophthora infestans")
                st.title("Symptom:")
                st.markdown("he first symptoms of late blight in the field are small, light to dark green, circular to irregular-shaped water-soaked spots. These lesions usually appear first on the lower leaves. Lesions often begin to develop near the leaf tips or edges, where dew is retained the longest.")
                st.title("Treatment:")
                st.markdown("1. Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation.")
                st.markdown("2. Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day — avoid overhead irrigation.")
                st.markdown("3. Destroy all tomato and potato debris after harvest ")
            else:
                st.tille("Congratulation")
                st.markdown("Your plant is healthy")
            
    

if __name__ == '__main__':
    main()
