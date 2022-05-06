from click import style


try:
    import requests
    from streamlit_lottie import st_lottie
    import streamlit as st
    import pandas as pd
    from streamlit_option_menu import option_menu
    from db import create_table,add_data,view

    st.set_page_config(page_title="Doctor's Page", page_icon=":doctor:", layout="wide")

    def main():
        selected = option_menu(
            menu_title=None,
            options=["Home","Profile","Prescribe","Recommend","Publications"],
            icons=['house','person','file-medical','people','book'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
            "container": {"padding": "6!important", "background-color": None, "max-width": "100%", "max-height": "100%"},
            "icon": {"color": "white", "font-size": "35px", }, 
            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"3px", "--hover-color": "green"},
            "nav-link-selected": {"background-color": "green"},
            },
        )

        create_table()
        if selected == "Home":
            st.header("Prescription History")
            history = view()
            st.write(history)

        if selected == "Prescribe":
            st.subheader("Prescribe")
            col1,col2,col3,col4,col5= st.columns(5)
            with col1:
                dates = st.date_input("Prescription Date")

            with col2:
                patient_ID = st.text_area("Patient ID")

            with col3:
                prescription = st.text_area("Prescription")

            with col4:
                diagnosis = st.text_area("Diagnosis")

            with col5:
                recommendation = st.text_area("Recommendation")

            if st.button("Prescribe"):
                add_data(dates,patient_ID,prescription,diagnosis,recommendation)
                st.success("Done")

    if __name__ == '__main__':
        main()

except Exception as e: 
    print(e)