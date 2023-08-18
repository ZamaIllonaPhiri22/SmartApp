import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle


st.set_page_config(layout='wide', page_title='Wizards Smart Money Management Classification', page_icon='🏠')
st.title('Wizards Smart Money Management Classification')

smart_money_df = pd.read_csv("Smart_Money_df.csv")
test_df = pd.read_csv("TestSM.csv")

st.sidebar.write("1.Predict Merchant Categorized As: ")
st.sidebar.write("2.Wizard Smart Money App Classification Analysis: ")

selected_option = st.sidebar.selectbox("Select an option", ["Predict Merchant Categorized As", "Wizard Smart Money App Classification Analysis"])


if selected_option == "Predict Merchant Categorized As":
    with st.form("prediction_form"):
        st.write("1. Display Merchant Categorized As Prediction\n")
        
        mon ={0:'January',1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11: 'December'}

        merchant_name = st.text_input("Enter Merchant Name:")
        purchase_value  = st.slider("Select Purchase Value:", min_value=0.0, max_value=90000.0, step=1.0)

        
        isPurchaseOpt ={0:'True',1:'False'}
        def format_func(options):
            return isPurchaseOpt[options]
        isPurchase = st.selectbox("Is Purchased via MPESA:",options=list(isPurchaseOpt.keys()), format_func=format_func)
        
        Gender={0:'Female',1:'Male'}
        def format_func(options):
            return Gender[options]
        user_gender = st.selectbox("Choose Gender:",options=list(Gender.keys()), format_func=format_func)
        
        age_ranges = [(18, 25), (26, 30), (31, 35), (36, 40), (41, 45), (46, 50)]

        selected_range = st.selectbox("Select Age Range:", options=[f"{start}-{end}" for start, end in age_ranges], key='user_age')

        user_hsthold = st.slider("Choose Household Count:", min_value=1, max_value=31, value=1, step=1)
        user_income = st.slider("Select User Income :", min_value=0, max_value=100000, step=100, key='user_income')
        day = st.slider("Choose Day of the Merchant Categorized:", min_value=1, max_value=31, value=1, step=1)

        
        monthOpt ={0:'January',1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11: 'December'}
        def format_func(options):
            return monthOpt[options]
        month = st.selectbox("Choose Month of the Merchant Categorized:",options=list(monthOpt.keys()), format_func=format_func)
        
        year = st.slider("Choose Year of the Merchant Categorized:", min_value=2017, max_value=2030, step=1)
        hour = st.number_input("Choose The Hour of the Merchant Categorized:")
        
        
        day_Purchased = st.slider("Choose Day of the Purchase:", min_value=1, max_value=31, value=1, step=1)
        mon ={0:'January',1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11: 'December'}
        def format_func(options):
            return mon[options]
    
        month_Purchased = st.selectbox("Choose Month of the Merchant Categorized:", options=list(mon.keys()), format_func=format_func, key='month_purchased')
        year_Purchased = st.slider("Choose Year of the Purchase:", min_value=2017, max_value=2030, step=1)
        hour_Purchased = st.number_input("Choose The Hour of the Purchase:") 
    

        submit_details_merchant = st.form_submit_button('Submit!')
        
        if submit_details_merchant:
            user_input = pd.DataFrame({
                'MERCHANT_NAME': [merchant_name],
                'PURCHASE_VALUE': [purchase_value],
                'IS_PURCHASE_PAID_VIA_MPESA_SEND_MONEY': [isPurchase],
                'IS_PURCHASE_PAID_VIA_MPESA_SEND_MONEY': [user_gender],
                'USER_AGE': [float(selected_range)],
                'USER_GENDER' : [user_gender],
                'USER_HOUSEHOLD': [user_hsthold],
                'USER_INCOME': [user_income],
                'Day_MERCHANT': [day],
                'Month_MERCHANT': [month],
                'Year_MERCHANT': [year],
                'Hour_MERCHANT': [hour],
                'Day_PURCHASED': [day_Purchased],
                'Month_PURCHASED': [month_Purchased],
                'Year_PURCHASED': [year_Purchased],
                'Hour_PURCHASED': [hour_Purchased]
            })
            
         
            user_input
            model_save_path = "Bills & Fees"
            with open(model_save_path, 'rb') as file:
                model1 = pickle.load(file)

            model_save_path = "Data & WiFi"
            with open(model_save_path, 'rb') as file:
                model2= pickle.load(file)
                
            model_save_path = "Education"
            with open(model_save_path, 'rb') as file:
                model3 = pickle.load(file)

            model_save_path = "Emergency fund"
            with open(model_save_path, 'rb') as file:
                model4 = pickle.load(file)
                
            model_save_path = "Family & Friends"
            with open(model_save_path, 'rb') as file:
                model5 = pickle.load(file)

            model_save_path = "Going out"
            with open(model_save_path, 'rb') as file:
                model6 = pickle.load(file)
                
            model_save_path = "Groceries"
            with open(model_save_path, 'rb') as file:
                model7 = pickle.load(file)

            model_save_path = "Health"
            with open(model_save_path, 'rb') as file:
                model8 = pickle.load(file)
                
            model_save_path = "Loan Repayment"
            with open(model_save_path, 'rb') as file:
                model9 = pickle.load(file)

            model_save_path = "Miscellaneous"
            with open(model_save_path, 'rb') as file:
                model10 = pickle.load(file)
                
            model_save_path = "Rent Mortgage"
            with open(model_save_path, 'rb') as file:
                model11 = pickle.load(file)
                
            model_save_path = "Shopping"
            with open(model_save_path, 'rb') as file:
                model12 = pickle.load(file)

            model_save_path = "Transport & Fuel"
            with open(model_save_path, 'rb') as file:
                model13 = pickle.load(file)
                 
            d = ['Bills & Fees','Data & WiFi',    'Education',    'Emergency fund',    'Family & Friends',    'Going out'    ,'Groceries',    'Health',    'Loan Repayment',    'Miscellaneous',    'Rent Mortgage',    'Shopping',    'Transport & Fuel']

            tt = pd.DataFrame()
            
            preds0 = model1.predict_proba(user_input)[:, 1]
            preds1 = model2.predict_proba(user_input)[:, 1]
            preds2 = model3.predict_proba(user_input)[:, 1]
            preds3 = model4.predict_proba(user_input)[:, 1]
            preds4 = model5.predict_proba(user_input)[:, 1]
            preds5 = model6.predict_proba(user_input)[:, 1]
            preds6 = model7.predict_proba(user_input)[:, 1]
            preds7 = model8.predict_proba(user_input)[:, 1]
            preds8 = model9.predict_proba(user_input)[:, 1]
            preds9 = model10.predict_proba(user_input)[:, 1]
            preds10 = model11.predict_proba(user_input)[:, 1]
            preds11 = model12.predict_proba(user_input)[:, 1]
            preds12 = model13.predict_proba(user_input)[:, 1]
                
            tt['Bills & Fees'] = preds0
            tt["Data & WiFi"] = preds1
            tt['Education'] = preds2
            tt['Emergency fund'] = preds3
            tt['Family & Friends'] = preds4
            tt['Going out'] = preds5
            tt['Groceries'] = preds6
            tt['Health'] = preds7
            tt['Loan Repayment'] = preds8
            tt['Miscellaneous'] = preds9
            tt['Rent Mortgage'] = preds10
            tt['Shopping'] = preds11
            tt['Transport & Fuel'] = preds12
                
            submission = tt[d]

            xs = submission.eq(submission.max(axis=1), axis=0)

            # join the column names of the max values of each row into a single string
            submission['Max'] = xs.dot(xs.columns)
            prediction = submission["Max"]
            
                # predicted_merchant = model.predict(user_input)

            st.write("Merchant Categorized Prediction: ", submission['Max'][0])
            # print(user_input)



