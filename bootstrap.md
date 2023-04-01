# Alexa skill bootstrap using ASK CLI (WIP)

Follow this steps to create a new Alexa skill from your local machine without accesing to Alexa developers console.


1. Install node and npm binaries on your system. Use the way you like to install this dependencies, in example:
    ```
    sudo apt-get install node npm
    ```
1. Install ASK CLI to deploy Alexa skills from command line
    ```
    sudo npm install -g ask-cli@2
    ```
1. Configure ASK CLI to allow communication with your Alexa developers console account. This command will follow you to configure all required stuff.
    ```
    ask configure
    ```
1. Create skill with ask cli
    ```
    ask new # your will create here the skill under YOUR_SKILL_FOLDER
    ask deploy (is required to upload the uterances to allow developers console route requests to the local skill properly)
    ```
1. Setup python environment
    ```
    pip install virtualenv
    pip install ask-sdk
    pip install ask-sdk-local-debug
    ```
1. Route Alexa requests to your Alexa skill in the Alexa developers console
    ```
    cd YOUR_SKILL_FOLDER 
    ask run (Will route your skill requests to your local code)
    ```
1. Open a conversation with your skill
    ```
    ask dialog (Will send your requests to your skill)
    User  > open change me
    Alexa > Welcome, you can say Hello or Help. Which would you like to try?
    User  > hello
    Alexa > Hello World!
    ```

References: 
- https://developer.amazon.com/en-US/docs/alexa/smapi/quick-start-alexa-skills-kit-command-line-interface.html#install-initialize
- https://developer.amazon.com/en-US/docs/alexa/alexa-skills-kit-sdk-for-python/set-up-the-sdk.html


## Testing Alexa skill local code
When I tested it gives me this error:
```
We're sorry!
An error occurred when we tried to process your request. Rest assured, we're already working on the problem and expect to resolve it shortly.
```
https://developer.amazon.com/en-US/docs/alexa/ask-toolkit/vs-code-testing-simulator.html

May be Amazon is having erros with this feature.