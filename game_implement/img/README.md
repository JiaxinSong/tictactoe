This is the implement of tree_baesd AI in a tic-tac-toe game.  
  
Rules: 
==
This game requires two players who hold x and o pieces respectively. The player who successfully places a certain number of pieces on the horizontal, vertical or diagonal successively is the winner. Compared with traditional tic-tac-toe games, the newly added rule is that, at the end of each turn, there is a 25% chance that the other player's turn gets skipped and the current player gets to go again.  
  

  
How to run:  
==
  
play with AI or baseline AI(random)  
--
run run.py  
  
Game flow:  
Choose the size of chess board first.   
Then choose the win condition.   
Choose to play with random player or AI player, if you choose AI: choose the depth of the search tree and numbers of nodes in each layer of tree.  
Choose to go fisrt or go second. If you choose go first, you will use o and your opponent will use x, vice verse.  
Game begin. Put your pieces in available positives.  
Once any player meets the victory condition or the board is full, game's over.  
  
  
100 battle between tree-based AI and baseline AI(random)  
--  
open 100battle.py  
comment out the code before first print() in main function  
change parameter  
```python
b = chessboard(7)                         # 7 means size of chessboard
res,turns,nodes = game2(c, 5, 3, 10, 2)   # 5 means winning rule: 5 in a row , 3 means layers of search tree, 10 means number of nodes each layer, 2 means tree-based AI will be x(second to play)
```


  
  
  
100 battle between baseline AI(random) and baseline AI(random)
 -- 
open 100battle.py
comment out the code after first print() in main function 
change parameter  
```python
b = chessboard(7)   # 7 means size of chessboard
res=game1(b,5,1)    # 5 means winning rule: 5 in a row
```
run 100battle.py




Results:
==







Introduction of functions:  
==


Functions in tree_related_functions.py:  

exminimax 
--
Use special minimax tree to get the utility of put piece ona certain position of chessboard  

paremeters:  
board：3 dimensions matrix   
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win  
action: (x,y) the position you want to put piece   
depth: depth of the tree  
node: number of nodes searched each layer of the tree  
l: vector to count how many nodes searched   

return:  
score : if o has an edge, it will be positive. If it can win the game in less depth, it will get bigger score. If not it will use special method to count the score of the state in the final depth   


make_act, recover_act: make action and undo action  
--

AI_action  
--
Put all the valid actions into the tree and choose the one makes best score  
  
paremeters:  
board：3 dimensions matrix   
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win  
depth: depth of the tree  
node: number of nodes searched each layer of the tree  
  
return:   
(score,position),nodes  
  
    
  
Functions in score.py:  
--
score:  
--
compare the max numbers of the x and o in a row which has a potential to reach the goal ( if the goal is 3 pieces in a row, the max numbers of o in state "xoox" is 0, since oo has no chance to become ooo ) and get the score of a certain state  
  
paremeters:  
matrix: one dimension matrix generated by board[1]-board[2], so it will have 0, 1, -1  
rule: numbers of pieces in a row to win  
  
return:  
score:   
if max of o in a row >max of x in a row:  
    return 0.5  
elif max of o in a row<max of x in a row:  
    return  -0.5  
else :  
    return 0  
  
together_row:  
--
get max number of pieces that have potential to meet the goal in a certain row   
  
paremeters:  
vec: one dimension matrix generated by board[1]-board[2], so it will have 0, 1, -1  
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win   
  
return:  
max_ to: max number of pieces that have potential to meet the goal in a certain row   