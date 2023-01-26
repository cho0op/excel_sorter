class Range:
    start = None
    end = None

    def __init__(self, start, end):
        self.end = end
        self.start = start

    def __repr__(self):
        return f"start={self.start};end={self.end}"
