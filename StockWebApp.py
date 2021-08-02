import streamlit as st
import csv
import urllib.request
import requests
import time
import json
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime


# Load the data
ma = ['AAA', 'AAM', 'AAT', 'ABS', 'ABT', 'ACB', 'ACC', 'ACL', 'ADG', 'ADS', 'AGG', 'AGM', 'AGR',
      'AMD', 'ANV', 'APC', 'APG', 'APH', 'ASG', 'ASM', 'ASP', 'AST', 'ATG', 'BBC', 'BCE', 'BCG',
      'BCM', 'BFC', 'BHN', 'BIC', 'BID', 'BKG', 'BMC', 'BMI', 'BMP', 'BRC', 'BSI', 'BTP', 'BTT',
      'BVH', 'BWE', 'C32', 'C47', 'CAV', 'CCI', 'CCL', 'CDC', 'CEE', 'CHP', 'CIG', 'CII', 'CKG',
      'CLC', 'CLG', 'CLL', 'CLW', 'CMG', 'CMV', 'CMX', 'CNG', 'COM', 'CRC', 'CRE', 'CSM', 'CSV',
      'CTD', 'CTF', 'CTG', 'CTI', 'CTS', 'CVT', 'D2D', 'DAG', 'DAH', 'DAT', 'DBC', 'DBD', 'DBT',
      'DC4', 'DCL', 'DCM', 'DGC', 'DGW', 'DHA', 'DHC', 'DHG', 'DHM', 'DIG', 'DLG', 'DMC', 'DPG',
      'DPM', 'DPR', 'DQC', 'DRC', 'DRH', 'DRL', 'DSN', 'DTA', 'DTL', 'DTT', 'DVP', 'DXG', 'DXV',
      'EIB', 'ELC', 'EMC', 'EVE', 'EVG', 'FCM', 'FCN', 'FDC', 'FIR', 'FIT', 'FLC', 'FMC', 'FPT',
      'FRT', 'FTM', 'FTS', 'GAB', 'GAS', 'GDT', 'GEG', 'GEX', 'GIL', 'GMC', 'GMD', 'GSP', 'GTA',
      'GTN', 'GVR', 'HAG', 'HAH', 'HAI', 'HAP', 'HAR', 'HAS', 'HAX', 'HBC', 'HCD', 'HCM', 'HDB',
      'HBC', 'HDG', 'HHP', 'HHS', 'HID', 'HII', 'HMC', 'HNG', 'HOT', 'HPG', 'HPX', 'HQC', 'HRC',
      'HSG', 'HSL', 'HT1', 'HTI', 'HTL', 'HTN', 'HTV', 'HU1', 'HU3', 'HUB', 'HVH', 'HVN', 'HVX',
      'IBC', 'ICT', 'IDI', 'IJC', 'ILB', 'IMP', 'ITA', 'ITC', 'ITD', 'JVC', 'KBC', 'KDC', 'KDH',
      'KHP', 'KMR', 'KOS', 'KPF', 'KSB', 'L10', 'LAF', 'LBM', 'LCG', 'LCM', 'LDG', 'LEC', 'LGC',
      'LGL', 'LHG', 'LIX', 'LM8', 'LPB', 'LSS', 'MBB', 'MCG', 'MCP', 'MDG', 'MHC', 'MIG', 'MSB',
      'MSH', 'MSN', 'MWG', 'NAF', 'NAV', 'NBB', 'NAV', 'NBB', 'NCT', 'NHA', 'NHH', 'NKG', 'NLG',
      'NNC', 'NSC', 'NT2', 'NTL', 'NVL', 'NVT', 'OCB', 'OGC', 'OGC', 'OPC', 'PAC', 'PAN', 'PC1',
      'PDN', 'PDR', 'PET', 'PGC', 'PGD', 'PGI', 'PHC', 'PHR', 'PIT', 'PJT', 'PLP', 'PLX', 'PME',
      'PLX', 'PME', 'PMG', 'PNC', 'PNJ', 'POM', 'POW', 'PPC', 'PSH', 'PTB', 'PTC', 'PTL', 'PVD',
      'PVT', 'PXI', 'PXS', 'PXT', 'QBS', 'QCG', 'RAL', 'RDP', 'REE', 'RIC', 'ROS', 'S4A', 'SAB',
      'SAM', 'SAV', 'SBA', 'SBT', 'SBV', 'SC5', 'SCD', 'SCR', 'SCS', 'SFC', 'SFG', 'SFI', 'SGN',
      'SGR', 'SGT', 'SHA', 'SHI', 'SHP', 'SII', 'SJD', 'SJF', 'SJS', 'SKG', 'SMA', 'SMB', 'SMC',
      'SPM', 'SRC', 'SRF', 'SSB', 'SSC', 'SSI', 'ST8', 'STB', 'STG', 'STK', 'SVC', 'SVD', 'SVI',
      'SVT', 'SZC', 'SZL', 'TAC', 'TBC', 'TCB', 'TCD', 'TCH', 'TCL', 'TCM', 'TCO', 'TCR', 'TCT',
      'TDC', 'TDG', 'TDH', 'TDM', 'TDP', 'TDW', 'TEG', 'TGG', 'THG', 'THI', 'TIP', 'TIX', 'TLD',
      'TLG', 'TLH', 'TMP', 'TMS', 'TMT', 'TN1', 'TNA', 'TNC', 'TNH', 'TNI', 'TNT', 'TPB', 'TPC',
      'TRA', 'TRC', 'TS4', 'TSC', 'TTA', 'TTB', 'TTE', 'TIF', 'TV2', 'TVB', 'TVS', 'TVT', 'TYA',
      'UDC', 'UIC', 'VAF', 'VCA', 'VCB', 'VCF', 'VCG', 'VCI', 'VDP', 'VDS', 'VFG', 'VGC', 'VHC',
      'VHM', 'VIB', 'VIC', 'VID', 'VIP', 'VIS', 'VIX', 'VJC', 'VMD', 'VND', 'VNE', 'VNG', 'VNL',
      'VNM', 'VNS', 'VOS', 'VPB', 'VPD', 'VPG', 'VPH', 'VPI', 'VPS', 'VRC', 'VRE', 'VSC', 'VSH',
      'VSI', 'VTB', 'VTO', 'YBM', 'YEG']

