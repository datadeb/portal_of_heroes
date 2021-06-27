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
    
    def initial_setup(self, number_cards, skill_cards):
        self.secret_numcards = random.shuffle(number_cards)
        self.open_numcards = self.secret_numcards[:4]
        self.secret_numcards = self.secret_numcards[4:]

        self.secret_skillcards = random.shuffle(skill_cards)
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
        self.disposed_numcards = 

    def renew_skill_cards(self):

    



class Player:
    def __init__(self,name):
        self.name = name
        self.point = 0
        self.inhand=[]
        self.deck=[]
        self.dia = 0

    def bring_number_card(self, num):
        self.inhand.append(num)

    def bring_skill_card(self,card):
        if len(self.deck)>2:
            print("cannot bring more card")
        else:
            self.deck.append(card)

    def renew_number_cards(self, gamefield):
        gamefield.renew_num_cards()
    
    def activate_skill_card(self,card):
        if #condition check
            self.deck.remove(card)
            self.point += card.score





def main():

    print("Game Start")

    #카드파일 가져오기 
    with open('number_cards.json') as f:
        number_cards =  json.load(f)

    with open('skill_cards.json') as f:
        skill_cards =  json.load(f)

    #player 몇명인지 입력받기
    nplayer = 0
    while not int(nplayer) in range(2,5):
        nplayer = input("Please enter number of players (2 - 5) : ")

    # player 생성
    active_players = {}
    for i in range(nplayer):
        name = 'player_{}'.format(i)
        active_players[name] = active_players.get(name, Player(name=name))

    # turn 정하기 

    # gamefiled 초기화



    while 종료되기 전
        for player 1~n
            if action 전 skill 있으면 사용
            for action 1~ (각 플레이어의 리밋)
                action입력받기
                action valid check
                action 수행
                    gamefield 업데이트
                    player deck 업데이트 
                    player 상태 업데이트
                    그 외 카드 및 스킬 에 따른 조건 update
                game end 조건 체크
            if action 후 skill 있으면 사용