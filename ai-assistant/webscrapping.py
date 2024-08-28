import requests
import json
from bs4 import BeautifulSoup
reviews = []
def get_reviews(professor_id):
  url = f"https://www.ratemyprofessors.com/professor/{professor_id}"
  headers = {"User-Agent": "Mozilla/5.0"}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")

  reviews = []

  for review in soup.find_all("div", class_="Rating__StyledRating-sc-1rhvpxz-1 jcIQzP"):
      professor = soup.find("div", class_="NameTitle__Name-dowf0z-0").text.strip()
      review_text = review.find("div", class_="Comments__StyledComments-dzzyvm-0").text.strip()
      subject = review.find("div", class_="RatingHeader__StyledClass-sc-1dlkqw1-3").text.strip()
      rating = float(review.find("div", class_="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2").text.strip())
      date = review.find("div", class_="TimeStamp__StyledTimeStamp-sc-9q2r30-0 bXQmMr RatingHeader__RatingTimeStamp-sc-1dlkqw1-4 iwwYJD").text.strip()
      reviews.append({
                "professor": professor,
                "review": review_text,
                "subject": subject,
                "rating": rating,
                "date" : date
            })
  return reviews

ids= [1621181, 2393114]
for id in ids:
  reviews.append(get_reviews(id))


data = {
    "reviews": reviews
}
with open("reviews.json", "w") as f:
    json.dump(data, f, indent=4)