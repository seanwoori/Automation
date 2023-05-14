import requests
import json

api_key = "Insert_API_KEY"

anode_materials = {
    "LCO": "CO",
    "LMO": "NI",
    "LNO": "MN",
    "NCM": "FE",
    "NCA": "FE",
    "LFP": "LI"
}

def create_url(symbols):
    return f"https://api.metals.live/v1/latest/{','.join(symbols)}?access_key={api_key}"

print("다음 중 양극재를 선택하세요:")
print("1. LCO")
print("2. LMO")
print("3. LNO")
print("4. NCM")
print("5. NCA")
print("6. LFP")

choice = int(input("선택: "))

if choice < 1 or choice > 6:
    print("잘못된 선택입니다.")
else:
    symbol = anode_materials[list(anode_materials.keys())[choice - 1]]

    url = create_url([symbol])

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("API 요청에 실패했습니다. 에러 메시지:", data["error"]["message"])
    else:
        loading = float(input(f"{list(anode_materials.keys())[choice - 1]} 양극재 로딩량을 입력하세요: "))

        price = data["rates"]["USD" + symbol] * loading

        print(f"{list(anode_materials.keys())[choice - 1]} 양극재 가격:", price)
