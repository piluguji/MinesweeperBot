from minesweeper import *
m = Minesweeper()

#print(m.board)

m.print()


"""print(m.nearby_mines((0,0)))


print(m.is_mine((0,0)))


s = Sentence(((0,0),(0
,1),(0,2)), 2)
print(s.__str__())



print(s.__str__())
print(s.known_safes())"""

ai = MinesweeperAI()


"""
for i in mineGame.knowledge:
    print(i.__str__())
print("Start")
mineGame.add_knowledge((0,0), 1)
for i in mineGame.knowledge:
    print(i.__str__())
print("--------------")
mineGame.add_knowledge((0,1), 1)
for j in mineGame.knowledge:
    print(j.__str__())
print("--------------")
mineGame.add_knowledge((0,2), 1)
for k in mineGame.knowledge:
    print(k.__str__())
print("--------------")
mineGame.add_knowledge((2,2), 1)
for k in mineGame.knowledge:
    print(k.__str__())
print("--------------")

mineGame.add_knowledge((2,1), 2)
for k in mineGame.knowledge:
    print(k.__str__())
print("-----yo67oo------")

print(mineGame.safes, mineGame.mines)"""

move = ai.make_safe_move()
if move is None:
    move = ai.make_random_move()

print(move)


