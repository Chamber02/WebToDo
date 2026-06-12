# Wire up the text input so pressing Enter on a new todo APPENDS it
# to todos.txt.
#
# Two Streamlit features we use here:
#
# 1. KEY argument
#    Every widget can be given a unique `key=`. That key becomes the
#    widget's slot in `st.session_state` — a special dict-like object
#    that holds the current value of each widget.
#       st.session_state["new_todo"] -> whatever's typed in the input
#
# 2. on_change callback
#    Pass a function to `on_change=`. Streamlit calls that function
#    whenever the widget's value changes. Inside the callback we can
#    read st.session_state["new_todo"], append it to the list, and
#    write the file back.
#
# Don't forget the trailing "\n" so each todo gets its own line in
# todos.txt. The file format is unchanged from the CLI/GUI versions —
# functions.py keeps working as-is.

import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.", 
         unsafe_allow_html=True)


##order of widgets is important
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: 
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


