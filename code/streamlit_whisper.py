import streamlit as st
import whisper
from pytube import YouTube

def main():
    st.title("Youtube to Text - Whiper new")
    menu = ["YouTube", "Audio File"]
    choice = st.sidebar.selectbox("Menu", menu)
    model = whisper.load_model("base")

    if choice == "YouTube":
        audio_file = None
        url = None
        # st.session_state.url_provided = False

        with st.form(key='youtube_form', clear_on_submit=True):
            url = st.text_input(label='Enter Youtube URL')
            submit_button = st.form_submit_button(label='Get Video')

        if submit_button:
            st.sidebar.success("Loading Video...")
            selected_video = YouTube(url)
            video_title = selected_video.title
            video_thumbnail = selected_video.thumbnail_url
            audio = selected_video.streams.filter(only_audio=True, file_extension='mp4').first()
            audio_file = 'captions.mp4'
            audio.download(filename=audio_file)
            st.sidebar.success("Video Loaded")
            st.image(video_thumbnail, caption=video_title)
            st.sidebar.success("Transcribing Audio")
            transcription = model.transcribe(audio_file)
            st.sidebar.success("Transcription Complete")
            st.markdown(transcription ["text"])
            # st.sidebar.header("Play Original Audio File")
            # st.sidebar.audio(audio_file)
    else:
        st.subheader("Audio file transcript using Whisper")
        audio_file = st.file_uploader("Upload Audio", type=["mp4", "mp3", "wav"])

        if st.sidebar.button("Transcribe Audio"):
            if audio_file is not None:
                st.sidebar.success("Transcribing Audio")
                transcription = model.transcribe(audio_file)
                st.sidebar.success("Transcription Complete")
                st.markdown(transcription ["text"])
                # st.sidebar.header("Play Original Audio File")
                # st.sidebar.audio(audio_file)
            else:
                st.sidebar.error("Upload a valida audio file")
                
    st.sidebar.header("Play Original Audio File")
    st.sidebar.audio(audio_file)

if __name__ == '__main__':
    main()

