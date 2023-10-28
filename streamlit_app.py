import streamlit as st
import requests, json, io

def convert_text_to_audio(text_input,voice,speed):
    loading_text = st.empty() 
    loading_text.text= 'Đang load...'
    url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
    data = {"text": text_input, "voice": voice, "id": "2", "without_filter": False, "speed": speed, "tts_return_option": 3}
    headers = {'Content-type': 'application/json', 'token': 'ZtLiDGJkyfHq0CJ8D18F2pp493u-8RFMBiIQULKbF67vCiT6-G0RKtWnK1LHBcV5'}

    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    data = response.content
    loading_text.text= ''
    st.audio(data, format="audio/mp3")
    with io.BytesIO(data) as f:
        st.download_button("Tải tệp âm thanh", f, file_name="audio.mp3", key="audio_download")
    

st.set_page_config(page_title="Text to audio",layout='wide')
st.title("Chuyển văn bản sang âm thanh")
with st.form(key='my_form'):
    c1, c2= st.columns([7,3])

    with c1:
        input_text = st.text_area('Nội dung:',height=150)
    with c2:
        voice = st.selectbox(
        'Chọn giọng đọc:',
        ('hn-quynhanh','hcm-diemmy','hue-maingoc','hn-phuongtrang','hn-thanhtung','hue-baoquoc','hcm-minhquan','trinhthiviettrinh','lethiyen','nguyenthithuyduyen','phamtienquan'))
        speed = st.slider("Chọn tốc độ đọc:", min_value=0.7, max_value=1.3, value=1.0, step=0.1, format="%.1f")      
    convert = st.form_submit_button('Chuyển đổi')
if convert:
  convert_text_to_audio(input_text, voice, speed)
else:
  st.write('Mời nhập data')
  