expList = pd.DataFrame(columns=['MÃ CỔ PHIẾU', 'GIÁ ĐÓNG CỬA', 'CHỈ SỐ RS', 'SMA50', 'SMA150', 'SMA200', 'ĐÁY 52 TUẦN', 'ĐỈNH 52 TUẦN'])
# df = pd.read_csv("ckhoan.csv",names=col_Names)
# df.head()
st.set_page_config(page_title='Khuyến nghị giao dịch cổ phiếu', page_icon=":shark:",layout="wide",initial_sidebar_state='collapsed')

def get_ckhoan():
    col_Names=["CK", "Tran", "San", "TC",
                 "Giamua3","KLmua3","Giamua2","KLmua2","Giamua1","KLmua1",
                 "GIÁ KHỚP","Khoiluongkhoplenh","Thaydoi","Phantramthaydoi",
                 "Giaban1","KLban1","Giaban2","KLban2","Giaban3","KLban3",
                 "TongKL", "Caonhat","Thapnhat","DTNNmua","DTNNban","DTNNdu"]
    df = pd.read_csv("ckhoan.csv", names = col_Names)
    df = df.drop(0)
    df.reindex(columns=['CK', 'Tran', 'San'])
    return df
# -=======================END OF GET_CKHOAN====================================================#
# @st.cache(allow_output_mutation=True)
def get_table():
    col_names = ["ID", "CK", "ISIN", "FIGI", "TENDOANHNGHIEP",
                 "KLDANGKY_NIEMYET", "KHỐI LƯỢNG LƯU HÀNH", "NGAYNIEMYET"]
    df1 = pd.read_csv("table.csv", names=col_names)
    df1 = df1.drop(0).drop(columns=['ID', 'ISIN', "FIGI"])
    df1.reindex(columns=['CK'])
    return df1
# -=======================END OF TABLE====================================================#

def get_stockfile():
    # stock = pd.read_csv('stock_file.csv')
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    stock = pd.read_csv('stock_file.csv',parse_dates=['Date'], date_parser=dateparse)
    stock.reindex(columns=['Date','Ticker'])  

    # for i in range(1, len(stock['Date'])):
    #     stock_loop = stock['Date'][i]
    #     stock_Date = datetime.datetime.strptime(stock_loop, '%Y-%m-%d')
    #     stock['Date'][i] = stock_Date.date()
    # stock['Date'] = pd.to_datetime(stock.Date)
    stock = stock.sort_values(by='Date', ascending=True)
    stock = stock.set_index('Date')
    return stock

