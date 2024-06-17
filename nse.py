import requests
import pandas as pd

def download(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'Cache-Control': 'no-cache',
    'Cookie':'_ga=GA1.1.1145294235.1709020281; _ga_QJZ4447QD3=GS1.1.1715225415.12.0.1715225416.0.0.0; defaultLang=en; nseQuoteSymbols=[{"symbol":"BEL","identifier":null,"type":"equity"},{"symbol":"NAVINFLUOR","identifier":null,"type":"equity"}]; nsit=RfrARw9n8QeUXCrtwBMNXOih; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxODYwNjg0OSwiZXhwIjoxNzE4NjE0MDQ5fQ.ALPuU7Tceb9anPwuAa2kElAuLjj4hH8oA5ohKe3UTF4; AKA_A2=A; bm_mi=5AAE324A5344A247CA10292186B08308~YAAQXdcLFx54nQSQAQAAC2jzJBhXdI01sTEu3Mud/eUXS+OevN9NS3dDtOgFydISdqGMBKcHR0cPXy2EgcNs/2y5wQBJns2hBHy14AsonGwU3t75ulZ8Cp/P3wGVGcr8PfOfwUHRazwmgbf66+LmnSd3jXAp0MIhoqA+jfNJe8xdrT4MHCyKHGFYbYl4Qo9+DX3lSlcrlz1MGfma6Rd39be2pEmwL6pbEK4vM3nOdelXOJ4C3XsbESUPgb+J+SctbYtyDWXM1rODtgeuQibCthXxpXay31EnD5mdaUvCZDX99BeK/s/fqTkm5RMhAbyHt6RgH4aizjozri9LQDhuzcEdumj9AYnJr5buRkZBufBtEcu+ChZ9lMyJAKXS2zn9~1; bm_sz=88185E3143B728B4919B40ECF41D46E5~YAAQXdcLFyB4nQSQAQAAC2jzJBg2HtIeJP8xureVyIdC3Mb/qFApqk5lDLfO3vHAblrvJwW0/McAIZezAl28ZqMC15Z3Fbk/y/YXhOl0m5v0k199zZ3AUL7KN8vI5fSxQ4RsBMBNm3j19yKTyv1QUG8tH7o47pYAD8P2Xu20vGnuqeOfeWM66HF7B9VcsjdHlICGnq/DXWgFGm+fRIGoEpfLRP7IZnmFu4wmtQvZ8h2Yn+OuSLKpMadRlJjYwOS9b6mGwfGB3glYWVOjHJ3QK5wdT+UgQ+T1P5mazSs+3BvCjc6JJdv2MV9PP4MGfLfJY0FIKJcA0fJzAs6XrPwN0++UZHuo0mXNAvIJsZjM+vUZNdxGZkTzqDivWK6j6ZXr/F2OHQiJSH/KLTvSVsWNuOmtVU2gqA==~4343092~3684656; _ga_87M7PJ3R97=GS1.1.1718605440.42.1.1718606856.0.0.0; RT="z=1&dm=nseindia.com&si=1e58f2b7-7c00-47bb-afd0-dba52f79e1be&ss=lxilaycf&sl=1&se=8c&tt=7g6&bcn=%2F%2F684d0d42.akstat.io%2F&ld=ui41"; ak_bmsc=26B86EEB1F6490F57F44CA215D91FF28~000000000000000000000000000000~YAAQXdcLFwN5nQSQAQAAkZrzJBj67gJ8t0X5LvFAII14z1Nk2v1KhHwxtcC/eGEy2SPeCOJvmrF3DMuEe+f+140vbt9Q47Yl/jEXf+xRUlLIp6H8mt+Zu4Los6WZEV/kp9pAnWG+hlZZdUJ+CN4kdaXA63Mfheuh9WwWDC5XvV7DwbHQ0z7THXiVPipZw0KJyEelLKttPXNUSZ7xQKNXZQxCZ8UIEuckzlEqi3ox+rmLpH5Qk4vdIa2HjqOaeGor57j/2wlvnXDP65SxsrMfmIQAfmhuXWYXFisxjuAtJZB0kU/E4vssMmiEr4QU3KE7jYaIvpvTG594gywYiQZwIbW6OCTUVkyfIf09Ixm3jd4Mot7r0tMKCJM1ezA7E0zhgq8/Q5evhIYGh1Vj9dBTahpOwZX+ufn/b9nylFZoW9uHnnQVU3GYYGbXSScTsy+WzRjrpKZe+U6z8O2Ew468g2ob6+mLYe3tmySFr9jENltXMo8x0lQkzGJBdr4mpCVCeJfGDVQAcO+FZAAMWsdtm3zZmM5g/54vegDCn/zDRUQuc59aDGyPyxm7oyWHPSfy18o=; _abck=0F5C311E1700E80FE7281C42F3230CE5~0~YAAQXdcLFzh5nQSQAQAASLHzJAwDdOOMQ4St4QHSP6Pe44Ttcn3OUyjEPdCbwuJSkIcLBmW1ezZalKc5TfmN/PCEu9560m+mqTYnV07YHZh9hkI36YlDf3l4vKNDkvQExNIM1VPzmtzJLnltz4B+dxVuZ0p8LDN4H0pd8b6RkZMg3bV+lHsI9LY0oQvdPfrqtReP7p2YF7sR7EPFbcaoP6hDD9TUpFSpjYNn/lj5IdOMvTvyPREjTj8IJSiX0KId1A/kBYmn326LUiwuvx1SE3y7Gq36gBeF1tYbR+FXgKi2ryTzwG2rHw8etfGgucbCXaVRyCNAiL7nkce5uMJ0bjQGSbXbFEwbKdaRZWgmEfDWhSq+9sq0liCiIsvBd+A=~-1~-1~-1; bm_sv=DC114F37837C955FD7BEBA3D2901031F~YAAQXdcLFzl5nQSQAQAASLHzJBiKla9RG2F5LEcPc9R5o0NM/PwSyWeq+3gyWxt1AS2IqmeMRkqAbI2cuewWYFReq5WBOPJEFKenI/rP2DOs2+w/NJWBAA/jwfjrwj+wVACU5WUBAFx83Kw8/ijq+3dJcjGROuQAeDbZUxwN7T9j1eX1ixIjgNY3dWw/uJneVaNsZy4dhbCmHO0Diw5GVdsk17dd2E+voB2c/4IyGImukRN67/PgVTdtXPuQbNjkW0TS~1'
}

