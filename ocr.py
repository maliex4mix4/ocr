import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing
import requests

#title
st.title("OCR - Extract Text from Images")

#subtitle
st.markdown("## Optical Character Recognition")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


# @st.cache
# def load_model(): 
#     reader = ocr.Reader(['en'],model_storage_directory='.')
#     return reader 

# reader = load_model() #load model

if image is not None:

    # input_image = Image.open(image) #read image
    # st.image(input_image) #display image

    # with st.spinner("Working! "):
        

    #     result = reader.readtext(np.array(input_image))

    #     result_text = [] #empty list for results


    #     for text in result:
    #         result_text.append(text[1])

        # st.write(result_text)

    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    files = {'image': image}
    r = requests.post(api_url, files=files)

    st.write(r.json())
        
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Malik Diyaolu")





