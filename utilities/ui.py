import streamlit as st
from datetime import datetime
import requests



API_URL = 'http://127.0.0.1:8000'

MIN_DATE = datetime(1920, 1, 1)
MAX_DATE = datetime.now()

def submit_request_post(form_data):
    try:
        resp = requests.post(f'{API_URL}/submit', json=form_data)
        st.success('You have successfully filled in the form')
        resp.raise_for_status()
    except Exception as e:
        st.warning(f'ERROR: {e}')
        st.write(resp.status_code)

def calculage_age(birth_date):
    birth_date = datetime(birth_date.year, birth_date.month, birth_date.day)
    age = MAX_DATE.year - birth_date.year
    if (birth_date.month > MAX_DATE.month) or (birth_date.month == MAX_DATE.month and birth_date.day > MAX_DATE.day):
        age -= 1
    return age


#MANAGE TABS
if "tabs" not in st.session_state:
    st.session_state.tabs = ['Input Form', 'Database']
tab_objects = st.tabs(st.session_state.tabs)

with tab_objects[0]:
    st.title('User Information Form')

    form_data = {
        'name': None,
        'surname': None,
        'gender': None,
        'age': None
    }

    with st.form(key='user_input_form', clear_on_submit=True):

        form_data['name'] = st.text_input("Enter your name: ")
        form_data['surname'] = st.text_input('Enter your surname: ')
        form_data['gender'] = st.selectbox("Gender", ['Female', 'Male', 'Other'])

        birth_date = st.date_input('Enter your birthdate', min_value=MIN_DATE, max_value=MAX_DATE)

        #CONFIGURE AGE
        if birth_date:
           age = calculage_age(birth_date)

        form_data['age'] = str(age)


        submit_button = st.form_submit_button(label='DONE')
        if submit_button:
            if not all(form_data.values()): #if the values were not filled in before pressing the button
                st.warning('ERROR! Please fill in all of the fields')
            else:
                st.balloons()
                submit_request_post(form_data)

with tab_objects[1]:
    try:
        resp = requests.get(f'{API_URL}/api/people')
        resp.raise_for_status()
        people_list = resp.json()
        st.write(people_list)
    except Exception as e:
        st.warning(f'ERROR: {e}')
        st.write(resp.status_code)