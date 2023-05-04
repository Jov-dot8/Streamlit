import streamlit as st
import pandas as pd
import os


def convert_csv_to_dat(csv_file):
    with open(csv_file.name, 'r') as file:
        data = file.read()
    dat_filename = os.path.splitext(csv_file.name)[0] + '.dat'
    with open(dat_filename, 'w') as file:
        file.write(data)
    return dat_filename


def main():
    st.title("CSV to DAT Converter")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        print("File successfully loaded!")
        dat_file = convert_csv_to_dat(uploaded_file)
        st.download_button(label="Download DAT File", data=dat_file, file_name=dat_file, mime="text/plain")

if __name__ == '__main__':
    main()
