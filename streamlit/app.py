import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import json

performance_list = pd.read_json("../data/performance_list.json")
performance_ranking = pd.read_json("../data/performance_ranking.json")
festival_list = pd.read_json("../data/festival_list.json")


with open("../data/performance_years_data.json", "r", encoding="utf-8") as f:

    year_data = json.load(f)


with open("../data/statistics_data.json", "r", encoding="utf-8") as f:

    statistics_data = json.load(f)

performance_count = pd.read_json("../data/performance_years_data.json")
performance_count.rename(index={"year2016": "2016", "year2017": "2017", "year2018": "2018",
                         "year2019": "2019", "year2020": "2020", "year2021": "2021"}, inplace=True)


performance_list.drop_duplicates()
st.set_page_config(layout="wide")


with st.sidebar:
    choose = option_menu("공연 정보", ["INFORMATION", "공연 목록", "예매 랭킹", "축제 목록", "공연 차트","대시보드"],
                         icons=['lightbulb', 'list-ul', 'list-ol',
                                'list-stars','graph-up-arrow'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"}
    }
    )


if choose == "공연 목록":

    with st.sidebar:

        genre_selectbox = st.selectbox(
            "장르별 분류",
            ("연극", "뮤지컬", "클래식", "오페라", "무용", "국악", "복합"))

    with st.sidebar:
        region_selectbox = st.selectbox(
            "지역별 분류",
            ("서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"))
    with st.sidebar:
        state_selectbox = st.selectbox(
            "공연 상태별 분류",
            ("공연중", "공연예정"))

    title = st.text_input('찾으시는 공연 제목을 입력하세요.', '')
    expander = st.expander("공연 예매 바로가기")
    expander.write("[인터파크](http://ticket.interpark.com/)")
    expander.write("[위메프](https://ticket.wemakeprice.com/)")

    link1 = "https://stackoverflow.com/questions/71641666/hyperlink-in-streamlit-dataframe"
    link2 = "https://stackoverflow.com/questions/71731937/how-to-plot-comparison-in-streamlit-dynamically-with-multiselect"

    if title != "":
        performance_list = performance_list.query(
            f'공연명.str.contains("{title}")')

    else:

        performance_list = performance_list[(performance_list["장르"] == genre_selectbox) & (performance_list["지역"] ==
                                                                                           region_selectbox) & (performance_list["상태"] == state_selectbox)]

    st.write(performance_list.to_html(escape=False, index=False, col_space=[
             490, 90, 360, 127, 127, 110, 70], justify='center'), unsafe_allow_html=True)


if choose == "예매 랭킹":

    with st.sidebar:

        genre_selectbox = st.selectbox(
            "장르별 분류",
            ("연극", "뮤지컬", "클래식", "오페라", "무용", "국악", "복합"))

    with st.sidebar:
        region_selectbox = st.selectbox(
            "지역별 분류",
            ("서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"))

    title = st.text_input('찾으시는 공연 제목을 입력하세요.', '')

    expander = st.expander("공연 예매 바로가기")
    expander.write("[인터파크](http://ticket.interpark.com/)")
    expander.write("[위메프](https://ticket.wemakeprice.com/)")

    link1 = "https://stackoverflow.com/questions/71641666/hyperlink-in-streamlit-dataframe"
    link2 = "https://stackoverflow.com/questions/71731937/how-to-plot-comparison-in-streamlit-dynamically-with-multiselect"

    if title != "":
        performance_ranking = performance_ranking.query(
            f'공연명.str.contains("{title}")')

    else:
        performance_ranking = performance_ranking[(performance_ranking["장르"] == genre_selectbox) & (performance_ranking["지역"] ==
                                                                                                    region_selectbox)]

    st.write(performance_ranking.to_html(escape=False, index=False, col_space=[
             80, 500, 80, 400, 127, 110, 70], justify='center'), unsafe_allow_html=True)


if choose == "축제 목록":

    with st.sidebar:
        region_selectbox = st.selectbox(
            "지역별 분류",
            ("서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"))
    with st.sidebar:
        state_selectbox = st.selectbox(
            "공연 상태별 분류",
            ("공연중", "공연예정"))

    title = st.text_input('찾으시는 공연 제목을 입력하세요.', '')

    expander = st.expander("공연 예매 바로가기")
    expander.write("[인터파크](http://ticket.interpark.com/)")
    expander.write("[위메프](https://ticket.wemakeprice.com/)")

    link1 = "https://stackoverflow.com/questions/71641666/hyperlink-in-streamlit-dataframe"
    link2 = "https://stackoverflow.com/questions/71731937/how-to-plot-comparison-in-streamlit-dynamically-with-multiselect"

    if title != "":
        festival_list = festival_list.query(f'축제명.str.contains("{title}")')

    else:

        festival_list = festival_list[(festival_list["지역"] ==
                                       region_selectbox) & (festival_list["상태"] == state_selectbox)]

    st.write(festival_list.to_html(escape=False, index=False, col_space=[
             490, 90, 360, 127, 127, 110, 70], justify='center'), unsafe_allow_html=True)


