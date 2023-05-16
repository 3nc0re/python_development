# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
#
# Your task is to create the TVController class and methods described above.
#
# ```
#
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#
#  class TVController:
#
# pass
#
#  controller = TVController(CHANNELS)
#
# controller.first_channel() == "BBC"
#
# controller.last_channel() == "TV1000"
#
# controller.turn_channel(1) == "BBC"
#
# controller.next_channel() == "Discovery"
#
# controller.previous_channel() == "BBC"
#
# controller.current_channel() == "BBC"
#
# controller.is_exist(4) == "No"
#
# controller.is_exist("BBC") == "Yes"

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVcontroller:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, N):
        if N > len(self.channels):
            return "No such channel"
        else:
            self.current_channel_index = N - 1
            return self.channels[self.current_channel_index]

    def next_channel(self):
        if self.current_channel_index == len(self.channels) - 1:
            self.current_channel_index = 0
        else:
            self.current_channel_index += 1
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        if self.current_channel_index == 0:
            self.current_channel_index = len(self.channels) - 1
        else:
            self.current_channel_index -= 1
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, N):
        if isinstance(N, int):
            if N > len(self.channels):
                return "No"
            else:
                return "Yes"
        elif isinstance(N, str):
            if N in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            return "No such channel"

controller = TVcontroller(CHANNELS)
first_channel = controller.first_channel()
print(first_channel)