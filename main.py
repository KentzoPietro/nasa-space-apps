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
page = st.sidebar.selectbox("What would you like to see ? ", ["Thalaxis","Planet Exterior", "Play 3D","Data",  "Thalaxis Bot","Quiz"])  # Use st.radio instead of selectbox


if page == "Thalaxis":
    st.header("Access our research paper below")
    with open("research.pdf", "rb") as file:
        st.download_button(label="Research Paper", data=file, file_name="Paper1.pdf")
    st.title("Welcome to Our Planet: Thalaxis")

    # Introduction
    st.write("""
    Thalaxis is a hypothetical planet created to visualize the possibilities of a complex ecosystem on a faraway celestial body where life is sustained in the absence of sunlight through chemosynthesis. The name Thalaxis came from the Greek word “thalasso” which means water, and the word “axis” which means center; therefore the name Thalaxis represents a planet with life forms which thrive in chemosynthetic ocean environments.
    """)

    # Subheader for Characteristics of Thalaxis
    st.subheader("Characteristics of Thalaxis")

    st.write("""
    Thalaxis is a planet located close to the Gas Giant Jupiter, and its neighboring planet Saturn, at a distance of approximately 10AU (Astronomical Unit) away from the Sun. It is a planet whose surface is covered with ice of 20km to 40km thickness, hiding a vast ocean of 20km to 50km depth, providing the possibilities of complex life forms exceeding microorganisms. Despite the harsh surface temperature of -180℃ to -100℃, its oceans are comforting the inhabitants with its warm oceans of 0℃ to 20℃ temperature. Its waters are neutral to slightly alkaline with a pH level of 7-9, allowing chemosynthetic organisms to thrive.
    """)

    # Subheader for Purpose
    st.subheader("Purpose")

    st.write("""
    By visualizing a celestial body which could sustain the life of its inhabitants through chemosynthesis, it is possible to:
    """)

    st.write("""
    1. **Expand the definition of habitability** – where sunlight is traditionally required to define a celestial body as habitable.
    2. **Open new targets for space explorations** – By understanding celestial bodies which are potentially habitable or those which are able to shelter living organisms, it is more than possible to guide space missions like the Europa Clipper or future explorations to Enceladus, where indicators of chemosynthetic life exists. Such actions would significantly accelerate human efforts on searching for extraterrestrial life.
    3. **Gain new insights on how organisms may survive in Earth’s harshest environments** – such as near the hydrothermal vents where chemosynthetic organisms thrive.
    4. **Prepare for future human colonization** – By understanding how life on celestial bodies with scarce oxygen and sunlight, it is possible to visualize plans on how humans may survive in other celestial bodies with harsh conditions compared to Earth through the use of chemosynthesis.
    """)

    st.image('europabg.png', caption='Thalaxis - A Hypothetical Planet', use_column_width=True)


elif page == "Play 3D":
    st.header("Visualize whatever you can imagine !")

    cols = st.columns(4)
    with cols[0]:
        color = st.color_picker("Pick a color", "#FF9900", key='color_file')
    with cols[1]:
        material = st.selectbox("Select a material", ["material", "wireframe"], key='material_file')
    with cols[2]:
        st.write('\n'); st.write('\n')
        auto_rotate = st.toggle("Auto rotation", key='auto_rotate_file')
    with cols[3]:
        height = st.slider("Height", min_value=50, max_value=1000, value=500, key='height_file')

    stl_from_file(  file_path='Moon.stl', 
                    color=color,
                    material=material,
                    auto_rotate=auto_rotate,
                    height=height,
                    key='example1')
    
    file_input = st.file_uploader("Or upload a STL file ", type=["stl"])

    cols = st.columns(4)
    with cols[0]:
        color = st.color_picker("Pick a color", "#0099FF", key='color_text')
    with cols[1]:
        material = st.selectbox("Select a material", ["material", "wireframe"], key='material_text')
    with cols[2]:
        st.write('\n'); st.write('\n')
        auto_rotate = st.toggle("Auto rotation", key='auto_rotate_text')
    with cols[3]:
        height = st.slider("Height", min_value=50, max_value=1000, value=500, key='height_text')
    if file_input:
        stl_from_text(  text=file_input.getvalue(), 
                        color=color,
                        material=material,
                        auto_rotate=auto_rotate,
                        height=height,
                        key='example2')


elif page == "Planet Exterior":

    # Header
    st.header("The Exterior to our World")
    st.write("A 3D Render of the Exterior of our Aquatic Chemosynthetic World")

    # Initialize a plotter object
    # Create a sphere mesh
    mesh = pv.Sphere(radius=1.0, center=(0, 0, 0))

    # Apply texture coordinates (UV mapping) to the mesh
    mesh.texture_map_to_sphere(inplace=True)

    # Load the correct image as a texture (updated to PPP.jpg)
    texture = pv.read_texture("texture.jpg")  # Adjust to the correct path

    # Add the mesh with the texture to the plotter
    plotter = pv.Plotter(window_size=[400, 400])
    plotter.add_mesh(
        mesh,
        texture=texture,  # Apply the image texture
        show_edges=False,
        ambient=0.2,
    )

    # Final touches
    plotter.background_color = "black"
    plotter.view_isometric()

    # Pass plotter to stpyvista
    stpyvista(plotter)
   # Data Page
