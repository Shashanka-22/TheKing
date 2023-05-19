from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#from streamlit_lottie from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#from streamlit_lottie import st_lottie1
import streamlit.components.v1 as components

st.set_page_config(page_title="Shashanka Anand Naik_1RN22EC113", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_BhbCTg.json")
lottie_coding1 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_q5pzdjc7.json")
lottie_coding2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_in4cufsz.json")
img_contact_from = Image.open("images/sha3.png")
img_lottie_animation = Image.open("images/sha1.png")
img_poster = Image.open("images/poster.png")
with st.container():
    st.subheader("Hi, I am Shashanka Anand Naik :wave:")
    st.write("Website for Environmetal Day")
    #st.title("Environmental Day")
    #left_column, right_column = st.columns(2)
    #with left_column:
    st.write('<span style="font-size:150px;">Environmetal Day</span>', unsafe_allow_html=True)
    #with right_column:
        #st_lottie(lottie_coding, height=300, key="coding")

def set_background_image(image_path):
    image = Image.open(image_path)
    return image

st.markdown(
    """
    <style>
    body {
        background-image: url("https://www.freepik.com/free-vector/hand-painted-watercolor-world-environment-day-illustration_13817379.htm#query=world%20environment%20day&position=1&from_view=keyword&track=ais");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("About Environmetal Day")
        st.write("World Environment Day, celebrated annually on June 5th, is a significant global event that promotes environmental awareness and encourages positive actions to protect and preserve the environment. Established by the United Nations in 1972, World Environment Day serves as a platform to address pressing environmental issues and mobilize individuals, communities, governments, and organizations worldwide to take action.Each year, World Environment Day focuses on a specific theme that highlights a particular environmental concern. The theme aims to raise awareness, promote sustainable practices, and drive meaningful change. It serves as an opportunity for governments, NGOs, and individuals to come together, organize activities, and engage in initiatives that contribute to a healthier and more sustainable planet.")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    st.write("---")
    st.header("Did you know ??")
    images_column, text_column = st.columns((3,2))
    with images_column:
        st.image(img_contact_from)
    with text_column:
        st.image(img_lottie_animation)
    #images_column, text_column = st.columns((1, 2))
    #with images_column:
       # st.image(img_lottie_animation)
    #with text_column:
        #st.subheader("shashank")
with st.container():
    st.write("---")
    st.header("Event poster:")
    images_column, text_column = st.columns((10,10))
    with text_column:
        st_lottie(lottie_coding1, height=700, key="coding1")
    with images_column:
        st.image(img_poster)
with st.container():
    st.write("---")
    st.header("Register here to join with us")
    contact_form ="""
    <form action="https://formsubmit.co/naikshashank2210@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="text" Phone number="Phone number" placeholder="Phone number" required>
     <input type="text" Age="Age" placeholder="Your age" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message about Environmental Day" required></textarea>
     <button type="submit">Submit</button>
</form>
"""
    left_column, right_column = st.columns((2,2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding2, height=600, key="coding2")


    
