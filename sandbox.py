import argparse

parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument('user_prompt', type=str, help= "User prompt")
args = parser.parse_args()
