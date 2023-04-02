# Alexa + Chatgpt

![image](https://user-images.githubusercontent.com/8049798/229324068-32287de1-a08e-40eb-bdaf-2e92c52b50c2.png)

## Usage

  There are two interaction models, in example, for es-ES:
  ```
  User > "Alexa, abre chat gpt"
  Alexa > "Chat GPT activado, ¿Qué necesitas? empieza la pregunta por la palabra 'dime'"
  User > "Dime ¿qué es lorem ipsum?"
  ```
  or
  ```
  User > "Alexa, abre chat gpt y dime ¿qué es lorem ipsum?"
  ```

## How to setup this skill to your Alexa Developers Console

### Using the Alexa Developers Console

To import an Alexa-hosted skill from a public Git repository

1. Open the [Alexa developer console](https://developer.amazon.com/alexa/console/ask) and log in.
1. Click **Create Skill**. The **Create a new skill page** appears.
1. For **Skill name**, you can use any name here. I set "Chat GPT".
1. For **Default language**, choose language, this skill is compatible with Spanish(Spain) and English(US).
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
- Update `openai.api_key` variable in [lambda_function.py](lambda/py/lambda_function.py) with an OpenAI API Key obtained from https://platform.openai.com/account/api-keys.
- Ensure the **Skill Invocation Name** is defined, In the ADC go to **Build tab**, **Invocations > Skill Invocation Name**, I used **"Chat gpt"**.
- In order to allow your Alexa devices run Chat gpt skill ensure that **Skill testing is enabled in Development mode**, go to **Test** tab and Select **Development**.

Now you can start using Chat GPT skill in your alexa devices!

# Troubleshooting

If the skill doesn't respond when you are sending a prompt it could be related to RateLimitError, see [here](https://help.openai.com/en/articles/6897202-ratelimiterror) for more information