if choose == "공연 차트":

    with st.sidebar:
        choice = st.selectbox(
            "지역별 분류",
            ("년도별 공연 누적 진행율", "장르별 공연 예매 상황"))

    if choice == "년도별 공연 누적 진행율":
        with st.sidebar:
            region_selectbox = st.selectbox(
                "지역별 분류",
                ("전국", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"))

        html = """<div>
    <canvas id="myChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {{
        type: 'line',
        data: {{
        labels : ["2016","2017","2018","2019","2020","2021","2022","2023"],
        datasets: [{{
            label: '연극',
            data: {actor_data},
            borderColor: 'rgb(251, 37, 118)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
        }},
        {{
            label: '뮤지컬',
            data: {musical_data},
            borderWidth: 2,
            backgroundColor: 'rgb(255, 255 ,255)',
            borderColor: 'rgb(63, 0, 113)'
            
            
        }},
        {{
            label: '클래식',
            data: {classic_data},
            borderWidth: 2,
            backgroundColor: 'rgb(255, 255 ,255)',
            borderColor: 'rgb(198, 155, 123)'
            
        }},
        {{
            label: '오페라',
            data: {opera_data},
            borderColor: 'rgb(149, 1, 1)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '무용',
            data: {dance_data},
            borderColor: 'rgb(62, 109, 156)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '국악',
            data: {korean_classical_data},
            borderColor: 'rgb(210, 0, 26)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '복합',
            data: {complex_data},
            borderColor: 'rgb(0, 0, 0)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }}]}},
        options: {{
            scales: {{
                
            y: {{
            beginAtZero: true
            }}
        }}
        }}
    }});

    </script>
    
        """.format(actor_data=list(year_data[region_selectbox]['연극'].values()), musical_data=list(year_data[region_selectbox]['뮤지컬'].values()), classic_data=list(year_data[region_selectbox]['클래식'].values()), opera_data=list(year_data[region_selectbox]['오페라'].values()),
                   dance_data=list(year_data[region_selectbox]['무용'].values()), korean_classical_data=list(year_data[region_selectbox]['국악'].values()), complex_data=list(year_data[region_selectbox]['복합'].values()))

        components.html(html, width=1000, height=1000)

    if choice == "장르별 공연 예매 상황":
        with st.sidebar:
            ticket_selectbox = st.selectbox(
                "티켓 분류",
                ("티켓판매액", "티켓판매수"))

        html = """<div>
    <canvas id="myChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {{
        type: 'line',
        data: {{
        labels : ["2016","2017","2018","2019","2020","2021","2022","2023"],
        datasets: [{{
            label: '연극',
            data: {actor_data},
            borderColor: 'rgb(251, 37, 118)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
        }},
        {{
            label: '뮤지컬',
            data: {musical_data},
            borderWidth: 2,
            backgroundColor: 'rgb(255, 255 ,255)',
            borderColor: 'rgb(63, 0, 113)'
            
            
        }},
        {{
            label: '클래식',
            data: {classic_data},
            borderWidth: 2,
            backgroundColor: 'rgb(255, 255 ,255)',
            borderColor: 'rgb(198, 155, 123)'
            
        }},
        {{
            label: '오페라',
            data: {opera_data},
            borderColor: 'rgb(149, 1, 1)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '무용',
            data: {dance_data},
            borderColor: 'rgb(62, 109, 156)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '국악',
            data: {korean_classical_data},
            borderColor: 'rgb(210, 0, 26)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }},
        {{
            label: '복합',
            data: {complex_data},
            borderColor: 'rgb(0, 0, 0)',
            backgroundColor: 'rgb(255, 255 ,255)',
            borderWidth: 2
            
        }}]}},
        options: {{
            scales: {{
                
            y: {{
            beginAtZero: true
            }}
        }}
        }}
    }});

    </script>
    
        """.format(actor_data=list(statistics_data[ticket_selectbox]['연극'].values()), musical_data=list(statistics_data[ticket_selectbox]['뮤지컬'].values()), classic_data=list(statistics_data[ticket_selectbox]['클래식'].values()), opera_data=list(statistics_data[ticket_selectbox]['오페라'].values()),
                   dance_data=list(statistics_data[ticket_selectbox]['무용'].values()), korean_classical_data=list(statistics_data[ticket_selectbox]['국악'].values()), complex_data=list(statistics_data[ticket_selectbox]['복합'].values()))

        components.html(html, width=1000, height=1000)

    if choice == "대시보드":
        
        html = ""
        
        
        
        
        # components.html(html, width=1000, height=1000)