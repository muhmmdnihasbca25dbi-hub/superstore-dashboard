import streamlit as st
import pandas as pd 
st.title('👫🏻student dataset with average')
data={'name':['deva','anand','rahul','divya','devapriya','devansh','sreeshma','santhosh','sudharsan','gowtham'],
'maths':[22,23,24,22,22,100,99,89,79,69],
'science':[22,23,24,22,22,90,99,89,79,69],
'english':[22,23,24,22,22,80,99,89,79,69],
'art':[22,23,24,22,22,80,90,100,70,60]
}
st.write(f"total number of students: {len(data['name'])}")

df=pd.DataFrame(data)
df['average']=df[['maths','science','english','art']].mean(axis=1).round(1)

st.write(df)
col1, col2, col3, col4 = st.columns(4)

class_avg = round(df["average"].mean(), 1)
highest_avg = round(df["average"].max(), 1)
lowest_avg = round(df["average"].min(), 1)
above_70 = (df["average"] >= 70).sum()

col1.metric("Class Average", class_avg)
col2.metric("Highest Average", highest_avg)
col3.metric("Lowest Average", lowest_avg)
col4.metric("Students ≥ 70", above_70)
st.subheader("Student Records")

st.dataframe(
    df.style.map(
        lambda x: "color:light blue" if x >= 70 else "color:red",
        subset=["average"]
    ),
    hide_index=True,
    use_container_width=True
)
st.subheader("🏆 Top 3 Students")

top3 = df.sort_values(
    by="average",
    ascending=False
).head(3)

top3.index = range(1, len(top3)+1)

st.table(top3)
summary = {}

for subject in ["maths", "science", "english", "art"]:
    summary[subject] = {
        "minimum": int(df[subject].min()),
        "maximum": int(df[subject].max()),
        "mean": round(df[subject].mean(), 1)
    }

st.subheader("Subject Summary")
st.json(summary)

st.divider()

st.caption("muhammed nihas | JSON Tree Viewer Project | 04 June 2026")