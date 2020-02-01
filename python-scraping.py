import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from subprocess import check_output



def main(url, sno):
  with requests.Session() as session:
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    image_name = soup.div.img['src']
    local_image_path = "/tmp/" + image_name + '.jpeg' 
    download_image_url = url + image_name
    image=session.get(download_image_url)
    with open(local_image_path, 'wb') as f:
      f.write(image.content)
    check_output(['convert', local_image_path, '-resample', '600', local_image_path])
    captcha = pytesseract.image_to_string(Image.open(local_image_path))
    submit_captcha=captcha.replace(" ","").upper
    data_obj = {'txtgno': sno, 'txtCaptcha': submit_captcha}
    result = session.post(url, data_obj)
    print(result.status_code)

    

if __name__ == "__main__":
  website_name = "https://results.unom.ac.in/nov2019/"
  main(website_name,211804220)


211804220


txtrgno
txtCaptcha
