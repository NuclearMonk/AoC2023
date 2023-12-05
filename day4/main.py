print(sum(filter(lambda x: x>= 1, map(lambda x:pow(2,len(set(map(int, x[0].split())).intersection(set(map(int, x[1].split())))) -1),(line.split(":")[1].split("|") for line in open("input.txt").read().splitlines())))))
wins = list(map(lambda x:len(set(map(int, x[0].split())).intersection(set(map(int, x[1].split())))),(line.split(":")[1].split("|") for line in open("input.txt").read().splitlines())))
cards = [1 for _ in wins]
for i, matches  in enumerate(wins):
    for j in filter(lambda x: x < len(wins),range(i+1,i+matches+1)):
        cards[j] += cards[i]
print(sum(cards))
stack = [i for i in range(len(wins))]
print(len([stack.extend(filter(lambda x: x < len(wins), range(i+1, i+1+wins[i]))) for i in stack]))