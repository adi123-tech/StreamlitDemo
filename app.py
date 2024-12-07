import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # You can process the video frame here if needed
        # For example, converting to grayscale or applying filters
        return frame

def main():
    st.title("WebRTC Live Stream with Streamlit")

    st.markdown("""
    This app demonstrates live streaming using WebRTC. 
    The video stream is captured from your camera and displayed in real-time.
    """)

    # WebRTC streamer
    webrtc_streamer(
        key="example",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},  # Enable video and disable audio
    )

    st.sidebar.title("Settings")
    st.sidebar.markdown("""
    - Use the above live stream for demo purposes.
    - Add additional configurations or processing as needed.
    """)

if __name__ == "__main__":
    main()
