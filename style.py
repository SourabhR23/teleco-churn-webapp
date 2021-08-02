import streamlit as st


# Streamlit Style Settings
def webapp_style():
    hide_streamlit_style = """
                <style>
                    .css-1kw01g3 {
                                background-color: rgb(9, 10, 10);
                                }
                    .css-euvo1l{
                                color: black;
                                }
                    a:link {
                            background-color: #f7f7f7;
                            text-decoration: underline;
                            }
                    h1 {
                        background-color: #3fb0ac;
                        }
                    #MainMenu {
                                visibility: none;
                                }
                    div.stButton > button:first-child{
                            background-color: #BE2F29;
                            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
                            }
                    footer {
                            visibility: hidden;
                            }
                    footer:after {
                                content:'Made by Sourabh Rasal ❤'; 
                                visibility: visible;
                                display: block;
                                position: relative;
                                text-align: center;
                                padding: 15px;
                                top: 2px;
                                }
    
                </style>
                """
    markdown = st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    return markdown