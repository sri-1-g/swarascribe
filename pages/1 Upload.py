import streamlit as st
from predict import predict_audio_class

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

col1, col2, col3 = st.columns(3)
with col2:
    st.image("upload.png")

st.write("Currently, the AI can analyze the following ragams: Kharaharapriya, Shankarabharanam, Khamboji, Bhairavi, and Kalyani. Don't worry, more are to come!")

uploaded_file = st.file_uploader("Choose a file")
st.divider()
audio_value = st.audio_input("Record a voice message")

if st.button("Analyze"):
    if uploaded_file:
        prediction = predict_audio_class(uploaded_file, is_widget_data=False)
    elif audio_value:
        prediction = predict_audio_class(audio_value, is_widget_data=True)

    if prediction == "Saveri":

        k1, k2 = st.columns(2)

        with k1:
            st.title("This song is in the ragam: Saveri")

            st.write(''' **Arohana**: S R₁ M₁ P D₁ Ṡ  
                        **Avarohana**: Ṡ N₃ D₁ P M₁ G₃ R₁ S''')

            st.markdown("""
            **Notes of Saveri:**
            - **S** (Shadjam)
            - **R₁** (Shuddha Rishabham)
            - **G₃** (Antara Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₁** (Shuddha Dhaivatam)
            - **N₃** (Kakali Nishadam)
            """)

            st.title("Janya Ragas of Saveri")

            st.markdown("""
            Saveri is a powerful Janya raga that evokes deep devotion and classical depth. 
            Some popular Janya and related ragas include:
            - 🎶 **Poornachandrika**
            - 🎶 **Janaranjani**
            - 🎶 **Devagandhari**
            - 🎶 **Nadanamakriya**
            - 🎶 **Suddha Saveri**
            - 🎶 **Karnataka Devagandhari**
            - 🎶 **Sourashtram**

            These ragas reflect the traditional and devotional strength of Saveri.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                submitted = st.form_submit_button("Submit")

        with k2:
            st.image("spec.png")

            st.title('Fun Facts About Saveri')

            st.markdown("""
            Saveri is one of the most ancient and devotional ragas in Carnatic music, known for its strong bhakti rasa. Here are some interesting facts about this raga:
            """)

            facts = [
                ("🎵 **Janya Raga**", "Saveri is a Janya raga of the 15th Melakarta Mayamalavagowla."),
                ("🔢 **Audava–Shadava Scale**", "Saveri uses 5 notes in ascent and 6 notes in descent."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is P (Paṅchamam), and the Samvadi is S (Shadjam)."),
                ("🌅 **Time of Performance**", "Traditionally performed in the early morning."),
                ("🎤 **Famous Compositions**", "Notable kritis include 'Rama Banatu' and 'Sankari Sankuru' by Tyagaraja."),
                ("💎 **Ancient Origins**", "Saveri is one of the oldest Carnatic ragas still in active performance."),
                ("🎶 **Vakra Prayogas**", "The raga features characteristic zig-zag movements in descent."),
                ("🩷 **Emotional Range**", "Saveri conveys devotion, surrender, and spiritual intensity."),
                ("🎻 **Vocal and Instrumental**", "Equally powerful in both vocal and instrumental performances."),
            ]

            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")

    elif prediction == "Mohanam":

        k1, k2 = st.columns(2)

        with k1:
            st.title("This song is in the ragam: Mohanam")

            st.write(''' **Arohana**: S R₂ G₃ P D₂ Ṡ  
                        **Avarohana**: Ṡ D₂ P G₃ R₂ S''')

            st.markdown("""
            **Notes of Mohanam:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₃** (Antara Gandharam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            """)

            st.title("Janya Ragas of Mohanam")

            st.markdown("""
            Mohanam is a bright and joyful Janya raga known for its uplifting and auspicious character. 
            Some popular Janya and related ragas include:
            - 🎶 **Hamsadhwani**
            - 🎶 **Shuddha Dhanyasi**
            - 🎶 **Kalyanavasantham**
            - 🎶 **Niroshta**
            - 🎶 **Madhyamavathi**
            - 🎶 **Desh**
            - 🎶 **Durga**

            These ragas reflect the energetic and joyful nature of Mohanam.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                submitted = st.form_submit_button("Submit")

        with k2:
            st.image("spec.png")

            st.title('Fun Facts About Mohanam')

            st.markdown("""
            Mohanam is one of the most popular pentatonic ragas in Carnatic music, celebrated for its bright and festive appeal. Here are some interesting facts about this raga:
            """)

            facts = [
                ("🎵 **Janya Raga**", "Mohanam is a Janya raga of the 28th Melakarta Harikambhoji."),
                ("🔢 **Audava Scale**", "It uses 5 notes in both ascent and descent."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is G₃ (Antara Gandharam), and the Samvadi is D₂ (Chatushruti Dhaivatam)."),
                ("🌅 **Time of Performance**", "Commonly performed in the evening."),
                ("🎤 **Famous Compositions**", "Popular kritis include 'Nannu Palimpa' by Tyagaraja and 'Mohana Rama' by Purandaradasa."),
                ("💎 **Name Meaning**", "Mohanam means 'that which enchants or mesmerizes.'"),
                ("🎶 **Hindustani Equivalent**", "Its Hindustani counterpart is Bhoop / Bhupali."),
                ("🩷 **Emotional Range**", "Mohanam conveys joy, devotion, and celebration."),
                ("🎻 **Vocal and Instrumental**", "Extremely popular in both vocal and instrumental concerts."),
            ]

            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")

    elif prediction == "Kanada":

        k1, k2 = st.columns(2)

        with k1:
            st.title("This song is in the ragam: Kanada")

            st.write(''' **Arohana**: S R₂ G₂ M₁ P D₂ Ṡ  
                        **Avarohana**: Ṡ N₂ D₂ P M₁ G₂ R₂ S''')

            st.markdown("""
            **Notes of Kanada:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₂** (Sadharana Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₂** (Kaisiki Nishadam)
            """)

            st.title("Janya Ragas of Kanada")

            st.markdown("""
            Kanada is a majestic and depth-filled Janya raga known for its gamaka-rich phrases and emotional gravitas. 
            Some popular Janya and related ragas include:
            - 🎶 **Darbari Kanada**
            - 🎶 **Nayaki**
            - 🎶 **Sahana**
            - 🎶 **Karnataka Devagandhari**
            - 🎶 **Bageshri**
            - 🎶 **Hindolam**
            - 🎶 **Manji**

            These ragas reflect the powerful and expressive nature of Kanada.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                submitted = st.form_submit_button("Submit")

        with k2:
            st.image("spec.png")

            st.title('Fun Facts About Kanada')

            st.markdown("""
            Kanada is a timeless and emotionally intense raga in Carnatic music, celebrated for its depth, oscillations, and expressive power. Here are some interesting facts about this raga:
            """)

            facts = [
                ("🎵 **Janya Raga**", "Kanada is a Janya raga of the 22nd Melakarta Kharaharapriya."),
                ("🔢 **Vakra–Sampurna Nature**", "Kanada employs zig-zag note movements with all seven notes used in descent."),
                ("🎶 **Signature Gamakas**", "Heavy oscillations on G₂ and N₂ define its personality."),
                ("🌅 **Time of Performance**", "Traditionally rendered in the late evening."),
                ("🎤 **Famous Compositions**", "Popular kritis include 'Sri Narada' by Tyagaraja and 'Enneramum' by Arunachala Kavi."),
                ("💎 **Hindustani Connection**", "Closely related to Darbari and Adana in Hindustani music."),
                ("🩷 **Emotional Range**", "Kanada conveys depth, yearning, and quiet grandeur."),
                ("🎻 **Vocal and Instrumental**", "Highly elegant in both vocal and instrumental performance."),
                ("📜 **Ancient Lineage**", "Kanada has roots in both Carnatic and Hindustani traditions."),
            ]

            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")
