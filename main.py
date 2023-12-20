from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def main1():
    # 바닥 | x, y, z 축
    main_floor = Entity(model='cube', position=(0, 0, 0), 
                        scale=(10, 1, 100), color=color.gray, collider='box')

    # 천장
    main_ceiling = Entity(model='cube', position=(0, 10, 0), 
                        scale=(10, 1, 100), color=color.gray, collider='box')

    # 왼쪽 벽
    main_left_wall = Entity(model='cube', position=(-5, 5, -5), 
                        scale=(1, 11, 110), color=color.white, collider='box',
                        texture='./assets/wall.jpg', texture_scale=(16, 10))

    # 오른쪽 벽
    main_left_wall = Entity(model='cube', position=(5, 5, 5), 
                        scale=(1, 11, 110), color=color.white, collider='box',
                        texture='./assets/wall.jpg', texture_scale=(16, 10))

# 앞쪽
def front():
    front_floor = Entity(model='cube', position=(-25, 0, 55), scale=(60, 1, 10), color=color.gray, collider='box')
    front_ceiling = Entity(model='cube', position=(-25, 10, 55), scale=(60, 1, 10), color=color.gray, collider='box')
    front_left_wall = Entity(model='cube', position=(-30, 5, 50), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
    front_right_wall = Entity(model='cube', position=(-20, 5, 60), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

    front_floor_2 = Entity(model='cube', position=(-50, 0, 80), scale=(10, 1, 60), color=color.gray, collider='box')
    front_ceiling_2 = Entity(model='cube', position=(-50, 10, 80), scale=(10, 1, 60), color=color.gray, collider='box')
    front_left_wall_2 = Entity(model='cube', position=(-55, 5, 75), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
    front_right_wall_2 = Entity(model='cube', position=(-45, 5, 85), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

# 뒷쪽
def back():
    back_floor = Entity(model='cube', position=(25, 0, -55), scale=(60, 1, 10), color=color.gray, collider='box')
    back_ceiling = Entity(model='cube', position=(25, 10, -55), scale=(60, 1, 10), color=color.gray, collider='box')
    back_left_wall = Entity(model='cube', position=(30, 5, -50), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
    back_right_wall = Entity(model='cube', position=(20, 5, -60), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

    back_floor_2 = Entity(model='cube', position=(50, 0, -80), scale=(10, 1, 60), color=color.gray, collider='box')
    back_ceiling_2 = Entity(model='cube', position=(50, 10, -80), scale=(10, 1, 60), color=color.gray, collider='box')
    back_left_wall_2 = Entity(model='cube', position=(55, 5, -75), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
    back_right_wall_2 = Entity(model='cube', position=(45, 5, -85), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

# 텔레포드, 위치 이동
def update():
    # 앞쪽으로 넘어갔을 때 뒤로 텔레포트
    if(player.position.x <-25 and player.position.z > 50):
        player.set_position(
            (50 + player.position.x,
            player.position.y,
            -110 + player.position.z))
    # 뒤쪽으로 넘어갔을 때 앞으로 텔레포트
    elif(player.position.x > 25 and player.position.z < -50):
        player.set_position(
            (-50 + player.position.x,
            player.position.y,
            110 + player.position.z)
        )

def tile():
    for i in range(-90, 91):
        tile = Entity(model='cube', position=(0, 0.5, 0.5*i), scale=(0.5, 0, 0.5),
                    texture='./assets/yellow_tile.jpg')

app = Ursina()
mouse.visible = False # 커서 제거

main1()
front()
back()
tile()

# EditorCamera() # 에디터 카메라로 보기
player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.5
player.speed = 15

app.run()