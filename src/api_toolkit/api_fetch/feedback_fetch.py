from pydantic import BaseModel

class FeedBackdata(BaseModel):
    username: str
    message: str

def feedback(data: FeedBackdata):
    print("\n status: succes")
    print(f"\n Note: Thankyou for your Feedback {data.username}!")
    print(f"\n Feedback recieved: {data.message}")