def get_vnitable():
    vni = pd.read_csv("vni_table.csv").drop(['a', 'b', 'c', 'd'], axis=1).apply(lambda x: x.str.replace(',', '.'))
    vni = vni.drop(0)
    vni.reindex(columns=['Date','VNI_Close'])  
    vni['VNI_Close'] = vni['VNI_Close'].astype(float)

    # for i in range(1, len(vni['Date'])):
    #     loop = vni['Date'][i]
    #     vni_Date = datetime.datetime.strptime(loop, '%d/%m/%Y')
    #     vni['Date'][i] = vni_Date.date()

    vni['Date'] = pd.to_datetime(vni['Date'])
    # vni['Date'] = pd.to_datetime(vni.Date)
    vni = vni.sort_values(by='Date', ascending=True)
    vni = vni.set_index('Date')
    vni['Percent Change'] = vni['VNI_Close'].pct_change()
    vni_return = (vni['Percent Change'] + 1).cumprod()[-1]
    return  vni_return

def get_khuyennghi(stock,vni_return):
    returns_multiples = []
    m = 0
    tic_stock = []

    for i in range(0, len(ma)):
        Tic = stock[stock["Ticker"] == ma[i]]
        m = len(Tic)
        tic_stock.append(Tic)
        #     print(m)
        Tic['Percent Change'] = Tic['Adj.Close'].pct_change()
        if m != 0:
            stock_return = (Tic['Percent Change'] + 1).cumprod()[-1]
            returns_multiple = round((stock_return / vni_return), 2)
        returns_multiples.append(returns_multiple)
    rs_df = pd.DataFrame(list(zip(ma, returns_multiples)), columns=['Ticker', 'Returns_multiple'])
    rs_df['RS_Rating'] = rs_df.Returns_multiple.rank(pct=True) * 100
    rs_df = rs_df[rs_df.RS_Rating >= rs_df.RS_Rating.quantile(.70)]
    rs_df = rs_df.sort_values(by='RS_Rating', ascending=False)
    # rs_df = rs_df.set_index('RS_Rating')
    return  rs_df


# @st.cache(allow_output_mutation=True)
def get_khuyen_nghi(ma):
    stock = pd.read_csv('stock_file.csv')
    stock.reindex(columns=['Date','Ticker'])  
    for i in range(1, len(stock['Date'])):
        stock_loop = stock['Date'][i]
        stock_Date = datetime.datetime.strptime(stock_loop, '%Y-%m-%d')
        stock['Date'][i] = stock_Date.date()
    stock['Date'] = pd.to_datetime(stock.Date)
    stock = stock.sort_values(by='Date', ascending=True)
    stock = stock.set_index('Date')
    vni = pd.read_csv("vni_table.csv").drop(['a', 'b', 'c', 'd'], axis=1).apply(lambda x: x.str.replace(',', '.'))
    vni = vni.drop(0)
    vni.reindex(columns=['Date','VNI_Close'])  
    vni['VNI_Close'] = vni['VNI_Close'].astype(float)

    for i in range(1, len(vni['Date'])):
        loop = vni['Date'][i]
        vni_Date = datetime.datetime.strptime(loop, '%d/%m/%Y')
        vni['Date'][i] = vni_Date.date()

    vni['Date'] = pd.to_datetime(vni.Date)
    vni = vni.sort_values(by='Date', ascending=True)
    vni = vni.set_index('Date')

    vni['Percent Change'] = vni['VNI_Close'].pct_change()
    vni_return = (vni['Percent Change'] + 1).cumprod()[-1]
    returns_multiples = []
    m = 0
    tic_stock = []

    for i in range(0, len(ma)):
        Tic = stock[stock["Ticker"] == ma[i]]
        m = len(Tic)
        tic_stock.append(Tic)
        #     print(m)
        Tic['Percent Change'] = Tic['Adj.Close'].pct_change()
        if m != 0:
            stock_return = (Tic['Percent Change'] + 1).cumprod()[-1]
            returns_multiple = round((stock_return / vni_return), 2)
        returns_multiples.append(returns_multiple)
    rs_df = pd.DataFrame(list(zip(ma, returns_multiples)), columns=['Ticker', 'Returns_multiple'])
    rs_df['RS_Rating'] = rs_df.Returns_multiple.rank(pct=True) * 100
    rs_df = rs_df[rs_df.RS_Rating >= rs_df.RS_Rating.quantile(.70)]
    rs_df = rs_df.sort_values(by='RS_Rating', ascending=False)

    return rs_df, stock
    # -=======================END OF KHUYEN_NGHI====================================================#
