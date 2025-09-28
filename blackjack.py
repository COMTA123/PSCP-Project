"""Project PSCP"""
import random
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

def bot_check():
    total = 0
    for i in player_list[0][3:]:
        point = i.split("_")[0] #แยกระหว่างตัวเลขกับชนิดไพ่
        if point.isnumeric():
            total += int(point)
        elif point in "JKQ": #เช็คว่า point เป็นตัวอักษรรึป่าว
            total += 10
        elif point == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
    return int(total)

def bot_turn():
    """ถ้าแต้มน้อยกว่า 18 ก็ Bot จะสุ่มการ์ดเพิ่ม"""
    while bot_check() < 18:
        random_card_bot = random.sample(card_list,1)[0] #สุ่มการ์ดเพิ่ม
        card_list.remove(random_card_bot)
        player_list[0].append(random_card_bot)

def action():
    """Player Select Action"""
    for k in range(1,amount_player+1): #loop ตาม player
        print(f"your card : {player_list[k][3:]}")
        player_action = str(input(f"เลือก Action player{k} : ")).lower() #รับinput action
        player_action = check_action(player_action) #เข้าฟังชันเช็คว่า input ถูกไหม
        match player_action:
            case "hit": #ถ้าเลือก Hit
                random_card(k)
                if check_score(k) > 21:
                    print("Your are Busted")
                    player_action = "stand"
                    pass
                while player_action == "hit":
                    """ทำซ้ำไปเรื่อยๆหากจนกว่าจะไม่เลือก hit"""
                    player_action = str(input(f"เลือก Action player{k} : ")).lower() #รับinputอีกครั้ง
                    player_action = check_action(player_action) #เข้าฟังชันเช็ค
                    if player_action == "stand":
                        break
                    random_card(k)
                    if check_score(k) > 21:
                        print("Your are Busted")
                        player_action = "stand"
                        break
            case "stand":
                """ไม่ทำไรเลย"""
                pass

def random_card(i):
    """สุ่มการ์ดเพิ่ม"""
    card = random.sample(card_list,1)[0] 
    player_list[i].append(card)
    card_list.remove(card)
    print(f"Got! : {card}")


def check_action(act):
    """เช็คว่าinput action ถูกไหม"""
    while act != "hit" and act != "stand":
        act = str(input("เลือก Action ไม่ถูกต้อง เลือกใหม่ : ")).lower()
    return act

def check_score(i):
    """รับค่าตำแหน่ง player ที่ต้องการเช็คเข้ามา"""
    total = 0
    ace = 0
    for j in player_list[i][3:]: #ให้เริ่มจากช่องที่ 3 เพราะ 0 1 2 ไม่ใช่การ์ด
        point = j.split("_")[0] #แยกระหว่างตัวเลขกับชนิดไพ่
        if point.isnumeric():
            total += int(point)
        elif point in "JKQ":
            total += 10
        else:
            ace += 1
            total += 11
    while total > 21 and ace > 0:
        total -= 10
        ace -= 1
    return total
def summarize():
    """วัดผลแพ้ชนะ"""
    bot_point = bot_check()
    print(f"Bot Point : {bot_point}")
    for j in range(1,amount_player+1):
        print(f"player {j} card : {player_list[j][3:]}")
        player_point = check_score(j)
        if bot_point > 21:
            if player_point < 21:
                print(f"Player {j} : WINNN")
                player_list[j][0] += player_list[j][2]*2 
            if player_point > 21:
                print(f"Player {j} : Losttt")
                player_list[j][0] -= player_list[j][2]
        elif player_point > 21:
            print(f"Player {j} : Losttt")
            player_list[j][0] -= player_list[j][2]
        elif player_point > bot_point :
            print(f"Player {j} : WINNN")
            player_list[j][0] += player_list[j][2]*2
        elif player_point < bot_point:
            print(f"Player {j} : Losttt")
            player_list[j][0] -= player_list[j][2]


amount_player = user_input()
insert_money(amount_player)
deal_cards()
action()
bot_turn()
summarize()
