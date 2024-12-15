import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pickle
import streamlit as st


st.set_page_config(
        page_title="Flat Resale Price",
        layout="wide",
        initial_sidebar_state="expanded")

scrolling_text = "<h1 style='color:orange; font-style:bold ; font-weight: bold;'><marquee>SINGAPORE FLAT RESALE PRICE</marquee></h1>"
st.markdown(scrolling_text, unsafe_allow_html=True)

with st.sidebar:
    select = option_menu(None,["Home","Price Prediction"],icons=["house-fill","graph-up-arrow"])
    
if select == "Home":
    

    st.header(':hammer_and_pick: :blue[TECHNOLOGIES USED]')

    st.write(':love_hotel: Python, Streamlit, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, Pickle, Streamlit-Option-Menu, Render')

    st.header(':page_with_curl: :red[ABOUT THE PROJECT]')

    st.write(":love_hotel: The project falls under the domain of Real Estate.")

    st.write(':love_hotel: Load and understand the resale flat price data through CSV files. Check the data for consistency and completeness.')

    st.write(':love_hotel: Loaded the resale flat price CSV into a DataFrame. Cleaned and filled missing values, addressed outliers,and adjusted data types. Analyzed data distribution and treated skewness.')

    st.write(':love_hotel: Understanding and visualizing the data using EDA techniques such as boxplots, histograms, and violin plots.')

    st.write(':love_hotel: Drop highly correlated columns using a heatmap from Seaborn.')

    st.write(''':love_hotel: Mean Absolute Error(MAE),Mean Squared Error(MSE),Root Mean Squared Error(RMSE),R-squared(R²).Split the dataset into training and testing sets. 
            Train and evaluate regression models for 'Predicted Resale_Price'. Pickled the trained models for deployment.''')

    st.write(':love_hotel: ML Regression model which predicts the :green[**‘Predicted Resale_Price :money_with_wings:’**].')

    st.write(''':love_hotel: In a Streamlit page,Developed a user interface for interacting with the models.Predicted selling price based on user input.''')

    st.write(':love_hotel: Deploy the web application on a hosting platform like Render for user access.')

