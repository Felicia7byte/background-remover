# background-remover
An AI-powered image background removal application built with Python and Streamlit using rembg and the pre-trained U²-NetP model.
# Features
- Upload JPG, JPEG, or PNG images
- Automatically remove image backgrounds
- Preview the original and processed images
- Download the result as a transparent PNG
# Tech Stack
Python, Streamlit, rembg, U²-NetP, Pillow
# How It Works
Upload Image -> U²-NetP Model -> Foreground Segmentation -> Background Removal -> Transparent PNG

The application uses the rembg library with the pre-trained U²-NetP model to separate the foreground from the background. The background is then removed and the processed image is returned as a PNG.
# Model
U²-NetP
# Live Demo
https://background-remover-test.streamlit.app/
