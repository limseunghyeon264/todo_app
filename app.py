import streamlit as st

st.title('📌To-do App📌')

# (할일 + 여부) 객체로 관리하기 위해 만든 클래스
class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    # def __str__(self):
    #    return f'Task: {self._task}, Done: {self.__task}'

    # 객체가 리스트 안에 있을 때 리스트 안의 요소들을 출력하면
    def __repr__(self):
        # return f'Task: {self.__task}, Done: {self.__done}'

        # repr은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는 게 원칙이다.
        # return f'Todo: {self.__task}, Done: {self.__done}'
        # return f'Todo: {self.__task!r}, Done: {self.__done}'

print(Todo('숙제하기'))
print(Todo(task='똘이 밥주기', done=True))
todo2 =eval(repr(todo))
print(id(todo2))

# Todo 객체를 list에 쌓는 용도의 함수(추가 할 할일을 작성하면 실행되는 함수)
def add_todo():
print(f'session_state에 new_task로 있는 값은? {st.session_state.new_task}')
todo = Todo(st.session_state['new_task'])
st.session_state['todos'].append(todo)
print(st.session_state['todos'])    # list를 출력하면 __str__은 주소값, __repr__은 Todo 객체의 문자열로 구성되어 나옴
st.session_state['new_task'] = ""

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다.
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo)   # input 창에 내용을 작성하고 엔터하면 add_todo함수 호출
                                                                           # 엔터하면 add_todo함수 호출
def toggle_done(index: int):
    todo = st.session_state.todos[index]
    todo.__done = not todo.__done

# todos(todo 객체를 담을 리스트를 초기화)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다.(session_state에 새로운 키 초기화)
st.text_inpiut('새로운 할일 추가', key='new_task', on_change=add_todo)   # input 창에 내용을 작성(기존과 다른 내용)하고
                                                                      # 엔터하면 add_todo함수 호출

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i}번째 todo => {todo}')
        col1, col2 = st.columns(0.1, 0.9)
        col1.checkbox(f'{1 + 1}', value=todo.__task, key=f'done_{i}', on_change=toggle_done)
        col2.markdown(f'~~{todo.__task}~~', unsafe_allow_html=True)

else:
    st.info('할일을 추가해 보세요.')

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i}번째 todo => {todo}')
        col1, col2 = st.columns([0.1], [0.9])