elif page == "Data":
    st.header("Visualization of Features comparing Celestial Bodies")        

        # Example of displaying a dataframe
    data = {
        "Planet": ["Thalaxis", "Earth", "Europa","Enceladus"],
        "Lower Quartile Depth": [31350,5450,82500 , 15250],
        "Median Depth": [37500,7300, 105000,20500  ],
        "Upper Quartile Depth": [43750,9150 ,127500 ,25750]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df.set_index('Planet', inplace=True)  # Set 'Planet' as the index

    # Reset index so 'Planet' becomes a column again (required for Plotly)
    df_reset = df.reset_index()

    # Use plotly.express to create an interactive heatmap
    fig = px.imshow(df, 
                    labels=dict(x="Oceans", y="Planets", color="Depth (m)"),
                    x=df.columns,
                    y=df_reset['Planet'],
                    color_continuous_scale='Blues')

    fig.update_layout(title="Ocean Depths", 
                    title_x=0.5, 
                    template="plotly_dark")

    # Display the plotly heatmap in Streamlit
    st.plotly_chart(fig)

    # Sample data for ice thickness in different planets (in kilometers)
    data1 = {
        'Planet': ['Thalaxis',  'Earth',   'Europa',  'Enceladus'],
        'Ice Type': ['Average', 'Average', 'Average', 'Average'],
        'Ice Thickness (km)': [30, 2.2, 20, 25]  # Ice thickness in kilometers
    }

    # Create a DataFrame
    df1 = pd.DataFrame(data1)


    # Map planets to numeric values for the y-axis
    planet_map = {'Thalaxis': 1, 'Earth': 2, 'Europa': 3, 'Enceladus': 4}
    df1['y'] = df1['Planet'].map(planet_map)

    # Function to create 3D towers based on Ice Thickness data
    def towers(a, e, pos_x, pos_y):
        # Create mesh points for each tower
        x, y, z = np.meshgrid(
            np.linspace(pos_x - a / 2, pos_x + a / 2, 2),  # x coordinates for the base
            np.linspace(pos_y - a / 2, pos_y + a / 2, 2),  # y coordinates for the base
            np.linspace(0, e, 2)                           # z coordinates (from 0 to height)
        )
        x = x.flatten()
        y = y.flatten()
        z = z.flatten()

        return go.Mesh3d(x=x, y=y, z=z, alphahull=1, flatshading=True)

    # Plot the 3D figure using Plotly
    fig = go.Figure(layout={'scene': {'aspectmode': "data"}, 'height': 700, 'width': 800})
    spacing_factor = 8
    # Loop through each row in the DataFrame and add the towers based on ice thickness
    for i, row in df1.iterrows():
        fig.add_trace(towers(1, row['Ice Thickness (km)'], i, row['y']))

    # Update layout for axis labels and title
    fig.update_layout(
        scene=dict(
            xaxis_title='Ice Thickness',
            yaxis=dict(
                title='Planet', 
                tickvals=[1, 2, 3, 4], 
                ticktext=['Thalaxis', 'Earth', 'Europa', 'Enceladus']
            ),
            zaxis_title='Ice Thickness (km)'  # Ice thickness in meters
        ),
        title="3D Visualization of Ice Thickness ",
        margin=dict(l=0, r=0, b=0, t=50),
        showlegend=False
    )

    # Display the 3D plot in Streamlit
    st.plotly_chart(fig)

    # Define your pH data for the planets, including the range (upper and lower bounds)
    data_comparison = {
        'Planet': ['Thalaxis', 'Earth', 'Europa', 'Enceladus'],
        'pH Level': [8, 8.05, 8.5, 10.8],  # Mean pH levels
        'pH Lower Bound': [7, 7.55, 7.95, 10.3],  # Lower bound of the range
        'pH Upper Bound': [9, 8.55, 9.05, 11.3]  # Upper bound of the range
    }

    # Convert the data into a DataFrame
    df_comparison = pd.DataFrame(data_comparison)

    # Calculate the error margins (difference from the mean pH Level)
    df_comparison['error_low'] = df_comparison['pH Level'] - df_comparison['pH Lower Bound']
    df_comparison['error_high'] = df_comparison['pH Upper Bound'] - df_comparison['pH Level']

    # Create a bar chart with error bars to show the range
    fig = px.bar(df_comparison, x='pH Level', y='Planet', 
                color='Planet',  # Color differentiation for each planet
                title="pH level across planets with range",
                orientation='h',  # Horizontal bars
                text='pH Level',  # Display the mean pH level inside the bars
                error_x_minus='error_low',  # Error bar lower range
                error_x='error_high'  # Error bar upper range
                )

    # Update layout for better visualization
    fig.update_layout(yaxis_title="Planet", xaxis_title="pH Level", 
                    title_x=0.5, template="plotly_dark", showlegend=False)

    # Display the chart in Streamlit (if using Streamlit)
    st.plotly_chart(fig)


    data_bubble = {
        'Planet': ['Thalaxis', 'Earth', 'Europa', 'Enceladus'],
        'Temperature (°C)': [20, 2, -2, -1],  # Temperatures in degrees Celsius
        'Pressure (psi)': [20250, 15750, 27981, 1078]  # Pressure in psi to represent bubble size
    }

    # Convert the data into a DataFrame
    df_bubble = pd.DataFrame(data_bubble)

    # Create a bubble chart
    fig = px.scatter(df_bubble, x='Planet', y='Temperature (°C)', 
                    size='Pressure (psi)', color='Planet', 
                    title="Ocean Temperature and Pressure ",
                    labels={'Temperature (°C)': 'Temperature (°C)', 'Planet': 'Planet'},
                    size_max=60,  # Max size of the bubbles
                    text='Pressure (psi)'  # Display pressure values inside the bubbles
                    )

    # Update layout for better visualization
    fig.update_layout(yaxis_title="Temperature (°C)", xaxis_title="Planet", 
                    title_x=0.5, template="plotly_dark")

    # Display the bubble chart in Streamlit
    st.plotly_chart(fig)




# RAG Bot that lets user ask questions about the planet.
elif page == "Thalaxis Bot":
    st.header("Thalaxis Bot")
    st.write("Our AI-Powered Chatbot that is capable of answering questions related to our planet")

    # Adding space between the prompt and the input box
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)  # Adding space

    # Container for the conversation display (simulating a chat box)
    conversation_container = st.container()

    # User chat input box
    userInput = st.chat_input("Want to know more about our world? Type your question below!")

    # If the user types a question, display the conversation
    if userInput:
        with conversation_container:
            # Display user message in the chat format
            st.chat_message("user").write(userInput)
        
        # Generate response from the bot (your existing bot function)
        response = infoBot(userInput)

        # Display bot response in the chat format
        with conversation_container:
            st.chat_message("assistant").write(response.response)

    # Additional spacing between elements if needed
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)  # More space for visual clarity

