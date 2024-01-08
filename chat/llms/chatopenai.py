from langchain.chat_models import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler
from queue import Queue



class StreamingHandler(BaseCallbackHandler):

    def __init__(self, queue):
         self.queue = queue

    def on_llm_new_token(self, token, **kwargs):
        self.queue.put(token)
        # print(token)

        # pass
    
    def on_llm_end(self, response, **kwargs):
         self.queue.put(None)

    def on_llm_error(self, error, **kwargs):
        self.queue.put(None)


def build_llm():
    return ChatOpenAI(streaming=True)