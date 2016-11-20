class Agent(object):
    def __init__(self, agent_host):
        self.agent_host = agent_host
    
    def move(speed):
        self.agent_host.sendCommand("move {}".format(speed))

    def turn(speed):
        self.agent_host.sendCommand("turn {}".format(speed))

    