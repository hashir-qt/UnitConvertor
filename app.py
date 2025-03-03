import streamlit as st # type: ignore

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

def main():
    st.set_page_config(page_title="Unit Convertor", layout='wide')
    st.title("Unit Converter")
    
    categories = {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701,
            "Nautical Mile": 0.000539957
        },
        "Weight": {
            "Kilogram": 1,
            "Gram": 1000,
            "Milligram": 1e6,
            "Pound": 2.20462,
            "Ounce": 35.274,
            "Ton": 0.001
        },
        "Temperature": "special",
        "Volume": {
            "Liter": 1,
            "Milliliter": 1000,
            "Cubic Meter": 0.001,
            "Gallon": 0.264172,
            "Quart": 1.05669,
            "Pint": 2.11338,
            "Cup": 4.22675,
            "Fluid Ounce": 33.814
        },
        "Speed": {
            "Meters per second": 1,
            "Kilometers per hour": 3.6,
            "Miles per hour": 2.23694,
            "Feet per second": 3.28084,
            "Knots": 1.94384
        },
        "Time": {
            "Second": 1,
            "Minute": 1/60,
            "Hour": 1/3600,
            "Day": 1/86400,
            "Week": 1/604800,
            "Month": 1/2.628e+6,
            "Year": 1/3.154e+7
        },
        "Area": {
            "Square Meter": 1,
            "Square Kilometer": 0.000001,
            "Square Mile": 3.861e-7,
            "Square Yard": 1.19599,
            "Square Foot": 10.7639,
            "Square Inch": 1550
        },
        "Fuel Economy": {
            "Kilometers per Liter": 1,
            "Miles per Gallon": 2.35215
        },
        "Pressure": {
            "Pascal": 1,
            "Bar": 1e-5,
            "PSI": 0.000145038
        },
        "Data Transfer Rate": {
            "Bits per Second": 1,
            "Kilobits per Second": 0.001,
            "Megabits per Second": 1e-6,
            "Gigabits per Second": 1e-9
        },
        "Digital Storage": {
            "Bit": 1,
            "Byte": 0.125,
            "Kilobyte": 0.000125,
            "Megabyte": 1.25e-7,
            "Gigabyte": 1.25e-10,
            "Terabyte": 1.25e-13
        },
        "Energy": {
            "Joule": 1,
            "Kilojoule": 0.001,
            "Calorie": 0.239006,
            "Kilocalorie": 0.000239006,
            "Watt-hour": 0.000277778
        },
        "Frequency": {
            "Hertz": 1,
            "Kilohertz": 0.001,
            "Megahertz": 1e-6,
            "Gigahertz": 1e-9
        },
        "Plane Angle": {
            "Degree": 1,
            "Radian": 0.0174533,
            "Gradian": 1.11111
        }
    }
    
    category = st.selectbox("Select category", list(categories.keys()))
    
    if category == "Temperature":
        temp_value = st.number_input("Enter value", value=0.0, format="%.2f")
        temp_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        temp_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
        if temp_from == temp_to:
            result = temp_value
        elif temp_from == "Celsius" and temp_to == "Fahrenheit":
            result = (temp_value * 9/5) + 32
        elif temp_from == "Celsius" and temp_to == "Kelvin":
            result = temp_value + 273.15
        elif temp_from == "Fahrenheit" and temp_to == "Celsius":
            result = (temp_value - 32) * 5/9
        elif temp_from == "Fahrenheit" and temp_to == "Kelvin":
            result = (temp_value - 32) * 5/9 + 273.15
        elif temp_from == "Kelvin" and temp_to == "Celsius":
            result = temp_value - 273.15
        elif temp_from == "Kelvin" and temp_to == "Fahrenheit":
            result = (temp_value - 273.15) * 9/5 + 32
        
        st.write(f"Converted Value: {result:.2f} {temp_to}")
    else:
        units = categories[category]
        value = st.number_input("Enter value", value=0.0, format="%.2f")
        from_unit = st.selectbox("From", list(units.keys()))
        to_unit = st.selectbox("To", list(units.keys()))
        
        result = convert_units(value, from_unit, to_unit, units)
        if result is not None:
            st.write(f"Converted Value: {result:.2f} {to_unit}")
        else:
            st.error("Invalid conversion.")
    
if __name__ == "__main__":
    main()
