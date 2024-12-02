import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialisierung des Session States für Daten und Modalfenster
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"
    ])
if "show_window" not in st.session_state:
    st.session_state.show_window = False  # Status des Fensters

# CSS für modales Fenster
st.markdown("""
    <style>
    .modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
        z-index: 10;
        border-radius: 10px;
    }
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.6);
        z-index: 9;
    }
    </style>
""", unsafe_allow_html=True)

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

# Button zum Öffnen des Eingabefensters
if st.button("Eingabe Sattelhals"):
    st.session_state.show_window = True  # Fenster anzeigen

# Simuliertes Fenster (Modal)
if st.session_state.show_window:
    st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)  # Hintergrund-Overlay

    # Inhalt des Fensters
    st.markdown('<div class="modal">', unsafe_allow_html=True)
    st.subheader("Eingabe Sattelhals")

    # Eingabeformular
    with st.form("sattelhals_form"):
        fin = st.text_input("FIN")
        produktvariante = st.selectbox("Produktvariante", ["Standard", "RoRo", "Co2"])
        im_takt = st.radio("Im Takt gefertigt?", ["Ja", "Nein"], horizontal=True)
        fehlercode = st.selectbox("Fehlercode", ["Keine", "Technische Störung", "Zündfehler", "Sonstiges"])
        bemerkung = st.text_area("Bemerkung")
        qualität = st.radio("Qualität", ["i.O.", "e.i.O.", "n.i.O."], horizontal=True)
        meldezeit = st.time_input("Meldezeit", value=datetime.now().time())
        taktzeit = st.text_input("Taktzeit", value="00:25:30")

        # Buttons im Fenster
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Eintrag hinzufügen")
        with col2:
            canceled = st.form_submit_button("Abbrechen")

        # Aktionen bei Button-Klick
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

    st.markdown('</div>', unsafe_allow_html=True)

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
