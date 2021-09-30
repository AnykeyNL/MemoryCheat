import PlaySingleRound
import time
import RobotSequences


RobotSequences.startgame()
time.sleep(3)

PlaySingleRound.playround(0)
time.sleep(3)
PlaySingleRound.playround(1)
time.sleep(3)
PlaySingleRound.playround(2)
time.sleep(3)
PlaySingleRound.playround(3)
time.sleep(3)
PlaySingleRound.playround(4)
time.sleep(3)
PlaySingleRound.playround(5)
time.sleep(5)

RobotSequences.pickprize()
time.sleep(2)
PlaySingleRound.SaveScreenshot("Prize")
time.sleep(2)
RobotSequences.finishgame()





