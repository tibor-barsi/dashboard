import streamlit as st
import datetime

st.title("Simple Dashboard Example")

# Sidebar for navigation
mode = st.sidebar.selectbox(
    "Choose Mode",
    ["Morning Planning", "Working Day", "Evening Review"]
)

# Main content based on mode
if mode == "Morning Planning":
    st.header("🌅 Today's Priorities")
    st.write(f"**Date:** {datetime.date.today()}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Calendar")
        st.write("• 9:00 AM - Team Meeting")
        st.write("• 2:00 PM - Client Call")
    
    with col2:
        st.subheader("Top Tasks")
        st.write("• Review project proposal")
        st.write("• Update dashboard mockup")

elif mode == "Working Day":
    st.header("⚡ Focus Mode")
    progress = st.slider("Today's Progress", 0, 100, 25)
    st.progress(progress)
    
    if st.button("Mark Current Task Complete"):
        st.success("Task marked complete!")

else:  # Evening Review
    st.header("📝 End of Day")
    
    with st.expander("Email Processing"):
        st.write("3 emails need review")
        if st.button("Process Emails"):
            st.info("Email drafts generated - review needed")
    
    with st.expander("Tomorrow Planning"):
        tomorrow_tasks = st.text_area("Tasks for tomorrow:")
        if st.button("Save Plan"):
            st.success("Tomorrow's plan saved!")