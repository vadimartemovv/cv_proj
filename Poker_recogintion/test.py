from deuces.Card import Card
from deuces.Evaluator import Evaluator

board = [Card.new('Ah'),Card.new('Kd'),Card.new('Jc')]
pl1_hand = [Card.new('7s'),Card.new('Th')]
pl2_hand = [Card.new('Ts'),Card.new('Qh')]
eval = Evaluator()
print(eval.evaluate(board, pl2_hand))