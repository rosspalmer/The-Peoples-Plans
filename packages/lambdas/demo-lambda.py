

def lambda_handler(event, context):

    print("HERE's the event! ->")
    print(event)

    print("WHERE is MISSING_PIG?!?!")
    pig = event.get("MISSING_PIG", "not found!")
    print(pig)

