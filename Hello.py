import streamlit as st

def main():
    st.title("Waste Management Web Application")
    st.image('ecosentry.jpeg')
    st.markdown("Welcome to our Waste Management Web Application!")
    st.write("This application aims to automate waste segregation and improve waste management processes using machine learning and advanced technologies.")

    st.header("Project Overview")
    st.write("Our project focuses on automating waste segregation using machine learning techniques. By leveraging computer vision and advanced algorithms, we aim to classify waste materials as recyclable or non-recyclable at disposal points.")

    st.header("Key Features")
    st.write("1. Real-time waste segregation using YOLOv8 model.")
    st.write("2. Garbage detection for identifying waste accumulation.")
    st.write("3. City-wide heatmap generation based on garbage detection data.")
    st.write("4. Chatbot for user engagement and information dissemination.")

    st.header("Technologies Used")
    st.write("- YOLOv8 model trained with over 5000 pre-processed and augmented images.")
    st.write("- Flask backend for real-time processing of webcam feeds.")
    st.write("- SocketIO connection for frontend display.")
    st.write("- OpenAI's GPT 3.5 Turbo model for chatbot development.")

    st.header("Objective")
    st.write("Our main goals are to create precise recognition algorithms, ensure swift processing, and boost recycling rates while minimizing manual labor and environmental impact in waste management.")

    st.header("Next Steps")
    st.write("We are continuously working to enhance the capabilities of our application, improve waste segregation accuracy, and expand its deployment to further locations for broader impact.")

if __name__ == '__main__':
    main()


