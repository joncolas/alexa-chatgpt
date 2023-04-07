# Alexa + Chatgpt

![image](https://user-images.githubusercontent.com/8049798/229324068-32287de1-a08e-40eb-bdaf-2e92c52b50c2.png)


## Description 

Alexa Skill to make conversations with ChatGPT.


## Features
- Send prompts to ChatGPT
- Conversational interaction, ChatGPT prompts are saved in the skill session.
- Supported languages English(en-US) and Spanish(es-ES)


## Usage

Interaction example:
  ```
  User > "Alexa, open chat gpt"
  Alexa > "Chat GPT activated, What do you need?"
  User > "Jarvis, ¿how much is 3+7?"
  Alexa > "The result is 10"
  User > "Jarvis, and if we replace 7 number by 2 ?"
  Alexa > "The result is 5"
  ```


## How to setup this skill to your Alexa Developers Console


### Using the Alexa Developers Console

To import an Alexa-hosted skill from a public Git repository

1. Open the [Alexa developer console](https://developer.amazon.com/alexa/console/ask) and log in.
1. Click **Create Skill**. The **Create a new skill page** appears.
1. For **Skill name**, use "chat gpt".
1. For **Default language**, choose language, this skill is compatible with English(en-US) and Spanish(es-ES).
1. For **Choose type of experience**, **select Other**.
1. For **Choose a model to add to your skill**, **select Custom**.
1. For **Choose a method to host your skill's backend resources**, select **Alexa-Hosted (Python)**.
1. For **Hosting region**, select one of your preference, the closer the better.
1. Click **Create Skill**. The **Choose a template to add to your skill** page appears.
1. Click **Import skill**. The **Import skill** dialog appears. Enter "https://github.com/joncolas/alexa-chatgpt.git"
1. Click **Continue**. The message **Creating your Alexa-hosted skill appears**. If Alexa validates that the Git repository contains an Alexa skill that it can import Alexa creates your Alexa-hosted skill.

Reference:
- https://developer.amazon.com/en-US/docs/alexa/hosted-skills/alexa-hosted-skills-git-import.html#import)


#### Final skill setup

Once the skill was imported to your Alexa Developer Console, enter inside and do this steps:
- Replace `YOUR_OPENAI_API_KEY` by your OpenAi ApiKey in [chatgpt.py](lambda/py/chatgpt.py) file. If you don't have it yet you can create a new one from https://platform.openai.com/account/api-keys.
- In order to allow your Alexa devices run Chat gpt skill ensure that **Skill testing is enabled in Development mode**, go to **Test** tab and Select **Development**.

Now you can start using Chat GPT skill in your alexa devices!


# Test ChatGPT python module localy

You can test ChatGPT python module from your local machine in the following way:
1. Change to the lambda/py directory
    ```
    cd lambda/py/
    ```
1. Set your OpenAI apiKey environment variable
    ```
    cp .env.template .env
    ```
1. Load environment
    ```
    source .env
    ```
1. Prepare a virtualenvironment for OpenAI
    ```
    pip install virtualenv
    virtualenv chatgpt_skill_module
    source chatgpt_skill_module/bin/activate
    pip install openai
    ```
1. Execute the script
    ```
    python test_chatgpt.py
    ```


# Limitations

By definition, Alexa can not wait more than 10 seconds to get response from a skill so if your prompt takes more than 10 seconds to resolve Chat GPT skill will give you error.


# Troubleshooting

You can check logs in CloudwatchLogs from the Code tab in the Alexa Developers Console.
