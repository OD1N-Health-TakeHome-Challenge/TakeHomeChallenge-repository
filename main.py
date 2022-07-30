import os
os.environ['KIVY_IMAGE'] = 'pil'

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
import boto3

Window.size = (800,500)

table_name = 'TakeHomeChallenge'

dynamodb_client = boto3.client('dynamodb')

# item_scarface
item_scarface  = {
  "serialNumber": {
    "S": "123"
  },
  "timeStamp": {
    "S": "2022"
  }
}

item_get = {
  "serialNumber": {
    "S": "123"
  },
  "timeStamp": {
    "S": "2022"
  }
}

class MyApp(App):
    def build(self):
        root_widget = Label(
            text='Here is the take-home coding challenge!\n --Haoyang Hong',
            font_size=40,
            italic=True,
            markup=True)
        return root_widget

if __name__ == '__main__':
    # put item
    dynamodb_client.put_item(TableName = table_name, Item = item_scarface)

    # get item
    resp = dynamodb_client.get_item(TableName=table_name, Key=item_get)
    print(resp)
    print(resp['Item'])
    print(resp['Item']['serialNumber']['S'])

    MyApp().run()




