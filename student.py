class Student:
    def __init__(self, name, section, roll, marks):
        self.name = name
        self.section = section
        self.roll = roll
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "roll": self.roll,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["section"],
            data["roll"],
            data["marks"]
        )

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def __str__(self):
        marks = ", ".join(
            f"{subject}: {mark}"
            for subject, mark in self.marks.items()
        )

        return (
            f"Roll No : {self.roll}\n"
            f"Name    : {self.name}\n"
            f"Section : {self.section}\n"
            f"Marks   : {marks}\n"
            f"Average : {self.average():.1f}\n"
            f"{'-' * 40}"
        )