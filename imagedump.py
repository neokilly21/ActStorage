import requests
import json
from datetime import datetime

# 이미지가 있는 image_url을 통해 file_name파일로 저장하는 함수
def save_image(image_url, file_name):
    img_response = requests.get(image_url)

    #요청에 성공하면
    if img_response.status_code == 200:
        #파일 저장
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)



# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK a08daf0476cc8ca5f7dd8ad868d5fdef"
}
data = {
    "query" : "고준희"
}

# 이미지 검색요청
response = requests.post(url, headers=headers, data=data)

# 요청에 실패했다면
if response.status_code != 200:
    print("error!  because ", response.json())
else:   # 성공했다면
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image url =", image_info['image_url'])

        # 저장할 이미지의 파일명 설정 , 검색어+시간+번호를 파일명으로 사용
        count = count + 1
        query = data["query"]     
        timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
        file_name = f"{query}_{timestamp}_{count}.jpg"
        #이미지 저장
        save_image(image_info['image_url'], file_name)


