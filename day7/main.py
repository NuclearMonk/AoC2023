from collections import Counter, OrderedDict


class Hand:
    card_order = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    def __init__(self, hand: str, bid: str) -> None:
        self.string = hand
        
        card_counts = list(Counter(self.string).most_common()) 
        if len(card_counts) != 1:
            self.hand_type = 10* card_counts[0][1] +card_counts[1][1]
        else:
            self.hand_type = 51
        self.bid = int(bid)

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        for x,y in zip(self.string, other.string):
            if self.card_order.index(x)< self.card_order.index(y):
                return True
            elif self.card_order.index(x)> self.card_order.index(y):
                return False

    def __str__(self) -> str:
         return f"{self.string} {self.bid} {self.hand_type}"

class JokerHand:
    card_order = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
    def __init__(self, hand: str, bid: str) -> None:
        self.string = hand
        card_counts = Counter(self.string).most_common()
        if len(card_counts) != 1:
            x = self.string.replace("J",  card_counts[0][0] if card_counts[0][0] != "J" else card_counts[1][0] )
            print()
            card_counts = Counter(x).most_common()
            self.hand_type = 10* card_counts[0][1] +card_counts[1][1]
        else:
            self.hand_type = 51
        self.bid = int(bid)

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        for x,y in zip(self.string, other.string):
            if self.card_order.index(x)< self.card_order.index(y):
                return True
            elif self.card_order.index(x)> self.card_order.index(y):
                return False

    def __str__(self) -> str:
         return f"{self.string} {self.bid} {self.hand_type}"

input_file = "input.txt"
lines = open(input_file).readlines()

# hands = sorted([Hand(*line.split()) for line in lines])
# print(*( (rank,str(hand)) for rank, hand  in enumerate(hands, start=1) ), sep="\n")
# print(sum (rank*hand.bid for rank, hand  in enumerate(hands, start=1) ))

hands = sorted([JokerHand(*line.split()) for line in lines])
print(*( (rank,str(hand)) for rank, hand  in enumerate(hands, start=1) ), sep="\n")
print(sum (rank*hand.bid for rank, hand  in enumerate(hands, start=1) ))

print(JokerHand("J2AQK", "0"))