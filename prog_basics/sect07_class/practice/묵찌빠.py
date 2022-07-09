"""
묵찌빠 게임

STEP1 : 게임시작 출력
STEP2 : 가위(0),바위(1),보(2)를 하여 공격/수비를 결정
STEP3 : [공격] or [수비] 묵(1), 찌(0), 빠(2) ?
STEP4 : 게임의 승부 or 공격/수비를 결정?
STEP5 : 결과메시지를 보여준다  

cf. 컴퓨터는 랜덤값, 플레이어는 입력값

"""
import random
import time

class GameMZP:
	# 속성
    player    = dict()     # 플레이어 {code:코드, disp:출력}
    computer  = dict()     # 컴퓨터
    is_attack = bool()     # True:공격, False:수비
    is_draw   = bool()     # True:비김
    is_over   = bool()     # True:종료
    mode = str()
    result = str()

    display = [
        { '0':'가위', '1':'바위', '2':'보' },
        { '0':'찌',   '1':'묵',  '2':'빠' },
    ]

    def __init__(self, name='사용자'):
        self.name = name

	# 메소드
    def start_game(self, step=0):
        print("묵찌빠 게임을 시작합니다!!!")
        self.is_draw = True
        self.is_over = False
        self.decide_attack_defense(step=0)


    def decide_attack_defense(self, step=0):
        """
            가위바위보를 하여 공격과 수비모드를 결정한다.
        """
        time.sleep(1)
        print('-'*50)

        while self.is_draw:
            self.set_player(step=0)
            self.set_computer(step=0)
            self.decide_winner()
            time.sleep(1)

    def play_game(self, step=1):
        """
            묵찌빠 게임을 진행한다
        """
        time.sleep(1)
        print('-' * 50)

        cnt = 0
        while not self.is_draw and not self.is_over:
            if cnt > 0:
                self.get_state()

            self.set_player(step)
            self.set_computer(step)
            self.decide_game_winner()
            cnt += 1
            time.sleep(1)

        if self.is_over:
            print('-'*50)
            self.get_state()
            print(self.result)


    def set_player(self, step=0):
        """
            사용자의 값을 입력 받는다.
                step=0 : 가위바위보 모드
                step=1 : 묵찌빠 모드
        """
        step = 0 if step==0 else 1
        if step == 0:
            code = input("가위(0)/바위(1)/보(2) : ")
        else:
            self.mode = "공격" if self.is_attack else "수비"
            code = input("[{}] 묵(1)/찌(0)/빠(2) : ".format(self.mode))

        self.player['code'] = code
        self.player['disp'] = self.display[step][code]

    def set_computer(self, step=0):
        step = 0 if step==0 else 1
        rnd_num = random.randint(0,2)
        code = str(rnd_num)

        self.computer['code'] = code
        self.computer['disp'] = self.display[step][code]

    def decide_winner(self):
        """
            가위바위보의 승부를 결정한다
        """
        if self.player['code'] == self.computer['code']:
            print('비겼습니다. 한번더 시도하세요!')
            self.is_draw = True
        else:
            self.is_draw = False
            if ( (self.player['code'] == '0' and self.computer['code'] == '2') or
                 (self.player['code'] == '1' and self.computer['code'] == '0') or
                 (self.player['code'] == '2' and self.computer['code'] == '1') ):
                self.is_attack = True
            else:
                self.is_attack = False

    def decide_game_winner(self):
        """
            묵찌빠 게임의 승부를 결정한다
        """
        if self.player['code'] == self.computer['code']:
            self.is_over = True
            if self.mode == "공격":
                self.result = "You Win!!!"
            else:
                self.result = "You Lose!!!"

        else:
            self.is_over = False
            if ((self.player['code'] == '0' and self.computer['code'] == '2') or
                    (self.player['code'] == '1' and self.computer['code'] == '0') or
                    (self.player['code'] == '2' and self.computer['code'] == '1')):
                self.is_attack = True
                self.mode == "공격"
            else:
                self.is_attack = False
                self.mode == "수비"


    # def play_game

    def get_state(self):
        """
            사용자와 컴퓨터의 상태값을 확인한다.
        """
        state = "{} : {} ".format(self.name, self.player)
        state+= "\n컴퓨터 : {} ".format(self.computer)

        # msg = "이겼으니 선공하세요." if self.is_attack else "졌으니 방어하세요"
        # self.mode = "공격" if self.is_attack else "수비"
        # state = '{}:{}, 컴퓨터:{} => {}'.format(self.name, self.player['disp'], self.computer['disp'], msg)
        state = '{}:{}, 컴퓨터:{} '.format(self.name, self.player['disp'], self.computer['disp'])
        print(state)


if __name__ == "__main__":
    gameMZP = GameMZP()
    gameMZP.start_game()
    gameMZP.get_state()
    gameMZP.play_game()
    print('-'*50)
    print("게임종료")

