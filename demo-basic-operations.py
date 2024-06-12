import streamlit as st
st.title("Hello, dog!")
st.header("You need to learn some basic operations")
st.subheader("eg, Visual Studio Code")
st.text("It's not that hard")

st.markdown("this is an image: \n \
            ![](https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%B0%8F%E7%8B%97&step_word=&hs=0&pn=34&spn=0&di=7360350738658099201&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2746853834%2C2480630502&os=3002931247%2C196678379&simid=3391555202%2C539076385&adpicid=0&lpn=0&ln=1852&fr=&fmq=1718116177585_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fimg2.pconline.com.cn%2Fpconline%2F0706%2F07%2F1031072_070611dog38.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fuwfit5g_z%26e3Brv5gstgj_z%26e3Bv54_z%26e3BvgAzdH3Fw6ptvsj_stfpAzdH3Fnnm_z%26e3Bip4s&gsm=1e&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCwzLDIsMSw2LDQsNSw4LDcsOQ%3D%3D&lid=8531937896645145113)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Reading',
                'Writing',
                'Coding',
                'Traveling'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    