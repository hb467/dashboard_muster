import streamlit as st
import pandas as pd
from datetime import datetime, time

# CSS-Styling für den blauen Hintergrund hinzufügen
st.markdown(
    """
    <style>
    .header {
        background-color: #2196F3; /* Blau */
        padding: 10px;
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

# Initialisierung des Session States für die Tabelle
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"
    ])

# Eingabeformulare für allgemeine Informationen
with st.form("general_form"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        datum = st.date_input("Datum", value=datetime.now())
    with col2:
        start = st.time_input("Start", value=time(14, 0))
    with col3:
        schicht = st.selectbox("Schicht", ["Früh", "Spät", "Nacht"])
    with col4:
        ende = st.time_input("Ende", value=time(22, 0))

    # Weitere Produktionsdaten
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        ausschuss = st.text_input("Ausschuss", value="0")
    with col6:
        schicht_soll = st.text_input("Schicht-SOLL", value="0")
    with col7:
        soll_aktuell = st.text_input("Soll Aktuell", value="0")
        ist_aktuell = st.text_input("Ist Aktuell", value="0")
    with col8:
        rückstand = st.text_input("Rückstand", value="0")
        direktläufer = st.text_input("Direktläufer", value="0")

    submitted_general = st.form_submit_button("Schichtdaten speichern")

# Eingabeformular für spezifische Daten
with st.form("entry_form"):
    st.subheader("Eingabe Sattelhals")
    fin = st.text_input("FIN")
    produktvariante = st.selectbox("Produktvariante", ["Standard", "RoRo", "Co2"])
    im_takt = st.radio("Im Takt gefertigt?", ["Ja", "Nein"], horizontal=True)
    fehlercode = st.selectbox("Fehlercode", ["Keine", "Technische Störung", "Zündfehler", "Sonstiges"])
    bemerkung = st.text_area("Bemerkung")
    qualität = st.radio("Qualität", ["i.O.", "e.i.O.", "n.i.O."], horizontal=True)
    meldezeit = st.time_input("Meldezeit", value=datetime.now().time())
    taktzeit = st.text_input("Taktzeit", value="00:25:30")

    submitted_entry = st.form_submit_button("Eintrag hinzufügen")

    if submitted_entry:
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

# Tabelle mit den Daten
st.subheader("Schichtübersicht")
st.table(st.session_state.data)

# Letzten Eintrag löschen
if st.button("Letzten Eintrag löschen"):
    if not st.session_state.data.empty:
        st.session_state.data = st.session_state.data.iloc[:-1]
        st.success("Letzter Eintrag gelöscht!")
    else:
        st.warning("Keine Einträge vorhanden!")
