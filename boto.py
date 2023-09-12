import streamlit as st
import boto3

# Get the name of the S3 bucket
bucket_name = st.text_input("Enter the name of the bucket")

# Get a video file from the user
video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

# Get the name of the file in the bucket
file_name = st.text_input("Enter the name of the file")

# Initialize the S3 client
s3 = boto3.client('s3',
                  region_name='us-east-1',  # Replace with your AWS region
                  aws_access_key_id='YOUR_ACCESS_KEY_ID',
                  aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')

# Upload the video to the specified S3 bucket
if bucket_name and video_file and file_name:
    try:
        # Upload the file directly from the file-like object
        s3.upload_fileobj(video_file, bucket_name, file_name)
        st.write(f'Successfully uploaded {file_name} to {bucket_name}')
    except Exception as e:
        st.write(f'Error uploading {file_name} to {bucket_name}: {str(e)}')
