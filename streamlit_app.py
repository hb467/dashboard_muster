import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialdaten (leere Tabelle)
if "entries" not in st.session_state:
    st.session_state.entries = pd.DataFrame(
        columns=["FIN", "Produktvariante", "Im Takt?", "Fehlercode", "Bemerkung", "Qualität", "Meldezeit", "Taktzeit"]
    )

# Layout und Titel
st.image("https://www.brueggen.com/fileadmin/_processed_/6/1/csm_logo_c6de901564.png", width=300)
st.title("Produktionsdokumentation")

# Spalten für Eingaben
col1, col2, col3, col4 = st.columns(4)

with col1:
    datum = st.date_input("Datum", value=datetime.now())
with col2:
    start = st.time_input("Start", value=time(14, 0))
with col3:
    schicht = st.selectbox("Schicht", ["Früh", "Spät", "Nacht"])
with col4:
    ende = st.time_input("Ende", value=time(22, 0))

# Weitere Eingaben
col5, col6, col7, col8 = st.columns(4)

with col5:
    ausschuss = st.text_input("Ausschuss", value="Ausschuss")
with col6:
    schicht_soll = st.text_input("Schicht-SOLL", value="Schicht-SOLL")
    soll_aktuell = st.text_input("Soll Aktuell", value="Soll Aktuell")
with col7:
    ist_aktuell = st.text_input("Ist Aktuell", value="Ist Aktuell")
    rückstand = st.text_input("Rückstand", value="Rückstand")
with col8:
    direktläufer = st.text_input("Direktläufer", value="Direktläufer")

# Eingabebereich für neue Daten
st.header("Eingabe Sattelhals")
with st.form("entry_form"):
    fin = st.text_input("FIN")
    produktvariante = st.selectbox("Produktvariante", ["Standard", "RoRo", "Co2"])
    im_takt = st.radio("Im Takt gefertigt?", ["Ja", "Nein"], horizontal=True)
    fehlercode = st.selectbox("Fehlercode", ["Keine", "Technische Störung", "Zündfehler", "Sonstiges"])
    bemerkung = st.text_area("Bemerkung")
    qualität = st.radio("Qualität", ["i.O.", "e.i.O.", "n.i.O."], horizontal=True)
    meldezeit = st.time_input("Meldezeit", value=datetime.now().time())
    taktzeit = st.text_input("Taktzeit", value="00:25:30")
    submitted = st.form_submit_button("Eintrag hinzufügen")

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
        st.session_state.entries = pd.concat([st.session_state.entries, pd.DataFrame([new_entry])], ignore_index=True)
        st.success("Eintrag hinzugefügt!")

# Tabelle anzeigen
st.header("Schichtübersicht")
st.table(st.session_state.entries)

# Letzten Eintrag löschen
if st.button("Letzten Eintrag löschen"):
    if not st.session_state.entries.empty:
        st.session_state.entries = st.session_state.entries.iloc[:-1]
        st.success("Letzter Eintrag gelöscht!")
    else:
        st.warning("Keine Einträge vorhanden!")

