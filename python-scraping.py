import requests
from bs4 import BeautifulSoup
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract




def main(url):
  with requests.Session() as session:
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    image_name = soup.div.img['src']
    local_image_path = "/tmp/" + image_name 
    download_image_url = url + image_name
    image=session.get(download_image_url)
    with open(local_image_path, 'wb') as f:
      f.write(image.content)
    print(pytesseract.image_to_string(Image.open(local_image_path)))

if __name__ == "__main__":
  website_name = "https://results.unom.ac.in/nov2019/"
  main(website_name)


211804220


txtrgno
txtCaptcha
