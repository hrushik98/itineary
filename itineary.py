import streamlit as st
import openai
openai.api_key = st.secrets['API_KEY']
st.title("Itineary Planner")
st.text("Travel planning, simplified.")
st.text("")
place = st.text_input("Enter the name of the place: ")
price = st.slider(
    "Select budget (in rupees)",
    min_value=10000,
    max_value=20000,
    step=5000,
    value=(10000)
)
number_of_days = st.slider(
    "Select the number of days:",
    min_value=1,
    max_value=10,
    step=1,
    value=(1)

)
def itineary(place, price, number_of_days):
    prompt = f"""
    Plan a {number_of_days} day Itenary in {place} within a budget of {price} rupees. Make sure to include the names of the places and a short description of what to do at those places. Give me answer in well formatted short paragraphs.  At the end of each paragraph, mention the places visted and in the next line, the estimated cost. After that, Seperate the paragraphs using with two line breaks.
    Follow this format:
    Day 1: <content> \n
    Places visited: <content> \n
    Estimated cost: <content> \n\n
    Day2:
    """
    prompt = prompt
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a an Assitant, that helps plan itinerarys"},
            {"role": "user", "content": f"{prompt}"},
        ]
    )

    final = response['choices'][0]['message']['content']
    split_paragraphs = final.split("\n\n")
    for i in split_paragraphs:
        st.header(i)
  
if st.button("Generate"):
    st.text("Generating... Please wait)
    itineary(place,price,number_of_days)


