import streamlit as st
from utils.run import RUN
import pandas as pd

obj1 = RUN()


def show_data(values):
    print("value is ",values)
    data_dict = {"username": [values[1]], "password": [values[2]] }
    df = pd.DataFrame(data_dict)
    st.dataframe(df)


if 'score' not in st.session_state:
    st.session_state['score'] = 0 

if 'verify_button' not in st.session_state:
    st.session_state['verify_button'] = 1

if 'train_button' not in st.session_state:
    st.session_state['train_button'] = 0

if 'predict_button' not in st.session_state:
    st.session_state['predict_button'] = 0


if "database_controller" not in st.session_state:
    st.session_state.database_controller = False 



app_mode = st.sidebar.selectbox('Choose the App mode',
['About App','Face Verification'])
if app_mode =='About App':
    with open("README.md", "r", encoding="utf-8") as fh:
        readme = ""
        unwanted_list = ['<h2>','![GIF]','## Dataset','<a href=','A demo']
        for line in fh:            
            if line.startswith(tuple(unwanted_list)): 
                continue
            readme = readme + line
    st.markdown(readme)

elif app_mode == "Face Verification" and st.session_state.score == 0:
    st.title("WEBCAM")
    WINDOW = st.image([])  
    if st.session_state.verify_button == 1: 
        take = st.button("Verify")
        if take:
            data = {"mode":"verify","image_area":WINDOW}
            # data = {"mode":"verify"}
            status = obj1.controller(data)
            if status['msg'] == "Verified":
                unique_id = status['unique_id']
                st.session_state.unique_id = unique_id
                st.session_state.score = 1
                st.success("User Verified")
            else:
                st.success("User Not Verified")
                st.session_state.train_button = 1
                st.session_state.verify_button = 0

    if st.session_state.train_button == 1:
        train = st.button("Take images")
        if train:
            data = {"mode":"train","image_area":WINDOW}
            # data = {"mode":"train"}
            status = obj1.controller(data)
            if status == "success":
                st.success("Image Trained Successfully")
                st.session_state.predict_button = 1
                st.session_state.train_button = 0
                st.session_state.verify_button = 0
                
    if st.session_state.predict_button == 1:
        predp = st.button("Predict")
        if predp:
            data = {"mode":"predict","image_area":WINDOW}
            # data = {"mode":"predict"}
            status = obj1.controller(data)
            if status['msg'] == "Verified":
                unique_id = status['unique_id']
                st.session_state.score = 1
                st.session_state.unique_id = unique_id
                st.success("User Verified")

if st.session_state.score == 1:
    app_mode2 = st.sidebar.selectbox('Data',
    ["Choose","Add","View","Update","Delete"]
    )

    if app_mode2 == "Add":
        with st.form(key="userdata",clear_on_submit=True):
            category = st.text_input("what data you want to store")
            username = st.text_input("Username")
            password = st.text_input("Password",type="password")

            submit = st.form_submit_button("save")
            if submit:
                data = [category,username,password]
                unique_id = st.session_state.unique_id
                status = obj1.encrypt_controller(unique_id = unique_id,data=data,mode=app_mode2)
                st.success(status)


    elif app_mode2 == "View":

        unique_id = st.session_state.unique_id
        datas = obj1.encrypt_controller(mode=app_mode2,unique_id=unique_id)
        options = []
        for _,data in datas.items():
            options.append(data[0])
        
        category = st.selectbox("Enter the category to fetch",options)

        if len(options):
            index = options.index(category)
            values = list(datas.values())[index]
            show_data(values)
        else:
            st.success("No data present Add it")

        # show = st.button("Show",key="Show",on_click=show_data(values))
        # if show:
            # username = st.write(f"{values[1]}")
            # password = st.write(f"{values[2]}")

    elif app_mode2 == "Update":

        unique_id = st.session_state.unique_id
        datas = obj1.encrypt_controller(mode="View",unique_id=unique_id)
        options = []
        _ids = []

        for _id,data in datas.items():
            options.append(data[0])
            _ids.append(_id)
        
        category = st.selectbox("Enter the category to fetch",options)
        username = st.text_input("Username")
        password = st.text_input("Password",type="password")
        update = st.button("Update")

        if update:
            index = options.index(category)
            idofdata = _ids[index]
            data = [category,username,password]
            status = obj1.encrypt_controller(unique_id = unique_id,data=data,mode=app_mode2,_id=idofdata)
            st.success(status)

    elif app_mode2 == "Delete":

        unique_id = st.session_state.unique_id
        datas = obj1.encrypt_controller(mode="View",unique_id=unique_id)
        options = []
        _ids = []

        for _id,data in datas.items():
            options.append(data[0])
            _ids.append(_id)

        category = st.selectbox("Enter the category to fetch",options)
        index = options.index(category)

        Delete = st.button("Delete")

        if Delete:
            idofdata = _ids[index]
            status = obj1.encrypt_controller(mode=app_mode2,_id=idofdata)
            st.success(status)

        
    
    


    
    
  
