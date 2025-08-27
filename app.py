import streamlit as st
from services.cognitive_search import search_faq
from services.openai_chat import refine_with_openai

# Streamlit page settings
st.set_page_config(page_title="AI-Powered FAQ Chatbot 🤖", layout="centered")

# Title
st.title("AI-Powered FAQ Chatbot 🤖")
st.caption("Ask me anything from the knowledge base powered by Azure Cognitive Search + Azure OpenAI.")

# Input box
user_query = st.text_input("💬 Your Question:", placeholder="e.g., What is Azure Cognitive Search?")

# Button logic
if st.button("🔍 Get Answer"):
    if user_query.strip():
        with st.spinner("🔎 Searching knowledge base..."):
            search_results = search_faq(user_query)

        if search_results:
            context = " ".join(search_results)
            
            with st.spinner("🤖 Thinking with OpenAI..."):
                final_answer = refine_with_openai(user_query, context)

            st.success("✅ Answer:")
            st.write(final_answer)

            # Show retrieved docs
            with st.expander("📂 Context Retrieved:"):
                for idx, res in enumerate(search_results, 1):
                    st.markdown(f"**{idx}.** {res}")

        else:
            st.error("❌ No results found in the knowledge base.")
    else:
        st.warning("⚠️ Please enter a question.")
