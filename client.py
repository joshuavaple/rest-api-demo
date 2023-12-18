import requests
import json
import jsonify

summarize_endpoint = 'http://127.0.0.1:5000/summarize'
ARTICLE = """ 
More training for door staff and funding for testing kits are among a package of measures announced to crack down on spiking.
The Home Office has said the law will also be "modernised" to make it clear spiking - putting alcohol or drugs into another person's drink or body without their consent - is a crime.
The plans have broadly been welcomed by campaigners.
But they stop short of calls from some to make spiking a specific offence.
The measures announced by the government include:
Training hundreds more door staff to stop potential perpetrators and signs someone may have been spiked
Investing in research into testing kits to detect if someone's drink has been spiked
Intensive operations by the National Police Chiefs' Council (NPCC) across England and Wales, targeting key weeks when spiking tends to be prevalent
An online tool to be rolled out to all police forces to make it easier for people to report spiking anonymously
Home Secretary James Cleverly said: "Spiking is a perverse crime which can have a lasting impact on victims.
"Our comprehensive new measures are designed to help police and staff in bars, restaurants, pubs and other premises to protect victims and bring more offenders to justice."

"""

def get_summary(text:str):
    body = {'text': text}
    response = requests.post(summarize_endpoint, json=body)
    return response.json()

if __name__ == '__main__':
    summary = get_summary(ARTICLE)
    print(summary)