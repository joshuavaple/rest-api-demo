from lib.helpers import clean_string


# we can send a string to the server and get a response instead of using postman:
import requests
import json

summarize_endpoint = "http://127.0.0.1:5000/summarize"
ARTICLE_1 = """ 
Luton's Premier League match at Bournemouth has been abandoned after their captain Tom Lockyer collapsed on the pitch.
Both sets of players were taken off midway through the second half as Lockyer received medical treatment.
After several minutes, he was taken off on a stretcher, applauded by all four sides of the ground.
Reports from the ground later said the 29-year-old defender was "alert and responsive".
Lockyer collapsed during the play-off final win against Coventry in May before being taken to hospital.
He subsequently had heart surgery and was given the all-clear to return to playing in June.
After confirmation the game was abandoned, both the Luton and Bournemouth players came back out on to the pitch to applaud the supporters.
The Premier League said in a statement: "The match between AFC Bournemouth and Luton Town FC has been abandoned due to a player medical incident.
"Our thoughts are with Tom Lockyer and all players involved in today's match."
"""

ARTICLE_2 = """ 
SINGAPORE: Singapore Prime Minister Lee Hsien Loong met his Japanese counterpart Fumio Kishida on Saturday (Dec 16) during his trip to Tokyo.
Mr Lee is in Tokyo from Dec 15 to Dec 18 for the ASEAN-Japan Commemorative Summit. 
The prime ministers welcomed the signing of a memorandum of cooperation to establish a green and digital shipping corridor between ports in Singapore and Japan.
The agreement will facilitate the adoption of digital solutions and the provision of zero and near-zero emission fuels through demonstration projects, said the Ministry of Foreign Affairs (MFA) in a statement on Saturday.
Both prime ministers also reaffirmed the longstanding and excellent relations between Singapore and Japan, and discussed how the countries could further expand and deepen cooperation in areas of mutual interest, such as the future economy, digitalisation, security, as well as sustainability and energy.
The leaders exchanged views on regional and international developments, and emphasised the importance of upholding a rules-based international order and the principles enshrined in the United Nations Charter.
"Both leaders welcomed the upgrade of ASEAN-Japan relations to a Comprehensive Strategic Partnership earlier this year, and noted that this would be an opportunity to further ties between both sides as well as jointly address the challenges facing the region," said MFA.
The prime ministers also "looked forward to celebrating 60 years of Singapore-Japan diplomatic relations in 2026".
"""
def get_summary(text):
    body = {"text": clean_string(text)}
    response = requests.post(summarize_endpoint, json=body)
    return response.json()

if __name__ == '__main__':
    summary_1 = get_summary(ARTICLE_1)
    print(summary_1)
    summary_2 = get_summary(ARTICLE_2)
    print(summary_2)
