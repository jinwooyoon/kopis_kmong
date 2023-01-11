import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import json
import random

def dashboard_markup():
    return """
<div class="container-fluid" style="width: 2800px">
  <div class="row">
    <div class="col-3">
      <div class="row">
        <div class="col-12">
          <h5 style="margin: 52px; text-align: center;"> 일일 티켓 판매 현황 </h5>
        </div>
        <div class="col-6">
          <div class="card" style="width: 340px">
            <div class="card-body">
              <div class="graph" style="margin-top: 35px;">
                <canvas id="barTicketSaleCount" width="300" height="220"></canvas>
              </div>
              <div class="graph" style="margin-top: 30px; margin-bottom: 50px;">
                <canvas id="doughnutProfitShare" width="300" height="240"></canvas>
              </div>
            </div>
          </div>
        </div>
        <div class="col-6">
          <div class="card" style="width: 340px">
            <div class="card-body">
              <div class="graph" style="margin-top: 35px;">
                <canvas id="barTicketProfit" width="300" height="220"></canvas>
              </div>
              <div class="graph" style="margin-top: 30px; margin-bottom: 50px;">
                <canvas id="doughnutAudienceShare" width="300" height="240"></canvas>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-2">
      <div class="card mg-20" style="width: 100%; height: 370px;">
        <div class="card-body">
            <div class="graph">
              <canvas id="lineYearAccumulate" width="365" height="300"></canvas>
            </div>
        </div>
      </div>
      <div class="card mg-20" style="width: 100%; height: 370px;">
        <div class="card-body">
          <div class="graph">
            <canvas id="lineYearTicketAccumulate" width="350" height="300"></canvas>
          </div>
        </div>
      </div>
    </div>
    <div class="col-2">
      <div class="card mg-20" style="width: 100%;height: 370px;">
        <div class="card-body">
          <div class="graph">
            <canvas id="saleForDay" width="350" height="300"></canvas>
          </div>
        </div>
      </div>
      <div class="card mg-20" style="width: 100%;height: 370px;">
        <div class="card-body">
          <div class="graph">
            <canvas id="barWinnerRank" width="350" height="300"></canvas>
          </div>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card mg-20" style="width: 540px">
        <div class="card-body">
          <div class="graph">
            <canvas id="scatterRelative" width="500" height="700"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
    """

def dashboard_style():
    return """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<style>
  .mg-20 {
    margin: 3px;
  }
</style>
    """

def dashboard_script():
    return """
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """

def dashboard_bar_ticket_sale_count(label, data):
    return """
    <script>
    const barTicketSaleCount = document.getElementById('barTicketSaleCount');
    new Chart(barTicketSaleCount, {
        type: 'bar',
        data: {
            labels: """ + str(label) + """,
            datasets: [
                {
                    label: '티켓 판매수',
                    data: """ + str(data) + """,
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
    """

def dashboard_bar_ticket_sale_profit(label, data):
    return """
    <script>
    const barTicketProfit = document.getElementById('barTicketProfit');
    new Chart(barTicketProfit, {
        type: 'bar',
        data: {
            labels: """ + str(label) +""",
            datasets: [{
                label: '티켓 판매액',
                data: """ + str(data) + """,
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
    """
def dashboard_doughnut_ticket_profit_share(label, data):
    return """
    <script>
    const doughnutProfitShare = document.getElementById('doughnutProfitShare');
    new Chart(doughnutProfitShare, {
        type: 'doughnut',
        data: {
            labels: """ + str(label) +""",
            datasets: [{
                label: '판매액 점유율',
                data: """ + str(data) + """,
            }]
        },
        options: {
            responsive: false,
            plugins: {
                legend: {
                    display: false,
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '판매액 점유율'
                }
            }
        },
    });
    </script>
    """

def dashboard_doughnut_ticket_audience_share(label, data):
    return """
    <script>
    const doughnutAudienceShare = document.getElementById('doughnutAudienceShare');
    new Chart(doughnutAudienceShare, {
        type: 'doughnut',
        data: {
            labels: """ + str(label) +""",
            datasets: [{
                label: '관객 점유율',
                data: """ + str(data) + """,
            }]
        },
        options: {
            responsive: false,
            plugins: {
                legend: {
                    display: false,
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '관객 점유율'
                }
            }
        },
    });
    </script>
    """

def dashboard_line_year_accumulate(label, data):

    datasets = ""
    for k, v in data.items():
        datasets += """
        {
            label: '""" + str(k) + """',
            data: """ + str(v) + """,
        },
        """

    return """
    <script>
    const lineYearAccumulate = document.getElementById('lineYearAccumulate');
    new Chart(lineYearAccumulate, {
        type: 'line',
        data: {
        labels: """ + str(label) + """,
        datasets: [
            """ + str(datasets) + """
        ]
        },
        options: {
            responsive: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '년도별 공연 누적 현황'
                }
            }
        },
    });
    </script>
    """

def dashboard_bar_sale_for_day(label, data):
    return """
    <script>
    const saleForDay = document.getElementById('saleForDay');
    new Chart(saleForDay, {
        type: 'bar',
        data: {
            labels: """ + str(label) +""",
            datasets: [
                {
                    label: '요일별 티켓 판매 현황',
                    data: """ + str(data) + """,
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
    """

def dashboard_line_year_tickt_accumulate(label, data):
    datasets = ""
    for k,v in data:
        datasets += """
        {
            label: '""" + str(k) + """',
            data: """ + str(v) + """,
        },
        """

    return """
    <script>
    const lineYearTicketAccumulate = document.getElementById('lineYearTicketAccumulate');
    new Chart(lineYearTicketAccumulate, {
        type: 'line',
        data: {
            labels: """+ str(label) +""",
            datasets: [
                """ + str(datasets) +"""
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '년도 별 티켓 판매 현황'
                }
            }
        },
    });
    </script>
    """

