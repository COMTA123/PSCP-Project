"""Project PSCP"""
player_list = [[10000]]
def user_input():
    """รับจำนวน Player และก็รับจำนวนเงินที่จะเล่น"""
    amount_player = int(input()) #รับค่าจำนวนคนเล่น
    while amount_player <= 0 or amount_player > 3:
        print("กรอกจำนวนผู้เล่นผิด")
        amount_player = int(input("กรอกใหม่อีกครั้ง"))
    for _ in range(1,amount_player+1): #รับเงินที่คนจะเล่นโดย ตำแหน่งที่ 0 เป็นของบอท
        start_money = 500            #เราเลยเริ่มตำแหน่งที่ 1
        player_list.append([start_money])
    print(player_list)
    return amount_player
def insert_money(amount_player):
    """ใส่จำนวนเงินที่จะลงในตานี้"""
    print(amount_player)
    for i in range(1,amount_player+1):
        money = int(input(f"Player[{i}] : ใส่จำนวนเงินที่จะลงในตานี้"))
        while money > player_list[i][0]:
            money = int(input("กรอกจำนวนเงินผิด"))
        player_list[i].append(money)
amount_player = user_input()
insert_money(amount_player)

def random_card():
    