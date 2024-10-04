# teams_alert

## Introduction

teams_alert is a python package that allows you to send alerts to Microsoft Teams. It is a simple package that allows you to send messages to a channel in Microsoft Teams.

## Getting Started

1. Installation process
```pip install teams_alert```

2. Import the package
```from teams_alert import TeamsAlert```

3. Create an instance of TeamsAlert
```teams_alert = TeamsAlert(webhook_url)```

4. Send a message - email is optional
```teams_alert.send("Some sort of title you'd want to use", "Some sort of message you'd want to send", "jimbo_p@oxy.com")```

![Result](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/result_card.JPG)

## How to get the webhook URL

1. Go to the Team and channel you are interested in posting to. Click the three dots next to the channel name and select "Workflows".

    ![Workflows](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/teams_workflows.JPG)

2. Find "Post to a channel when a webhook request is received"

    ![Post to a channel when a webhook request is received](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/teams_webhook_workflow.JPG)

3. Name the workflow if you so desire

    ![Name the workflow](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/workflows_naming.JPG)

4. Check that the Team and Channel are correct

    ![Check that the Team and Channel are correct](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/workflow_team_and_channel.JPG)

5. Copy the webhook URL

    ![Get the webhook URL](https://raw.githubusercontent.com/jimbo-p/teams_alert/c367c1ff8612c09aeea7bea15c2b1a7d71ecc478/docs/workflow_URL2.JPG)
