import streamlit as st
# st.title("welcome to my app!!")
# name= st.text_input("Enter your name")
# age=st.number_input("Enter yiur age !!")

# if st.button("Submit"):
#     st.write(f"hello {name} and your age is {age}")
    

st.title("My Streamlit App")  # Large title
st.header("This is a header")  # Section header
st.subheader("This is a subheader")  # Subsection
st.text("This is some plain text")  # Plain text
st.markdown("<h1>Markdown Support</h1>",unsafe_allow_html=True)  #
st.markdown("<marquee>new</marquee>",unsafe_allow_html=True) 
st.markdown("🔥 :smile: :rocket:")
st.markdown('<span style="color:red">This is red text</span>', unsafe_allow_html=True)
st.image("./iMG/th.jpg")
st.radio('Pick tour gender',options=['male','female'])

st.selectbox("Select city",options=['Delhi','Kolkata','Chandigarh'])