

class Stream:
    '''
    A single stream
    '''

    def __init__(self, username: str, title: str, description: str):
        self.username = username
        self.title = title
        self.description = description

    def start(self):
        '''
        To be called when a stream starts
        '''

    def stop(self):
        '''
        To be called when a stream stops
        '''