# @st.cache(allow_output_mutation=True)
# @st.cache(suppress_st_warning=True)
def get_condition(exportList,rs_df, stock):
    rs_stocks = rs_df['Ticker']
    for st in rs_stocks:
        try:
            df = stock[stock["Ticker"] == st]
            sma = [50, 150, 200]
            for x in sma:
                df["SMA_" + str(x)] = round(df['Adj.Close'].rolling(window=x).mean(), 2)
            # Storing required values
            currentClose = df["Adj.Close"][-1]
            Pre_Close = df["Adj.Close"][-2]
            currentOpen = df["Open"][-1]
            Volume = df["Volume"][-1]
            Pre_volume = df["Volume"][-2]
            moving_average_50 = df["SMA_50"][-1]
            moving_average_150 = df["SMA_150"][-1]
            moving_average_200 = df["SMA_200"][-1]
            low_of_52week = round(min(df["Low"][-260:]), 2)
            high_of_52week = round(max(df["High"][-260:]), 2)
            RS_Rating = round(rs_df[rs_df['Ticker'] == st].RS_Rating.tolist()[0])
            try:
                moving_average_200_20 = df["SMA_200"][-20]
            except Exception:
                moving_average_200_20 = 0
            # Condition 1: Current Price > 150 SMA and > 200 SMA
            condition_1 = currentClose > moving_average_150 > moving_average_200
            # Condition 2: 150 SMA and > 200 SMA
            condition_2 = moving_average_150 > moving_average_200
            # Condition 3: 200 SMA trending up for at least 1 month
            condition_3 = moving_average_200 > moving_average_200_20
            # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
            condition_4 = moving_average_50 > moving_average_150 > moving_average_200
            # Condition 5: Current Price > 50 SMA
            condition_5 = currentClose > moving_average_50
            # Condition 6: Current Price is at least 30% above 52 week low
            condition_6 = currentClose >= (1.3 * low_of_52week)
            # Condition 7: Current Price is within 25% of 52 week high
            condition_7 = currentClose >= (.75 * high_of_52week)
            # Condition 8: Close price > Open Price
            condition_8 = currentClose > currentOpen
            # Condition 9 : Increase volume
            condition_9 = Volume > (1.5 * Pre_volume) and currentClose >  (1.01 * Pre_Close)
            # If all conditions above are true, add stock to exportList
            if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7 and condition_8 and condition_9):
                exportList = exportList.append({'MÃ CỔ PHIẾU': st, 'GIÁ ĐÓNG CỬA': currentClose,'CHỈ SỐ RS': RS_Rating, 'SMA50': moving_average_50, 'SMA150': moving_average_150,
                        'SMA200': moving_average_200, 'ĐÁY 52 TUẦN': low_of_52week, 'ĐỈNH 52 TUẦN': high_of_52week}, ignore_index=True)
        except Exception as e:
            print(e)
            print(f"Could not gather data on {st}")
    # currentClose
    exportList = exportList.sort_values(by='CHỈ SỐ RS', ascending=False)
   
    return exportList

