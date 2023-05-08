push = require 'push'         --import class
Class = require 'class'
require 'Ball'
require 'Paddle'

--physical window
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
--virtual window size:  Your coordinates will be based on this system
VIRTUAL_WIDTH = 243
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200

--Runs when the game first starts up, only once... only once
function love.load()
     love.graphics.setDefaultFilter('nearest','nearest')

     love.window.setTitle('Pong')
     --set the seed or the "randomness" of the serve
     --if we set the "randomness" based on time, in theory it is the most random
     math.randomseed(os.time())

     --more retro looking font we need to load it in   newFont('file',size)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)
     largeFont = love.graphics.newFont('font.ttf',16)
     --set the font to the retro look
     love.graphics.setFont(smallFont)

     sounds = {
          ['paddle_hit'] = love.audio.newSource('Sounds/paddle_hit.wav', 'static'),
          ['score'] = love.audio.newSource('Sounds/score.wav', 'static'),
          ['wall_hit'] = love.audio.newSource('Sounds/wall_hit.wav', 'static')

     }
     --initialize our virtual res screen inside of the original window size
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=false,
          vsync=true
     })

     --set up the score
     player1Score = 7
     player2Score = 7
     player3Score = 7
     player4Score = 7
     
     --create a Paddle
     player1 = Paddle(10,30,5,20)
     player2 = Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)
     player3 = Paddle(30,10,20,5)
     player4 = Paddle(30,230,20,5)

     --create a Ball
     --     Constructor(x,y,w,h)
     ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

     servingPlayer = 1
     gameState = 'start'
end

--update runs every time the screen refreshes
function love.update(dt)
     -- player 1 movement
     if love.keyboard.isDown('w') then
          player1.dy=-PADDLE_SPEED
     elseif love.keyboard.isDown('s') then
          player1.dy=PADDLE_SPEED
     else
          player1.dy=0
     end
     -- player 2 movement
     if love.keyboard.isDown('p') then
          player2.dy=-PADDLE_SPEED
     elseif love.keyboard.isDown(';') then
          player2.dy=PADDLE_SPEED
     else
          player2.dy=0
     end
     if love.keyboard.isDown('t') then
          player3.dx=-PADDLE_SPEED
     elseif love.keyboard.isDown('g') then
          player3.dx=PADDLE_SPEED
     else
          player3.dx=0
     end
     if love.keyboard.isDown('o') then
          player4.dx=-PADDLE_SPEED
     elseif love.keyboard.isDown('l') then
          player4.dx=PADDLE_SPEED
     else
          player4.dx=0
     end


     if gameState=='serve' then
          --before switching to play, set the ball's velocity
          if servingPlayer == 1 then
               ball.dy = math.random(-50,50)
               ball.dx = math.random(140,200)
          elseif servingPlayer == 2 then
               ball.dy = math.random(-50,50)
               ball.dx = -math.random(140,200)
          elseif servingPlayer == 3 then
               ball.dy = math.random(140,200)
               ball.dx = math.random(-50,50)
          elseif servingPlayer == 4 then
               ball.dy = -math.random(140,200)
               ball.dx = math.random(-50,50)
          end
          









     elseif gameState == 'play' then
          -- paddle collision
          if ball:collides(player1) then
               ball.dx = -ball.dx * 1.03     --1.03 to speed up
               ball.x = player1.x+5            --to move the ball off of the paddle 

               --reset the y velocity
               if ball.dy<0 then
                    ball.dy = -math.random(10,150)
               else
                    ball.dy = math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          if ball:collides(player2) then
               ball.dx = -ball.dx * 1.03     --1.03 to speed up
               ball.x = player2.x-5            --to move the ball off of the paddle 

               --reset the y velocity
               if ball.dy<0 then
                    ball.dy = -math.random(10,150)
               else
                    ball.dy = math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end

          if ball:collides(player3) then
               ball.dy = -ball.dy * 1.03     --1.03 to speed up
               ball.y = player3.y+5            --to move the ball off of the paddle 

               --reset the y velocity
               if ball.dx<0 then
                    ball.dx = -math.random(10,150)
               else
                    ball.dx = math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end
          -- wall collision
          if ball:collides(player4) then
               ball.dy = -ball.dy * 1.03     --1.03 to speed up
               ball.y = player4.y-5            --to move the ball off of the paddle 

               --reset the y velocity
               if ball.dx<0 then
                    ball.dx = -math.random(10,150)
               else
                    ball.dx = math.random(10,150)
               end
               sounds['paddle_hit']:play()
          end

          ball:update(dt)
     end

     --scoring
     if ball.x < 0 then
          player1Score = player1Score - 1
          servingPlayer = 2
          if player2Score ==0 then
              ball:update(dt)
          else
          gameState='serve'
          end
          ball:reset()
          sounds['score']:play()
     end
     if ball.x > VIRTUAL_WIDTH then
          player2Score = player2Score - 1
          servingPlayer = 1
          if player1Score == 0 then
               ball:update(dt)
          else
          gameState='serve'
          end
          ball:reset()
          sounds['score']:play()
     end



     if ball.y < 0 then
          servingPlayer = 4
          player3Score = player3Score - 1

          if player3Score == 0 then
               ball:update(dt)
          else
          gameState='serve'
          end
          
          ball:reset()
          sounds['score']:play()
     end




     if ball.y > VIRTUAL_HEIGHT then
          servingPlayer = 3
          player4Score = player4Score - 1
          if player4Score ==0 then
               ball:update(dt)
               gameState='done'
          else
          gameState='serve'
          end
          
          ball:reset()
          sounds['score']:play()
     end

     player1:update(dt)
     player2:update(dt)
     player3:update(dt)
     player4:update(dt)
