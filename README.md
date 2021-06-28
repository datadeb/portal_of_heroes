# portal_of_heroes

This is a toy project of making my favourite card game "Portal of Heroes" (https://boardgamegeek.com/boardgame/181960/portal-heroes)



**Information**


- Field Status

- Player Status

- 숫자카드들의 정보

- 스킬카드의 정보

- Player의 Action


**만드는 부분**

- UI
- Rule
- Skill cards 미완성카드 (추가스킬 아직)
  - 3점 반딧불카드 양옆사람 활성화가능 
  - 카드마다 User가 읽을 수 있게 조건을 말로 써주기?
  - 2점 골렘카드 액션 즉시 3회발동
  - 

- Skill cards json 포함내용
  - name : 카드이름 (string)
  - score : 카드 점수 (int)
  - condition : 카드 발동조건 딕셔너리 (dict)
    - base : 조건 종류
      - general : 가장 기본적인 발동조건. list of number cards required (list)
      - dia : number of dia required (int)
      - generalandDia : 조건과 다이아1개 (이 카드 사실 한개밖에 없어서 크게 신경 안써도됨)
      - equalcards : number of any equal cards required (int)
      - three_sums_up : 세장의 카드의 합이 몇이 될지 (int)
      - consecutive : 연속적인 n장의 카드 (int)
      - any_sums_up : 10
      - three_which_is : even/odd
      - and : and 컨디션 2개의 리스트
      - or : or 컨디션 2개의 리스트
    - body : 조건내용
  - bonus_dia : number of dia given to player as a bonus when activated (int)
  - 