import streamlit as st
import pandas as pd
import rtfng
from io import StringIO

# Title of the web app
st.title('RTF to CSV Converter')

# File uploader
uploaded_file = st.file_uploader("Choose an RTF file", type="rtf")

if uploaded_file is not None:
    # Convert RTF to plain text using rtfng
    rtf_content = uploaded_file.read().decode("utf-8")
    text_content = rtfng.RtfParser().parse(rtf_content)

    # Convert to DataFrame
    data = StringIO(text_content)
    df = pd.read_csv(data)

    # Display DataFrame
    st.write(df)

    # Downloadable CSV link
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='output_file.csv',
        mime='text/csv',
    )