url = 'https://www.nseindia.com/api/market-data-pre-open?key=FO'

data = download(url, headers)


symbol_details = []
for item in data.get('data', []):
    metadata = item.get('metadata', {})
    detail = {
        'Symbol': metadata.get('symbol'),
        'Last Price': metadata.get('lastPrice'),
        'Change': metadata.get('change'),
        'Percentage Change': metadata.get('pChange'),
        'Previous Close': metadata.get('previousClose'),
        'Market Cap': metadata.get('marketCap'),
        'Year High': metadata.get('yearHigh'),
        'Year Low': metadata.get('yearLow'),
        'IEP': metadata.get('iep'),
        # 'Chart Today Path': metadata.get('chartTodayPath')
    }
    symbol_details.append(detail)

# Create a DataFrame
df = pd.DataFrame(symbol_details)




# Display the DataFrame
# print(df)
# Round numerical columns
df_rounded = df.round({
    'Previous Close': 2,
    'Last Price': 2,
    'Change': 2,
    '% Change': 2,
    'Market Cap': 2,
    'Year High': 2,
    'Year Low': 2,
})

# Specify the CSV filename
csv_filename = 'symbol_details.csv'

# Save rounded DataFrame to CSV
df_rounded.to_csv(csv_filename, index=False)

print(f'Saved DataFrame to {csv_filename} after rounding numerical values.')

