import json
import random

# Set card field

class Gamefield:
    def __init__(self):
        self.open_numcards = []
        self.secret_numcards = []
        self.disposed_numcards = []
        self.open_skillcards = []
        self.secret_skillcards = []
        self.disposed_skillcards = []
        #카드파일 가져오기 
        with open('./number_cards.json','r') as f:
            # print('f:', f)
            self.secret_numcards =  json.loads(f.read())

        # print(self.secret_numcards)
        with open('./skill_cards.json','r') as f:
            self.secret_skillcards =  json.loads(f.read())

    
    def initial_setup(self):
        random.shuffle(self.secret_numcards)
        # print(self.secret_numcards)
        self.open_numcards = self.secret_numcards[:4]
        self.secret_numcards = self.secret_numcards[4:]

        random.shuffle(self.secret_skillcards)
        self.open_skillcards = self.secret_skillcards[:2]
        self.secret_skillcards = self.secret_skillcards[2:]


    def num_card_taken(self, cardindex):
        takencard = self.open_numcards.pop(cardindex)
        self.open_numcards.append(self.secret_numcards.pop())
        return takencard
    
    def skill_card_taken(self, cardindex):
        takencard = self.open_skillcards.pop(cardindex)
        self.open_skillcards.append(self.secret_skillcards.pop())
        return takencard

    def renew_num_cards(self):
        self.disposed_numcards 
        return

    def renew_skill_cards(self):
        return

class Player:
    def __init__(self,name):
        self.name = name
        self.point = 0
        self.inhand=[]
        self.deck=[]
        self.dia = 0
        self.handlimit = 5
        self.permanentinhand=[]
        self.actionlimit = 3


    def bring_number_card(self, num):
        self.inhand.append(num)

    def bring_skill_card(self,card):
        if len(self.deck)>2:
            print("cannot bring more card")
        else:
            self.deck.append(card)

    def renew_number_cards(self, gamefield):
        gamefield.renew_num_cards()
    
    # def activate_skill_card(self,card):
    #     if #condition check
    #         self.deck.remove(card)
    #         self.point += card.score





def startGame():

    print("Welcome to the Portal of Heroes. Game Start!")

    #player 몇명인지 입력받기
    nplayer = 0
    while not int(nplayer) in range(2,6):
        nplayer = input("Please enter the number of players (2 - 5) : ")


    # player 생성
    active_players = {}
    for i in range(int(nplayer)):
        name = 'player_{}'.format(i)
        active_players[name] = active_players.get(name, Player(name=name))
    

    # 플레이 순서 정하기
    players_in_list = list(active_players.keys())
    random.shuffle(players_in_list)
    print(players_in_list)

    # gamefiled 초기화
    field = Gamefield()
    field.initial_setup()

    print(f"""
        ------------------------------------
        FIELD
        opened_num_cards : {field.open_numcards}
        opened_skill_cards : {field.open_skillcards}
        ------------------------------------"""
    )
    n_round = 0

    while True: # 게임 종료되기전
        print("Round", n_round)
        for playername in players_in_list: # player들 턴 돌아가면서 
            

            player = active_players[playername]
            limit = player.actionlimit # 현재 player의 리밋값 받아오기
            print(f"{playername}'s turn. {limit} actions remaining")
            while limit>0: # 리밋값을 하나씩 까면서 액션 수행
                chosenaction = int(input(f"{limit} actions remaining. Which action would you do? \n 1. get number card \n 2. get skill card \n 3. swap number cards \n 4. activate my point \n"))
                if chosenaction == 1:  # 숫자카드 가져오기
                    numbercard = int(input(f"which number will you bring? \n 1.{field.open_numcards[0]} \n 2.{field.open_numcards[1]} \n 3.{field.open_numcards[2]} \n 4.{field.open_numcards[3]} \n"))
                    player.inhand.append(field.open_numcards[numbercard-1]) # 손에 고른 카드가 들어옴
                    del field.open_numcards[numbercard-1] # 고른 인덱스를 깔려있는 카드에서 지움 
                    field.open_numcards.append((field.secret_numcards.pop())) # 새 카드 한장 깠어

                    limit = limit-1 # 리밋 업데이트 해줌 
                elif chosenaction == 2: # 캐릭터 카드 가져오기
                    limit = limit-1
                elif chosenaction == 3:  # 필드 숫자카드 갈아엎기
                    limit = limit-1                 
                elif chosenaction == 4:  # 점수내기
                    limit = limit-1
                else:
                    print("Wrong input")

                
        n_round += 1



    # while 종료되기 전
    #     for player 1~n                                                               [완료]
    #         if action 전 skill 있으면 사용
    # actionLimit = player.actionLimit                                                 [완료]
    #         for action 1~actionLimit (각 플레이어의 리밋)                             [완료]
    #             action입력받기                                                       [완료]
    #             action valid check (
    #                   1. 숫자 가져온다 - 가져오는 숫자가 필드에 있는지
    #                   2. 캐릭터 가져온다 - 플레이어 덱이 꽉차있지 않은지
    #                   3. 숫자 갈기 - 그냥 하면 돼
    #                   4. 점수를 낸다 
    #                       4.1 점수를 낼 카드를 유저가 선택
                                # 2,1
                                # validcheck
                                # player.dia
    #                       4.2 그 카드의 조건을 읽어주고 유저가 조건 카드를 내게 해
    #                           - 몇장을 내라고 알려줘야됨
    #                       4.3 유저가 낸 카드가 유저가 들고 있는 카드가 맞는지
    #                       4.4 유저가 낸 카드가 조건에 부합하는지 )
    #             action 수행
    #                 gamefield 업데이트
    #                 player deck 업데이트 
    #                 player 상태 업데이트
    #                 그 외 카드 및 스킬 에 따른 조건 update
    #             game end 조건 체크
    #         if action 후 skill 있으면 사용
    return


if __name__ == "__main__":
    startGame()