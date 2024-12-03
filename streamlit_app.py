import streamlit as st
import pandas as pd
from datetime import datetime, time

# Erweiterte Darstellung einstellen
st.set_page_config(layout="wide", page_title="Produktionsdokumentation")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"
    ])
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False  # Status für das Anzeigen des Modals

# CSS-Styling für modale Eingabe und Header
st.markdown(
    """
    <style>
    .header {
        background-color: #2196F3; /* Blau */
        padding: 5px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .header img {
        max-width: 150px;
    }
    .header h1 {
        color: white;
        margin-left: 20px;
        font-size: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header mit Logo und Titel
st.markdown(
    """
    <div class="header">
        <img src="https://www.brueggen.com/fileadmin/_processed_/6/1/csm_logo_c6de901564.png" alt="Logo">
        <h1>Produktionsdokumentation</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Allgemeine Eingaben für Datum, Zeit und Schicht
col1, col2, col3, col4 = st.columns(4)
with col1:
    datum = st.date_input("Datum", value=datetime.now())
with col2:
    start = st.time_input("Start", value=time(14, 0))
with col3:
    schicht = st.selectbox("Schicht", ["Früh", "Spät", "Nacht"])
with col4:
    ende = st.time_input("Ende", value=time(22, 0))

# Button: "Eingabe Sattelhals"
if st.button("Eingabe Sattelhals"):
    st.session_state.show_modal = True  # Modal anzeigen

# Modal für die Eingabe, wenn der Button geklickt wird
if st.session_state.show_modal:
    with st.form("sattelhals_form"):
        st.subheader("Eingabe Sattelhals")
        fin = st.text_input("FIN")
        produktvariante = st.selectbox("Produktvariante", ["Standard", "RoRo", "Co2"])
        im_takt = st.radio("Im Takt gefertigt?", ["Ja", "Nein"], horizontal=True)
        fehlercode = st.selectbox("Fehlercode", ["Keine", "Technische Störung", "Zündfehler", "Sonstiges"])
        bemerkung = st.text_area("Bemerkung")
        qualität = st.radio("Qualität", ["i.O.", "e.i.O.", "n.i.O."], horizontal=True)
        meldezeit = st.time_input("Meldezeit", value=datetime.now().time())
        taktzeit = st.text_input("Taktzeit", value="00:25:30")

        # Buttons im Modal
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Eintrag hinzufügen")
        with col2:
            cancel = st.form_submit_button("Abbrechen")

        # Eintrag hinzufügen
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
            st.session_state.show_modal = False  # Modal schließen

        # Modal schließen, wenn Abbrechen gedrückt wird
        if cancel:
            st.session_state.show_modal = False

# Tabelle mit den eingegebenen Daten
st.markdown(
    """
    <div style="text-align: center;">
        <h3>Schichtübersicht</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.table(st.session_state.data)

# Letzten Eintrag löschen
if st.button("Letzten Eintrag löschen"):
    if not st.session_state.data.empty:
        st.session_state.data = st.session_state.data.iloc[:-1]
        st.success("Letzter Eintrag gelöscht!")
    else:
        st.warning("Keine Einträge vorhanden!")

