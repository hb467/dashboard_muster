import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialisierung des Session States für die Tabelle und das "Fenster"
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"
    ])
if "show_window" not in st.session_state:
    st.session_state.show_window = False  # Status für das Anzeigen des "Fensters"

# Header mit Logo und Titel
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:5px; text-align:center;">
        <img src="https://www.brueggen.com/fileadmin/_processed_/6/1/csm_logo_c6de901564.png" alt="Logo" style="max-width:150px;">
        <h1 style="color:white; margin: 0;">Produktionsdokumentation</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Button zum Öffnen des "Fensters"
if st.button("Eingabe Sattelhals"):
    st.session_state.show_window = True  # Fenster anzeigen

# Dynamisches "Fenster" mit Eingabeinformationen
if st.session_state.show_window:
    st.subheader("Eingabe Sattelhals")
    with st.form("sattelhals_form"):
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

        # Aktionen bei Klick
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
            st.session_state.show_window = False  # Fenster schließen

        if canceled:
            st.session_state.show_window = False  # Fenster schließen

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
