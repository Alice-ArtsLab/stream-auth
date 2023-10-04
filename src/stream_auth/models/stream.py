

class Stream:
    '''
    A single stream
    '''

    def __init__(self, name: str, description: str, username: str):
        self.name = name
        self.description = description
        self.user = username

    def start(self):
        '''
        To be called when a stream starts
        '''

    def stop(self):
        '''
        To be called when a stream stops
        '''
