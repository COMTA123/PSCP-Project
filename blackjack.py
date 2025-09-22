"""Project PSCP"""
import random
card_list =["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
"AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
"AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
"AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
player_list = [[10000]]
def user_input():
    """รับจำนวน Player และก็รับจำนวนเงินที่จะเล่น"""
    amount_player = int(input()) #รับค่าจำนวนคนเล่น
    while amount_player <= 0 or amount_player > 3: #เช็คให้ไม่เกิน 3 และมากกว่า 0
        print("กรอกจำนวนผู้เล่นผิด")
        amount_player = int(input("กรอกใหม่อีกครั้ง"))
    for _ in range(1,amount_player+1): #รับเงินที่คนจะเล่นโดย ตำแหน่งที่ 0 เป็นของบอท เราเลยเริ่มตำแหน่งที่ 1
        start_money = 1000 #กำหนดเงินในบัญชีเริ่มต้นของทุกคน
        player_list.append([start_money])
    return amount_player #ให้ส่งจำนวนผู้เล่นออกมานอก function
def insert_money(amount_player):
    """ฟังชันให้ผู้เล่นเลือกลงจำนวนเงิน"""
    for i in range(1,amount_player+1): #loop ให้ทุก player
        money = int(input(f"Player[{i}] : ใส่จำนวนเงินที่จะลงในตานี้"))
        while money > player_list[i][0] or money <= 0: #เช็คว่าใส่เงินมากกว่าที่มีรึป่าว หรือ ใส่เงินน้อยกว่า 0 รึป่าว
            money = int(input("กรอกจำนวนเงินผิด"))
        player_list[i].append(money)

def deal_cards():
    """randomCard 2 ใบ"""
    global card_list
    card_list =["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
"AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
"AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
"AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
    for i in range(1,amount_player+1):
        random_card1 = random.sample(card_list,1)[0]
        player_list[i].append(random_card1)
        card_list.remove(random_card1)
        random_card2 = random.sample(card_list,1)[0]
        player_list[i].append(random_card2)
        card_list.remove(random_card2)
    print("--------------------------------------")
    print(card_list)
    print("--------------------------------------")
    print(player_list)

def action():
    """Player Select Action"""
    print(card_list)
    for i in range(1,amount_player+1):
        player_action = str(input(f"เลือก Action player{i} : ")).lower()
        player_action = check_action(player_action)
        match player_action:
            case "hit":
                random_card_hit = random.sample(card_list,1)[0]
                player_list[i].append(random_card_hit)
                card_list.remove(random_card_hit)
                player_action = str(input(f"เลือก Action player{i} : ")).lower()
                player_action = check_action(player_action)
                while player_action == "hit":
                    random_card_hit = random.sample(card_list,1)[0]
                    player_list[i].append(random_card_hit)
                    card_list.remove(random_card_hit)
                    player_action = str(input(f"เลือก Action player{i} : ")).lower()
                    player_action = check_action(player_action)
            case "stand":
                pass
        print(f"player{i} : {player_list[i]}")
def check_action(act):
    while act != "hit" and act != "stand":
        act = str(input("เลือก Action ไม่ถูกต้อง เลือกใหม่ : ")).lower()
    return act
def check_score():
    for i in range(1,amount_player+1):
        for j in player_list[1][2:]:
            

amount_player = user_input()
insert_money(amount_player)
deal_cards()
action()
check_score()



