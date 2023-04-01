# alexa-chatgpt

## Usage

  The interaction model only is in spanish by the moment
  ```
  User > "Alexa, abre [YOUR_SKILL_NAME]"
  Alexa > "Alexa mejorada activada, ¿qué necesitas?"
  User > "Dime [CHAT_GPT_PROMPT]"
  ```
  In example,
  ```
  User > Alexa, abre Inteligencia artificial
  Alexa > Alexa mejorada activada, ¿qué necesitas? 
  User > Dime "¿que és lorem ipsum?"
  ```
  or
  ```
  User > Alexa, abre Inteligencia artificial y dime "¿que és lorem ipsum?"
  ```

## How to setup this skill to your Alexa Developers Console

### OPTION 1: Using the Alexa Developers Console

To import an Alexa-hosted skill from a public Git repository

1. Open the [Alexa developer console](https://developer.amazon.com/alexa/console/ask) and log in.
1. Click **Create Skill**. The **Create a new skill page** appears.
1. For **Skill name**, you can use any name here. I set "ChatGPT".
1. For **Default language**, choose a language. By the moment this skill only works in Spanish.
1. For **Choose a model to add to your skill**, **select Custom**.
1. For **Choose a method to host your skill's backend resources**, select **Alexa-Hosted (Python)**.
1. Click **Create Skill**. The **Choose a template to add to your skill** page appears.
1. Click **Import skill**. The **Import skill** dialog appears. Enter "https://github.com/joncolas/alexa-chatgpt.git"
1. Click **Continue**. The message **Creating your Alexa-hosted skill appears**. If Alexa validates that the Git repository contains an Alexa skill that it can import Alexa creates your Alexa-hosted skill.

[From "Import an Alexa-hosted skill from a public Git project"](https://developer.amazon.com/en-US/docs/alexa/hosted-skills/alexa-hosted-skills-git-import.html#import)

**Remeber** to update `openai.api_key` variable with your key obtained from https://platform.openai.com/account/api-keys

# Troubleshooting

If the skill doesn't respond when you are asking for a question it could be related to RateLimitError, [see](https://help.openai.com/en/articles/6897202-ratelimiterror) for more information
