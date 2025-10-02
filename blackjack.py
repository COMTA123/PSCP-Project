"""Project PSCP"""
import random
players = [[10000,0,0]]

def get_num_players():
    """รับจำนวน Player และก็รับจำนวนเงินที่จะเล่น"""
    num = True
    while num:
        try:
            num_players = int(input("Enter number of players: ")) #รับค่าจำนวนคนเล่น
            while num_players <= 0 or num_players > 3: #เช็คให้ไม่เกิน 3 และมากกว่า 0
                print("Invalid number of players.")
                num_players = int(input("Enter again: "))
            num = False
        except:
            print("Invalid number of players.")

    for i in range(1,num_players+1): #loop ตามจำนวน Player ช่องที่ 0
        """รับเงินที่คนจะเล่นโดย ตำแหน่งที่ 0 เป็นของบอท เราเลยเริ่มตำแหน่งที่ 1"""
        start_money = 1000 #กำหนดเงินในบัญชีเริ่มต้นของทุกคน
        players.append([start_money])
        players[i].append(0)

    return num_players #ให้ส่งจำนวนผู้เล่นออกมานอก function

def place_bets(num_players):
    """ฟังชันให้ผู้เล่นเลือกลงจำนวนเงิน"""
    for pid in range(1,num_players+1): #loop ตามจำนวน Player
        if players[pid][0] <= 0:
            print(f"Player {pid} has run out of money. Game over!")
            continue

        bet = True
        while bet:
            try:
                bet_amount = int(input(f"Player {pid}, enter your bet: "))
                while bet_amount > players[pid][0] or bet_amount <= 0: #เช็คว่าใส่เงินมากกว่าที่มีรึป่าว หรือ ใส่เงินน้อยกว่า 0 รึป่าว
                    print("Invalid bet.")
                    bet_amount = int(input("Enter again: "))
                bet = False
            except:
                print("Invalid number of players.")

        if not index:
            players[pid].append(bet_amount) #เพิ่ม bet_amount เข้าไปใน playerlist ในช่องplayer pid
        else:
            players[pid][2] = bet_amount

def deal_starting_cards():
    """randomCard 2 ใบ"""
    global deck
    deck = [
    "A_♠", "2_♠", "3_♠", "4_♠", "5_♠", "6_♠", "7_♠", "8_♠", "9_♠", "10_♠", "J_♠", "Q_♠", "K_♠",
    "A_♥", "2_♥", "3_♥", "4_♥", "5_♥", "6_♥", "7_♥", "8_♥", "9_♥", "10_♥", "J_♥", "Q_♥", "K_♥",
    "A_♦", "2_♦", "3_♦", "4_♦", "5_♦", "6_♦", "7_♦", "8_♦", "9_♦", "10_♦", "J_♦", "Q_♦", "K_♦",
    "A_♣", "2_♣", "3_♣", "4_♣", "5_♣", "6_♣", "7_♣", "8_♣", "9_♣", "10_♣", "J_♣", "Q_♣", "K_♣"
] #สร้าง list deck

    for i in range(0,num_players+1): #loop ตามจำนวน Player และบอทตำแหน่งที่ 0 ด้วย

        card1 = random.sample(deck,1)[0] #สุ่มการ์ดใบแรก
        players[i].append(card1) #เพิ่มการ์ดเข้า playerlist
        deck.remove(card1)#ลบออกจากcardlist

        card2 = random.sample(deck,1)[0]#สุ่มใบสอง
        players[i].append(card2)#เพิ่มการ์ด
        deck.remove(card2)#ลบออก

def calculate_bot_score():
    """คิดคะแนนให้บอท"""
    score_total = 0
    ace_count = 0

    for i in players[0][3:]:
        point = i.split("_")[0] #แยกระหว่างตัวเลขกับชนิดไพ่

        if point.isnumeric():
            score_total += int(point)

        elif point in "JKQ": #เช็คว่า point เป็นตัวอักษรรึป่าว
            score_total += 10

        else: #ถ้าได้ Ace
            ace_count += 1
            score_total += 11

    while score_total > 21 and ace_count > 0: #ถ้าเคยได้ ace แล้ว แต้มมากกว่า 21 จะเปลี่ยน ace 1
        score_total -= 10
        ace_count -= 1

    return int(score_total)

def bot_draw_until_safe():
    """ถ้าแต้มน้อยกว่า 18 ก็ Bot จะสุ่มการ์ดเพิ่ม"""
    while calculate_bot_score() < 18:
        bot_new_card = random.sample(deck,1)[0] #สุ่มการ์ดเพิ่ม
        deck.remove(bot_new_card) #ลบออกจากdeck เพื่อไม่ให้ซ้ำ
        players[0].append(bot_new_card) #เพิ่มเข้า list players

def player_turns():
    """Player Select Action"""
    for pid in range(1,num_players+1): #loop ตาม player pid = player id
        if players[pid][0] <= 0:
            continue
        print(f"\n{'Player ' + str(pid) + '\'s Turn':-^40}")
        print(f"Bot cards: {players[0][3]} XX")
        show_hand(pid)
        player_action = str(input(f"\nChoose action for Player {pid} (hit/stand): ")).lower() #รับinput action
        player_action = validate_action(player_action) #เข้าฟังชันเช็คว่า input ถูกไหม

        match player_action:
            case "hit": #ถ้าเลือก Hit
                draw_card(pid) #จั่วการ์ด

                if calculate_score(pid) > 21: #เช็คว่า bust ไหม
                    print("You are Busted!")
                    player_action = "stand"
                    pass

                while player_action == "hit": #เช็คว่าเลือก hit ต่อไหม
                    """ทำซ้ำไปเรื่อยๆหากจนกว่าจะไม่เลือก hit"""
                    player_action = str(input(f"\nChoose action for Player {pid} (hit/stand): ")).lower() #รับinputอีกครั้ง
                    player_action = validate_action(player_action) #เข้าฟังชันเช็ค

                    if player_action == "stand": #ถ้า hit แล้ว stand ก็จบเลย
                        break

                    draw_card(pid)#ถ้าไม่ stand ก็ให้จั่ว
                    if calculate_score(pid) > 21:#เช็คว่า bust ไหม
                        print("You are Busted!")
                        player_action = "stand"
                        break
            case "stand": #ถ้า stand ก็ข้ามเลย
                """ไม่ทำไรเลย"""
                continue

