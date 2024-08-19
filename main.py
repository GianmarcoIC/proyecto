
import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configurar Supabase
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Sistema de Gestión de Almacén")

# Función para mostrar productos
def mostrar_productos():
    data = supabase.table('productos').select('*').execute()
    df = pd.DataFrame(data.data)
    st.write(df)

# Funciones CRUD
def crear_producto(nombre, cantidad, categoria_id):
    supabase.table('productos').insert({'nombre': nombre, 'cantidad': cantidad, 'categoria_id': categoria_id}).execute()

def actualizar_producto(id, nombre, cantidad, categoria_id):
    supabase.table('productos').update({'nombre': nombre, 'cantidad': cantidad, 'categoria_id': categoria_id}).eq('id', id).execute()

def eliminar_producto(id):
    supabase.table('productos').delete().eq('id', id).execute()

# Interfaz de usuario
st.sidebar.header("Operaciones CRUD")
opcion = st.sidebar.selectbox("Selecciona una operación", ["Ver Productos", "Agregar Producto", "Actualizar Producto", "Eliminar Producto"])

if opcion == "Ver Productos":
    mostrar_productos()

elif opcion == "Agregar Producto":
    nombre = st.sidebar.text_input("Nombre del Producto")
    cantidad = st.sidebar.number_input("Cantidad", min_value=0)
    categoria_id = st.sidebar.text_input("ID de la Categoría")
    if st.sidebar.button("Agregar"):
        crear_producto(nombre, cantidad, categoria_id)
        st.success("Producto agregado con éxito!")
        mostrar_productos()

elif opcion == "Actualizar Producto":
    id = st.sidebar.text_input("ID del Producto")
    nombre = st.sidebar.text_input("Nuevo Nombre del Producto")
    cantidad = st.sidebar.number_input("Nueva Cantidad", min_value=0)
    categoria_id = st.sidebar.text_input("Nuevo ID de la Categoría")
    if st.sidebar.button("Actualizar"):
        actualizar_producto(id, nombre, cantidad, categoria_id)
        st.success("Producto actualizado con éxito!")
        mostrar_productos()

elif opcion == "Eliminar Producto":
    id = st.sidebar.text_input("ID del Producto")
    if st.sidebar.button("Eliminar"):
        eliminar_producto(id)
        st.success("Producto eliminado con éxito!")
        mostrar_productos()
