import streamlit as st

# Bootstrap CSS einbinden
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        .input-area {
            margin-bottom: 0.1rem;
        }
        .header-background {
            background-color: #2196F3;
            padding: 10px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .header-background h3 {
            color: white;
            margin: 0;
        }
        .logo {
            max-width: 100%;
            height: auto;
        }
        .container-fluid {
            background-color: skyblue;
            padding: 20px;
        }
        .middle-text {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML für das Layout
st.markdown(
    """
    <div class="container-fluid">
        <div class="row">
            <!-- Logo Bereich -->
            <div class="col-4">
                <img src="https://via.placeholder.com/150" alt="Logo" class="logo" />
            </div>

            <!-- Titel und Auswahl -->
            <div class="col-8">
                <div class="header-background">
                    <h3>Produktionsdokumentation</h3>
                    <select class="form-select form-select-sm" aria-label="Arbeitsbereich auswählen">
                        <option selected>Arbeitsbereich wählen</option>
                        <option value="Sattelhals">Sattelhals</option>
                        <option value="Lackierung">Lackierung</option>
                    </select>
                </div>
            </div>
        </div>

        <!-- Eingabebereich -->
        <div class="row mt-4">
            <div class="col-md-6">
                <label for="startDate">Datum</label>
                <input id="startDate" class="form-control" type="date" />
            </div>
            <div class="col-md-6">
                <label for="startShift">Startzeit</label>
                <input id="startShift" class="form-control" type="time" />
            </div>
        </div>

        <!-- Schichtübersicht -->
        <div class="row mt-4">
            <div class="col-md-12 middle-text">
                Schichtübersicht
            </div>
        </div>

        <!-- Tabelle -->
        <div class="row mt-4">
            <div class="col-md-12">
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
                        <!-- Platzhalter für Tabellenzeilen -->
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
        </div>

        <!-- Buttons -->
        <div class="row mt-4">
            <div class="col-md-6">
                <button class="btn btn-primary w-100">Eingabe Sattelhals</button>
            </div>
            <div class="col-md-6">
                <button class="btn btn-danger w-100">Letzten Eintrag löschen</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
