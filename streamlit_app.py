import streamlit as st

# Bootstrap CSS einbinden
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        .header {
            background-color: #2196F3;
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        .table-container {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Kopfzeile
st.markdown(
    """
    <div class="header">
        <h1>Produktionsdokumentation</h1>
        <p>Wählen Sie die Arbeitsbereiche und geben Sie die Daten ein.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Eingabebereich
st.markdown(
    """
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <label for="startDate">Datum</label>
                <input id="startDate" class="form-control" type="date" />
            </div>
            <div class="col-md-6">
                <label for="startShift">Startzeit</label>
                <input id="startShift" class="form-control" type="time" />
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-6">
                <label for="shift">Schicht</label>
                <select id="shift" class="form-select">
                    <option value="Früh">Früh</option>
                    <option value="Spät">Spät</option>
                    <option value="Nacht">Nacht</option>
                </select>
            </div>
            <div class="col-md-6">
                <label for="endShift">Endzeit</label>
                <input id="endShift" class="form-control" type="time" />
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Tabellenbereich
st.markdown(
    """
    <div class="container table-container">
        <h2>Schichtübersicht</h2>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>FIN</th>
                    <th>Produktvariante</th>
                    <th>Im Takt?</th>
                    <th>Fehlercode</th>
                    <th>Bemerkung</th>
                    <th>Qualität</th>
                    <th>Meldezeit</th>
                    <th>Taktzeit</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>123456</td>
                    <td>Standard</td>
                    <td>Ja</td>
                    <td>Keine</td>
                    <td>Alles OK</td>
                    <td>i.O.</td>
                    <td>14:00</td>
                    <td>00:25:30</td>
                </tr>
            </tbody>
        </table>
    </div>
    """,
    unsafe_allow_html=True,
)

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("Eingabe Sattelhals")
with col2:
    st.button("Letzten Eintrag löschen")
