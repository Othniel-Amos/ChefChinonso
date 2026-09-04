# LLM 

## configure.py 
<p>This configures the API key by accessing a hidden .env file. It then uses that key to call the gemini API to get a response from the gemini model 3.1-Flash-Lite.</p>
<p>A class is then created using this model to handle chatting with the chat bot and to abstract as much of the back end configurations as possible</p>
<p>This class then gets called upon by the other .py files</p>

## web_app.py 
<p>Using streamlit, all of the data is output to a locally hosted website allowing for a clean UI</p>

## main.py 
<p>Mostly for debugging, this allows direct communictaion with the bot from CLI</p> 

## LLM 
<p>The LLM used here is the gemini model 3.1-Flash-Lite. It is used for its fast response time, its generosity with the amount of tokens that can be output daily and majorly for the fact that this model is <i>free</i> <i><b>(No credit cards attached)</b></i>. </p> 

## [Video Demo](https://quantilumbi-my.sharepoint.com/:v:/p/othniel_a/IQBiJQ4UUqOrTbExQGBqXccTAfUA2x2tp_ESz6bacWj3ulc?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=PqCuy6) 

<footer>Thank you</footer>