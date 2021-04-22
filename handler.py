import json


def calculatebmi(height,weight):
    i = weight / (height * height)
    index = round(i, 2)
    print("height: ", height, "KG, weight: ", weight, "M")

    if index < 19:
        result = "under weight"
    elif 25 > index > 20:
        result = "normal weight"
    elif 30 > index > 25:
        result = "over weight"
    else:
        result = "obesity"

    return {
        'bmi': index,
        'result': result
    }


def lambda_handler(event, context):
    #height = event['height']
    #weight = event['weight']
    #res = calculatebmi(event['weight'], event['height'])
    data = json.loads(event['body'])
    height=data['height']
    weight=data['weight']
    res = calculatebmi(height,weight)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'},
        'body': json.dumps(res)
    }
