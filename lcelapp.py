from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

groq_api_key = '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'
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

def translate_text(language: str, text: str):
    try:
        generic_template = "Present the output by only translating the following input into {language}:"
        prompt = ChatPromptTemplate.from_messages(
            [("system", generic_template), ("user", "{text}")]
        )
        
        parser = StrOutputParser()
        
        chain = prompt | model | parser
        
        result = chain.invoke({"language": language, "text": text})
        
        if isinstance(result, str):
            return result.strip()  
        else:
            return "Translation failed: Unexpected response format."
    except Exception as e:
        return f"Error: {str(e)}"

st.title("Multilingual LLM Translator")

st.sidebar.header("Translation Options")

popular_languages = [
    "French", "Spanish", "German", "Tamil", "Hindi",
    "Chinese", "Japanese", "Korean", "Arabic", "Portuguese"
]
selected_language = st.sidebar.selectbox("Select a popular language:", popular_languages)

custom_language = st.sidebar.text_input(
    "Or enter a different target language:", ""
)

target_language = custom_language.strip() if custom_language.strip() else selected_language

text = st.text_area("Enter the text you want to translate (input can be in any language):", "")

if st.button("Translate"):
    if target_language and text.strip():
        with st.spinner("Translating..."):
            result = translate_text(target_language, text.strip())
        if result.startswith("Error:") or result == "Translation failed: Unexpected response format.":
            st.error(result)
        else:
            st.success("Translation Complete!")
            st.write(f"**Translated Text ({target_language}):**")
            st.write(result)
    else:
        st.error("Please provide both the target language and text to translate.")
