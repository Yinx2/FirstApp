import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")
    
    # Sidebar Navigation
    st.sidebar.title("Portfolio Navigator")
    page = st.sidebar.radio("Go to", 
        ["About Me", "Projects", "Skills", "Experience", "Contact"]
    )
    
    # About Me Page
    if page == "About Me":
        st.title("👋 Hi, I'm [Your Name]")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("/images.jpeg", caption="Your Profile Picture", width=250)
        
        with col2:
            st.markdown("""
            ## Professional Summary
            I'm a passionate [Your Profession] with expertise in [Key Skills]. 
            I love solving complex problems and creating innovative solutions.

            ### Key Highlights
            - 🚀 [X] years of professional experience
            - 💻 Specialization in [Your Primary Domain]
            - 🏆 Proven track record of [Key Achievement]
            """)
    
    # Projects Page
    elif page == "Projects":
        st.title("🛠 Projects")
        
        projects = [
            {
                "name": "Project 1", 
                "description": "Detailed description of Project 1",
                "technologies": ["Python", "Streamlit", "Data Analysis"],
                "github_link": "https://github.com/yourusername/project1"
            },
            {
                "name": "Project 2", 
                "description": "Detailed description of Project 2",
                "technologies": ["Machine Learning", "Tensorflow", "React"],
                "github_link": "https://github.com/yourusername/project2"
            }
        ]
        
        for project in projects:
            with st.expander(project["name"]):
                st.write(project["description"])
                st.write("**Technologies:**", ", ".join(project["technologies"]))
                st.markdown(f"[GitHub Link]({project['github_link']})")
    
    # Skills Page
    elif page == "Skills":
        st.title("💡 Skills")
        
        skills_data = {
            "Programming Languages": ["Python", "JavaScript", "SQL"],
            "Frameworks": ["Streamlit", "React", "Django"],
            "Tools": ["Git", "Docker", "AWS"]
        }
        
        for category, skills in skills_data.items():
            st.subheader(category)
            cols = st.columns(len(skills))
            for i, skill in enumerate(skills):
                cols[i].metric(label=skill, value="★★★★☆")
    
    # Experience Page
    elif page == "Experience":
        st.title("💼 Professional Experience")
        
        experiences = [
            {
                "company": "nig",
                "role": "sjiejdei",
                "duration": "Jan 2020 - Present",
                "description": "Led development of scalable web applications..."
            },
            {
                "company": "Startup B",
                "role": "Data Scientist",
                "duration": "Jun 2017 - Dec 2019",
                "description": "Developed machine learning models for predictive analytics..."
            }
        ]
        
        for exp in experiences:
            st.markdown(f"""
            ### {exp['role']} at {exp['company']}
            **{exp['duration']}**
            
            {exp['description']}
            """)
    
    # Contact Page
    elif page == "Contact":
        st.title("📬 Contact Me")
        
        with st.form(key="contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submit_button = st.form_submit_button("Send Message")
            
            if submit_button:
                st.success("Message sent successfully! I'll get back to you soon.")

if __name__ == "__main__":
    main()

# Requirements.txt content
"""
streamlit
plotly
pandas
"""
