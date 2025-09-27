"""Project PSCP"""
import random
card_list =["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
"AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
"AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
"AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
player_list = [[10000,0,0]]

def user_input():
    """รับจำนวน Player และก็รับจำนวนเงินที่จะเล่น"""
    amount_player = int(input()) #รับค่าจำนวนคนเล่น
    while amount_player <= 0 or amount_player > 3: #เช็คให้ไม่เกิน 3 และมากกว่า 0
        print("กรอกจำนวนผู้เล่นผิด")
        amount_player = int(input("กรอกใหม่อีกครั้ง"))
    for i in range(1,amount_player+1): #loop ตามจำนวน Player
        """รับเงินที่คนจะเล่นโดย ตำแหน่งที่ 0 เป็นของบอท เราเลยเริ่มตำแหน่งที่ 1"""
        start_money = 1000 #กำหนดเงินในบัญชีเริ่มต้นของทุกคน
        player_list.append([start_money])
        player_list[i].append(0)
    return amount_player #ให้ส่งจำนวนผู้เล่นออกมานอก function

def insert_money(amount_player):
    """ฟังชันให้ผู้เล่นเลือกลงจำนวนเงิน"""
    for i in range(1,amount_player+1): #loop ตามจำนวน Player
        money = int(input(f"Player[{i}] : ใส่จำนวนเงินที่จะลงในตานี้"))
        while money > player_list[i][0] or money <= 0: #เช็คว่าใส่เงินมากกว่าที่มีรึป่าว หรือ ใส่เงินน้อยกว่า 0 รึป่าว
            money = int(input("กรอกจำนวนเงินผิด"))
        player_list[i].append(money) #เพิ่ม money เข้าไปใน playerlist ในช่องplayer i
        print(player_list)

def deal_cards():
    """randomCard 2 ใบ"""
    global card_list
    card_list = [
    "A_S", "2_S", "3_S", "4_S", "5_S", "6_S", "7_S", "8_S", "9_S", "10_S", "J_S", "Q_S", "K_S",
    "A_H", "2_H", "3_H", "4_H", "5_H", "6_H", "7_H", "8_H", "9_H", "10_H", "J_H", "Q_H", "K_H",
    "A_D", "2_D", "3_D", "4_D", "5_D", "6_D", "7_D", "8_D", "9_D", "10_D", "J_D", "Q_D", "K_D",
    "A_C", "2_C", "3_C", "4_C", "5_C", "6_C", "7_C", "8_C", "9_C", "10_C", "J_C", "Q_C", "K_C"
]
    for i in range(0,amount_player+1): #loop ตามจำนวน Player และบอทตำแหน่งที่ 0 ด้วย
        random_card1 = random.sample(card_list,1)[0] #สุ่มการ์ดใบแรก
        player_list[i].append(random_card1) #เพิ่มการ์ดเข้า playerlist
        card_list.remove(random_card1)#ลบออกจากcardlist
        random_card2 = random.sample(card_list,1)[0]#สุ่มใบสอง
        player_list[i].append(random_card2)#เพิ่มการ์ด
        card_list.remove(random_card2)#ลบออก
def action():
    """Player Select Action"""
    for k in range(1,amount_player+1): #loop ตาม player
        print(f"your card : {player_list[k][3:]}")
        player_action = str(input(f"เลือก Action player{k} : ")).lower() #รับinput action
        player_action = check_action(player_action) #เข้าฟังชันเช็คว่า input ถูกไหม
        match player_action:
            case "hit": #ถ้าเลือก Hit
                random_card_hit = random.sample(card_list,1)[0] #สุ่มการ์ดเพิ่ม
                player_list[k].append(random_card_hit) #เพิ่มการ์ดเข้าplayerlist
                card_list.remove(random_card_hit) #ลบการออก card list
                if check_score(k) > 21:
                    print("แตกกกก")
                    player_action = "stand"
                while player_action == "hit":
                    """ทำซ้ำไปเรื่อยๆหากจนกว่าจะไม่เลือก hit"""
                    player_action = str(input(f"เลือก Action player{k} : ")).lower() #รับinputอีกครั้ง
                    player_action = check_action(player_action) #เข้าฟังชันเช็ค
                    random_card_hit = random.sample(card_list,1)[0]
                    player_list[k].append(random_card_hit)
                    card_list.remove(random_card_hit)
                    if check_score(k) > 21:
                        print("แตกกกก")
                        player_action = "stand"
            case "stand":
                """ไม่ทำไรเลย"""
                pass

def check_action(act):
    """เช็คว่าinput action ถูกไหม"""
    while act != "hit" and act != "stand":
        act = str(input("เลือก Action ไม่ถูกต้อง เลือกใหม่ : ")).lower()
    return act

def check_score(i):
    """รับค่าตำแหน่ง player ที่ต้องการเช็คเข้ามา"""
    for j in player_list[i][3:]: #ให้เริ่มจากช่องที่ 3 เพราะ 0 1 2 ไม่ใช่การ์ด
        print(f"Your card : {j}")
        point = j.split("_")[0] #แยกระหว่างตัวเลขกับชนิดไพ่
        if point in "JKQ": #เช็คว่า point เป็นตัวอักษรรึป่าว
            point = 10
        elif point == "A": 
            a_select = int(input("11 or 1 : ")) #ให้เลือกว่า A จะกี่แต้ม
            while a_select != 11 and a_select != 1:
                a_select = int(input("กรอกผิด กรุณากรอกใหม่"))
            if a_select == 11:
                point = 11
            elif a_select == 1:
                point = 1
        player_list[i][1] += int(point) #บวกแต้มเข้าใน playerlist
    return player_list[i][1]

amount_player = user_input()
insert_money(amount_player)
deal_cards()
action()
