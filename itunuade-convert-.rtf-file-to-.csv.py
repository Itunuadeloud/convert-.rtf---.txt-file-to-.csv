#import streamlit as st
#import pandas as pd
#import rtfng
#from io import StringIO

# Title of the web app
#st.title('RTF to CSV Converter')

# File uploader
#uploaded_file = st.file_uploader("Choose an RTF file", type="rtf")

#if uploaded_file is not None:
    # Convert RTF to plain text using rtfng
 #   rtf_content = uploaded_file.read().decode("utf-8")
  #  text_content = rtfng.RtfParser().parse(rtf_content)

    # Convert to DataFrame
  #  data = StringIO(text_content)
   # df = pd.read_csv(data)

    # Display DataFrame
   # st.write(df)

    # Downloadable CSV link
  #  csv = df.to_csv(index=False).encode('utf-8')
  #  st.download_button(
     #   label="Download CSV",
     #   data=csv,
      #  file_name='output_file.csv',
      #  mime='text/csv',
 #   )


#import streamlit as st
#import pandas as pd
#from striprtf.striprtf import rtf_to_text  # Importing striprtf to convert RTF to text
#from io import StringIO

# Title of the web app
#st.title('RTF to CSV Converter')

# File uploader
#uploaded_file = st.file_uploader("Choose an RTF file", type="rtf")

#if uploaded_file is not None:
    # Convert RTF to plain text using striprtf
    #rtf_content = uploaded_file.read().decode("utf-8")
   # text_content = rtf_to_text(rtf_content)  # Convert the RTF content to plain text

    # Convert the plain text to a DataFrame (Assuming the text is formatted correctly for a table)
   # data = StringIO(text_content)
   # df = pd.read_csv(data)

    # Display the DataFrame
   # st.write(df)

    # Create a downloadable CSV link
   # csv = df.to_csv(index=False).encode('utf-8')
    #st.download_button(
    #    label="Download CSV",
    #    data=csv,
    #    file_name='output_file.csv',
    #    mime='text/csv',
   # )


import streamlit as st
import pandas as pd
from striprtf.striprtf import rtf_to_text  # Importing striprtf to convert RTF to text
from io import StringIO

# Title of the web app
st.title('RTF to CSV Converter')

# File uploader
uploaded_file = st.file_uploader("Choose an RTF file", type="rtf")

if uploaded_file is not None:
    # Get the original file name without the extension
    original_file_name = uploaded_file.name.rsplit('.', 1)[0]

    # Convert RTF to plain text using striprtf
    rtf_content = uploaded_file.read().decode("utf-8")
    text_content = rtf_to_text(rtf_content)  # Convert the RTF content to plain text

    # Convert the plain text to a DataFrame (Assuming the text is formatted correctly for a table)
    data = StringIO(text_content)
    df = pd.read_csv(data)

    # Display the DataFrame
    st.write(df)

    # Create a downloadable CSV link using the original file name
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f'{original_file_name}.csv',  # Use the original file name for the CSV
        mime='text/csv',
    )