def show_hand(i):
    """เปิดการ์ดบนมือและก็คะแนนตอนนั้น"""
    print(f"Your cards: {players[i][3:]}")
    print(f"Your total points: {calculate_score(i)}")

def draw_card(i):
    """สุ่มการ์ดเพิ่ม และโชว์การ์ดที่ได้"""
    card = random.sample(deck,1)[0] #สุ่ม
    players[i].append(card) #เพิ่ม
    deck.remove(card) #ลบ
    show_hand(i) #โชว์
    print(f"New card: {card}") #โชว์


def validate_action(act):
    """เช็คว่าinput action ถูกไหม"""

    while act != "hit" and act != "stand":
        act = str(input("Invalid action. Enter again (hit/stand): ")).lower() 

    return act

def calculate_score(i):
    """รับค่าตำแหน่ง player ที่ต้องการเช็คเข้ามา"""
    score_total = 0
    ace_count = 0

    for j in players[i][3:]: #ให้เริ่มจากช่องที่ 3 เพราะ 0 1 2 ไม่ใช่การ์ด
        point = j.split("_")[0] #แยกระหว่างตัวเลขกับชนิดไพ่

        if point.isnumeric(): #ถ้าตัวเลขก็บวกตรงๆเลย
            score_total += int(point)

        elif point in "JKQ": #JKQ ก็ให้บวก 10
            score_total += 10

        else: #A ให้บวก 11 ไว้ก่อน
            ace_count += 1
            score_total += 11

    while score_total > 21 and ace_count > 0: #ถ้าแต้มเกิน 21 แล้วเคยได้ A จะปรับ 1 ให้
        score_total -= 10
        ace_count -= 1

    return score_total

def summarize_results():
    """วัดผลแพ้ชนะ"""
    lost_count = 0
    bot_point = calculate_bot_score() #เก็บค่าแต้มบอท
    for pid in range(1,num_players+1): #loopตาม จำนวนplayer
        if players[pid][0] <= 0:
            lost_count += 1
            continue
        print(f"\n{f'Player {pid}':-^40}") 
        print(f"{f"Bot Points: {bot_point}":^40}")
        show_hand(pid) #เปิดการ์ดให้ดู
        player_point = calculate_score(pid) #เก็บค่าคะแนน

        if player_point > 21:  # Player bust
            print(f"Player {pid} : Lost")
            players[pid][0] -= players[pid][2]

        elif bot_point > 21:  # Bot bust -> player auto win
            print(f"Player {pid} : Win")
            players[pid][0] -= players[pid][2]
            players[pid][0] += players[pid][2]* 2

        elif player_point > bot_point:  # Player closer to 21
            print(f"Player {pid} : Win")
            players[pid][0] -= players[pid][2]
            players[pid][0] += players[pid][2]* 2

        elif player_point < bot_point:  # Bot closer
            print(f"Player {pid} : Lost")
            players[pid][0] -= players[pid][2]

        else: # player_point == bot_point
            print(f"Player {pid} : Draw")
    if lost_count == num_players:
        print("All players are out of money. Game over!")
        return True
    return False
"""รันเกม"""
index = 0
num_players = get_num_players() 
place_bets(num_players)
deal_starting_cards()
player_turns()
bot_draw_until_safe()
all_lost = summarize_results()

"""ถ้ายังไม่แพ้ ก็จะถามว่าเล่นต่อไหม"""
if not all_lost:
    play_again = input("Play again? yes/no: ").lower()

"""เช็คว่าinputถูกไหม"""
while play_again != "yes" and play_again != "no":
    print("Invalid input. Enter yes/no.")
    play_again = input("Play again? yes/no : ").lower()

"""ถ้าเล่นต่อก็ Loop"""
while play_again == "yes":
    index += 1

    for idx in range(0,num_players+1): # idx = index
        del players[idx][3:]
        if idx: #ถ้าผ่านไปแล้วรอบนึง
            print(f"Player {idx}'s Balance: {players[idx][0]}")

    """รันเกม"""
    all_lost = False
    place_bets(num_players)
    deal_starting_cards()
    player_turns()
    bot_draw_until_safe()
    all_lost = summarize_results()
    if all_lost:
        break
    play_again = input("Play again? yes/no : ").lower()

    """รับค่าว่าเล่นต่อไหมเช็คว่าผิดไหม"""
    while play_again != "yes" and play_again != "no":
        print("Invalid input. Enter yes/no.")
        play_again = input("Play again? yes/no : ").lower()

for idx in range(1,num_players+1):
    """เลิกเล่นแล้วปริ้นคำขอบคุณและสรุปผล"""
    print("\n")
    print(f"{'Thank you for playing':-^40}")
    print(f"{f'Player {idx}':^40}")
    print(f"Your final balance is: {players[idx][0]}")
    print(f"{'':-^40}")
