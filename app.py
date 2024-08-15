import streamlit as st
import pickle

df=pickle.load(open('movies.pkl','rb'))
movie_list=df['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=df[df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    lst=[]
    for i in movies_list:
        lst.append(df.iloc[i[0]].title)
    return lst

st.title('Movie Recommender System')
option=st.selectbox('Enter movie',(movie_list))

if st.button('Recommend'):
    rec=recommend(option)
    st.write(rec)