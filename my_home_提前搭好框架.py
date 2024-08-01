'我的主页'
import streamlit as st
from PIL import Image
#from streamlit_drawable_canvas import st_canvas#可删
#from PIL import Image#可删

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '我的古诗搜索', '我的跳转', '我的答题器'])

def page_1():
    '''我的兴趣推荐'''
    with open('在银河中孤独摇摆.mp3', 'rb')as f:
        mymp3=f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('书籍推荐')
    st.image("人类群星闪耀时.gif")
    st.write('----------------------------------------------')
    st.write('还是语文书让我知道这本书的，看那个文章挺喜欢的')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序：sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img_change(img,0,1,2))
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
    def img_change(img, rc, gc, bc):
        '''图片处理'''
        width, height = img.size
        img_array = img.load()
        for x in range(width):
            for y in range(height):
                r = img_array[x, y][rc]
                g = img_array[x, y][gc]
                b = img_array[x, y][bc]
                img_array[x, y] = (r, g, b)
        return img

def page_3():
    '''我的智能词典'''
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
        print(words_list)
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
        st.write('查询次数:', times_dict[n])
        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word =='snow':
            st.snow()
            st.write('曾莉荃 ENG-DBLD')
    
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
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
    name = st.selectbox('我是……', ['杨瑾诚', '李致远', '陈阳森', '罗天', '黄久晟'])
    new_message = st.text_input('想要说的话')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page_5():
    '''我的古诗搜索'''
    st.write('古诗词搜索')
    st.write('目前只有静夜思，望岳，逢入京使')
    with open('古诗词.txt', 'r', encoding='utf-8') as f:
        ws_list = f.read().split('\n')
        print(ws_list)
    for i in range(len(ws_list)):
        ws_list[i] = ws_list[i].split('#')
    ws_dict = {}
    for i in ws_list:
        ws_dict[i[1]] = [int(i[0]), i[2]]
    with open('古诗.txt', 'r', encoding='utf-8') as f:
        tims_list = f.read().split('\n')
    for i in range(len(tims_list)):
        tims_list[i] = tims_list[i].split('#')
    tims_dict = {}
    for i in tims_list:
        tims_dict[int(i[0])] = int(i[1])
    w = st.text_input('请输入要查询的古诗')
    if w in ws_dict:
        st.write(ws_dict[w])
        n = ws_dict[w][0]
        if n in tims_dict:
            tims_dict[n] += 1
        else:
            tims_dict[n] = 1
        with open('古诗.txt', 'w', encoding='utf-8') as f:
            mess = ''
            for k, v in tims_dict.items():
                mess += str(k) + '#' + str(v) + '\n'
                mess = mess[:-1]
                f.write(mess)
        st.write('查询次数:', tims_dict[n])

def page_6():
    '''我的跳转'''
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('----')
    st.write('除了本主站之外，我还会将有趣内容推荐给你！')
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili'])
    if go == '百度':
        st.link_button('跳转到'+go, 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/')

def page_7():
    '''我的答题器'''
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    st.write('----')
    st.write('这道题选什么？')
    cb1 = st.checkbox('1 16*5=80')
    cb2 = st.checkbox('2 4的算术平方根是2')
    cb3 = st.checkbox('3 9的平方根是3')
    cb4 = st.checkbox('4 1993没有相反数')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if cb1 == True and cb2 == True and cb3 == False and cb4 == False:
            st.write('回答正确')
        else:
            st.write('回答错误')
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的古诗搜索':
    page_5()
elif page == '我的跳转':
    page_6()
elif page == '我的答题器':
    page_7()