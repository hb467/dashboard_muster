import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialisierung des Session State für das Modal
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False  # Modal-Fenster-Status

# Funktion zum Öffnen und Schließen des Modals
def open_modal():
    st.session_state.show_modal = True

def close_modal():
    st.session_state.show_modal = False

# Header mit Titel und Button
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:5px; text-align:center;">
        <h1 style="color:white; margin:0;">Produktionsdokumentation</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Button: Öffnet das Modal
if st.button("Eingabe Sattelhals"):
    open_modal()

# Modal-Fenster-Inhalt (simuliert)
if st.session_state.show_modal:
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); 
                    position: fixed; 
                    top: 0; left: 0; 
                    width: 100%; height: 100%; 
                    z-index: 9;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            position: fixed; 
            top: 50%; left: 50%; 
            transform: translate(-50%, -50%);
            background-color: white; 
            padding: 20px; 
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); 
            z-index: 10; 
            border-radius: 10px; 
            text-align: center;
            width: 50%;">
            <h2>Eingabe Sattelhals</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Eingabeformular im "Modal"
    with st.form("sattelhals_form", clear_on_submit=True):
        fin = st.text_input("FIN")
        produktvariante = st.selectbox("Produktvariante", ["Standard", "RoRo", "Co2"])
        im_takt = st.radio("Im Takt gefertigt?", ["Ja", "Nein"], horizontal=True)
        fehlercode = st.selectbox("Fehlercode", ["Keine", "Technische Störung", "Zündfehler", "Sonstiges"])
        bemerkung = st.text_area("Bemerkung")
        qualität = st.radio("Qualität", ["i.O.", "e.i.O.", "n.i.O."], horizontal=True)
        meldezeit = st.time_input("Meldezeit", value=datetime.now().time())
        taktzeit = st.text_input("Taktzeit", value="00:25:30")

        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Eintrag hinzufügen")
        with col2:
            canceled = st.form_submit_button("Abbrechen")

        # Aktionen
        if submitted:
            st.success("Eintrag hinzugefügt!")
            close_modal()

        if canceled:
            close_modal()

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <small>&copy; 2024 Produktionsdokumentation</small>
    </div>
    """,
    unsafe_allow_html=True
)
