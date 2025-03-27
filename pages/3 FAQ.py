import streamlit as st
st.set_page_config(layout="wide")
st.html(
    """
<style>
.st-emotion-cache-9s49fs, .st-emotion-cache-a6n1w7 {
    color: #fad07d !important;
}
</style>
"""
)
st.sidebar.image("swara.png")

def main():
    st.title("FAQ - Carnatic Music Ragam Detection")
    st.write("Welcome to the FAQ section for our ragam detection tool. Here, we provide answers to common questions to help you get the most out of this tool.")

    with st.expander("How does the ragam detection work?"):
        st.write("""
            Our tool uses advanced audio analysis to detect ragas in Carnatic music. It listens to the audio file you upload, identifies the frequency patterns, 
            and compares them to a large database of known ragas. By analyzing the sequence of notes and how they are expressed (e.g., the gamakas or ornamentations), 
            it determines which raga the audio most closely matches. The tool works by recognizing key features of a raga, such as its scale, phrasing, and the emotional quality it conveys.
        """)

    with st.expander("What types of audio files are supported?"):
        st.write("""
            Our tool supports three common audio formats: MP3, WAV, and FLAC. MP3 is widely used for its smaller file size, but WAV and FLAC provide higher-quality, 
            uncompressed audio. WAV files are ideal for those who want pure, unaltered sound, and FLAC files, while compressed, still retain lossless quality, which is great for 
            preserving every detail of the performance. No matter which format you choose, the tool can process them effectively.
        """)

    with st.expander("Is the detection 100% accurate?"):
        st.write("""
            While the detection tool is highly accurate, it's important to note that no system is perfect. The accuracy can be influenced by several factors:
            - **Audio Quality**: If the recording has poor quality or distortion, it can affect the detection.
            - **Background Noise**: If there’s too much noise, like other sounds or instruments, the tool might struggle to isolate the raga accurately.
            - **Vocal Clarity**: If the singing is not clear or off-pitch, it can lead to a less accurate result.
            Despite these challenges, the tool generally performs well in detecting ragas from clear, well-recorded performances.
        """)

    with st.expander("Can I use instrumental music for ragam detection?"):
        st.write("""
            Yes, you can upload instrumental music for ragam detection, but vocal music tends to yield more accurate results. The reason is that vocals clearly emphasize the swaras (notes),
            making it easier for the tool to identify the raga. In instrumental music, various instruments can sometimes blend the notes together, which may make the raga identification a bit more complex. 
            However, if the instrumental performance follows a clear raga structure, the tool can still detect the raga with good accuracy.
        """)

    with st.expander("How long does the detection process take?"):
        st.write("""
            The detection process usually takes just a few seconds to a minute, depending on the file size and the complexity of the music. If the file is large or has many instruments, it may take a little longer. 
            However, the tool is optimized to handle most audio files efficiently, and you should generally get results quickly. If the server is particularly busy, there may be slight delays, but we aim to keep the wait time minimal.
        """)

    with st.expander("Do I need an internet connection to use this tool?"):
        st.write("""
            Yes, an internet connection is required because the tool operates on cloud servers. Once you upload your audio file, it gets processed remotely, which allows the system to do the heavy lifting. 
            This means you don’t need a powerful computer to run the tool – just an internet connection to access the cloud-based system and get your results.
        """)

    with st.expander("Can I get notations for the detected ragam?"):
        st.write("""
            Yes! After the raga is detected, we provide notations for popular compositions in that raga. These notations are available for some of the well-known pieces composed by masters like 
            Tyagaraja, Muthuswami Dikshitar, and others. Notations are typically provided in both traditional Carnatic notation and western staff notation, 
            so you can choose the format that’s most comfortable for you. These notations will help you understand how the raga is traditionally performed and give you a solid foundation to practice.
        """)

    with st.expander("Who can use this tool?"):
        st.write("""
            This tool is for anyone interested in Carnatic music, whether you're a beginner or an experienced musician. It’s useful for students learning ragas, musicians looking to identify ragas 
            in recordings, or simply music enthusiasts curious about the vast world of Carnatic music. It can also be helpful for teachers and researchers who want to explore ragas more deeply.
            Whether you're practicing or just exploring, this tool can enhance your learning and help you engage with Carnatic music in a new way.
        """)
    st.write("\n## General Carnatic Music FAQs")

    with st.expander("What is Carnatic music?"):
        st.write("""
            Carnatic music is a classical music tradition from South India. It’s known for its deep emotional expressiveness and its emphasis on melody (ragas) and rhythm (talas). 
            The music is centered around improvisation, with compositions often built upon a raga's structure. This allows for a lot of creativity while still adhering to the traditional framework. 
            Carnatic music is both devotional and artistic, with many compositions praising deities or expressing spiritual ideas. The tradition is centuries-old and remains an integral part of Indian culture.
        """)

    with st.expander("What are the basic elements of Carnatic music?"):
        st.write("""
            Carnatic music is built on three fundamental elements:
            - **Sruti**: The pitch, which serves as the foundation for the music.
            - **Raga**: The melodic framework that defines the mood and structure of the piece.
            - **Tala**: The rhythmic cycle, which provides a framework for the performance.
            Together, these elements combine to form a structured yet flexible musical system where the performer can express creativity within a set framework.
        """)

    with st.expander("What is a Ragam?"):
        st.write("""
            A raga is a melodic structure that forms the basis of a Carnatic music composition. It is more than just a scale – it includes specific notes (called swaras) arranged in a particular order, 
            along with unique rules for how those notes should be used and connected. Each raga has its own emotional flavor, and the performer can improvise within this framework to convey a specific mood or feeling.
            Some ragas evoke joy, others sorrow, and still others devotion or serenity. The variety in ragas is what makes Carnatic music so rich and expressive.
        """)

    with st.expander("What is a Kriti?"):
        st.write("""
            A Kriti is a form of structured composition in Carnatic music. It typically consists of three parts: 
            - **Pallavi**: The opening section, which introduces the main theme.
            - **Anupallavi**: The second section, which develops the theme further.
            - **Charanam**: The concluding section, which brings the composition to a close.
            Kritis are known for their lyrical beauty and often express devotion, spiritual themes, or personal emotions. They are a central part of Carnatic music and serve as vehicles for both structured performance and improvisation.
        """)

    with st.expander("Who are some famous Carnatic musicians?"):
        st.write("""
            Some of the most revered figures in Carnatic music include:
            - **Tyagaraja**: A prolific composer whose works form the cornerstone of Carnatic music.
            - **Muthuswami Dikshitar**: Known for his intricate compositions and contribution to the tradition.
            - **Syama Sastri**: A key figure in the early development of Carnatic music.
            - **MS Subbulakshmi**: A legendary vocalist who brought Carnatic music to a global audience.
            - **Balamuralikrishna**: A virtuoso known for his mastery in both vocal and instrumental music.
            These musicians helped shape Carnatic music as we know it today, and their works continue to inspire musicians and audiences worldwide.
        """)

if __name__ == "__main__":
    main()
