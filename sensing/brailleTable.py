# Send stimulation
def sendKorean(arr):
    Boom(arr) # to be continued
    sleep(0.3)
    Boom(arr)
    sleep(0.3)

# Boom !!
def Boom(arr):
  print("Boom !!", arr)
  return

class brailleTable():

    def __init__(self):
        self.korean = ["ㄱ":"010000", "ㄴ":"110000", "ㄷ":"011000", "ㄹ":"000100", "ㅁ":"101000", "ㅂ":"010100", "ㅅ":"000001", "ㅇ":"001111", "ㅈ":"010001", "ㅊ":"000101", "ㅋ":"111000", "ㅌ":"101100", "ㅍ":"110100", "ㅎ":"011100", "ㄲ":"000001010000", "ㄸ":"000001011000", "ㅃ":"000001010100", "ㅆ":"000001000001", "ㅉ":"000001010000", "ㅏ":"101001", "ㅑ":"010110", "ㅓ":"011010", "ㅕ":"100101", "ㅗ":"100011", "ㅛ":"010011", "ㅜ":"110010", "ㅠ":"110001", "ㅡ":"011001", "ㅣ":"100110", "ㅐ":"101110", "ㅔ":"110110", "ㅚ":"110111", "ㅘ":"101011", "ㅝ":"111010", "ㅢ":"011101", "ㅖ":"010010", "ㅟ":"110010101110", "ㅒ":"010110101110", "ㅙ":"101011101110", "ㅞ":"111010101110", "1":"100000", "2":"101000", "3":"110000", "4":"110100", "5":"100100", "6":"111000", "7":"111100", "8":"101100", "9":"011000", "0":"011100"]
       
        

    def alertKorean(self, jamo_str):
        
        for charater in jamo_str:
            signal = self.korean[charater]

            for i in len(signal//6)
                sendKorean[signal[i:i+5]]

        return