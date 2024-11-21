import streamlit as st

st.image("images/banner.png", use_container_width=True)
st.markdown(
    """
    <style>
        /* Center the header and apply styling */
        .main-header {
            text-align: center;
            font-size: 2.5em;
            color: #556B2F; /* Olive green */
            font-weight: bold;
            margin-bottom: 30px;
            font-family: Arial, sans-serif;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #f8f9f5; /* Light eucalyptus background */
            padding: 20px;
            border-right: 2px solid #d2d7c7; /* Soft olive border */
        }

        /* Dropdown styling */
        .stSelectbox [data-baseweb="select"] {
            border: 1px solid #556B2F; /* Olive green border */
            border-radius: 5px;
        }

        /* General font styling for body */
        body {
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-header'>La Poigne d'Acier</div>", unsafe_allow_html=True)

st.write("Welcome to the home page!")
st.write("")
left, right = st.columns(2)
with left:
     st.page_link(page="pages/Member.py",label="Member")

with right:
     st.page_link(page="pages/Admin.py",label="Admin")

# st.markdown(
#     """
#     <style>
#     .custom-button {
#         display: block;
#         margin: auto;
#         padding: 15px 20px;
#         font-size: 18px;
#         color: black;
#         text-decoration: none;
#         border: 1px solid;
#         border-radius: 5px;
#         cursor: pointer;
#         text-align: center;
#         background-color: transparent;
#     }

#     .custom-button:hover {
#         color: black;
#     }

#     /* Dark mode detection */
#     @media (prefers-color-scheme: dark) {
#         .custom-button {
#             color: white; /* White text by default in dark mode */
#             border-color: white; /* White border in dark mode */
#         }
#         .custom-button:hover {
#             color: white; /* Keep white text on hover in dark mode */
#         }
#     }
#     </style>
#     <a href="http://localhost:8501/Member" class="custom-button">Member</a>
#     """,
#     unsafe_allow_html=True
# )

# # Button to redirect to the quiz page
# st.markdown(
#     """
#     <style>
#     .custom-button {
#         display: block;
#         margin: auto;
#         padding: 15px 20px;
#         font-size: 18px;
#         color: black;
#         text-decoration: none;
#         border: 1px solid;
#         border-radius: 5px;
#         cursor: pointer;
#         text-align: center;
#         background-color: transparent;
#     }

#     .custom-button:hover {
#         color: black;
#     }

#     /* Dark mode detection */
#     @media (prefers-color-scheme: dark) {
#         .custom-button {
#             color: white; /* White text by default in dark mode */
#             border-color: white; /* White border in dark mode */
#         }
#         .custom-button:hover {
#             color: white; /* Keep white text on hover in dark mode */
#         }
#     }
#     </style>
#     <a href="http://localhost:8501/Admin" class="custom-button">Admin</a>
#     """,
#     unsafe_allow_html=True
# )
