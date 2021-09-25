class TV:
    def __init__(self, channel, volume):
        if 0 < channel <= 20:
            self.__channel = channel
        else:
            raise ValueError("Телевизор словил только 20 каналов, выполняю выключение")
        if 0 <= volume <= 100:
            self.__volume = volume
        else:
            raise ValueError("Телевизор не может поставить такую громкость, выполняю выключение")

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, chan):
        if 0 < chan <= 20:
            self.__channel = chan
        else:
            print("Телевизор словил только 20 каналов")

    
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vol):
        if 0 <= vol <= 100:
            self.__volume = vol
        else:
            print("Телевизор не может поставить такую громкость")

def main():
    obj = TV(int(input("Канал :")), int(input("Громкость :")))

    choice = None
    while choice != "0":
        print(f"""
        0 - Выйти,
        1 - Изменить канал,
        2 - Изменить громкость
        Громкость : {obj.volume}
        Канал : {obj.channel}
        """)
        choice = input()
        if choice == "1":
            obj.channel = int(input("Канал :"))
        elif choice == "2":
            obj.volume = int(input("Громкость :"))
    
    print("Пока")

main()
