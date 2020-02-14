import uuid

class Player:

  def __init__(self):
    self._x = 0
    self._y = 0
    self._id = uuid.uuid4()

  def __repr__(self):
    return str(self.position)

  def __str__(self):
    return str(self.position)

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @property
  def position(self):
    return (self.x, self.y)

  @property
  def id(self):
    return self._id

  def move(self, direction):
    if direction == 0:
      self._y += 1
    if direction == 1:
      self._x += 1
    if direction == 2:
      self._y -= 1
    if direction == 3:
      self._x -= 1

class Game:

  def __init__(self):
    self._id = uuid.uuid4()
    self._players = []

  @property
  def id(self):
    return self._id

  def add_player(self, player):
    self._players.append(player)

  def get_player(self, player_id):
    return list(filter(lambda x: x.id == player_id, self._players))[0]
