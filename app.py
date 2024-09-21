import streamlit as st
from video_processor import capture_video
from audio_processor import extract_audio
from transcription import transcribe_audio
from analysis import topic_mastery, communication, non_verbal, response_quality, overall_performance
from utils import report_generator, data_manager

def main():
    st.title("Interview Assessment App")

    if st.button("Start Interview"):
        video_file = capture_video()
        audio_file = extract_audio(video_file)
        transcript = transcribe_audio(audio_file)

        # Perform analyses
        topic_insights = topic_mastery.analyze(transcript)
        communication_insights = communication.analyze(audio_file, transcript)
        non_verbal_insights = non_verbal.analyze(video_file)
        response_insights = response_quality.analyze(transcript)

        # Generate overall performance and feedback
        overall_insights = overall_performance.analyze(
            topic_insights, communication_insights, non_verbal_insights, response_insights
        )

        # Generate and display report
        report = report_generator.create_report(
            topic_insights, communication_insights, non_verbal_insights, 
            response_insights, overall_insights
        )
        st.write(report)

if __name__ == "__main__":
    main()