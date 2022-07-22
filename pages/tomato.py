from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
# Keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import streamlit as st

# Flask utils
#from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
from PIL import Image, ImageOps
from io import BytesIO
#import cv2


# Define a flask app
#app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='tomato_Leaf_cnn.h5'

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
    st.title("Tomato")
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
            result = "bacteriaol spot"
        elif(preds==1):
            result = "early blight"
        elif(preds==2):
            result = "late blight"
        elif(preds==3):
            result = "leaf mold"
        elif(preds==4):
            result = "septoria"
        elif(preds==5):
            result = "spider_mites"
        elif(preds==6):
            result = "target spot"
        elif(preds==7):
            result = "yellow leaf curl"
        elif(preds==8):
            result = "mosaic virus"
        else:
            result = "healthy"
        
    #basepath = os.path.dirname(__file__)
    #file_path = os.path.join(basepath,secure_filename(image.name))
        if st.button("Predict"):
            st.success('{}'.format(result))
            if(preds==0):
                st.title("Cause:")
                st.markdown("Bacterial spot is caused by four species of Xanthomonas and occurs worldwide wherever tomatoes are grown. Bacterial spot causes leaf and fruit spots, which leads to defoliation, sun-scalded fruit, and yield loss.")
                st.title("Symptom:")
                st.markdown("On tomato, leaf lesions are initially circular and water-soaked and may be surrounded by a faint yellow halo. In general, spots are dark brown to black and circular on leaves and stems. Spots rarely develop to more than 3 mm in diameter. ")
                st.title("Treatment:")
                st.markdown("The most effective management strategy is the use of pathogen-free certified seeds and disease-free transplants to prevent the introduction of the pathogen into greenhouses and field production areas. In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet. Eliminate solanaceous weeds in and around tomato and pepper production areas. Do not spray, tie, harvest, or handle wet plants as that can spread the disease.")
            elif(preds==1):
                st.title("Cause:")
                st.markdown("Early blight is a fungal disease caused by Alternaria solani. It can occur at any time during the growing season. High humidity and temperatures above 75°F cause it to spread rapidly")
                st.title("Symptom:")
                st.markdown("The first sign that your plants are infected with early blight is usually the appearance of dark brown spots on the lower leaves. This disease usually progresses from the bottom of the plant to the top")
                st.title("Treatment:")
                st.markdown("Keep the potato plants healthy and stress free by providing adequate nutrition and sufficient irrigation, especially later in the growing season after flowering when plants are most susceptible to the disease.Burn or bag infected plant parts. Do NOT compost")
            elif(preds==2):
                st.title("Cause:")
                st.markdown("Late blight is caused by the fungal-like oomycete pathogen Phytophthora infestans")
                st.title("Symptom:")
                st.markdown("he first symptoms of late blight in the field are small, light to dark green, circular to irregular-shaped water-soaked spots. These lesions usually appear first on the lower leaves. Lesions often begin to develop near the leaf tips or edges, where dew is retained the longest.")
                st.title("Treatment:")
                st.markdown("1. Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation.")
                st.markdown("2. Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day — avoid overhead irrigation.")
                st.markdown("3. Destroy all tomato and potato debris after harvest ")
            elif(preds==3):
                st.title("Cause:")
                st.markdown("Leaf mold of tomato is caused by pathogen Passalora fulva. It is found throughout the world, predominantly on tomatoes grown where the relative humidity is high, particularly in plastic greenhouses.")
                st.title("Symptom:")
                st.markdown("Symptoms start as pale green to yellowish spots on upper leaf surfaces that turn a bright yellow. The spots merge as the disease progresses and the foliage then dies. Infected leaves curl, wither, and often drop from the plant.")
                st.title("Treatment:")
                st.markdown("The pathogen P. fulfa can survive on infected plant debris or in the soil, although the initial source of the disease is often infected seed. The disease is spread by rain and wind, on tools and clothing, and via insect activity. High relative humidity (greater that 85%) combined with high temperatures encourages the spread of the disease. With that in mind, if growing tomatoes in a greenhouse, maintain night temps higher than outside temperatures.")
            elif(preds==4):
                st.title("Cause:")
                st.markdown("Septoria is caused by a fungus, Septoria lycopersici, which overwinters in old tomato debris and on wild Solanaceous plants. The fungus is spread by wind and rain, and flourishes in temperatures of 60 to 80 degrees F. (16-27 C.).")
                st.title("Treatment:")
                st.markdown("Treating septoria leaf spot disease after it appears is achieved with fungicides. The chemicals need to be applied on a seven to ten day schedule to be effective. Spraying begins after blossom drop when the first fruits are visible. The most commonly used chemicals are maneb and chlorothalonil. Potassium bicarbonate, ziram, and copper products are a few other sprays useful against the fungus")
            elif(preds==5):
                st.title("Cause:")
                st.markdown("As the summer heat continues, it is common to see spider mites on commercial and home-grown tomatoes. Heat, drought, water stress, the presence of a large number of weeds, and incorrect use of insecticides can lead to high buildup of mites on tomatoes")
                st.title("Symptom:")
                st.markdown("Spider mite feeding can cause numerous yellow or white tiny granulated spots on tomato leaves. The infestation mostly occurs under hot and dry conditions. Spider mites are very tiny and can be seen on underside of the leaves. During heavy infestation spider mites can be seen all over the plant.")
                st.title("Treatment:")
                st.markdown("Avoid continuous cropping of tomato and related plants which makes it difficult to control red spider mites, since they always have a plant to feed on. Remove remains (residues) from a previous crop and destroy before planting new crop. Use fungicides with sulphur, since they reduce populations of mites. You can also use miticides which are specific for mites e.g. Dynamec (active ingredient abamectin), Oberon (spiromesifen) or Omite (propargite).")
            elif(preds==6):
                st.title("Cause:")
                st.markdown("Target spot of tomato is caused by the fungal pathogen Corynespora cassiicola.1 The disease occurs on field-grown tomatoes in tropical and subtropical regions of the world.")
                st.title("Symptom:")
                st.markdown("The initial foliar symptoms are pinpoint-sized, water-soaked spots on the upper leaf surface. The spots develop into small, necrotic lesions that have light brown centers and dark margins. These symptoms may be confused with symptoms of bacterial spot.The lesions increase in size, become circular with gray to pale brown centers. As the lesions enlarge, they can develop darker concentric circles, hence, the name target spot ")
                st.title("Treatment:")
                st.markdown("Cultural practices for target spot management include improving airflow through the canopy by wider plant spacing and avoiding over-fertilizing with nitrogen, which can cause overly lush canopy formation. Products containing chlorothalonil, mancozeb, and copper oxychloride have been shown to provide good control of target spot in research trials. The strobilurin fungicides azoxystrobin and pyraclostrobin, the fungicide boscalid, and the systemic acquired resistance (SAR) elicitor acibenzolar-S-methyl have also been shown to provide good control of target spot.")
            elif(preds==7):
                st.title("Cause:")
                st.markdown("The diseae caused by tomato yellow leaf curl virus(TYLCV). TYLCV is transmitted by adult silverleaf whiteflies and can spread rapidly")
                st.title("Symptom:")
                st.markdown("Typical symptoms for this disease in tomato are yellow (chlorotic) leaf edges, upward leaf cupping, leaf mottling, reduced leaf size, and flower drop")
                st.title("Treatment:")
                st.markdown("Use a neonicotinoid insecticide, such as dinotefuran (Venom) imidacloprid (AdmirePro, Alias, Nuprid, Widow, and others) or thiamethoxam (Platinum), as a soil application or through the drip irrigation system at transplanting of tomatoes or peppers")
            elif(preds==8):
                st.title("Cause:")
                st.markdown("the disease caused by Mosaic virus")
                st.title("Symptom:")
                st.markdown("1. TYellow, white or green stripes/ streaks/ spots on foliage")
                st.markdown("2. Wrinkled, curled, or small leaves")
                st.title("Treatment:")
                st.markdown("1. The virus can be spread through human activity, tools, and equipment. Frequently wash your hands and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4 parts water) to reduce the risk of contamination.")
                st.markdown("2. Avoid working in the garden during damp conditions (viruses are easily spread when plants are wet")
                st.markdown("3. Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.")
                st.markdown("4. Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost.")
            else:
                st.title("Congratulation")
                st.markdown("Your plant is healthy")
    

if __name__ == '__main__':
    main()
