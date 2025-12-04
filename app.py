import streamlit as st
import pandas as pd
from collections import Counter


st.set_page_config(page_title="Rimini Street (CTF)", layout="wide")
st.write("## RIMINI STREET (CTF)")


# preprocess data and cache it
@st.cache_data
def load_data():
    df = pd.read_csv("dataset.csv", dtype=str)
    df['dateAdded'] = pd.to_datetime(df['dateAdded'], errors='coerce')
    df['dueDate'] = pd.to_datetime(df['dueDate'], errors='coerce')
    df['knownRansomwareCampaignUse'] = df['knownRansomwareCampaignUse'].fillna('No')
    return df


# laod data returns the preprocessed df
df = load_data()



tab1, tab2 = st.tabs(["CVE Analysis", "Trends & Statistics"])


# Individual CVE analysis
with tab1:
    st.header("Individual CVE Analysis")
    cve_input = st.text_input("Enter CVE ID (e.g., CVE-2020-0601)")
    if cve_input:
        row = df[df['cveID'].str.upper() == cve_input.strip().upper()]
        if not row.empty:
            rec = row.iloc[0]
            st.markdown(f"### {rec.cveID}")
            st.write(f"**Vendor/Project:** {rec.vendorProject}")
            st.write(f"**Product:** {rec.product}")
            st.write(f"**Vulnerability Name:** {rec.vulnerabilityName}")
            st.write(f"**Date Added:** {rec.dateAdded}")
            st.write(f"**Due Date:** {rec.dueDate}")
            st.write(f"**CWE(s):** {rec.cwes}")
            st.write(f"**Known Ransomware Use:** {rec.knownRansomwareCampaignUse}")
            st.write(f"**Required Action:** {rec.requiredAction}")
            st.write(f"**Short Description:** {rec.shortDescription}")
            st.write("**Notes:**", rec.notes)
        else:
            st.warning("CVE not found.")



# Trend & Statistics
with tab2:
    st.header("Trends & Statistics")
    vendor = st.text_input("Filter by Vendor/Project (partial or full match)")
    product = st.text_input("Filter by Product (partial or full match)")
    keyword = st.text_input("Search in Vulnerability Name or Description")
    ransomware_only = st.checkbox("Known Ransomware Campaign Use only", value=False)


    # Filter df
    filtered = df.copy()
    if vendor:
        filtered = filtered[filtered['vendorProject'].str.contains(vendor, case=False, na=False)]

    if product:
        filtered = filtered[filtered['product'].str.contains(product, case=False, na=False)]

    if keyword:
        filtered = filtered[
            filtered['vulnerabilityName'].str.contains(keyword, case=False, na=False) |
            filtered['shortDescription'].str.contains(keyword, case=False, na=False)
        ]
    if ransomware_only:
        filtered = filtered[filtered['knownRansomwareCampaignUse'].str.lower() == 'yes']


    st.write(f"**{len(filtered)} vulnerabilities match your filters.**")
    st.dataframe(filtered[['cveID','vendorProject','product','vulnerabilityName','dateAdded','cwes','knownRansomwareCampaignUse']])


    st.subheader("Statistics")

    # Most used vendors/products
    st.write("**Top 10 Vendors**")
    st.bar_chart(filtered['vendorProject'].value_counts().head(10))
    st.write("**Top 10 Products**")
    st.bar_chart(filtered['product'].value_counts().head(10))


    # CWE frequency
    if "cwes" in filtered.columns:
        
        cwes_flat = filtered['cwes'].dropna().str.split(",")
        cwe_counter = Counter([cwe.strip() for sublist in cwes_flat for cwe in (sublist if isinstance(sublist, list) else [sublist]) if cwe and cwe.strip()])

        if cwe_counter:
            chart_df = pd.DataFrame(cwe_counter.most_common(10), columns=["CWE", "Count"])
            st.write("**Top CWE(s):**")
            st.bar_chart(chart_df.set_index("CWE"))
        else:
            st.info("No CWE data to chart.")

    # Vulnerability trend by dateAdded
    if not filtered['dateAdded'].isnull().all():
        st.write("**Vulnerabilities Added Over Time**")
        trend = filtered['dateAdded'].dt.to_period('M').value_counts().sort_index()
        trend.index = trend.index.to_timestamp()
        st.line_chart(trend)
    else:
        st.info("No dateAdded data to plot trend.")

    # Known ransomware stats
    ransomware_count = (filtered['knownRansomwareCampaignUse'].str.lower() == "yes").sum()
    st.metric("Known Ransomware CVEs in result", ransomware_count)