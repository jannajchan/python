"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Get data from API (data.go.th)
# ----------------------------------------------------------------------------------------------------------------------
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import requests

# === Configuration ===
TH_FONT_PATH = "C:\\Windows\\Fonts\\upcel.ttf"
FONT_PROP = fm.FontProperties(fname=TH_FONT_PATH)

def getResponseDataFromAPI(params):
    # URL of the API endpoint
    url = "https://opend.data.go.th/get-ckan/datastore_search"

    # Optional: If the API requires an API key
    headers = {
        "api-key" : "LLkds0iPgrsMdk6sZzfwRJQgpIW1oIjF"
    }

    # Make the GET request
    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON
        records = data.get("result", {}).get("records", [])  # Extract records
        return records
    else:
        print("Error:", response.status_code, response.text)
        return None

def plotPieChart(labels, values, title):
    plt.pie(values, labels=labels, autopct='%1.1f%%', textprops={"fontproperties": FONT_PROP, "fontsize": 16})
    plt.title(title, fontproperties=FONT_PROP, fontsize=24)
    plt.show()

def plotBarChart(xlabel, x, ylabel, y, title):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(x, y)

    # Set title and axis labels using Thai font
    plt.title(title, fontproperties=FONT_PROP, fontsize=24)
    plt.xlabel(xlabel, fontproperties=FONT_PROP, fontsize=16)
    plt.ylabel(ylabel, fontproperties=FONT_PROP, fontsize=16)

    # Rotate x-labels for readability
    plt.xticks(rotation=90, ha='right', fontproperties=FONT_PROP, fontsize=12)
    plt.yticks(fontproperties=FONT_PROP, fontsize=12)

    # Optionally: add values on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + max(y)*0.01, f'{int(yval)}', ha='center', va='bottom', fontproperties=FONT_PROP, fontsize=10)

    plt.tight_layout()
    plt.show()

"""
# [💪 Challenge ✨1] Get data from API-GorBorKor, and plot pie chart ==================================================
# ----------------------------------------------------------------------------------------------------------------------
    ข้อมูลจำนวนสมาชิกของแต่ละช่วยอายุ กองทุนบำเหน็จบำนาญข้าราชการ (กบข)
    URL: https://data.go.th/dataset/opn00010
# ----------------------------------------------------------------------------------------------------------------------
"""
def plotChartGorBorKor():
    params = {
        "resource_id" : "1b216364-bf2c-4085-b757-2f903b3ba0fd"
        # ,"limit" : 5, # Number of records to retrieve
    }
    records = getResponseDataFromAPI(params)
        
    dataDict = {}
    for record in records:
        if record["AgeTierName"] in dataDict:
            dataDict[record["AgeTierName"]] += 1
        else:
            dataDict[record["AgeTierName"]] = 1

    x = list(dataDict.keys())
    y = list(dataDict.values())
    plotPieChart(x, y, "Pie Chart แสดงจำนวนสมาชิกของแต่ละช่วงอายุ")

plotChartGorBorKor()


"""
# [💪 Challenge ✨2] Get data from API-WaterConsumption, and plot pie chart ===========================================
# ----------------------------------------------------------------------------------------------------------------------
    สถิติการใช้น้ำประปา ปี พ.ศ.2568 (100 รายการ)
    URL: hhttps://data.go.th/dataset/cus_consumption
# ----------------------------------------------------------------------------------------------------------------------
"""
def plotChartWaterConsumption():
    params = {
        "resource_id" : "645cbbfe-1c02-4c76-9439-8e51d266908a"
        ,"limit" : 100, # Number of records to retrieve
    }
    records = getResponseDataFromAPI(params)
        
    df = pd.DataFrame(records)
    sum_by_tambon_name = df.groupby('tambon_name')['consumption'].sum()
    dataDict = sum_by_tambon_name.to_dict()

    x = list(dataDict.keys())
    y = list(dataDict.values())
    plotBarChart("ตำบล", x, "ปริมาณการใช้น้ำ (ลบ.ม.)", y, "สถิติการใช้น้ำประปา ปี พ.ศ.2568")

plotChartWaterConsumption()