import streamlit as st
import cv2
import tempfile

def webcam_control():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Create a temporary file to store the video
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    video_filename = temp_file.name

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

    # Streamlit components for webcam control
    start_button = st.button("Start Interview")
    stop_button = st.button("Stop Interview")
    video_placeholder = st.empty()

    recording = False

    while True:
        if start_button:
            recording = True
            start_button = False

        if stop_button:
            recording = False
            break

        if recording:
            ret, frame = cap.read()
            if ret:
                # Write the frame to the video file
                out.write(frame)
                # Display the frame in Streamlit
                video_placeholder.image(frame, channels="BGR")

    # Release everything when done
    cap.release()
    out.release()

    return video_filename

# Call the function in your Streamlit app
video_file = webcam_control()
st.write(f"Video saved as: {video_file}")