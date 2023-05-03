import streamlit as st
import csv

# Function to convert CSV to DAT
def convert_csv_to_dat(csv_file):
    with open(csv_file.name, 'r') as file:
        # Read the CSV file
        csv_reader = csv.reader(file)

        # Create a new file for the DAT file
        dat_file = csv_file.name.replace('.csv', '.dat')
        with open(dat_file, 'w') as new_file:
            # Write each row to the new file
            for row in csv_reader:
                new_file.write('|'.join(row) + '\n')

    return dat_file

# Main Streamlit app code
def main():
    # Set the title and subtitle of the app
    st.title('CSV to DAT Converter')
    st.subheader('Convert a CSV file to a DAT file')

    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader('Choose a CSV file')

    # If a file has been uploaded
    if uploaded_file is not None:
        # Show the name of the file
        st.write('File name:', uploaded_file.name)

        # Convert the CSV file to a DAT file
        dat_file = convert_csv_to_dat(uploaded_file)

        # Allow the user to download the DAT file
        st.download_button('Download DAT file', dat_file)

# Run the app
if __name__ == '__main__':
    main()
