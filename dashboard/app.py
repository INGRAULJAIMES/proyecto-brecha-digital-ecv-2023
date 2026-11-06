import sys
import os
from pathlib import Path

# Añadir la raíz del proyecto al sys.path para que Streamlit Cloud encuentre 'dashboard'
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import plotly.express as px
from dashboard.data_loader import get_validated_data, DataValidationError
from dashboard.config import CLUSTER_NAMES


st.set_page_config(page_title="Brecha Digital Colombia", layout="wide", page_icon="📊")

def main():
    st.title("📊 Dashboard: Brecha Digital en Colombia (ECV 2023)")
    st.markdown("Herramienta interactiva para la focalización multidimensional de política pública.")

    try:
        df = get_validated_data()
    except DataValidationError as e:
        st.error(f"**Error de datos:** {e}")
        st.stop()
    except Exception as e:
        st.error("**Error inesperado:** No se pudieron cargar los datos. Contacta al administrador.")
        st.exception(e)
        st.stop()

    st.sidebar.header("Navegación")
    vista = st.sidebar.radio(
        "Selecciona una vista:",
        ["📊 Impacto de Negocio", "🔬 Rigor Estadístico", "📂 Explorador de Perfiles"]
    )

    if vista == "📊 Impacto de Negocio":
        st.header("Impacto de Focalización y Ahorro Potencial")
        col1, col2, col3 = st.columns(3)
        elite_pct = (df["Cluster"] == 3).mean() * 100
        excluidos_pct = df["Cluster"].isin([2, 5]).mean() * 100
        col1.metric("Élite Digital", f"{elite_pct:.1f}%", "Ya incluidos")
        col2.metric("Exclusión Severa", f"{excluidos_pct:.1f}%", "Sin smartphone")
        col3.metric("Brecha de Género", "15%", "Odds Ratio 0.85")

        conteo = df["Cluster_Nombre"].value_counts().reset_index()
        conteo.columns = ["Perfil", "Cantidad"]
        fig = px.bar(conteo, x="Perfil", y="Cantidad",
                     title="Distribución de la Población por Perfil",
                     color="Perfil")
        st.plotly_chart(fig, use_container_width=True)

    elif vista == "🔬 Rigor Estadístico":
        st.header("Métricas de Validación del Modelo")
        st.table({
            "Métrica": ["ARI (Bootstrap)", "ARI (K-Means vs GMM)", "F1-Macro (RF)", "Odds Ratio (Smartphone)"],
            "Valor": [0.9254, 0.7306, 0.52, 64.1],
            "Interpretación": ["Clústeres estables", "Concordancia algorítmica",
                               "La demografía no predice el clúster", "El hardware es la barrera principal"]
        })

    elif vista == "📂 Explorador de Perfiles":
        st.header("Explorador de Perfiles")
        st.sidebar.subheader("Filtros")

        cluster_options = df["Cluster_Nombre"].dropna().unique().tolist()
        cluster_filter = st.sidebar.multiselect("Perfil", cluster_options, default=cluster_options)

        estrato_options = df["Estrato_Categoria"].dropna().unique().tolist()
        estrato_filter = st.sidebar.multiselect("Estrato", estrato_options, default=estrato_options[:3])

        df_filtered = df[
            (df["Cluster_Nombre"].isin(cluster_filter)) &
            (df["Estrato_Categoria"].isin(estrato_filter))
        ]

        if df_filtered.empty:
            st.warning("No hay registros que cumplan con los filtros seleccionados.")
        else:
            st.dataframe(
                df_filtered[["Cluster_Nombre", "P6040", "P6020", "Estrato_Categoria", "P1082S2", "P1083S5"]],
                use_container_width=True
            )
            csv = df_filtered.to_csv(index=False).encode("utf-8")
            st.download_button("Descargar selección en CSV", csv, "perfiles_filtrados.csv", "text/csv")

if __name__ == "__main__":
    main()