import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rugby Master Platform", layout="wide")
df = pd.read_csv("season_stats.csv")

st.title("🏆 Super Rugby Master Platform")

# Highlight the Matchup Boosts
st.subheader("Tactical Player Matrix")
st.dataframe(
    df.style.background_gradient(subset=['Priority_Score'], cmap='RdYlGn')
    .highlight_max(subset=['Matchup_Bonus'], color='#2e7d32'),
    use_container_width=True
)

st.info("💡 Green Highlights in 'Matchup_Bonus' indicate players facing weak defensive structures this round.")