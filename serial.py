"""Python serial number generator."""

class SerialGenerator:

    def __init__(self, start=0):
        """Make a new generator, starting at start"""

        self.start = self.next = start

    def __repr__(self):
        """Show representation"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next number"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the number"""

        self.next = self.start


