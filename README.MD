# Prototipo Senda URJC

Este repositorio contiene el prototipo evolutivo desarrollado para la práctica de la asignatura **Análisis e Ingeniería de Requisitos**. 

El objetivo de este código no es ser una aplicación de producción, sino una **Prueba de Concepto (PoC)** que demuestra la trazabilidad y viabilidad de los requisitos funcionales y el modelado UML definidos en la Especificación de Requisitos Software (ERS).

## Funcionalidades Implementadas

* **Simulación SSO URJC (RF1):** Validación de credenciales en el login restringida exclusivamente a dominios `@urjc.es` y `@alumnos.urjc.es`.
* **Modo "Voy Contigo" (RF33, RF35):** Máquina de estados simulada en JavaScript que representa el flujo de monitorización: `Ruta Activa` -> `Prealerta (30s)` -> `Alerta/Confirmación`.
* **Gestión de Incidencias (RF15):** Formulario tipificado y listado de anomalías en el entorno (farolas fundidas, zonas solitarias, obstáculos y puntos con dificultad) con persistencia en memoria.

## Tecnologías Utilizadas

* **Backend:** Python 3 + Flask (Estructura de enrutamiento y lógica de negocio).
* **Frontend:** HTML5, CSS3 (Bootstrap) y JavaScript (Lógica de estados en el cliente).
* **IA Generativa:** Codex / VS Code (Desarrollo iterativo guiado por prompts documentados en la memoria de la práctica).

## Instrucciones de Despliegue y Ejecución

1. **Clonar el repositorio:**
   Abre tu terminal y ejecuta:
   ```bash
   git clone https://github.com/fernanrama/Senda-URJC-Prototipo.git
   cd SendaURJC_Prototipo
   ```

2. **Instalar dependencias:**
   Asegúrate de tener Python instalado en tu sistema. Luego instala el framework Flask:
   ```bash
   pip install flask
   ```

3. **Ejecutar el servidor local:**
   Inicia la aplicación ejecutando el archivo principal:
   ```bash
   python app.py
   ```

4. **Acceso al prototipo:**
   Abre tu navegador web de preferencia y dirígete a la siguiente dirección:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)