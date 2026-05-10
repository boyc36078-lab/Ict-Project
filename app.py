import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- Header & Identification ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown(f"""
**Developer:** Saim Anwar  
**Roll Number:** 25-ME-107
""")
st.divider()

# --- Sidebar Navigation ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

# --- Material Density Data ---
# Density in kg/m^3
density_data = {
    "Material": ["Steel", "Aluminum", "Copper", "Cast Iron", "Titanium", "Gold", "Water", "Concrete", "Lead"],
    "Density (kg/m³)": [7850, 2700, 8960, 7200, 4500, 19300, 1000, 2400, 11340]
}
df = pd.DataFrame(density_data)

if option == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category", ["Length", "Mass", "Pressure", "Force"])
        value = st.number_input("Enter Value", value=1.0)

    # Conversion Logic
    if category == "Length":
        units = {"Meters": 1, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084}
    elif category == "Mass":
        units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Newtons (on Earth)": 9.806}
    elif category == "Pressure":
        units = {"Pascal (Pa)": 1, "Bar": 1e-5, "PSI": 0.000145038, "Atmosphere": 9.8692e-6}
    elif category == "Force":
        units = {"Newton (N)": 1, "Kilo-Newton (kN)": 0.001, "Pound-force (lbf)": 0.224809}

    with col2:
        from_unit = st.selectbox("From", list(units.keys()))
        to_unit = st.selectbox("To", list(units.keys()))

    # Calculation: Base Value = Input / (Unit Factor) -> Result = Base Value * (Target Factor)
    base_value = value / units[from_unit]
    result = base_value * units[to_unit]

    st.success(f"**Result:** {value} {from_unit} = {result:.4f} {to_unit}")

else:
    st.header("🔬 Material Density Checker")
    st.write("Search for common engineering materials to find their density.")
    
    search_query = st.text_input("Search Material (e.g., Steel, Copper)")
    
    if search_query:
        filtered_df = df[df['Material'].str.contains(search_query, case=False)]
        st.table(filtered_df)
    else:
        st.table(df)

    st.info("Note: Values provided are standard approximations at room temperature.")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.write("Created for Mechanical Engineering Project")
