import streamlit as st
import json

def load_knowledge_base():
    try:
        with open('doj_knowledge.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Knowledge base file not found")
        return {}

def main():
    st.title("Department of Justice Virtual Assistant")
    
    # Load knowledge base
    kb = load_knowledge_base()
    
    # Chat interface
    query = st.text_input("How can I help you?")
    
    if query:
        st.write(f"You asked: {query}")
        st.write("Bot: I'm here to help with DOJ-related queries.")
        
        # Feedback buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍"):
                st.success("Thank you for the feedback!")
        with col2:
            if st.button("👎"):
                st.error("Thank you for the feedback!")

if __name__ == "__main__":
    main()