elif select =="Price Prediction":
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    
    year = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                    2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    
    town_values=["ANG MO KIO","BEDOK","BISHAN","BUKIT BATOK","BUKIT MERAH","BUKIT PANJANG","BUKIT TIMAH","CENTRAL AREA",
                    "CHOA CHU KANG","CLEMENTI","GEYLANG","HOUGANG","JURONG EAST","JURONG WEST","KALLANG/WHAMPOA","LIM CHU KANG",
                    "MARINE PARADE","PASIR RIS","PUNGGOL","QUEENSTOWN","SEMBAWANG","SENGKANG","SERANGOON",
                    "TAMPINES","TOA PAYOH","WOODLANDS","YISHUN"]
    
    town_encoded = {"ANG MO KIO":0,"BEDOK":1,"BISHAN":2,"BUKIT BATOK":3,"BUKIT MERAH":4,"BUKIT PANJANG":5,"BUKIT TIMAH":6,"CENTRAL AREA":7,
                    "CHOA CHU KANG":8,"CLEMENTI":9,"GEYLANG":10,"HOUGANG":11,"JURONG EAST":12,"JURONG WEST":13,"KALLANG/WHAMPOA":14,"LIM CHU KANG":15,
                    "MARINE PARADE":16,"PASIR RIS":17,"PUNGGOL":18,"QUEENSTOWN":19,"SEMBAWANG":20,"SENGKANG":21,"SERANGOON":22,
                    "TAMPINES":23,"TOA PAYOH":24,"WOODLANDS":25,"YISHUN":26}
    
    flat_type= ["1 ROOM","2 ROOM","3 ROOM","4 ROOM","5 ROOM","EXECUTIVE","MULTI GENERATION",'MULTI-GENERATION']

    flat_type_encoded = {"1 ROOM":0,"2 ROOM":1,"3 ROOM":2,"4 ROOM":3,"5 ROOM":4,"EXECUTIVE":5,"MULTI GENERATION":6,'MULTI-GENERATION':7}
    
    flat_model=['2-ROOM','3GEN','ADJOINED FLAT','APARTMENT','DBSS','IMPROVED','IMPROVED-MAISONETTE','MAISONETTE','MODEL A','MODEL A-MAISONETTE',
                'MODEL A2','MULTI GENERATION','NEW GENERATION','PREMIUM APARTMENT','PREMIUM APARTMENT LOFT','PREMIUM MAISONETTE','SIMPLIFIED','STANDARD',
                'TERRACE','TYPE S1','TYPE S2']

    flat_model_encoded = {'2-ROOM':0,'3GEN':1,'ADJOINED FLAT':2,'APARTMENT':3,'DBSS':4,'IMPROVED':5,'IMPROVED-MAISONETTE':6,'MAISONETTE':7,'MODEL A':8,'MODEL A-MAISONETTE':9,
                'MODEL A2':10,'MULTI GENERATION':11,'NEW GENERATION':12,'PREMIUM APARTMENT':13,'PREMIUM APARTMENT LOFT':14,'PREMIUM MAISONETTE':15,'SIMPLIFIED':16,'STANDARD':17,'TERRACE':18,'TYPE S1':19,'TYPE S2':20}
    
    lease_commence_year=[1977, 1976, 1978, 1979, 1984, 1980, 1985, 1981, 1982, 1986, 1972,1983, 1973, 1969, 1975, 1971, 1974, 1967, 1970, 1968, 1988, 1987,
                        1989, 1990, 1992, 1993, 1994, 1991, 1995, 1996, 1997, 1998, 1999,2000, 2001, 1966, 2002, 2006, 2003, 2005, 2004, 2008, 2007, 2009,
                        2010, 2012, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]   
    
    floor_area_sqm_values = [31, 73, 67, 82, 74, 88, 89, 83, 68, 75, 81, 91, 92, 93, 95, 94, 100, 108, 103, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 128, 130, 133, 134, 135, 139, 140, 141, 142, 144, 146, 147, 148, 150, 151, 152, 154, 155, 156, 158, 160, 161, 162, 163, 164, 165, 168, 169, 170, 172, 173, 174, 175, 176, 179, 180, 183, 184, 185, 187, 188, 190, 193, 194, 195, 198, 199, 201, 202, 204, 210, 213, 217, 220, 223, 224, 226, 229, 230, 232, 233, 240, 247, 248, 251, 258, 259]
    
    
    with st.form('prediction'):
        
        col1, col2 = st.columns(2)
        
        with col1:

            Month=st.selectbox(label='**Month**',options=month,index=None)

            Year=st.selectbox(label='**Year**',options=year,index=None)
            
            Town_Name=st.selectbox(label='**Town Name**',options=town_values,index=None)
            
            Flat_type=st.selectbox(label='**Flat Type**',options=flat_type,index=None)

            Flat_model=st.selectbox(label='**Flat Model**',options=flat_model,index=None)
            
            Floor_area_sqm = st.selectbox('**Select Floor Area(sqm):**',options=floor_area_sqm_values,index=None)

        with col2:

            Lease_Commence_year=st.selectbox(label='**Lease Commence Year**',options=lease_commence_year,index=None)

            storey_range_start= st.slider("**Enter Starting number of Storey(Min:1/ Max:49)**",min_value=1,max_value=49)

            storey_range_end= st.slider("**Enter ending number of Storey(Min:1/ Max:51)**",min_value=1,max_value=51)

            Price_per_sqm=st.number_input(label='**Price Per Sqm [min=161,max=15591.0]**',min_value=161.0,max_value=15591.0)

            button=st.form_submit_button('PREDICT RESALE PRICE',use_container_width=True)
            
            
        if button:

            if not all([Month,Year,Town_Name,Flat_type,Flat_model,Floor_area_sqm,Lease_Commence_year,storey_range_start,storey_range_end,Price_per_sqm]):
                    
                    st.error(":rotating_light: Fill all the required fields.")

            else:
                with open(r'C:\Users\ADMIN\Desktop\raraj\Decisiontree.pkl','rb') as file_1:
                    decision_tree_model= pickle.load(file_1)
                    
                a1 = int(Month)

                b1 = int(Year)

                c1=town_encoded[Town_Name]  

                d1=flat_type_encoded[Flat_type]
                
                e1=flat_model_encoded[Flat_model]

                f1=float(Floor_area_sqm)

                g1 = int(storey_range_start)

                h1 = int(storey_range_end)

                i1=float(Price_per_sqm)
                
                user_data=np.array([[a1,b1,c1,d1,e1,f1,Lease_Commence_year,np.log(g1),np.log(h1),np.log(i1)]])
                
                st.write("Encoded Input Data:",user_data) 
                
                new_pred_1 = decision_tree_model.predict(user_data)

                resale_price = np.exp(new_pred_1[0])

                formatted_price = f"{resale_price:,.2f}"

                st.write(f'## :red[PREDICTED RESALE PRICE: {formatted_price}]')

        