elif selected_option == "Wizard Smart Money App Classification Analysis":
    def analysis_vis():
        st.write("Smart Money Management Classification Analysis\n")

        plt.figure(figsize=(10, 6))
        plt.hist(smart_money_df['USER_AGE'], bins=20, edgecolor='k', alpha=0.7)
        plt.title('Distribution of User Age')
        plt.xlabel('User Age')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        
        average_income_by_category = smart_money_df.groupby('MERCHANT_CATEGORIZED_AS')['USER_INCOME'].mean()
        plt.figure(figsize=(10, 6))
        average_income_by_category.plot(kind='bar')
        plt.title('Average User Income by Merchant Category')
        plt.xlabel('Merchant Category')
        plt.ylabel('Average User Income')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)

        plt.figure(figsize=(10, 6))
        plt.scatter(smart_money_df['USER_AGE'], smart_money_df['USER_INCOME'], alpha=0.5)
        plt.title('Relationship between User Age and Income')
        plt.xlabel('User Age')
        plt.ylabel('User Income')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)

        plt.figure(figsize=(10, 6))
        plt.hist(smart_money_df['USER_AGE'], bins=20, edgecolor='k', alpha=0.7)
        plt.title('Distribution of User Age')
        plt.xlabel('User Age')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)

        st.pyplot(plt.figure(figsize=(10, 6)))
        smart_money_df.boxplot(column='PURCHASE_VALUE', by='MERCHANT_CATEGORIZED_AS', vert=False)
        plt.title('Distribution of Purchase Value by Merchant Category')
        plt.xlabel('Merchant Category')
        plt.ylabel('Purchase Value')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt) 


        
    with st.form(key='analysis_form'):
        analysis_vis()
        st.form_submit_button('Submit!')


st.balloons()
