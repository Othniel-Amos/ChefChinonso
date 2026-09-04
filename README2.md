# LLM ChatBot Chef Chinonso 

## A brief description 

<p>Chef Chinonso is an AI powered chatbot which can converse with you about any <b>Nigerian</b> dish. Chef Chinonso is quite the jovial chat bot cracking jokes while talking in Nigerian pidgin English. There are two types of app for this chat bot </p> 

- One is a web app 
- The second app uses a CLI 

<p>The reason why there are two apps is because I was personally intrested with how to implement a ChatBot on the web. I've seen many different platforms integrate a ChatBot on their webpage so I wanted to challenge myself and see how easy it would be to build one onto a webpage.</p> 

### Web App 
<p>Using the web app you can communicate to the ChatBot Chef Chinonso. Chef Chinonso is powered by Gemini 3.1 flash lite model.</p>
<p>One major challenge I had was limiting the use of output tokens. When asked a simple prompt the AI would often use way too many tokens to answer it. In order to combat this, in the system instructions of the AI I added that responses should be brief</p>
<p>Another challenge that I had was deciding which AI model I should use. Initially I wanted to use Open AI but that required attaching a card to use the model. That's how I settled on using Gemini as it has quite a generous free tier <i>(without attaching any cards)</i></p> 

<p>Below are some steps on how to use the web app</p>

- What the User sees upon launching the app 
<img width="1918" height="919" alt="image" src="https://github.com/user-attachments/assets/4c58d96e-afe9-4ec7-895d-f0141f1cb400" />
 

- User types a prompt 
<img width="1009" height="796" alt="image" src="https://github.com/user-attachments/assets/d2d15a99-a693-49a0-aea4-20bd77a3210e" />


- The LLM's response 
<img width="969" height="924" alt="image" src="https://github.com/user-attachments/assets/a563e09c-bbff-4cbf-b07e-60b165430b69" />


- What happens when the user tries to go of topic 
<img width="935" height="620" alt="image" src="https://github.com/user-attachments/assets/fb339f60-5b5f-4a65-8afa-b6e57184560b" />

### CLI App 

- The command line app works exactly the same as the web app just in the PowerShell terminal 

- Notice that the ChatBot usually writes in markdown which isn't rendered in the terminal but it is rendered in the web app   
<img width="1260" height="491" alt="image" src="https://github.com/user-attachments/assets/83218025-ed87-4f74-ae06-cf9bd3a4845f" />




