import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("Gündəlik Planlama")
st.subheader("Planlama proqramından istifadənin qaydaları. Yeni plan əlavə etmək üçün aşağıda gördüyünüz boşluğa yazıb Enter düyməsinə tıklamağınız kifayətdir. İş bitdikdən sonra isə hər bir yazının qarşısında checkbox-a tıklasanız həmin plan silinəcək. Əgər error olarsa 2 dəfə cəld klik etdikdə silinir.")
st.write("Bu proqram başlanğıc üçün yazılmışdır")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Plan əlavə et", placeholder="Yeni plan əlavə edin...",
              on_change=add_todo, key='new_todo')
