import json

def gen_card_to_person(title: str, message: str, email: str,) -> str:
    """
    Generates a JSON payload for a message to send to a Microsoft Teams Channel with a person tagged.
    
    Args:
        title (str): The title of the message.
        message (str): The message to send.
        email (str): The email of the person to tag.
    """
    card_to_person = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {

                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "",
                                    "wrap": "true",
                                    "size": "Large",
                                    "weight": "Bolder",
                                    "color": "Attention",
                                    "maxLines": 0,
                                    "horizontalAlignment": "Left",
                                    "id": "title"
                                },
                                {
                                    "type": "ColumnSet",
                                    "minHeight": "0px",
                                    "style": "emphasis",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Attention:",
                                                    "wrap": "true",
                                                    "id": "lbl_attention",
                                                    "size": "Medium",
                                                    "weight": "Bolder",
                                                    "color": "Warning"
                                                },
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Message: ",
                                                    "wrap": "true",
                                                    "size": "Medium",
                                                    "weight": "Bolder",
                                                    "color": "Accent",
                                                    "id": "lbl_msg"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "<at>User_1</at>",
                                                    "wrap": "true",
                                                    "id": "txt_attention"
                                                },
                                                {
                                                    "type": "TextBlock",
                                                    "text": "",
                                                    "wrap": "true",
                                                    "id": "txt_msg"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "msteams": {
                        "entities": [
                            {
                                "type": "mention",
                                "text": "<at>User_1</at>",
                                "mentioned": {
                                    "id": ""
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
    card_to_person["attachments"][0]["content"]["body"][0]["items"][0]["text"] = title
    card_to_person["attachments"][0]["content"]["body"][0]["items"][1]["columns"][1]["items"][1]["text"] = message
    card_to_person["attachments"][0]["content"]["msteams"]["entities"][0]["mentioned"]["id"] = email
    payload = json.dumps(card_to_person)
    
    return payload

def gen_card_no_person(title: str, message: str) -> str:
    """
    Generates a JSON payload for a message to send to a Microsoft Teams Channel without tagging a person.
    
    Args:
        title (str): The title of the message.
        message (str): The message to send.
    """
    card_no_person = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {

                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "",
                                    "wrap": "true",
                                    "size": "Large",
                                    "weight": "Bolder",
                                    "color": "Attention",
                                    "maxLines": 0,
                                    "horizontalAlignment": "Left",
                                    "id": "title"
                                },
                                {
                                    "type": "ColumnSet",
                                    "minHeight": "0px",
                                    "style": "emphasis",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Message: ",
                                                    "wrap": "true",
                                                    "size": "Medium",
                                                    "weight": "Bolder",
                                                    "color": "Accent",
                                                    "id": "lbl_msg"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "",
                                                    "wrap": "true",
                                                    "id": "txt_msg"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
    card_no_person["attachments"][0]["content"]["body"][0]["items"][0]["text"] = title
    card_no_person["attachments"][0]["content"]["body"][0]["items"][1]["columns"][1]["items"][0]["text"] = message
    payload = json.dumps(card_no_person)
    return payload

