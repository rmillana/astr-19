import sys

class Cat:
    def print(self):
        print("Animal: Cat")
        print(f"Arm length: {self.arm_length} inches")
        print(f"Leg length: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Furry: {'Yes' if self.is_furry else 'No'}")

        
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

def main():
    my_cat = Cat(arm_length=6.0, leg_length=8.5, num_eyes=2, has_tail=True, is_furry=True)
    my_cat.print()
    
if __name__ == "__main__":
    main()