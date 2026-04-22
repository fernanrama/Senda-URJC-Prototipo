from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "senda-urjc-prototipo-secret"

ALLOWED_DOMAINS = ("@urjc.es", "@alumnos.urjc.es")
INCIDENCIA_TYPES = (
    "Farola fundida",
    "Zona solitaria/miedo",
    "Obstáculo en la vía",
    "Punto con dificultad",
)

# In-memory store for the prototype.
incidencias_db = []


def is_valid_urjc_email(email: str) -> bool:
    """Allow only institutional URJC email domains."""
    normalized = email.strip().lower()
    return normalized.endswith(ALLOWED_DOMAINS)


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        if not email or not password:
            error = "Por favor, completa todos los campos."
        elif not is_valid_urjc_email(email):
            error = "Solo se permiten correos institucionales @urjc.es o @alumnos.urjc.es."
        else:
            # Prototype login: store minimal user data in session.
            session["user"] = {
                "nombre": email.split("@")[0],
                "correo": email.strip().lower(),
                "rol": "estudiante",
            }
            return redirect(url_for("dashboard"))

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=user)


@app.route("/voy-contigo")
def voy_contigo():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    return render_template("voy_contigo.html", user=user)


@app.route("/reportar-incidencia", methods=["GET", "POST"])
def reportar_incidencia():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))

    error = None

    if request.method == "POST":
        tipo = request.form.get("tipo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()

        if tipo not in INCIDENCIA_TYPES:
            error = "Selecciona un tipo de incidencia válido."
        elif not descripcion:
            error = "La descripción es obligatoria."
        else:
            incidencias_db.append(
                {
                    "tipo": tipo,
                    "descripcion": descripcion,
                    "estado": "En Revisión",
                }
            )
            return redirect(url_for("reportar_incidencia"))

    return render_template(
        "reportar_incidencia.html",
        user=user,
        incidencias=incidencias_db,
        tipos_incidencia=INCIDENCIA_TYPES,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
