#Interfaz
import streamlit as st
from equipos import cargar_datos, guardar_datos, Equipo, Criticidad

st.title("Registro de Equipos Biomédicos")
st.write("Bienvenido al sistema de registro - CMQ MORENO")

st.divider()


if "equipos" not in st.session_state:
    st.session_state.equipos = cargar_datos()


st.subheader("Agregar equipo")
nombre = st.text_input("Nombre del equipo")
serie = st.text_input("Número de serie")
estado = st.selectbox("¿Está operativo?", ["Seleccionar", "Sí", "No"])
criticidad = st.selectbox("Criticidad del equipo", ["Seleccionar", "Alta", "Media", "Baja"])
criticidad_justificacion = st.text_input("Justificación de la criticidad")
proximo_mantenimiento = st.date_input("Próximo mantenimiento programado")

if st.button("Registrar equipo"):
    if nombre and serie and estado != "Seleccionar" and criticidad != "Seleccionar" and criticidad_justificacion:
        st.session_state.equipos.append(Equipo(
            nombre=nombre,
            serie=serie,
            estado=estado,
            criticidad=Criticidad(criticidad),
            criticidad_justificacion=criticidad_justificacion,
            proximo_mantenimiento=str(proximo_mantenimiento)
        ))
        guardar_datos(st.session_state.equipos)
        estado_texto = "Operativo" if estado.lower() in ["si", "sí"] else "Requiere mantenimiento"
        st.success(f"{nombre} - S/N: {serie} registrado correctamente como {estado_texto}")

st.divider()
st.subheader("Resumen")


equipos = st.session_state.equipos
if equipos:
    operativos = [e for e in equipos if e.estado.lower() in ["si", "sí"]]
    mantenimiento = [e for e in equipos if e.estado.lower() not in ["si", "sí"]]

    col1, col2 = st.columns(2)
    col1.metric("Operativos", f"{len(operativos)} ({len(operativos)/len(equipos)*100: .1f}%)")
    col2.metric("Requieren mantenimiento", f"{len(mantenimiento)} ({len(mantenimiento)/len(equipos)*100: .1f}%)")

    st.subheader("Lista de equipos")
    equipos_display = []
    for e in equipos:
        equipos_display.append({
            "Nombre": e.nombre,
            "Serial number": e.serie,
            "Estado": "Operativo" if e.estado.lower() in ["si", "sí"] else "Requiere mantenimiento"
        })
    st.table(equipos_display)
else:
    st.info("Aún no hay equipos registrados.")