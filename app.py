import streamlit as st
import pandas as pd

# Título do app
st.title("Análise Gravimétrica de Resíduos")

# Upload da tabela
uploaded_file = st.file_uploader("Envie um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("### Prévia dos dados carregados:")
    st.dataframe(df.head())
    
    # Seleção de UF e Unidade
    ufs = st.multiselect("Selecione as UFs", df["UF"].unique())
    unidades = st.multiselect("Selecione as Unidades de Tratamento", df["Unidade"].unique())
    
    # Filtrando os dados
    if ufs and unidades:
        df_filtered = df[(df["UF"].isin(ufs)) & (df["Unidade"].isin(unidades))]
    elif ufs:
        df_filtered = df[df["UF"].isin(ufs)]
    elif unidades:
        df_filtered = df[df["Unidade"].isin(unidades)]
    else:
        df_filtered = df
    
    st.write("### Dados Filtrados:")
    st.dataframe(df_filtered)
    
    # Criando abas para visualização
    tab1, tab2, tab3, tab4 = st.tabs(["Resíduos Urbanos", "Resíduos de Construção", "Redução de Peso", "Valor Energético"])
    
    # Separação por categorias
    residuos_urbanos = ["Papel/Papelão", "Plásticos", "Vidros", "Metais", "Orgânicos"]
    residuos_construcao = ["Concreto", "Argamassa", "Tijolo", "Madeira", "Papel", "Plástico", "Metal", 
                           "Material agregado", "Terra bruta", "Pedra", "Caliça Retida", "Caliça Peneirada", 
                           "Cerâmica", "Material orgânico e galhos", "Outros", "Outros Processados"]
    reducao_peso = ["Redução Peso Seco", "Redução Peso Líquido"]
    valor_energetico = ["Valor energético (MJ/ton)"]
    
    with tab1:
        st.write("### Resíduos Urbanos")
        st.bar_chart(df_filtered[residuos_urbanos])
    
    with tab2:
        st.write("### Resíduos de Construção")
        st.bar_chart(df_filtered[residuos_construcao])
    
    with tab3:
        st.write("### Redução de Peso")
        st.bar_chart(df_filtered[reducao_peso])
    
    with tab4:
        st.write("### Valor Energético")
        st.bar_chart(df_filtered[valor_energetico])
