import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialisierung des Session State für die Tabelle und das Modal
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"
    ])
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False  # Status des Modals

# Funktionen zum Öffnen und Schließen des Modals
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

# Simuliertes modales Fenster (wird angezeigt, wenn show_modal = True)
if st.session_state.show_modal:
    # Overlay für das Fenster
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

    # Modales Fenster
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
            text-align: left;
            width: 50%;">
        """,
        unsafe_allow_html=True
    )

    st.subheader("Eingabe Sattelhals")

    # Eingabeformular
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
            new_entry = {
                "FIN": fin,
                "Produktvariante": produktvariante,
                "Im Takt?": im_takt,
                "Fehlercode": fehlercode,
                "Bemerkung": bemerkung,
                "Qualität": qualität,
                "Meldezeit": str(meldezeit),
                "Taktzeit": taktzeit,
            }
            st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_entry])], ignore_index=True)
            st.success("Eintrag hinzugefügt!")
            close_modal()

        if canceled:
            close_modal()

    st.markdown("</div>", unsafe_allow_html=True)

# Tabelle mit den eingegebenen Daten
st.subheader("Schichtübersicht")
st.table(st.session_state.data)

# Letzten Eintrag löschen
if st.button("Letzten Eintrag löschen"):
    if not st.session_state.data.empty:
        st.session_state.data = st.session_state.data.iloc[:-1]
        st.success("Letzter Eintrag gelöscht!")
    else:
        st.warning("Keine Einträge vorhanden!")
