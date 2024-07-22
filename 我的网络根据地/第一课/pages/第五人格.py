import streamlit as st
st.write('# :red[世界就是一个巨大的第五人格！！]')

st.write('以下哪位求生者不可以饮用调酒师调制的烈性多夫林？')
a1 = st.checkbox('医生')
a2 = st.checkbox('祭司')
a3 = st.checkbox('空军')
a4 = st.checkbox('舞女')

st.write('以下哪一位监管者的扮演难度不为三张面具？')
b1 = st.checkbox('梦之女巫')
b2 = st.checkbox('“记录员”')
b3 = st.checkbox('破轮')
b4 = st.checkbox('歌剧演员')

st.write('以下哪种监管者天赋对求生者的治疗速度不起到降低的作用？')
c1 = st.checkbox('恐慌')
c2 = st.checkbox('崩坏')
c3 = st.checkbox('恶化')
c4 = st.checkbox('后遗症')

st.write('以下哪位求生者的推演系统中没有“遇见队友”这个目标？')
d1 = st.checkbox('咒术师')
d2 = st.checkbox('玩具商')
d3 = st.checkbox('昆虫学者')

st.write('以下混沌纷争中的模式，哪一个无法在18：30体验到？')
e1 = st.checkbox('塔罗')
e2 = st.checkbox('黑杰克')
e3 = st.checkbox('噩梦逐影')
e4 = st.checkbox('联合狩猎')

l = [a3,b4,c4,d2,e4]
if st.button('确认答案'):
    if True in l:
        st.image('蝶的认可.jpg')
        st.write('蝶的认可')
    else:        
        st.write('集美，怎么了？')
        st.image('脑子呢.jpg')
