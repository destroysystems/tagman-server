#!/usr/bin/env python

import asyncio
import websockets

import game
import uuid

async def hello(websocket, path):
  print(f'Game id: {g.id}')
  while True:
    command = await websocket.recv()
    print(f'Received command: {command}')
    try:
      cmd, direction = command.split(',')
      if cmd == 'newSession':
        print(f'- Session request')
        p = game.Player()
        print(f'- Player created with id {p.id}')
        g.add_player(p)
        await websocket.send(f'{p.id},{p.x},{p.y}')
        continue

      playerId = uuid.UUID(cmd)
      player = g.get_player(playerId)
      if player:
        player = player
        print(f'- Found player with id {player.id} in position ({p.x},{p.y})')
      else:
        print(f'No players found with id {playerId}')
      player.move(direction)
      print(f'- Player {p.id} moved to position ({p.x},{p.y})')
      await websocket.send(f'{p.id},{p.x},{p.y}')

    except Exception as e:
      print(command)
      print(e)
      continue

g = game.Game()

start_server = websockets.serve(hello, port=8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