def dashboard_bar_winner_rank(label, data):
    return """
    <script>
    const barWinnerRank = document.getElementById('barWinnerRank');
    new Chart(barWinnerRank, {
        type: 'bar',
        data: {
            labels: """+ str(label) + """,
            datasets: [{
                label: '공연장 별 수상작 공연 횟수 랭킹',
                data: """ + str(data) + """,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
    """

def dashboard_bar_show_count_rank(label, data):
    return """
    <script>
    const barShowCountRank = document.getElementById('barShowCountRank');
    new Chart(barShowCountRank, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '뮤지컬 공연 상연 횟수 랭킹',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
    """

def dashboard_scatter_relative(data):

    dataset = ""
    for v in data:
        r = random.randrange(1, 255)
        g = random.randrange(1, 255)
        b = random.randrange(1, 255)
        dataset += """
        {
            label: '""" + str(v[0]) + """',
            data: """ + str(v[1]) + """,
            backgroundColor: 'rgb(""" + str(r) + """, """ + str(g) + """, """ + str(b) + """)'
        },
        """

    return """
    <script>
    const scatterRelative = document.getElementById('scatterRelative');
    new Chart(scatterRelative, {
        type: 'scatter',
        data: {
            datasets: [
            """ + dataset + """
            ]
        },
        options: {
            scales: {
              x: {
                type: 'linear',
                position: 'bottom'
              }
            },
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: '공연 기간 / 상연 횟수 상관관계'
                }
            }
        },
    });
    </script>
    """

def open_json_file(src_file):
    return_json_dict = {}
    with open(src_file, "r", encoding="utf-8") as f:
        return_json_dict = json.load(f)
    return return_json_dict

performance_list = pd.read_json("../data/performance_list.json")
performance_ranking = pd.read_json("../data/performance_ranking.json")
festival_list = pd.read_json("../data/festival_list.json")

new_year_data = open_json_file("../new_data/performance_years_data.json")
year_data = open_json_file("../data/performance_years_data.json")
statistics_data = open_json_file("../new_data/statistics_data.json")
daily_ticket_sales = open_json_file("../new_data/daily_ticket_sales.json")
day_ticket_counter = open_json_file("../new_data/day_ticket_counter.json")
count_by_hall_rank = open_json_file("../data/count_by_hall_ranking.json")
whole_seoul_musical = open_json_file("../new_data/whole_seoul_musical.json")
scatter_result = open_json_file("../data/scatter_result.json")

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

if choose == "대시보드":

    style = dashboard_style()
    script = dashboard_script()

    d_t_s_lables = daily_ticket_sales["장르"]
    d_t_s_count = daily_ticket_sales["티켓판매수"]
    script += dashboard_bar_ticket_sale_count(d_t_s_lables, d_t_s_count)
    d_t_s_profit = daily_ticket_sales["티켓판매액"]
    script += dashboard_bar_ticket_sale_profit(d_t_s_lables, d_t_s_profit)

    d_t_s_profit_share = daily_ticket_sales["티켓점유율"]
    script += dashboard_doughnut_ticket_profit_share(d_t_s_lables, d_t_s_profit_share)
    d_t_s_audience_share = daily_ticket_sales["관객점유율"]
    script += dashboard_doughnut_ticket_audience_share(d_t_s_lables, d_t_s_audience_share)


    d_t_c_labels = day_ticket_counter["day"]
    d_t_c_count = day_ticket_counter["티켓판매수"]
    script += dashboard_bar_sale_for_day(d_t_c_labels, d_t_c_count)

    y_t_a_labels = statistics_data["years"]

    target = "티켓판매액"
    y_t_a_datasets = []
    with st.sidebar:
        choice = st.selectbox(
            "년도별 티켓 판매 현황",
            ("티켓판매액", "티켓판매수")
        )
        y_t_a_datasets = [
            ("연극", statistics_data[choice]["연극"]),
            ("뮤지컬", statistics_data[choice]["뮤지컬"]),
            ("클래식", statistics_data[choice]["클래식"]),
            ("오페라", statistics_data[choice]["오페라"]),
            ("무용", statistics_data[choice]["무용"]),
            ("국악", statistics_data[choice]["국악"]),
            ("복합", statistics_data[choice]["복합"])
        ]

    script += dashboard_line_year_tickt_accumulate(
        y_t_a_labels, y_t_a_datasets
    )

    w_s_m_labels = whole_seoul_musical["공연명"]
    w_s_m_play_count = whole_seoul_musical["상연횟수"]
    script += dashboard_bar_winner_rank(w_s_m_labels, w_s_m_play_count)

    s_c_r_dataset = [
        ["연극", scatter_result["연극"]],
        ["뮤지컬", scatter_result["뮤지컬"]],
        ["클래식", scatter_result["클래식"]],
        ["오페라", scatter_result["오페라"]],
        ["무용", scatter_result["무용"]],
        ["국악", scatter_result["국악"]],
        ["복합", scatter_result["복합"]]
    ]
    script += dashboard_scatter_relative(s_c_r_dataset)

    location_list = []
    select_data = {}
    year_labels = new_year_data['years']
    for location, v in new_year_data.items():
        if location != 'years':
            location_list.append(location)
    with st.sidebar:
        choice = st.selectbox(
            "지역별 분류",
            location_list
        )
        select_data = new_year_data[choice]

    script += dashboard_line_year_accumulate(year_labels, select_data)
    script += dashboard_bar_show_count_rank([], [])

    html = style + dashboard_markup() + script

    components.html(html, width=2800, height=900)
