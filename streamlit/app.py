import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import json

def dashboard_markup():
    return """
    <div class="contents">
    <div class="row3">
        <div class="column3_1">
            <div class="row">
                <div class="column">
                    <div class="graph">
                        <canvas id="barTicketSaleCount"></canvas>
                    </div>
                    <div class="graph">
                        <canvas id="doughnutProfitShare"></canvas>
                    </div>
                </div>
                <div class="column">
                    <div class="graph">
                        <canvas id="barTicketProfit"></canvas>
                    </div>
                    <div class="graph">
                        <canvas id="doughnutAudienceShare"></canvas>
                    </div>
                </div>
            </div>
            <div class="row height2">
                <div class="graph">
                    <canvas id="lineYearAccumulate"></canvas>
                </div>
            </div>
        </div>
        <div class="column3_2">
            <div class="row">
                <div class="graph">
                    <canvas id="saleForDay"></canvas>
                </div>
            </div>
            <div class="row">
                <div class="graph">
                    <canvas id="lineYearTicketAccumulate"></canvas>
                </div>
            </div>
        </div>
        <div class="column3_3">
            <div class="row">
                <div class="graph">
                    <canvas id="barWinnerRank"></canvas>
                </div>
            </div>
            <div class="row">
                <div class="graph">
                    <canvas id="barShowCountRank"></canvas>
                </div>
            </div>
            <div class="row">
                <div class="graph">
                    <canvas id="scatterRelative"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    """

def dashboard_style():
    return """
    .column3_1 {
  float: left;
  width: 31%;
}

.column3_2 {
  float: left;
  width: 38.5%;
}

.column3_3 {
  float: left;
  width: 25.5%;
}

/* Clear floats after the columns */
.row3:after {
  content: "";
  display: block;
  clear: both;
  height: 100%
}

.column {
  float: left;
  width: 50%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: block;
  clear: both;
  height: 100%
}

.graph {
}

.contents {
    height: 100%
}

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
            responsive: true,
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
            responsive: true,
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
    return """
    <script>
    const lineYearAccumulate = document.getElementById('lineYearAccumulate');
    new Chart(lineYearAccumulate, {
        type: 'line',
        data: {
        labels: ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
        datasets: [
            {
                label: '년도별 공연 누적 현황',
                data:[100,200,300,400,200,100,600,700],
            },
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
    return """
    <script>
    const lineYearTicketAccumulate = document.getElementById('lineYearTicketAccumulate');
    new Chart(lineYearTicketAccumulate, {
        type: 'line',
        data: {
            labels: ['a','b','c','d','e','f','g'],
            datasets: [
                {
                    label: 'Dataset 1',
                    data:[-100,2,3,40,5,60,7],
                },
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
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '공연장 별 수상작 공연 횟수 랭킹',
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

def dashboard_scatter_relative(label, data):
    return """
    <script>
    const scatterRelative = document.getElementById('scatterRelative');
    new Chart(scatterRelative, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: [{
                  x: -10,
                  y: 0
                }, {
                  x: 0,
                  y: 10
                }, {
                  x: 10,
                  y: 5
                }, {
                  x: 0.5,
                  y: 5.5
                }],
                backgroundColor: 'rgb(255, 99, 132)'
            }]
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

year_data = open_json_file("../data/performance_years_data.json")
statistics_data = open_json_file("../data/statistics_data.json")
daily_ticket_sales = open_json_file("../data/daily_ticket_sales.json")
day_ticket_counter = open_json_file("../data/day_ticket_sales_counter.json")
count_by_hall_rank = open_json_file("../data/count_by_hall_ranking.json")
whole_seoul_musical = open_json_file("../data/whole_seoul_musical.json")
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

    daily_ticket_sales_labels = []
    daily_ticket_sales_nums = []
    daily_ticket_profit = []
    daily_ticket_profit_share = []
    daily_ticket_audience_share = []
    total_profit = 0
    for k, v in daily_ticket_sales.items():
        daily_ticket_sales_labels.append(k)
        daily_ticket_sales_nums.append(v["티켓판매수"])
        daily_ticket_profit.append(v["티켓판매액"])
        total_profit += int(v["티켓판매액"])
        daily_ticket_audience_share.append(v["관객점유율"])
    for v in daily_ticket_profit:
        daily_ticket_profit_share.append((int(v) / total_profit) * 100)

    week_sale_labels = []
    week_sale_profit = []
    for k, v in day_ticket_counter.items():
        week_sale_labels.append(k)
        week_sale_profit.append(float(v["티켓판매액"]))

    style = "<style>" + dashboard_style() + "</style>"
    script = ""
    script += dashboard_bar_ticket_sale_count(daily_ticket_sales_labels, daily_ticket_sales_nums)
    script += dashboard_bar_ticket_sale_profit(daily_ticket_sales_labels, daily_ticket_profit)
    script += dashboard_doughnut_ticket_profit_share(daily_ticket_sales_labels, daily_ticket_profit_share)
    script += dashboard_doughnut_ticket_audience_share(daily_ticket_sales_labels, daily_ticket_audience_share)
    script += dashboard_line_year_accumulate([], [])
    script += dashboard_bar_sale_for_day(week_sale_labels, week_sale_profit)
    script += dashboard_line_year_tickt_accumulate([], [])
    script += dashboard_bar_winner_rank([], [])
    script += dashboard_bar_show_count_rank([], [])
    script += dashboard_scatter_relative([], [])
    html = style + dashboard_markup() + script

    components.html(html, width=1500, height=800)
