'''我的主页'''
for i in messages_list:
    if i[1] == '杨瑾诚':
        with st.chat_message('✈️'):
            st.text(i[1],':',i[2])
    elif i[1] == '李致远':
        with st.chat_message('⛲'):
            st.text(i[1],':',i[2])
    elif i[1] == '陈阳森':
        with st.chat_message('⛽'):
            st.write(i[1],':',i[2])
    elif i[1] == '罗天':
        with st.chat_message('⛺'):
            st.write(i[1],':',i[2])
    elif i[1] == '黄久晟':
        with st.chat_message('⛳'):
            st.write(i[1],':',i[2])