import streamlit as st
import pandas as pd
import os

# --- File to store data ---
DATA_FILE = 'research_profiles.csv'

# --- Load existing data or create new ---
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=[
        "Full Name", "Designation", "Department", "Institute",
        "Email", "Phone", "Google Scholar", "Scopus", "ResearchGate",
        "ORCID", "Web of Science", "Vidwan"
    ])
    df.to_csv(DATA_FILE, index=False)

# --- Title ---
st.title("🎓 Online Research Profile Manager")

# --- Tabs for navigation ---
tab1, tab2, tab3 = st.tabs(["Create / Update Profile", "View All Profiles", "Delete Profile"])

# --- Tab 1: Create or Update Profile ---
with tab1:
    st.subheader("➕ Add or Update Researcher Profile")
    name = st.text_input("Full Name")
    designation = st.text_input("Designation")
    department = st.text_input("Department")
    institute = st.text_input("Institute")
    email = st.text_input("E-Mail ID")
    phone = st.text_input("Phone Number")

    st.markdown("**Platform URLs**")
    scholar = st.text_input("Google Scholar")
    scopus = st.text_input("Scopus")
    researchgate = st.text_input("ResearchGate")
    orcid = st.text_input("ORCID")
    wos = st.text_input("Web of Science")
    vidwan = st.text_input("Vidwan")

    if st.button("Save / Update"):
        new_data = {
            "Full Name": name,
            "Designation": designation,
            "Department": department,
            "Institute": institute,
            "Email": email,
            "Phone": phone,
            "Google Scholar": scholar,
            "Scopus": scopus,
            "ResearchGate": researchgate,
            "ORCID": orcid,
            "Web of Science": wos,
            "Vidwan": vidwan
        }

        # Check if profile exists
        if name in df["Full Name"].values:
            df.loc[df["Full Name"] == name] = new_data
            st.success("Profile updated successfully.")
        else:
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            st.success("Profile created successfully.")

        df.to_csv(DATA_FILE, index=False)

# --- Tab 2: View Profiles ---
with tab2:
    st.subheader("🔍 Researcher Profiles")
    st.dataframe(df, use_container_width=True)

# --- Tab 3: Delete Profile ---
with tab3:
    st.subheader("❌ Delete a Researcher Profile")
    names = df["Full Name"].tolist()
    name_to_delete = st.selectbox("Select Profile to Delete", names)

    if st.button("Delete Profile"):
        df = df[df["Full Name"] != name_to_delete]
        df.to_csv(DATA_FILE, index=False)
        st.success(f"Profile of {name_to_delete} deleted successfully.")
