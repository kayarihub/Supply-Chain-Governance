import streamlit as st
import pandas as pd
from risk_assessment import main, ROOT
st.set_page_config(page_title="Supplier Governance", layout="wide")
main()
df = pd.read_csv(ROOT / "reports/risk_register.csv")
st.title("Supply Chain Governance | Risk Intelligence")
st.caption("Synthetic portfolio data • illustrative internal policy")
categories = st.multiselect("Category", sorted(df.category.unique()), default=sorted(df.category.unique()))
df = df[df.category.isin(categories)]
a,b,c,d = st.columns(4)
a.metric("Suppliers", len(df))
b.metric("Control pass rate", f"{(df.exceptions.eq(0).mean()*100):.1f}%" if len(df) else "N/A")
c.metric("High risk", int(df.tier.eq("High").sum()))
d.metric("Annual spend", f"${df.annual_spend.sum():,.0f}")
st.bar_chart(df.tier.value_counts())
st.subheader("Risk register")
st.dataframe(df.sort_values("score", ascending=False), hide_index=True)
st.download_button("Export risk register", df.to_csv(index=False), "risk_register.csv")
