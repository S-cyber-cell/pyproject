import requests
import streamlit as st

API_URL = "https://api.mymemory.translated.net/get?q=Hello World!&langpair=en|it"


LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Arabic": "ar",
    "Azerbaijani": "az",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Marathi": "mr",
    "Norwegian": "no",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy"
}

def translate(text, source, target):
    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["responseData"]["translatedText"]
    except requests.exceptions.RequestException as e:
        return f"API error: {e}"
    except KeyError:
        return "Unexpected API response."

# Streamlit UI
st.set_page_config(page_title="Translator App", page_icon="🌐", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2294ed;'>🌐 Multi-Language Translator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #577592;'>Powered by MyMemory API</p>", unsafe_allow_html=True)

with st.form("translate_form"):
    text = st.text_area("Enter text to translate:", height=150)
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("Source Language", list(LANGUAGES.keys()), index=list(LANGUAGES.keys()).index("English"))
    with col2:
        target = st.selectbox("Target Language", list(LANGUAGES.keys()), index=list(LANGUAGES.keys()).index("Spanish"))

    submit = st.form_submit_button("🌟 Translate")

if submit:
    if text.strip():
        translated = translate(text, LANGUAGES[source], LANGUAGES[target])
        st.markdown(
            f"<div style='background-color: black; padding: 15px; border-radius: 10px;'><b>Translated Text:</b><br>{translated}</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter some text to translate.")