# -=======================END OF GET_CONDITION====================================================#
# @st.cache(allow_output_mutation=True)
# @st.cache(suppress_st_warning=True)
def get_condition_2(exportList2,rs_df, stock):
    rs_stocks = rs_df['Ticker']
    for st in rs_stocks:
        try:
            df = stock[stock["Ticker"] == st]
            sma = [50, 150, 200]
            for x in sma:
                df["SMA_" + str(x)] = round(df['Adj.Close'].rolling(window=x).mean(), 2)
            # Storing required values
            currentClose = df["Adj.Close"][-1]
            Pre_Close = df["Adj.Close"][-2]
            currentOpen = df["Open"][-1]
            Volume = df["Volume"][-1]
            Volumn_20_average = df["Volume"][-20:].mean()
            Pre_volume = df["Volume"][-2]
            moving_average_50 = df["SMA_50"][-1]
            moving_average_150 = df["SMA_150"][-1]
            moving_average_200 = df["SMA_200"][-1]
            low_of_52week = round(min(df["Low"][-260:]), 2)
            high_of_52week = round(max(df["High"][-260:]), 2)
            RS_Rating = round(
                rs_df[rs_df['Ticker'] == st].RS_Rating.tolist()[0])
            try:
                moving_average_200_20 = df["SMA_200"][-20]
            except Exception:
                moving_average_200_20 = 0
            # Condition 1: Current Price > 150 SMA and > 200 SMA
            condition_1 = currentClose > moving_average_150 > moving_average_200
            # Condition 2: 150 SMA and > 200 SMA
            condition_2 = moving_average_150 > moving_average_200
            # Condition 3: 200 SMA trending up for at least 1 month
            condition_3 = moving_average_200 > moving_average_200_20
            # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
            condition_4 = moving_average_50 > moving_average_150 > moving_average_200
            # Condition 5: Current Price > 50 SMA
            condition_5 = currentClose > moving_average_50
            # Condition 6: Current Price is at least 30% above 52 week low
            condition_6 = currentClose >= (1.3 * low_of_52week)
            # Condition 7: Current Price is within 25% of 52 week high
            condition_7 = currentClose >= (.75 * high_of_52week)
            #         If all conditions above are true, add stock to exportList
            if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7):
                exportList2 = exportList2.append(
                    {'MÃ CỔ PHIẾU': st, 'GIÁ ĐÓNG CỬA': currentClose, 'CHỈ SỐ RS': RS_Rating, 'SMA50': moving_average_50,
                     'SMA150': moving_average_150, 'SMA200': moving_average_200, 'ĐÁY 52 TUẦN': low_of_52week, 'ĐỈNH 52 TUẦN': high_of_52week},
                    ignore_index=True)
        except Exception as e:
            print(e)
            print(f"Could not gather data on {st}")
    # currentClose
    exportList2 = exportList2.sort_values(by='CHỈ SỐ RS', ascending=False)
    # time.sleep(2)
    return exportList2
