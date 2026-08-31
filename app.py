import streamlit as st
from rembg import remove, new_session
from PIL import Image
import io

st.title("AI Background Remover")

@st.cache_resource
def load_model():
    return new_session("u2netp")

uploaded_file = st.file_uploader(
    "Upload the image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    input_image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.image(input_image, caption="Original")

        if st.button("Remove Background"):
            output_image = remove(input_image, session=load_model())

            with col2:
                st.image(output_image, caption="Result")

                buffer = io.BytesIO()
                output_image.save(buffer, format="PNG")

                st.download_button(
                    "Download Result",
                    buffer.getvalue(),
                    "background_removed.png",
                    "image/png"
                )
