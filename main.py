import streamlit as st
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import pandas as pd
import pyvista as pv
from stpyvista import stpyvista
from InfoBot import infoBot
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st
from streamlit_stl import stl_from_file, stl_from_text
import os

pv.start_xvfb()  # Start the virtual frame buffer


def check_answers(answers):
        correct_answers = {
        1: "C", 2: "A", 3: "B", 4: "C", 5: "B", 6: "B", 7: "C", 8: "C", 9: "C", 10: "C"
        }
        score = 0
        for i in range(1, 11):
            if answers.get(i) == correct_answers[i]:
                score += 1
        return score
vid1 = open('ocvid3.mp4','rb')
vid2 = open('ocvid4.mp4','rb')

# Set page title and favicon
st.set_page_config(page_title="Planet Thalaxis", page_icon="🌑",layout = "wide")

# Custom CSS for styling the Streamlit app
st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E; /* Dark background for the main content */
            color: white;  /* White text */
            padding: 20px;
        }

        /* Add dark grey background to the sidebar and ensure the text is readable */
        .css-1d391kg {  /* Sidebar class */
            background-color: #333333 !important; /* Darker grey */
            border: 2px solid red; /* Red border */
            padding: 10px;
            border-radius: 10px; /* Rounded corners */
            color: #FFFFFF !important; /* Ensure sidebar text is white */
            margin-top: -50px !important;  /* Move sidebar up */
        }

        /* Sidebar selectbox and text */
        .css-1cpxqw2, .css-16huue1 {  
            color: #FFFFFF !important; /* Ensure text is white */
            background-color: #444444 !important; /* Slightly lighter grey for input box */
        }

        /* Adjust the sidebar image (logo) */
        [data-testid="stSidebar"] img {
            margin-top: -60px !important; /* Bring logo up */
            margin-bottom: 10px !important; /* Adjust space below the logo */
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        /* Styling for the main header and subheader */
        h1 {
            font-size: 2.5em; /* Adjust the title size */
            color: #CCCCCC;  /* Light grey color for the title */
        }

        h2 {
            font-size: 2.0em; /* Adjust the subheader size */
            color: #CCCCCC;  /* Light grey color for the subheader */
        }

        /* Styling for the description */
        .description {
            font-size: 1.5em;
            line-height: 1.6;
            color: #B0C4DE;  /* Light steel blue for text */
            padding-top: 10px;
            padding-bottom: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
            background-color: #2E2E2E;
            border-radius: 10px;
            padding: 20px;
        }

        .description p {
            margin: 0;
        }

        /* Custom styling for the HeatMap link */
        a {
            font-size: 1.8em;  /* Bigger font size for the HeatMap link */
            color: #FFD700 !important;  /* Gold color for emphasis */
            text-decoration: underline;
        }

    </style>
    """, unsafe_allow_html=True)


# Main container with title and subtitle
# Main container with centered title
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])  # Add three columns for centering
    with col2:
        st.markdown("<h1 style='text-align: center;'>Planet Thalaxis</h1>", unsafe_allow_html=True)


# Horizontal divider
st.divider()

# Sidebar setup with logo and page selection
st.sidebar.image('LOGO.png', width=150)
page = st.sidebar.selectbox("What would you like to see ? ", ["Thalaxis","Planet Exterior", "Play 3D","Data",  "Thalaxis Bot","Quiz"    ])  # Use st.radio instead of selectbox


import streamlit as st
from PIL import Image

# Load and display image
image = Image.open("europabg.png")

# Main page layout
if page == "Thalaxis":
    # Add a sidebar selection to switch between sections
    st.sidebar.title("Explore Thalaxis")
    section = st.sidebar.radio("Navigate", ["Overview", "Research Paper", "Planet Details", "Purpose","Short Animation"])

    # Overview Section
    if section == "Overview":
        st.title("Welcome to Our Planet: Thalaxis")
        st.markdown("""
        **Thalaxis** is a hypothetical planet designed to showcase the potential for life on a distant celestial body, where sunlight is not the primary source of energy. On Thalaxis, life thrives through chemosynthesis, utilizing chemical reactions in deep ocean ecosystems.
        """)

    # Research Paper Section
    if section == "Research Paper":
        st.header("Access our research paper below")
        with open("research.pdf", "rb") as file:
            st.download_button(label="Download Research Paper", data=file, file_name="Thalaxis_Research_Paper.pdf")

    # Planet Details Section
    if section == "Planet Details":
        st.header("Planet Thalaxis: Details and Characteristics")
        st.subheader("Characteristics of Thalaxis")
        st.markdown("""
        Thalaxis is a planet situated near the Gas Giants, Jupiter and Saturn, about 10 Astronomical Units (AU) from the Sun. Its surface is covered with a thick layer of ice, ranging from 20km to 40km in thickness. Beneath this ice lies a vast ocean with depths ranging from 20km to 50km, harboring life that thrives in chemosynthetic environments.

        Despite surface temperatures between -180°C and -100°C, the oceans of Thalaxis remain at a warmer 0°C to 20°C, providing a suitable habitat for life. The ocean's neutral to slightly alkaline pH levels of 7-9 further support the development of complex life forms beyond microorganisms.
        """)

    # Purpose Section
    if section == "Purpose":
        st.header("The Purpose Behind Thalaxis")
        st.markdown("""
        By imagining a planet like Thalaxis, we can explore new horizons in the search for life and our understanding of habitability. Here are some of the key objectives:
        """)
        st.write("""
        1. **Redefine Habitability** – Traditionally, habitability is associated with the presence of sunlight. Thalaxis challenges this by presenting a world where life is sustained without it.
        2. **New Targets for Space Exploration** – Understanding planets like Thalaxis helps guide missions to moons like Europa or Enceladus, where chemosynthesis may exist.
        3. **Insights on Earth's Extremophiles** – Studying how life survives in extreme environments on Thalaxis can enhance our understanding of Earth's most resilient organisms.
        4. **Human Colonization in Harsh Environments** – The knowledge gained from studying such planets could one day help us colonize other worlds with challenging conditions.
        """)

    if section == "Short Animation":
        st.header("Underwater Animation")
        st.subheader("Hydrothermal Vents on Seamount")
        st.video(vid1)
        st.subheader("Organisms inhabiting the chemosynthetic ocean")
        st.video(vid2)
        st.write("AI-Generated Videos that depicts the Underwater Conditions in a Chemosynthetic Ocean")

    # Add final image for visual appeal
    st.image('europabg.png', caption='Thalaxis - A Hypothetical Planet', use_column_width=True)


elif page == "Play 3D":
    st.header("Hydrothermal Vents Imagined")

    cols = st.columns(4)
    with cols[0]:
        # Remove color picker and set a fixed color
        color = "#A9A9A9"  # Dark grey color
    with cols[1]:
        material = st.selectbox("Select a material", ["material", "wireframe"], key='material_file')
    with cols[2]:
        st.write('\n'); st.write('\n')
        auto_rotate = st.toggle("Auto rotation", key='auto_rotate_file')
    with cols[3]:
        height = st.slider("Height", min_value=50, max_value=1000, value=500, key='height_file')

    stl_from_file(  file_path='vents.stl', 
                    color=color,
                    material=material,
                    auto_rotate=auto_rotate,
                    height=height,
                    key='example1')

# Define the page
elif page == "Planet Exterior":

    # Page Header and Description
    st.title("Explore the Exterior of Our World")
    st.write("""
        ### A Glimpse into the Exterior:
        Dive into the detailed 3D render of our **Aquatic Chemosynthetic World**. 
        Rotate, zoom, and explore the planet's surface from all angles.
    """)

    # Sidebar for User Interaction
    st.sidebar.subheader("Rendering Options")
    ambient_slider = st.sidebar.slider("Ambient Lighting", min_value=0.0, max_value=1.0, value=0.2)
    edge_display = st.sidebar.checkbox("Show Mesh Edges", value=False)
    
    st.sidebar.subheader("Controls")
    st.sidebar.write("Use your mouse to interact with the 3D model.")

    # Initialize a plotter object and create the sphere mesh
    mesh = pv.Sphere(radius=1.0, center=(0, 0, 0))

    # Apply texture coordinates (UV mapping) to the mesh
    mesh.texture_map_to_sphere(inplace=True)

    # Load the texture image
    texture = pv.read_texture("texture.jpg")  # Adjust to the correct path

    # Create the plotter for rendering
    plotter = pv.Plotter(window_size=[500, 500])
    plotter.add_mesh(
        mesh,
        texture=texture,  # Apply the image texture
        show_edges=edge_display,  # Add a checkbox for user control
        ambient=ambient_slider,  # Slider for ambient lighting control
    )

    # Customize view settings
    plotter.background_color = "black"
    plotter.view_isometric()

    # Render the plotter in Streamlit using stpyvista
    stpyvista(plotter)

   # Data Page
elif page == "Data":
    st.title("Celestial Bodies Feature Comparison")

    # Visualization of Ocean Depths
    st.header("Ocean Depths Comparison")
    st.write("Interactive heatmap comparing ocean depths across different celestial bodies.")

    # Example of displaying a dataframe with quartile depths
    data = {
        "Planet": ["Thalaxis", "Earth", "Europa", "Enceladus"],
        "Lower Quartile Depth": [31350, 5450, 82500, 15250],
        "Median Depth": [37500, 7300, 105000, 20500],
        "Upper Quartile Depth": [43750, 9150, 127500, 25750]
    }
    df = pd.DataFrame(data)
    df.set_index('Planet', inplace=True)
    df_reset = df.reset_index()

    # Use plotly.express to create an interactive heatmap
    fig = px.imshow(df, 
                    labels={"x": "Depth Metrics", "y": "Planet", "color": "Depth (m)"},
                    x=df.columns,
                    y=df_reset['Planet'],
                    color_continuous_scale='Blues')

    fig.update_layout(title="Ocean Depths Across Planets", title_x=0.5, template="plotly_dark")
    st.plotly_chart(fig)

    # Ice Thickness 3D Towers Visualization
    st.header("Ice Thickness Comparison")
    st.write("3D visualization of ice thickness on various planets.")

    data1 = {
        'Planet': ['Thalaxis', 'Earth', 'Europa', 'Enceladus'],
        'Ice Type': ['Average', 'Average', 'Average', 'Average'],
        'Ice Thickness (km)': [30, 2.2, 20, 25]
    }
    df1 = pd.DataFrame(data1)

    planet_map = {'Thalaxis': 1, 'Earth': 2, 'Europa': 3, 'Enceladus': 4}
    df1['y'] = df1['Planet'].map(planet_map)

    def towers(a, e, pos_x, pos_y):
        x, y, z = np.meshgrid(
            np.linspace(pos_x - a / 2, pos_x + a / 2, 2),
            np.linspace(pos_y - a / 2, pos_y + a / 2, 2),
            np.linspace(0, e, 2)
        )
        return go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(), alphahull=1, flatshading=True)

    fig = go.Figure(layout={'scene': {'aspectmode': "data"}, 'height': 700, 'width': 800})
    for i, row in df1.iterrows():
        fig.add_trace(towers(1, row['Ice Thickness (km)'], i, row['y']))

    fig.update_layout(
        scene=dict(
            xaxis_title='Ice Thickness Visualization',
            yaxis=dict(
                title='Planet', 
                tickvals=[1, 2, 3, 4], 
                ticktext=['Thalaxis', 'Earth', 'Europa', 'Enceladus']
            ),
            zaxis_title='Ice Thickness (km)'
        ),
        title="3D Ice Thickness Across Planets",
        margin=dict(l=0, r=0, b=0, t=50),
        showlegend=False
    )
    st.plotly_chart(fig)

    # pH Level Comparison
    st.header("pH Levels Across Planets")
    st.write("Bar chart with error bars showing the pH levels of different planets.")

    data_comparison = {
        'Planet': ['Thalaxis', 'Earth', 'Europa', 'Enceladus'],
        'pH Level': [8, 8.05, 8.5, 10.8],
        'pH Lower Bound': [7, 7.55, 7.95, 10.3],
        'pH Upper Bound': [9, 8.55, 9.05, 11.3]
    }
    df_comparison = pd.DataFrame(data_comparison)
    df_comparison['error_low'] = df_comparison['pH Level'] - df_comparison['pH Lower Bound']
    df_comparison['error_high'] = df_comparison['pH Upper Bound'] - df_comparison['pH Level']

    fig = px.bar(df_comparison, x='pH Level', y='Planet', color='Planet', 
                 title="pH Levels with Range (Error Bars)", orientation='h',
                 text='pH Level', error_x_minus='error_low', error_x='error_high')

    fig.update_layout(yaxis_title="Planet", xaxis_title="pH Level", title_x=0.5, template="plotly_dark", showlegend=False)
    st.plotly_chart(fig)

    # Temperature and Pressure Bubble Chart
    st.header("Temperature and Pressure Comparison")
    st.write("Bubble chart displaying the temperature and pressure for various celestial bodies.")

    data_bubble = {
        'Planet': ['Thalaxis', 'Earth', 'Europa', 'Enceladus'],
        'Temperature (°C)': [20, 2, -2, -1],
        'Pressure (psi)': [20250, 15750, 27981, 1078]
    }
    df_bubble = pd.DataFrame(data_bubble)

    fig = px.scatter(df_bubble, x='Planet', y='Temperature (°C)', size='Pressure (psi)', color='Planet', 
                     title="Ocean Temperature and Pressure Comparison",
                     labels={'Temperature (°C)': 'Temperature (°C)', 'Planet': 'Planet'},
                     size_max=60, text='Pressure (psi)')

    fig.update_layout(yaxis_title="Temperature (°C)", xaxis_title="Planet", title_x=0.5, template="plotly_dark")
    st.plotly_chart(fig)



# RAG Bot that lets user ask questions about the planet.
elif page == "Thalaxis Bot":
    st.title("Thalaxis Bot")
    st.write("Ask our AI-Powered Bot anything about **Thalaxis**, the aquatic chemosynthetic world. It is here to help you explore and learn!")

    # Adding a visual divider for clarity
    st.markdown("---")

    # Container for the conversation display (simulating a chat box)
    conversation_container = st.container()

    # User input box with a prompt message
    userInput = st.chat_input("Ask a question about Thalaxis:")

    # Process user input and display conversation
    if userInput:
        with conversation_container:
            # Display user message in chat format
            st.chat_message("user").write(userInput)
        
        # Generate response from the bot using the existing bot function (infoBot)
        response = infoBot(userInput)

        # Display bot's response in chat format
        with conversation_container:
            st.chat_message("assistant").write(response.response)

    # Add spacing for better layout
    st.markdown("<br><br>", unsafe_allow_html=True)

elif page == "Quiz":
    st.title("🌍 Thalaxis Quiz")

    st.markdown("Test your knowledge on chemosynthesis and related topics. Good luck!")

    # List of quiz questions and options
    questions = {
        1: ("What is the main energy form used by chemosynthesis?", 
            {"A": "Solar energy", "B": "Wind energy", "C": "Chemical energy", "D": "Potential energy"}),
        2: ("Which moon orbits Jupiter?", 
            {"A": "Europa", "B": "Enceladus", "C": "Moon", "D": "Atlas"}),
        3: ("On which celestial body is chemosynthesis likely to sustain life?", 
            {"A": "Mars", "B": "Europa", "C": "Venus", "D": "Mercury"}),
        4: ("What type of environment is essential for chemosynthetic organisms to thrive?", 
            {"A": "Sunlight-rich environments", "B": "Oxygen-rich environments", "C": "Dark, hydrothermal vent-rich environments", "D": "Desert environments"}),
        5: ("What role do hydrothermal vents play in supporting life through chemosynthesis?", 
            {"A": "They provide light for photosynthesis.", "B": "They release chemicals like hydrogen sulfide that chemosynthetic organisms use.", "C": "They increase the oxygen concentration in the water.", "D": "They provide shelter for marine animals."}),
        6: ("In what type of conditions would chemosynthesis be the dominant form of life sustenance?", 
            {"A": "In environments with abundant sunlight.", "B": "In environments with extreme cold and darkness, like under thick ice.", "C": "In desert ecosystems.", "D": "On planets close to their stars."}),
        7: ("What is the primary difference between chemosynthesis and photosynthesis?", 
            {"A": "Chemosynthesis uses light energy, while photosynthesis uses chemical energy.", "B": "Chemosynthesis occurs only in the presence of oxygen.", "C": "Chemosynthesis uses chemical reactions to produce food, while photosynthesis uses light.", "D": "Photosynthesis occurs in the dark, while chemosynthesis requires sunlight."}),
        8: ("What type of organisms typically perform chemosynthesis on Earth?", 
            {"A": "Plants", "B": "Algae", "C": "Bacteria", "D": "Fish and marine mammals"}),
        9: ("Which of the following environments on Earth is most similar to the hypothesized conditions on a planet sustaining life through chemosynthesis?", 
            {"A": "Coral reefs", "B": "Tropical rainforests", "C": "Hydrothermal vents on the ocean floor", "D": "Desert sand dunes"})
    }

    # Store the correct answers
    correct_answers = {
        1: "C", 2: "A", 3: "B", 4: "C", 5: "B", 6: "B", 7: "C", 8: "C", 9: "C"
    }

    # Initialize user answers and score
    user_answers = {}

    # Create form to submit all answers at once
    with st.form("quiz_form"):
        total_questions = len(questions)
        for q_num, (q_text, options) in questions.items():
            st.subheader(f"Question {q_num}/{total_questions}")
            user_answers[q_num] = st.radio(q_text, list(options.keys()), format_func=lambda x: options[x])
        
        # Submit button inside the form
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Calculate the score
        score = 0
        for q_num, answer in user_answers.items():
            if answer == correct_answers[q_num]:
                score += 1

        # Display the score
        st.write(f"### Your final score: **{score}/{total_questions}**")
        
        # Provide detailed feedback per question
        st.markdown("### Detailed Feedback")
        for q_num, answer in user_answers.items():
            if answer == correct_answers[q_num]:
                st.success(f"Question {q_num}: Correct! ✅")
            else:
                st.error(f"Question {q_num}: Incorrect. ❌ The correct answer is {correct_answers[q_num]}.")

        # Provide overall feedback
        if score == total_questions:
            st.balloons()  # Celebration effect for perfect score
            st.success("Perfect score! You're a chemosynthesis expert! 🎉")
        elif score > total_questions / 2:
            st.info("Great job! You have a solid understanding. 👍")
        else:
            st.warning("Keep learning, you're on the right track! 📚")

        # Option to retake the quiz
        if st.button("Retake Quiz"):
            st.experimental_rerun()  # Restart the quiz
