from urllib import request

notice_url= 'http://www.data.gov.bd/api/download/?id=02b25f92-8a24-489c-906e-3b5703650df4'

def download_csv(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url=r'notice_encoded.csv'#txt / csv
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_csv(notice_url)
