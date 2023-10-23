import streamlit as st

def apply_css_styling():
    st.markdown(
        """
        <style>
        body {
            font-family: "Source Sans Pro", sans-serif";
            background-color: #f7f7f7;
        }
        
        .title-container {
            display: flex;
            margin-top: -50px;
            justify-content: left;
            align-items: center;
            height: 90px;
            font-family: 'Segoe UI';
            background-color: #F7F7F7;
        }

        .title-text {
            font-size: 49px;
            font-weight: bold;
            color: #333333;
            font-family: 'Arial', sans-serif;
        }

        .subtitle-container {
            display: flex;
            margin:auto;
            justify-content: left;
            align-items: left;
            height: 40px;
            font-family: 'Segoe UI';
            background-color: #F7F7F7;
        }


        .subtitle-text {
            font-size: 22px;
            font-weight: light;
            color: #333333;
            font-family: 'Arial', sans-serif;

        }
        .header-container {
            display: flex;
            margin:auto;
            justify-content: left;
            align-items: left;
            height: 40px;
            font-family: 'Segoe UI';
            background-color: #F7F7F7;
        }

        .header-text {
            font-size: 18px;
            font-weight: light;
            color: #333333;
            font-family: 'Arial', sans-serif;

        }

        .upload-header-container {
            display: flex;
            margin:auto;
            justify-content: left;
            align-items: left;
            height: 40px;
            font-family: 'Segoe UI';
            background-color: #F7F7F7;
        }

        .upload-header-text {
            font-size: 18px;
            font-weight: bold;
            color: #333333;
            font-family: 'Arial', sans-serif;

        }
        .empty-box {
            border: 1px solid #333333;
            padding: 10px;
            margin-bottom: 10px;
        }
        .file-container {
            display: flex;
            margin:auto;
            justify-content: left;
            align-items: left;
            height: 40px;
            font-family: 'Segoe UI';
            background-color: #F7F7F7;
        }


        .file-text {
            font-size: 18px;
            font-weight: light;
            color: #333333;
            font-family: 'Arial', sans-serif;

        }
        .sidebar-header-container{
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #F7F7F7;
            border-radius: 3px;
            height: 60px;
            margin-bottom: 10px;
        }
        .sidebar-header-text{
            font-size: 22px;
            font-weight: bold;
            color: #333333;
            font-family: 'Arial', sans-serif;
            margin: 4px;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #333333;
            margin-bottom: 16px;
            text-align: center;
        }
        .stButton button {
            background-color: #ebf0fa;
            color: #4f0e0e;
            font-weight: bold;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .stButton button:hover {
            background-color: #1e3d7b;
            color: white;
        }

        .stForm button {
            background-color: #F7F7F7;
            color: #4f0e0e;
            font-weight: bold;
            padding: 8px 16px;
            border-radius: 4px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .sidebar .sidebar-content {
            width: 250px;
            font-family: 'Segoe UI';
            background-color: #395161;
        }
        .streamlit-expander
        {
            border: none;
        }
        .streamlit-expanderHeader {
            color: black;
            text-shadow: 5px;
            background-color:#7194da;
            
        }
        .streamlit-expanderHeader:hover {
            color: black;
            background-color: #7194da;
        }

        .st-co{
            background-color:#7194da;
            color: black;
            text-shadow: 5px;
        }
        
        .e1ugi8lo1 .css-fblp2m .ex0cdmw0{
            color: #F9F0E6;
           
        }
    
        .stForm button:hover {
            background-color: #1e3d7b;
            color: white;
        }
        
        .stMarkdown {
            line-height: 1.5;
        }

        </style>
        """,
        unsafe_allow_html=True
    )