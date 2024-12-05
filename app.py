import streamlit as st
import json

def load_knowledge_base():
    try:
        with open('doj_knowledge.json', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            data = [json.loads(line) for line in lines if line.strip()]
        return data
    except FileNotFoundError:
        st.error("Knowledge base file (doj_knowledge.json) not found")
        return []
    except json.JSONDecodeError:
        st.error("Error parsing knowledge base file")
        return []

def find_response(query, knowledge_base):
    query_lower = query.lower()
    for item in knowledge_base:
        if 'prompt' in item and query_lower in item['prompt'].lower():
            return item['completion']
    return "I'm here to help with DOJ-related queries. Please ask about divisions, services, or legal procedures."

def main():
    st.title("Department of Justice Virtual Assistant")
    
    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Load knowledge base
    kb = load_knowledge_base()
    
    # Chat interface
    query = st.text_input("How can I help you?")
    
    if query:
        # Find response from knowledge base
        response = find_response(query, kb)
        
        # Add to chat history
        st.session_state.chat_history.append({"query": query, "response": response})
        
        # Display chat history
        for chat in st.session_state.chat_history:
            st.write(f"You: {chat['query']}")
            st.write(f"Bot: {chat['response']}")
            
            # Feedback buttons for the latest message only
            if chat == st.session_state.chat_history[-1]:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍", key=f"like_{len(st.session_state.chat_history)}"):
                        st.success("Thank you for the feedback!")
                with col2:
                    if st.button("👎", key=f"dislike_{len(st.session_state.chat_history)}"):
                        st.error("Thank you for the feedback!")

if __name__ == "__main__":
    main()