# -=======================END OF GET_CONDITION_2====================================================#
# @st.cache(allow_output_mutation=True)
# @st.cache(suppress_st_warning=True)
def get_vonhoa(hose):
    hose['GIÁ KHỚP'] = hose['GIÁ KHỚP'].astype(float)
    hose['Thaydoi'] = hose['Thaydoi'].astype(float)
    hose['KHỐI LƯỢNG LƯU HÀNH'] = hose['KHỐI LƯỢNG LƯU HÀNH'].apply( lambda x: float(x.replace('.', '').replace(',', '.')))
    # VONHOA column
    hose['VỐN HÓA THỊ TRƯỜNG'] = hose['GIÁ KHỚP'] * hose['KHỐI LƯỢNG LƯU HÀNH']
    # Von hoa plot
    vonhoa = hose[['CK', 'GIÁ KHỚP', 'KHỐI LƯỢNG LƯU HÀNH', 'Thaydoi', 'VỐN HÓA THỊ TRƯỜNG']].copy()
    vonhoa = vonhoa.dropna()
    conditions = [(vonhoa['Thaydoi'] > 0), (vonhoa['Thaydoi'] < 0),(vonhoa['Thaydoi'] == 0)]
    values = ['Tăng giá', 'Giảm giá', 'Đứng giá']
    vonhoa['BIẾN ĐỘNG'] = np.select(conditions, values)
    area = vonhoa['VỐN HÓA THỊ TRƯỜNG']
    vonhoaplot = px.scatter(vonhoa, x='GIÁ KHỚP', y='KHỐI LƯỢNG LƯU HÀNH',
                            size=area, color='BIẾN ĐỘNG',
                            color_discrete_map={'Tăng giá': 'green', 'Giảm giá': 'red', 'Đứng giá': 'yellow'},
                            hover_name='CK')
    
    vonhoaplot.update_layout(title='Vốn hoá', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    vonhoaplot.update_layout(font_family="Courier New",font_color="blue", title_font_family="Times New Roman",
                             title_font_color="red",
                             legend_title_font_color="green")
    return vonhoaplot
 # -=======================END OF GET_VONHOA====================================================#

# @st.cache(allow_output_mutation=True)
# @st.cache(suppress_st_warning=True)
def get_dandat(hose):
    
    hshort = hose[['CK', 'VỐN HÓA THỊ TRƯỜNG', "Thaydoi"]].copy()
    hshort['weights'] = hshort['VỐN HÓA THỊ TRƯỜNG'].apply(lambda x: x/hshort['VỐN HÓA THỊ TRƯỜNG'].sum())
    hshort['DIEMANHHUONG'] = hshort["Thaydoi"]*hshort['weights']
    mask = hshort['DIEMANHHUONG'] < 0
    hshort['DIEMANHHUONGDUONG'] = hshort['DIEMANHHUONG'].mask(mask)
    hshort['DIEMANHHUONGAM'] = hshort['DIEMANHHUONG'].mask(~mask)
    hshort = hshort.set_index('CK')
    topduong = hshort.nlargest(10, 'DIEMANHHUONGDUONG')
    topam = hshort.nsmallest(10, 'DIEMANHHUONGAM')
    d = (topduong["DIEMANHHUONGDUONG"].reset_index()).set_index('CK')
    a = (topam["DIEMANHHUONGAM"].sort_values(ascending=False).reset_index()).set_index('CK')
    dandat = pd.concat([d, a])
    dandatplot = go.Figure()
    dandatplot = dandatplot.add_trace(go.Bar(x=dandat.index, y=dandat['DIEMANHHUONGDUONG'],
                                             name='Điểm ảnh hưởng dương', marker={'color': 'green'}, width=0.8))
    dandatplot = dandatplot.add_trace(go.Bar(x=dandat.index, y=dandat['DIEMANHHUONGAM'],
                                             name='Điểm ảnh hưởng âm', marker={'color': 'red'}, width=0.8))
    dandatplot.update_layout(title_text='Nhóm dẫn dắt thị trường', autosize=False,legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    dandatplot.update_layout(barmode='group', xaxis_tickangle=-45)  
    dandatplot.update_layout(font_family="Courier New",font_color="blue", title_font_family="Times New Roman",
                             title_font_color="red",
                             legend_title_font_color="green")  
    return dandatplot
# -=======================END OF GET_DANDAT====================================================#
# @st.cache(allow_output_mutation=True)
@st.cache(suppress_st_warning=True)
def display(st,vonhoaplot,dandatplot,exportList2,exportList):
    # st.set_page_config(page_title='Khuyến nghị giao dịch cổ phiếu', page_icon=None,layout="wide",initial_sidebar_state='auto')
    st.markdown('<p style="font: 24px bold Georgia, serif; text-transform: uppercase; color: blue;text-align: center;font-weight: bold;"> Khuyến nghị giao dịch cổ phiếu</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:25px">Tổng quan thị trường</p>', unsafe_allow_html=True)
    col1, col2 = st.beta_columns(2)
    with col1:
        st.plotly_chart(vonhoaplot)
        st.markdown('<p style="font: 16px bold Georgia, serif; text-transform: uppercase; color: blue;text-align: center;">Danh sách cổ phiếu có xu hướng tăng</p>',unsafe_allow_html=True)
        st.table(exportList2.assign(hack='').set_index('hack'))
    with col2:
        st.plotly_chart(dandatplot)
        st.markdown('<p style="font: 16px bold Georgia, serif; text-transform: uppercase; color: blue;text-align: center;">Danh sách cổ phiếu khuyến nghị mua hôm nay</p>',unsafe_allow_html=True)
        st.table(exportList.assign(hack='').set_index('hack'))

# -=======================END OF DISPLAY====================================================#
#                                                                                           #
#======================START PROGRAM========================================================#

def main():
    df_ckhoan = get_ckhoan()
    df_table = get_table()
    hose = df_table.merge(df_ckhoan)
    # sort theo cột
    hose.sort_values(by=['CK', 'TENDOANHNGHIEP'])
    hose.reindex(columns=['CK'])
    vonhoaplot = get_vonhoa(hose)
     # Dan dat thi truong
    dandatplot = get_dandat(hose)
    stock = get_stockfile()
    vni_return = get_vnitable()
    rs_df = get_khuyennghi(stock,vni_return)
    # start = time.time()
    exportList = get_condition(expList,rs_df, stock)
    st.write('exportList 1 :' , exportList)
    exportList = exportList.loc[{18,4,12,6}]
    # print(end - start)
    exportList2 = get_condition_2(expList,rs_df, stock)
    display(st, vonhoaplot, dandatplot,exportList2,exportList)
# ========================================MAIN==============================================#

if __name__ == "__main__":
    main()