end

function love.keypressed(key)
     --keys can be accessed by string name
     if key =='escape' then
          love.event.quit()
     elseif key=='enter' or key=='return' then
          if gameState == 'start' then
               gameState = 'serve'
          elseif gameState == 'serve' then
               gameState = 'play'
          elseif gameState == 'done' then
               gameState='serve'
               player1Score = 7
               player2Score = 7
               player3Score = 7
               player4Score = 7
               ball:reset()
               if winningPlayer == 1 then
                    servingPlayer = 2
               else
                    servingPlayer = 1
               end
          end
     end
end

--Called after update function by Love2D, this draws what is on your screen
function love.draw()
     --begin redering a virtual res
     push:apply('start')

     -- clear the screen AND set the background color(R,G,B,A)
     love.graphics.clear(40,45,52,255)

     love.graphics.setFont(smallFont)
     if gameState == 'start' then
          love.graphics.setFont(smallFont)
          love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
          love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
     elseif gameState == 'serve' then
          love.graphics.setFont(smallFont)
          love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
               0, 10, VIRTUAL_WIDTH, 'center')
          love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
     elseif gameState == 'play' then
          -- no UI messages to display in play
     elseif gameState == 'done' then
        love.graphics.setFont(largeFont)
        love.graphics.printf('Player ' .. tostring(winningPlayer) .. ' wins!',
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.setFont(smallFont)
        love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')
     end
     love.graphics.setFont(scoreFont)
     love.graphics.setColor(255,0,0)
     if player1Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 2.5)
     love.graphics.setColor(32, 50, 255)
     if player2Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 2.5)
     love.graphics.setColor(28, 185, 87)
     if player3Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     love.graphics.print(tostring(player3Score), VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 4)
     love.graphics.setColor(224, 233, 29)
     if player4Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     love.graphics.print(tostring(player4Score), VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 2 + 20)


     
     love.graphics.setColor(255,0,0)
     if player1Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     player1:render()


     love.graphics.setColor(32, 50, 255)
     if player2Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     player2:render()


     love.graphics.setColor(28, 185, 87)
     if player3Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     player3:render()

     love.graphics.setColor(224, 233, 29)
     if player4Score <= 0 then
          love.graphics.setColor(17, 17, 17)
     end
     player4:render()


     love.graphics.setColor(236, 237, 228)
     --ball
     ball:render()

     displayFPS()

     --end rendering of virtual res
     push:apply('end')
end

function displayFPS()
     -- simple FPS display across all states
     love.graphics.setFont(smallFont)
     love.graphics.setColor(0, 255, 0, 255)
     love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
 end
