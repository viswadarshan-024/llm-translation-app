# Multilingual LLM Translator 🌍

This project is a multilingual translation app built with Streamlit and powered by the Groq Model (Gemma2-9b-It). It uses the LangChain framework for constructing a modular chain of prompts, models, and output parsers. The app allows users to translate text into a variety of target languages effortlessly.

**Features ✨**

* **Multilingual Translation:** Translate text into popular languages like French, Spanish, German, Tamil, and more.
* **Custom Language Input:** Specify any custom target language if it’s not listed in the sidebar.
* **Dynamic Chain Integration:** Leverages the power of the LangChain pipeline to combine prompts, models, and parsers effectively.
* **Fast and Intuitive Interface:** Built with Streamlit for an interactive and user-friendly experience.

---

**Technologies & Libraries Used 📚**

1. **LangChain**
    * **Purpose:** For modular pipeline construction, combining prompts, models, and parsers.
    * **Unique Usage:** Utilized the `StrOutputParser` from LangChain to ensure output is parsed as a clean string. 

2. **Groq Model (Gemma2-9b-It)**
    * **Purpose:** The core model for handling text translation.
    * **Unique Usage:** Used the ChatGroq integration to seamlessly connect the Groq model with the LangChain pipeline.

3. **Streamlit**
    * **Purpose:** For building the web-based user interface.
    * **Unique Usage:** Sidebar customization and dynamic input features to provide both pre-defined and custom language options.

4. **Python**
    * **Purpose:** General-purpose programming language for implementing the app logic.
    * **Unique Usage:** Exception handling and custom modular functions for translation processing.
  
---

**How It Works 🛠️**

**User Input:**

1. Enter the text to translate.
2. Select a target language from the sidebar or specify a custom one.

**Pipeline Execution:**

1. The input is processed using the LangChain pipeline (prompt | model | parser).
2. The Groq model generates the translation output, parsed by `StrOutputParser` for a clean string response.

**Translation Output:**

The translated text is displayed dynamically on the interface.

---