elif page == "Quiz":
    def check_answers(answers):
        correct_answers = {
        1: "C", 2: "A", 3: "B", 4: "C", 5: "B", 6: "B", 7: "C", 8: "C", 9: "C", 10: "C"
        }
        score = 0
        for i in range(1, 11):
            if answers.get(i) == correct_answers[i]:
                score += 1
        return score


if page == "Thalaxis Bot":
    st.header("Thalaxis Bot")
    st.write("Ask our AI Thalaxis Bot something regarding our planet and it'll deliver an answer!!")

    # Adding space between the prompt and the input box
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Container for the conversation display (simulating a chat box)
    conversation_container = st.container()

    # User chat input box
    userInput = st.chat_input("Want to know more about our world? Type your question below!")

    # If the user types a question, display the conversation
    if userInput:
        with conversation_container:
            # Display user message in the chat format
            st.chat_message("user").write(userInput)

        # Generate response from the bot (simulated here)
        response = f"Simulated response for: {userInput}"

        # Display bot response in the chat format
        with conversation_container:
            st.chat_message("assistant").write(response)

    # More space between conversation and bottom
    st.markdown("<br><br>", unsafe_allow_html=True)

elif page == "Quiz":
    st.header("Thalaxis Quiz")
    
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

    # Store the answers
    correct_answers = {
        1: "C", 2: "A", 3: "B", 4: "C", 5: "B", 6: "B", 7: "C", 8: "C", 9: "C"
    }

    # Dictionary to store user answers
    user_answers = {}

    # Loop through the questions and display them with radio buttons for answers
    for q_num, (q_text, options) in questions.items():
        user_answers[q_num] = st.radio(q_text, list(options.keys()), format_func=lambda x: options[x])

    # Submit button
    if st.button("Submit"):
        # Calculate the score
        score = 0
        for q_num, answer in user_answers.items():
            if answer == correct_answers[q_num]:
                score += 1
        
        # Display the score
        st.write(f"Your score: {score}/{len(questions)}")

        # Provide feedback based on the score
        if score == len(questions):
            st.success("Perfect score! You're a chemosynthesis expert!")
        elif score > len(questions) / 2:
            st.info("Great job! You have a solid understanding.")
        else:
            st.warning("Keep learning, you're on the right track!")